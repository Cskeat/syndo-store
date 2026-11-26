import os, base64

site_dir = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store"
assets_dir = os.path.join(site_dir, "assets")
out_dir = os.path.join(site_dir, "kv_uploads")
os.makedirs(out_dir, exist_ok=True)

# 1. index.html
with open(os.path.join(site_dir, "index.html"), "r", encoding="utf-8") as f:
    html_text = f.read()
b64_html = base64.b64encode(html_text.encode("utf-8")).decode("ascii")

with open(os.path.join(out_dir, "upload_html.js"), "w", encoding="utf-8") as f:
    f.write(f'''async () => {{
  const accountId = 'd00fd38122de785b06c503de99e7c6df';
  const kvId = '74073670e70a4ce9b53013c4a3cf8bc8';
  const b64 = "{b64_html}";
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  const text = new TextDecoder('utf-8').decode(bytes);

  const res = await cloudflare.request({{
    method: 'PUT',
    path: `/accounts/${{accountId}}/storage/kv/namespaces/${{kvId}}/values/index.html`,
    headers: {{ 'Content-Type': 'text/html; charset=utf-8' }},
    body: text
  }});
  return {{ success: res.success }};
}}''')

# 2. Images
images = ['53778.jpg', '53779.jpg', '53771.jpg', '53769.jpg', '125950.jpg', '442570.jpg']
for img in images:
    opt_path = os.path.join(assets_dir, 'opt_' + img)
    with open(opt_path, "rb") as f:
        img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode("ascii")
    js_name = f"upload_{img.replace('.', '_')}.js"
    with open(os.path.join(out_dir, js_name), "w", encoding="utf-8") as f:
        f.write(f'''async () => {{
  const accountId = 'd00fd38122de785b06c503de99e7c6df';
  const kvId = '74073670e70a4ce9b53013c4a3cf8bc8';
  const b64 = "{b64_img}";
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);

  const res = await cloudflare.request({{
    method: 'PUT',
    path: `/accounts/${{accountId}}/storage/kv/namespaces/${{kvId}}/values/assets%2F{img}`,
    headers: {{ 'Content-Type': 'application/octet-stream' }},
    body: bytes
  }});
  return {{ img: "{img}", success: res.success }};
}}''')

print("All upload scripts generated in", out_dir)
