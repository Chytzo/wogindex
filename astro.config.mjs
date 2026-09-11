import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
export default defineConfig({
  site: 'https://wogindex.com',
  base: '/wogindex/',
  integrations: [tailwind()],
});