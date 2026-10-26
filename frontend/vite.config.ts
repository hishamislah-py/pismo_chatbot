import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// The browser only talks to the Vite origin; /api is forwarded to the FastAPI backend, so no CORS setup is needed.
// IPv4 loopback on purpose: on this Windows host "localhost" tries ::1 first and the backend listens on 127.0.0.1.
// PISMO_API_TARGET / PISMO_UI_PORT override the defaults (e.g. a second backend on another port).
const apiTarget = process.env.PISMO_API_TARGET || 'http://127.0.0.1:8000'
const uiPort = Number(process.env.PISMO_UI_PORT) || 5173

export default defineConfig({
  plugins: [react()],
  server: {
    port: uiPort,
    strictPort: true,
    proxy: {
      '/api': {
        target: apiTarget,
        changeOrigin: true,
        // generation can take up to ASSISTANT_TIMEOUT_S (90 s); keep the proxy open longer than the client timeout
        timeout: 130_000,
        proxyTimeout: 130_000,
      },
    },
  },
})
