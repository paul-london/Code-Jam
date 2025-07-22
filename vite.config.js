import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "/Park-Hopper-Routes/",  // ← required for GitHub Pages
  plugins: [react()],
  build: {
    outDir: "docs",  // tells Vite to build into the docs/ folder
  },
  server: {
    port: 3000,
  },
});
