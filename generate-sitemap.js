const fs = require('fs');
const path = require('path');

// Configuration
const DOMAIN = 'https://freightlabsagency.com'; // Update this to your actual domain
const OUTPUT_FILE = 'sitemap.xml';

// Priority and change frequency for different page types
const pageConfig = {
  'index.html': { priority: '1.0', changefreq: 'weekly' },
  'about/index.html': { priority: '0.8', changefreq: 'monthly' },
  'contact/index.html': { priority: '0.8', changefreq: 'monthly' },
  'freightseo/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightleads/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freightcontent/index.html': { priority: '0.9', changefreq: 'weekly' },
  'ai-seo-logistics/index.html': { priority: '0.9', changefreq: 'weekly' },
  'google-ads-logistics/index.html': { priority: '0.9', changefreq: 'weekly' },
  '3pl-seo/index.html': { priority: '0.9', changefreq: 'weekly' },
  'transportation-seo/index.html': { priority: '0.9', changefreq: 'weekly' },
  'seo-trucking-companies/index.html': { priority: '0.9', changefreq: 'weekly' },
  'seo-warehousing/index.html': { priority: '0.9', changefreq: 'weekly' },
  'seo-supply-chain-companies/index.html': { priority: '0.9', changefreq: 'weekly' },
  'logistics-lead-generation/index.html': { priority: '0.9', changefreq: 'weekly' },
  'lead-generation-for-freight-brokers/index.html': { priority: '0.9', changefreq: 'weekly' },
  'shipper-lead-generation/index.html': { priority: '0.9', changefreq: 'weekly' },
  'logistics-consulting/index.html': { priority: '0.8', changefreq: 'monthly' },
  'logistics-web-design/index.html': { priority: '0.9', changefreq: 'weekly' },
  'facebook-ads-logistics/index.html': { priority: '0.8', changefreq: 'weekly' },
  'linkedin-ads-logistics/index.html': { priority: '0.8', changefreq: 'weekly' },
  'web-design-trucking-companies/index.html': { priority: '0.8', changefreq: 'weekly' },
  'warehousing-fulfillment/index.html': { priority: '0.9', changefreq: 'weekly' },
  'freight-forwarding-transportation/index.html': { priority: '0.9', changefreq: 'weekly' },
  'supply-chain-technology/index.html': { priority: '0.9', changefreq: 'weekly' },
  'ecommerce-d2c-logistics/index.html': { priority: '0.9', changefreq: 'weekly' },
  'cold-chain-logistics/index.html': { priority: '0.9', changefreq: 'weekly' },
  'last-mile-urban-delivery/index.html': { priority: '0.9', changefreq: 'weekly' },
  'case-studies/index.html': { priority: '0.9', changefreq: 'weekly' },
  'guides/index.html': { priority: '0.9', changefreq: 'weekly' },
};

// Find all HTML files recursively
function findHTMLFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir).sort();

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      // Skip node_modules, .git, and other non-content directories
      if (!['node_modules', '.git', '.agents', '.codex', 'dist', 'build'].includes(file)) {
        findHTMLFiles(filePath, fileList);
      }
    } else if (file === 'index.html') {
      // Only canonical directory pages belong in the sitemap. This avoids
      // accidentally publishing templates or alternate .html URLs.
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

  sitemap += '</urlset>\n';

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
