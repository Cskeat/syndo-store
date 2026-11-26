import json
import os

html_path = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store\index_standalone.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

json_html = json.dumps(html)

worker_code = f"""
const SITE_HTML = {json_html};

addEventListener('fetch', event => {{
  event.respondWith(handleRequest(event.request));
}});

async function handleRequest(request) {{
  const url = new URL(request.url);
  
  if (url.pathname === '/robots.txt') {{
    return new Response('User-agent: *\\nAllow: /\\nSitemap: https://syndotech.my/sitemap.xml', {{
      headers: {{ 'content-type': 'text/plain; charset=utf-8' }}
    }});
  }}
  
  return new Response(SITE_HTML, {{
    headers: {{
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'public, max-age=1800, s-maxage=86400',
      'x-content-type-options': 'nosniff',
      'referrer-policy': 'strict-origin-when-cross-origin'
    }}
  }});
}}
"""

worker_path = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store\worker.js"
with open(worker_path, "w", encoding="utf-8") as f:
    f.write(worker_code)

print("Generated worker.js size:", os.path.getsize(worker_path), "bytes")
