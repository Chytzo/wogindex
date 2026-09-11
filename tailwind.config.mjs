/** @type {import("tailwindcss").Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        dark: { bg: "#1a0e04", card: "#261608", card2: "#2a1a08", border: "#3a2610", sidebar: "#200f05" },
        accent: "#e8962e",
        cream: "#f0e8d0",
        mud: "#a89878",
        gold: { light: "#f0d080", DEFAULT: "#e8962e", dark: "#c8922a" },
        quality: { common: "#c9c2ab", uncommon: "#22c55e", rare: "#3b82f6", epic: "#a855f7", legendary: "#f97316", mythic: "#ef4444" },
      },
      fontFamily: {
        pixel: ["'Press Start 2P'", "monospace"],
        body: ["Lato", "'Segoe UI'", "Tahoma", "sans-serif"],
      },
    },
  },
  plugins: [],
};