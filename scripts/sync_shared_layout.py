#!/usr/bin/env python3

import re
from pathlib import Path


PAGES = {
    "index.html": {"current": "home", "companies_href": "#portfolio"},
    "about.html": {"current": "about", "companies_href": "/index.html#portfolio"},
    "contact.html": {"current": "contact", "companies_href": "/index.html#portfolio"},
    "investor-page.html": {"current": "investors", "companies_href": "/index.html#portfolio"},
    "press.html": {"current": "press", "companies_href": "/index.html#portfolio"},
    "privacy-policy.html": {"current": None, "companies_href": "/index.html#portfolio"},
    "terms-of-service.html": {"current": None, "companies_href": "/index.html#portfolio"},
    "404.html": {"current": None, "companies_href": "/index.html#portfolio"},
    "updates.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
    "q1-2026-portfolio-update.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
    "portfolio-update-q4-2025.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
    "portfolio-update-q3-2025.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
    "portfolio-update-q2-2025.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
    "founder-note-services-to-product-flywheel.html": {"current": "updates", "companies_href": "/index.html#portfolio"},
}

NAV_ITEMS = [
    ("Home", "/", "home"),
    ("About", "/about.html", "about"),
    ("Companies", None, "companies"),
    ("Investors", "/investor-page.html", "investors"),
    ("Contact", "/contact.html", "contact"),
    ("Updates", "/updates.html", "updates"),
    ("Press", "/press.html", "press"),
]

FOOTER = """<footer>
    <div class="container">
        <p>&copy; 2025 SaaSier Inc. All rights reserved. | <a href="/">Home</a> | <a href="/about.html">About</a> |
            <a href="/contact.html">Contact</a> | <a href="/press.html">Press</a> | <a href="/privacy-policy.html">Privacy Policy</a> | <a href="/terms-of-service.html">Terms of Service</a>
        </p>
        <div class="social-links">
            <a href="https://www.linkedin.com/company/saasierinc" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
        </div>
    </div>
</footer>"""


def build_header(current: str | None, companies_href: str) -> str:
    items = []
    for label, href, key in NAV_ITEMS:
        if key == "companies":
            href = companies_href
        aria = ' aria-current="page"' if current == key else ""
        items.append(f'                <li><a href="{href}"{aria}>{label}</a></li>')

    nav = "\n".join(items)
    return f"""<header>
    <nav>
        <a href="/" class="logo">
            <img src="images/saasier-logo.png" alt="SaaSier Inc" height="80">
        </a>
        <button class="mobile-menu-btn" aria-label="Toggle navigation" aria-controls="nav-menu" aria-expanded="false">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </button>
        <ul class="nav-links" id="nav-menu">
{nav}
        </ul>
    </nav>
</header>"""


def replace_once(pattern: str, replacement: str, text: str, path: Path) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one match for {pattern!r} in {path}")
    return updated


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for relative_path, config in PAGES.items():
        path = root / relative_path
        text = path.read_text()
        text = replace_once(r"<header>.*?</header>", build_header(config["current"], config["companies_href"]), text, path)
        text = replace_once(r"<footer>.*?</footer>", FOOTER, text, path)
        path.write_text(text)
        print(f"synced {relative_path}")


if __name__ == "__main__":
    main()
