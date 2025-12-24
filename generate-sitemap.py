#!/usr/bin/env python3
"""
Sitemap Generator for Freight Labs
Automatically generates sitemap.xml from HTML files
"""

import os
import datetime
from pathlib import Path

# Configuration
DOMAIN = 'https://freightlabs.com'  # Update this to your actual domain
OUTPUT_FILE = 'sitemap.xml'

# Priority and change frequency for different page types
PAGE_CONFIG = {
    'index.html': {'priority': '1.0', 'changefreq': 'weekly'},
    'about/index.html': {'priority': '0.8', 'changefreq': 'monthly'},
    'services/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'process/index.html': {'priority': '0.8', 'changefreq': 'monthly'},
    'freightads/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'freightseo/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'freightleads/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'freightdesign/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'freightcontent/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'guides/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'warehousing-fulfillment/index.html': {'priority': '0.9', 'changefreq': 'weekly'},
    'local-seo-for-3pls/index.html': {'priority': '0.7', 'changefreq': 'monthly'},
    '3pl-marketing-mistakes/index.html': {'priority': '0.7', 'changefreq': 'monthly'},
}

# Directories to skip
SKIP_DIRS = {'node_modules', '.git', 'dist', 'build', '__pycache__', '.vscode'}

# Files to skip
SKIP_FILES = {'template.html', 'google*.html'}  # Add any other files to skip


def find_html_files(root_dir='.'):
    """Find all HTML files in the directory tree"""
    html_files = []
    root_path = Path(root_dir)

    for file_path in root_path.rglob('*.html'):
        # Skip files in excluded directories
        if any(skip_dir in file_path.parts for skip_dir in SKIP_DIRS):
            continue
            
        # Skip specific files
        if file_path.name in SKIP_FILES:
            continue
            
        html_files.append(file_path)

    return sorted(html_files)


def get_file_mod_time(file_path):
    """Get the last modification time of a file"""
    timestamp = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def generate_sitemap():
    """Generate sitemap.xml from HTML files"""
    html_files = find_html_files()

    # Start XML
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for file_path in html_files:
        # Convert to relative path
        relative_path = str(file_path).replace('\\', '/')
        if relative_path.startswith('./'):
            relative_path = relative_path[2:]

        # Get modification time
        last_mod = get_file_mod_time(file_path)

        # Build URL
        if relative_path.endswith('index.html'):
            # Directory style: path/to/index.html -> path/to/
            url = relative_path[:-10]  # Remove 'index.html'
            if not url: # Root index.html becomes empty string
                url = '' 
            elif not url.endswith('/'):
                url += '/'
        else:
            # Clean URL style: path/to/page.html -> path/to/page/
            url = relative_path[:-5]  # Remove '.html'
            if not url.endswith('/'):
                url += '/'
            
        # Get config or use defaults
        config = PAGE_CONFIG.get(relative_path, {
            'priority': '0.7',
            'changefreq': 'monthly'
        })

        # Add URL entry
        sitemap_lines.extend([
            '  <url>',
            f'    <loc>{DOMAIN}/{url}</loc>',
            f'    <lastmod>{last_mod}</lastmod>',
            f'    <changefreq>{config["changefreq"]}</changefreq>',
            f'    <priority>{config["priority"]}</priority>',
            '  </url>'
        ])

    sitemap_lines.append('</urlset>')

    # Write to file
    sitemap_content = '\n'.join(sitemap_lines)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f'✅ Sitemap generated successfully with {len(html_files)} URLs')
    print(f'📄 Output: {OUTPUT_FILE}')

    # Print file list for verification
    print('\n📋 Pages included:')
    for file_path in html_files:
        print(f'   - {file_path}')


if __name__ == '__main__':
    try:
        generate_sitemap()
    except Exception as e:
        print(f'❌ Error generating sitemap: {e}')
        exit(1)
