import base64
import os

html_path = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store\index_standalone.html"
with open(html_path, "rb") as f:
    html_bytes = f.read()

b64_str = base64.b64encode(html_bytes).decode("ascii")

worker_code = f"""
const B64_SITE = "{b64_str}";

let cachedHtml = null;

function getHtml() {{
  const bin = atob(B64_SITE);
  const len = bin.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {{
    bytes[i] = bin.charCodeAt(i);
  }}
  return new TextDecoder("utf-8").decode(bytes);
}}

addEventListener("fetch", event => {{
  event.respondWith(handleRequest(event.request));
}});

async function handleRequest(request) {{
  const url = new URL(request.url);
  
  if (url.pathname === "/robots.txt") {{
    return new Response("User-agent: *\\nAllow: /\\nSitemap: https://syndotech.my/sitemap.xml", {{
      headers: {{ "content-type": "text/plain; charset=utf-8" }}
    }});
  }}

  if (!cachedHtml) {{
    cachedHtml = getHtml();
  }}

  return new Response(cachedHtml, {{
    headers: {{
      "content-type": "text/html; charset=utf-8",
      "cache-control": "public, max-age=1800, s-maxage=86400",
      "x-content-type-options": "nosniff",
      "referrer-policy": "strict-origin-when-cross-origin"
    }}
  }});
}}
"""

worker_path = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store\worker.js"
with open(worker_path, "w", encoding="utf-8") as f:
    f.write(worker_code)

print("Generated worker.js with base64 payload. Size:", os.path.getsize(worker_path), "bytes")
