const fs = require('fs');
const path = require('path');

// Configuration
const DOMAIN = 'https://freightlabs.com'; // Update this to your actual domain
const OUTPUT_FILE = 'sitemap.xml';

// Priority and change frequency for different page types
const pageConfig = {
  'index.html': { priority: '1.0', changefreq: 'weekly' },
  'about/index.html': { priority: '0.8', changefreq: 'monthly' },
  'services/index.html': { priority: '0.9', changefreq: 'weekly' },
  'process/index.html': { priority: '0.8', changefreq: 'monthly' },
  'freightads/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightseo/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightleads/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightdesign/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightcontent/index.html': { priority: '0.9', changefreq: 'weekly' },
};

// Find all HTML files recursively
function findHTMLFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      // Skip node_modules, .git, and other non-content directories
      if (!['node_modules', '.git', 'dist', 'build'].includes(file)) {
        findHTMLFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });

  return fileList;
}

// Generate sitemap XML
function generateSitemap() {
  const htmlFiles = findHTMLFiles('.');
  const currentDate = new Date().toISOString().split('T')[0];

  let sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n';
  sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

  htmlFiles.forEach(file => {
    // Convert file path to relative URL
    const relativePath = file.replace(/\\/g, '/').replace('./', '');

    // Get file modification time
    const stats = fs.statSync(file);
    const lastMod = stats.mtime.toISOString().split('T')[0];

    // Build URL (remove index.html for cleaner URLs)
    let url = relativePath.replace('index.html', '');
    if (url && !url.endsWith('/')) {
      url += '/';
    }
    url = url || '';

    // Get priority and changefreq from config or use defaults
    const config = pageConfig[relativePath] || { priority: '0.7', changefreq: 'monthly' };

    sitemap += '  <url>\n';
    sitemap += `    <loc>${DOMAIN}/${url}</loc>\n`;
    sitemap += `    <lastmod>${lastMod}</lastmod>\n`;
    sitemap += `    <changefreq>${config.changefreq}</changefreq>\n`;
    sitemap += `    <priority>${config.priority}</priority>\n`;
    sitemap += '  </url>\n';
  });

  sitemap += '</urlset>';

  // Write sitemap to file
  fs.writeFileSync(OUTPUT_FILE, sitemap);
  console.log(`✅ Sitemap generated successfully with ${htmlFiles.length} URLs`);
  console.log(`📄 Output: ${OUTPUT_FILE}`);
}

// Run the generator
try {
  generateSitemap();
} catch (error) {
  console.error('❌ Error generating sitemap:', error);
  process.exit(1);
}
