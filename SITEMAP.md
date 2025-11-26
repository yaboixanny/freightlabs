# Sitemap Auto-Generation

This directory includes automated sitemap generation for the Freight Labs website.

## Files

- **sitemap.xml** - The generated XML sitemap (automatically created)
- **generate-sitemap.py** - Script to generate/regenerate the sitemap
- **watch-sitemap.py** - File watcher that auto-regenerates sitemap on HTML changes
- **generate-sitemap.js** - Node.js version (alternative if you prefer Node.js)

## Quick Start

### 1. Generate Sitemap Manually

Run this command whenever you add or modify HTML files:

```bash
python3 generate-sitemap.py
```

### 2. Auto-Generate on File Changes (Recommended)

For automatic sitemap updates whenever you create or modify HTML files:

**First-time setup:**
```bash
pip3 install watchdog
```

**Run the watcher:**
```bash
python3 watch-sitemap.py
```

The watcher will:
- Monitor all HTML files in the project
- Automatically regenerate sitemap.xml when changes are detected
- Run in the background until you press Ctrl+C

## Configuration

### Update Your Domain

Edit the domain in [generate-sitemap.py](generate-sitemap.py):

```python
DOMAIN = 'https://freightlabs.com'  # Change this to your actual domain
```

### Customize Page Priorities

Edit the `PAGE_CONFIG` dictionary in [generate-sitemap.py](generate-sitemap.py):

```python
PAGE_CONFIG = {
    'index.html': {'priority': '1.0', 'changefreq': 'weekly'},
    'about/index.html': {'priority': '0.8', 'changefreq': 'monthly'},
    # Add more pages as needed
}
```

**Priority values:**
- 1.0 = Most important (homepage)
- 0.9 = High priority (main service pages)
- 0.8 = Medium-high (about, process pages)
- 0.7 = Default for other pages
- 0.5 = Lower priority pages

**Change frequency options:**
- `always` - Changes every time it's accessed
- `hourly` - Changes hourly
- `daily` - Changes daily
- `weekly` - Changes weekly
- `monthly` - Changes monthly
- `yearly` - Changes yearly
- `never` - Archived content

## Submitting to Search Engines

### Google Search Console

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select your property
3. Go to Sitemaps (in the left sidebar)
4. Enter `sitemap.xml` and click Submit

### Bing Webmaster Tools

1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Select your site
3. Go to Sitemaps
4. Enter `https://freightlabs.com/sitemap.xml` and submit

### Add to robots.txt

Create or update your `robots.txt` file with:

```
User-agent: *
Allow: /

Sitemap: https://freightlabs.com/sitemap.xml
```

## Workflow

### When Adding New Pages

**Option 1: Automatic (Recommended)**
1. Run `python3 watch-sitemap.py` in a terminal
2. Create or edit HTML files
3. Sitemap automatically updates

**Option 2: Manual**
1. Create or edit HTML files
2. Run `python3 generate-sitemap.py`
3. Sitemap is regenerated with new pages

## Troubleshooting

### "watchdog package not found"

Install the required Python package:
```bash
pip3 install watchdog
```

### Sitemap not updating

1. Make sure you're running the script from the project root directory
2. Check that HTML files are not in excluded directories (node_modules, .git, etc.)
3. Verify file permissions allow reading HTML files

### Wrong domain in sitemap

Update the `DOMAIN` variable in [generate-sitemap.py](generate-sitemap.py:11)

## Using Node.js Instead

If you prefer Node.js, you can use the included [generate-sitemap.js](generate-sitemap.js):

```bash
# Install Node.js first (if not installed)
# Then run:
node generate-sitemap.js
```

## Integration with Build Process

You can add sitemap generation to your deployment workflow:

### Git Pre-Commit Hook

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
python3 generate-sitemap.py
git add sitemap.xml
```

### Before Deployment

Add to your deployment script:
```bash
python3 generate-sitemap.py
# then deploy files...
```

## Support

For issues or questions, contact: hello@freightlabs.com
