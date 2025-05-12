import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
    plugins: [
        tailwindcss(),
    ],
    server: {
        watch: {
            ignored: ['!../../../**/*'], // Ensure Vite watches parent folder
        }
    },
    build: {
        outDir: 'dist', // Output directory
        assetsDir: 'compiled', // Keep assets in a specific folder
        sourcemap: true,
        rollupOptions: {
            output: {
                entryFileNames: 'compiled/[name].js',
                chunkFileNames: 'compiled/[name].js',
                assetFileNames: 'compiled/[name][extname]'
            }
        }
    }
})