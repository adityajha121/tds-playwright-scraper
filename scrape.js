const { chromium } = require('playwright');

const seeds = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60];

// Update this URL pattern if the actual URLs differ
const getUrl = (seed) => `https://sanand0.github.io/tdsdata/scraping/?seed=${seed}`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  let grandTotal = 0;

  for (const seed of seeds) {
    const url = getUrl(seed);
    console.log(`Scraping seed ${seed}: ${url}`);
    
    await page.goto(url, { waitUntil: 'networkidle' });
    
    // Extract all numbers from all table cells
    const numbers = await page.$$eval('table td, table th', cells =>
      cells.map(c => parseFloat(c.textContent.trim())).filter(n => !isNaN(n))
    );
    
    const seedTotal = numbers.reduce((a, b) => a + b, 0);
    console.log(`  Seed ${seed}: found ${numbers.length} numbers, sum = ${seedTotal}`);
    grandTotal += seedTotal;
  }

  await browser.close();
  console.log(`\nTOTAL SUM (seeds 51-60): ${grandTotal}`);
})();
