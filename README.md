# SaaSier Website

Official website for [SaaSier Inc.](https://www.linkedin.com/company/saasierinc)

## About

SaaSier provides tools and solutions to help SaaS companies streamline their operations and grow more efficiently.

## Site Structure

```
saasier-website/
├── index.html              # Homepage
├── about.html              # About page
├── contact.html            # Contact page
├── press.html              # Press/Media page
├── investor-page.html      # Investor relations
├── privacy-policy.html     # Privacy policy
├── terms-of-service.html   # Terms of service
├── 404.html                # Custom 404 page
├── css/
│   └── style.css           # Main stylesheet
├── js/
│   ├── script.js           # Main JavaScript
│   └── menu.js             # Mobile menu functionality
└── images/                 # Site images and icons
```

## Development

This is a static website built with HTML, CSS, and vanilla JavaScript. No build process required.

### Local Development

Open `index.html` in a browser or serve it locally:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (npx)
npx serve
```

Then visit `http://localhost:8000`

## Deployment

Deploy by uploading the contents to your web host. All files are static and can be served from any static hosting provider (Netlify, Vercel, GitHub Pages, etc.).

## License

© 2025 SaaSier Inc. All rights reserved.
