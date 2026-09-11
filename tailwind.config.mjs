/** @type {import("tailwindcss").Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        dark: { bg: "#0f1117", card: "#1a1d29", border: "#2a2d3a" },
        accent: "#3b82f6",
        quality: { common: "#9ca3af", uncommon: "#22c55e", rare: "#3b82f6", epic: "#a855f7", legendary: "#f97316", mythic: "#ef4444" },
      },
    },
  },
  plugins: [],
};
