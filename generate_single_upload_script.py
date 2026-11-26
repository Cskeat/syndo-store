import os, json, base64

site_dir = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store"
assets_dir = os.path.join(site_dir, "assets")

# index.html
with open(os.path.join(site_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

html_json = json.dumps(html)
js_html = f"""async () => {{
  const accountId = 'd00fd38122de785b06c503de99e7c6df';
  const kvId = '74073670e70a4ce9b53013c4a3cf8bc8';
  const html = {html_json};
  const res = await cloudflare.request({{
    method: 'PUT',
    path: `/accounts/${{accountId}}/storage/kv/namespaces/${{kvId}}/values/index.html`,
    headers: {{ 'Content-Type': 'text/html; charset=utf-8' }},
    body: html
  }});
  return {{ success: res.success }};
}}"""

with open(os.path.join(site_dir, "run_upload_html.js"), "w", encoding="utf-8") as f:
    f.write(js_html)

print("Generated run_upload_html.js:", len(js_html), "bytes")

# Each image
images = ['53778.jpg', '53779.jpg', '53771.jpg', '53769.jpg', '125950.jpg', '442570.jpg']
for img in images:
    with open(os.path.join(assets_dir, 'opt_' + img), "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    js_img = f"""async () => {{
  const accountId = 'd00fd38122de785b06c503de99e7c6df';
  const kvId = '74073670e70a4ce9b53013c4a3cf8bc8';
  const b64 = "{b64}";
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  const res = await cloudflare.request({{
    method: 'PUT',
    path: `/accounts/${{accountId}}/storage/kv/namespaces/${{kvId}}/values/assets%2F{img}`,
    headers: {{ 'Content-Type': 'application/octet-stream' }},
    body: bytes
  }});
  return {{ img: '{img}', success: res.success }};
}}"""
    with open(os.path.join(site_dir, f"run_upload_{img}.js"), "w", encoding="utf-8") as f:
        f.write(js_img)
    print(f"Generated run_upload_{img}.js:", len(js_img), "bytes")
