import { transform } from '@astrojs/compiler';
import { readFileSync } from 'node:fs';
const s = readFileSync('/tmp/test_body.astro', 'utf-8');
const { code } = await transform(s, {
  filepath: '/tmp/test_body.astro',
  astroConfig: { base: '/wogindex/', site: 'https://wogindex.com' }
});
const glines = code.split('\n');
for (let i = 0; i < glines.length; i++) {
  if (glines[i].includes('href') || glines[i].includes('BASE_URL')) {
    console.log('GEN ' + i + ' ' + JSON.stringify(glines[i]));
  }
}