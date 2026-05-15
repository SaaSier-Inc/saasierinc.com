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
├── contact.html
├── press.html
├── investor-page.html
├── updates.html
├── privacy-policy.html
├── terms-of-service.html
├── 404.html
├── css/style.css
├── js/script.js
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

## Deployment

The repo deploys to GitHub Pages from `main` via `.github/workflows/deploy.yml`. All files are static and can also be served by any static host.

Security headers are maintained in both `vercel.json` and `_headers`; GitHub Pages uses the HTML CSP fallback meta tags.

## License

© 2026 SaaSier Inc. All rights reserved.
