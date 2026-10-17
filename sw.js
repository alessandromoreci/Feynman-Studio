// Feynman Studio — service worker: makes the installed app work offline.
// The app itself is fetched from the network first (so you always get the latest version when online)
// and kept as a fallback; the LaTeX and PDF libraries are kept after the first visit.
const CACHE = 'feynman-studio-3.1';
const CORE = ['./', './index.html', './manifest.webmanifest', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];
const LIBS = [
  'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js',
  'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js'
];
self.addEventListener('install', (e)=>{
  e.waitUntil(caches.open(CACHE).then(async (c)=>{
    await Promise.all(CORE.map(u=> c.add(u).catch(()=>{})));
    await Promise.all(LIBS.map(u=> fetch(u, { mode: 'no-cors' }).then(r=> c.put(u, r)).catch(()=>{})));
  }));
  self.skipWaiting();
});
self.addEventListener('activate', (e)=>{
  e.waitUntil(caches.keys().then(keys=> Promise.all(keys.filter(k=> k.startsWith('feynman-studio-') && k !== CACHE).map(k=> caches.delete(k)))).then(()=> self.clients.claim()));
});
self.addEventListener('fetch', (e)=>{
  const req = e.request;
  if(req.method !== 'GET') return;
  const url = new URL(req.url);
  if(url.origin === location.origin){
    // the app: network first, cached copy when offline
    e.respondWith(fetch(req).then((r)=>{ if(r.ok){ const cp = r.clone(); caches.open(CACHE).then(c=> c.put(req, cp)); } return r; })
      .catch(()=> caches.match(req, { ignoreSearch: true }).then(r=> r || (req.mode === 'navigate' ? caches.match('./index.html') : Response.error()))));
    return;
  }
  // libraries and their fonts: cache first, then the network (and keep what comes back)
  e.respondWith(caches.match(req).then(hit=> hit || fetch(req).then((r)=>{ if(r.ok || r.type === 'opaque'){ const cp = r.clone(); caches.open(CACHE).then(c=> c.put(req, cp)); } return r; })));
});
