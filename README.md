# SaaSier Website

Official static website for [SaaSier Inc.](https://saasierinc.com), the women-owned holding company behind focused software companies and active product assets.

## Current public portfolio

- Hive Minded AI — vertical AI SaaS for beekeeping operations.
- MockForge — service virtualization and realistic API simulation for development, QA, and integration teams.
- SaaSy Solutions LLC — consulting and implementation arm for commercial and government-ready buyers.
- HelloSaaSy.ai — SaaS platform owned by SaaSy Solutions LLC.
- CodeDig — live PR risk and blast-radius analysis product, planned as a future standalone company once the entity is set up.

## Site Structure

```
saasierinc.com/
├── index.html
├── about.html
├── capability-statement.html
├── contact.html
├── press.html
├── investor-page.html
├── updates.html
├── privacy-policy.html
├── terms-of-service.html
├── 404.html
├── css/style.css
├── js/script.js
├── js/analytics.js
├── scripts/sync_shared_layout.py
├── _headers
├── vercel.json
└── images/
```

## Development

This is a static HTML/CSS/vanilla JavaScript site. No build process is required.

After editing shared navigation or footer content, run:

```bash
python3 scripts/sync_shared_layout.py
```

Local preview:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Analytics

`js/analytics.js` loads PostHog (US cloud) and tags visits referred by AI assistants
(ChatGPT, Perplexity, Claude, Gemini, Copilot, Meta AI, Grok, DeepSeek, Mistral, You.com,
Phind) with an `ai_referral_landing` event and an `ai_referrer` property. It does nothing
until `POSTHOG_KEY` at the top of the file holds a real project key (`phc_...`). The site has
no build step, so the key is pasted into the file; PostHog project keys are public by design.

Every HTML page must include it once in `<head>`:

```html
<script src="/js/analytics.js" defer></script>
```

Run `node --test scripts/analytics.test.js` after adding a page; it checks the include, the
CSP allowance for PostHog, and the AI-referrer classification.

## Deployment

The repo deploys to GitHub Pages from `main` via `.github/workflows/deploy.yml`. All files are static and can also be served by any static host.

Security headers are maintained in both `vercel.json` and `_headers`; GitHub Pages uses the HTML CSP fallback meta tags.

## License

© 2026 SaaSier Inc. All rights reserved.
