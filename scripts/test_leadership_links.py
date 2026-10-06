"""Check the public leadership cards and their profile destinations."""

from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {
    "Macon Wright": ("Founder & CEO", "https://www.linkedin.com/in/macon-wright-125889104/"),
    "Raymond Clanan": ("Co-founder & CTO", "https://www.linkedin.com/in/raymondclanan/"),
}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Node:
    def __init__(self, tag="root", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []
        self.text = ""

    def descendants(self):
        yield self
        for child in self.children:
            yield from child.descendants()

    def all_text(self):
        return self.text + " ".join(child.all_text() for child in self.children)

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()


class PageParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].text += data


class LeadershipLinksTest(unittest.TestCase):
    def test_home_and_about_credit_both_leaders_and_link_their_personal_profiles(self):
        for filename in ("index.html", "about.html"):
            page = PageParser((ROOT / filename).read_text(encoding="utf-8")).root
            cards = [node for node in page.descendants() if node.has_class("leader-profile")]
            self.assertEqual(len(cards), len(PROFILES), filename)
            for name, (role, url) in PROFILES.items():
                with self.subTest(page=filename, person=name):
                    card = next(node for node in cards if name in node.all_text())
                    expected_role = "CTO" if filename == "index.html" and name == "Raymond Clanan" else role
                    self.assertIn(expected_role, card.all_text())
                    links = [node for node in card.descendants() if node.tag == "a"]
                    self.assertEqual(len(links), 1)
                    self.assertEqual(links[0].attrs["href"], url)
                    self.assertEqual(links[0].attrs["aria-label"], f"{name} on LinkedIn")
                    self.assertEqual(links[0].attrs["target"], "_blank")
                    self.assertTrue({"noopener", "noreferrer"} <= set(links[0].attrs["rel"].split()))
                    image = next(node for node in card.descendants() if node.tag == "img")
                    self.assertTrue((ROOT / image.attrs["src"]).is_file())
                    if filename == "index.html" and name == "Raymond Clanan":
                        self.assertEqual(image.attrs["alt"], "Raymond Clanan, CTO of SaaSier Inc")
                        self.assertNotIn("co-founder", card.all_text().lower())

    def test_company_footer_retains_company_identity(self):
        for filename in ("index.html", "about.html"):
            page = PageParser((ROOT / filename).read_text(encoding="utf-8")).root
            social = next(node for node in page.descendants() if node.has_class("social-links"))
            link = next(node for node in social.descendants() if node.tag == "a")
            self.assertEqual(link.attrs["href"], "https://www.linkedin.com/company/saasierinc")


if __name__ == "__main__":
    unittest.main()
