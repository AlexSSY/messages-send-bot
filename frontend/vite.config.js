import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
 import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: { 
    allowedHosts: ["ae8a072e589f.ngrok-free.app"],
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    }
  }
})
