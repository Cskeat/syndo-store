import os

site_dir = r"C:\Users\ruhoo\OpenBot\Shared\syndo-store"
os.makedirs(site_dir, exist_ok=True)
index_path = os.path.join(site_dir, "index.html")

html_content = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <title>Syndo Store — SyndoTech Malaysia Official Flagship</title>
  <meta name="description" content="SyndoTech Malaysia official online direct store. 4K Zero-Bonding Interactive Smart Boards, 32-inch Rotating Stand TV, and Smart Pharmacy Dispensing Solutions." />
  
  <style>
    :root {
      --ink-primary: #1D1D1F;
      --ink-navy: #0A1A3A;
      --ink-secondary: #6E6E73;
      --ink-tertiary: #86868B;
      --studio-light: #F5F5F7;
      --studio-card: #FFFFFF;
      --studio-border: #D2D2D7;
      --linkblue: #0066CC;
      --blue-accent: #0071E3;
      --blue-hover: #0077ED;
      --brand-blue: #0077ED;
      --success: #34C759;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      background-color: #FFFFFF;
      color: var(--ink-primary);
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Inter", "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
      line-height: 1.5;
    }

    a { color: inherit; text-decoration: none; }
    button { font-family: inherit; cursor: pointer; border: none; background: none; }

    .headline-tight { letter-spacing: -0.035em; }
    .subhead-tight { letter-spacing: -0.015em; }

    /* Frosted Sticky Navbar */
    .nav-frosted {
      position: sticky;
      top: 0;
      z-index: 50;
      height: 52px;
      background-color: rgba(255, 255, 255, 0.88);
      backdrop-filter: saturate(180%) blur(20px);
      -webkit-backdrop-filter: saturate(180%) blur(20px);
      border-bottom: 1px solid rgba(0, 0, 0, 0.08);
      transition: background-color 0.3s ease;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Announcement Ribbon */
    .ribbon {
      background: var(--studio-light);
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
      font-size: 13px;
      padding: 10px 16px;
      text-align: center;
      color: var(--ink-primary);
    }
    .ribbon a {
      color: var(--linkblue);
      margin-left: 6px;
      font-weight: 500;
    }
    .ribbon a:hover { text-decoration: underline; }

    /* Section General */
    section {
      padding: 80px 24px;
      position: relative;
    }

    .section-eyebrow {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--ink-secondary);
      margin-bottom: 8px;
    }

    .section-title {
      font-size: 48px;
      font-weight: 700;
      line-height: 1.08;
      letter-spacing: -0.03em;
      color: var(--ink-primary);
      margin-bottom: 14px;
    }

    .section-sub {
      font-size: 21px;
      font-weight: 400;
      line-height: 1.4;
      color: var(--ink-secondary);
      max-width: 680px;
      margin: 0 auto 20px;
    }

    .section-price {
      font-size: 16px;
      font-weight: 500;
      color: var(--ink-primary);
      margin-bottom: 24px;
    }

    /* Buttons */
    .btn-primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--ink-primary);
      color: #FFFFFF;
      font-size: 15px;
      font-weight: 500;
      padding: 10px 24px;
      border-radius: 999px;
      transition: all 0.2s ease;
    }
    .btn-primary:hover {
      background: #000000;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }

    .btn-blue {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--blue-accent);
      color: #FFFFFF;
      font-size: 15px;
      font-weight: 500;
      padding: 10px 24px;
      border-radius: 999px;
      transition: all 0.2s ease;
    }
    .btn-blue:hover {
      background: var(--blue-hover);
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(0,113,227,0.3);
    }

    .btn-link {
      font-size: 16px;
      color: var(--linkblue);
      display: inline-flex;
      align-items: center;
      gap: 4px;
      margin-left: 20px;
    }
    .btn-link:hover { text-decoration: underline; }

    /* Realistic 65" Board Hardware Simulation */
    .board-stage {
      max-width: 860px;
      margin: 40px auto 0;
      position: relative;
    }

    .board-bezel {
      background: linear-gradient(160deg, #2b2d30 0%, #17181a 45%, #0e0f11 100%);
      border-radius: 14px;
      padding: 12px 12px 28px 12px;
      box-shadow:
        0 30px 70px -20px rgba(0, 0, 0, 0.4),
        0 0 0 1px rgba(255, 255, 255, 0.1) inset,
        0 2px 6px rgba(0, 0, 0, 0.6);
      position: relative;
    }

    .board-cam-bar {
      width: 120px;
      height: 16px;
      margin: -24px auto 8px;
      background: linear-gradient(to bottom, #383a3f, #1b1c1e);
      border-radius: 8px 8px 0 0;
      border-top: 1px solid rgba(255,255,255,0.2);
      border-left: 1px solid rgba(255,255,255,0.1);
      border-right: 1px solid rgba(255,255,255,0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 -2px 6px rgba(0,0,0,0.25);
    }
    .cam-lens {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #050608;
      border: 1px solid #4a4d55;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .cam-pupil {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #0088FF;
      box-shadow: 0 0 4px #0088FF;
    }
    .cam-mic {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #555;
    }

    .board-screen-glass {
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #0A0C10;
      border-radius: 4px;
      overflow: hidden;
      position: relative;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.8) inset;
    }

    .board-chin {
      position: absolute;
      bottom: 6px;
      left: 0;
      right: 0;
      text-align: center;
      height: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .board-chin span {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.15em;
      color: rgba(255, 255, 255, 0.85);
      text-transform: uppercase;
    }

    /* Screen OS Modes */
    .board-os-view {
      position: absolute;
      inset: 0;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
      display: flex;
      flex-direction: column;
    }
    .board-os-view.active {
      opacity: 1;
      pointer-events: auto;
    }

    /* Android 14 UI */
    .android-wallpaper {
      background:
        radial-gradient(ellipse 130% 60% at 50% 105%, #9b7a45 0%, #876632 40%, transparent 42%),
        radial-gradient(ellipse 120% 50% at 20% 100%, #b59155 0%, #9b7a45 40%, transparent 42%),
        linear-gradient(180deg, #1b9bf0 0%, #4ec0ff 55%, #74d0ff 100%);
      color: #FFFFFF;
      padding: 16px 24px;
      justify-content: space-between;
    }
    .android-topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 500;
      color: rgba(255, 255, 255, 0.95);
      text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    .android-clock-section {
      text-align: center;
      margin: auto 0;
    }
    .android-clock {
      font-size: 52px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -0.02em;
      text-shadow: 0 2px 10px rgba(0,0,0,0.25);
    }
    .android-date {
      font-size: 13px;
      color: rgba(255, 255, 255, 0.9);
      margin-top: 4px;
    }
    .android-search {
      width: 280px;
      height: 28px;
      background: rgba(0, 0, 0, 0.25);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 999px;
      margin: 12px auto 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 14px;
      font-size: 11px;
      color: rgba(255, 255, 255, 0.8);
    }
    .android-dock {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 24px;
      padding-bottom: 8px;
    }
    .dock-app {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: transform 0.2s ease;
    }
    .dock-app:hover {
      transform: translateY(-3px);
    }
    .dock-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    }
    .dock-label {
      font-size: 11px;
      font-weight: 500;
      text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }

    /* Interactive Whiteboard Canvas */
    .whiteboard-view {
      background: #FFFFFF;
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
    }
    .whiteboard-toolbar {
      height: 44px;
      background: #F2F2F7;
      border-bottom: 1px solid #D1D1D6;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      gap: 12px;
    }
    .color-swatch {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: transform 0.15s ease;
    }
    .color-swatch.active {
      transform: scale(1.2);
      border-color: #000;
    }
    .wb-btn {
      padding: 5px 12px;
      background: #FFFFFF;
      border: 1px solid #C7C7CC;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 500;
      color: #1D1D1F;
    }
    .wb-btn:hover { background: #E5E5EA; }
    .canvas-container {
      flex: 1;
      position: relative;
      background: #FFFFFF;
      cursor: crosshair;
    }
    #whiteboardCanvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      touch-action: none;
    }

    /* Windows 11 OPS Desktop */
    .windows-view {
      background: url('assets/53778.jpg') center/cover no-repeat;
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      color: #FFFFFF;
    }
    .windows-overlay {
      position: absolute;
      inset: 0;
      background: rgba(10, 15, 25, 0.45);
      backdrop-filter: blur(2px);
    }
    .windows-content {
      position: relative;
      z-index: 2;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .win-taskbar {
      height: 38px;
      background: rgba(255, 255, 255, 0.75);
      backdrop-filter: blur(20px);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 0 16px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    .win-icon {
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }

    /* Real Room View */
    .room-view {
      background: url('assets/53778.jpg') center/cover no-repeat;
      position: absolute;
      inset: 0;
    }

    /* Board Control Pill Bar */
    .board-pill-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin-top: 20px;
      flex-wrap: wrap;
    }
    .mode-pill {
      padding: 8px 16px;
      border-radius: 999px;
      background: var(--studio-light);
      border: 1px solid var(--studio-border);
      font-size: 13px;
      font-weight: 500;
      color: var(--ink-secondary);
      transition: all 0.2s ease;
    }
    .mode-pill.active {
      background: var(--ink-primary);
      color: #FFFFFF;
      border-color: var(--ink-primary);
    }
    .mode-pill:hover:not(.active) {
      border-color: var(--ink-primary);
      color: var(--ink-primary);
    }

    /* 32" Stand TV Stage */
    .stand-stage {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 40px auto 0;
      max-width: 500px;
      position: relative;
    }
    .stand-pivot-wrapper {
      width: 360px;
      height: 360px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .stand-tv-chassis {
      width: 330px;
      height: 204px;
      background: linear-gradient(145deg, #FFFFFF 0%, #F0F2F5 60%, #E4E6EA 100%);
      border-radius: 16px;
      padding: 8px 8px 24px 8px;
      box-shadow:
        0 24px 48px -10px rgba(0, 0, 0, 0.2),
        0 4px 12px rgba(0, 0, 0, 0.08),
        0 0 0 1px rgba(255, 255, 255, 0.95) inset,
        0 0 0 1.5px rgba(0, 0, 0, 0.08);
      transform-origin: center center;
      transform: rotate(0deg);
      transition: transform 0.75s cubic-bezier(0.25, 1, 0.35, 1), box-shadow 0.75s ease;
      position: relative;
      display: flex;
      flex-direction: column;
      z-index: 5;
    }
    .stand-tv-chassis.portrait {
      transform: rotate(-90deg);
      box-shadow:
        -24px 0 48px -10px rgba(0, 0, 0, 0.2),
        -4px 0 12px rgba(0, 0, 0, 0.08),
        0 0 0 1px rgba(255, 255, 255, 0.95) inset,
        0 0 0 1.5px rgba(0, 0, 0, 0.08);
    }
    .stand-screen-inner {
      width: 314px;
      height: 172px;
      background: #000;
      border-radius: 9px;
      overflow: hidden;
      position: relative;
    }
    .stand-gyro-content {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 314px;
      height: 172px;
      transform: translate(-50%, -50%) rotate(0deg);
      transition: transform 0.75s cubic-bezier(0.25, 1, 0.35, 1), width 0.75s ease, height 0.75s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      background: url('assets/53771.jpg') center/cover no-repeat;
    }
    .stand-tv-chassis.portrait .stand-gyro-content {
      width: 172px;
      height: 314px;
      transform: translate(-50%, -50%) rotate(90deg);
    }
    .stand-chin-text {
      height: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #6E6E73;
      text-transform: uppercase;
    }
    .stand-pole {
      width: 14px;
      height: 180px;
      background: linear-gradient(90deg, #D0D3D9 0%, #FFFFFF 50%, #C4C8CF 100%);
      margin-top: -30px;
      border-radius: 7px;
      box-shadow: 0 6px 16px rgba(0,0,0,0.1);
      z-index: 2;
    }
    .stand-base {
      width: 160px;
      height: 24px;
      background: radial-gradient(ellipse at 50% 40%, #FFFFFF 0%, #EBEDF2 65%, #D6DAE2 100%);
      border-radius: 50%;
      box-shadow:
        0 14px 28px -6px rgba(0, 0, 0, 0.22),
        0 2px 6px rgba(0, 0, 0, 0.08);
      margin-top: -8px;
      z-index: 1;
    }

    /* Grid Cards */
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 40px;
    }
    @media (max-width: 900px) {
      .grid-3 { grid-template-columns: 1fr; }
      .grid-4 { grid-template-columns: repeat(2, 1fr); }
      .section-title { font-size: 36px; }
      .section-sub { font-size: 18px; }
    }
    @media (max-width: 600px) {
      .grid-4 { grid-template-columns: 1fr; }
    }

    .feature-card {
      background: var(--studio-light);
      border-radius: 20px;
      padding: 32px;
      border: 1px solid rgba(0,0,0,0.05);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .feature-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.06);
    }
    .feature-icon {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
      color: var(--blue-accent);
    }
    .feature-card h3 {
      font-size: 21px;
      font-weight: 600;
      color: var(--ink-primary);
      margin-bottom: 10px;
    }
    .feature-card p {
      font-size: 15px;
      color: var(--ink-secondary);
      line-height: 1.45;
    }

    /* Real Proof Photo Gallery */
    .gallery-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      grid-gap: 20px;
      margin-top: 40px;
    }
    @media (max-width: 860px) {
      .gallery-grid { grid-template-columns: 1fr; }
    }
    .gallery-item {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      background: #E5E5EA;
      aspect-ratio: 4/3;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }
    .gallery-item.large {
      aspect-ratio: 16/10;
    }
    .gallery-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }
    .gallery-item:hover img {
      transform: scale(1.03);
    }
    .gallery-caption {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 16px 20px;
      background: linear-gradient(to top, rgba(0,0,0,0.75), transparent);
      color: #FFFFFF;
      font-size: 13px;
      font-weight: 500;
    }

    /* Comparison Table */
    .table-wrapper {
      margin-top: 40px;
      overflow-x: auto;
      border-radius: 20px;
      border: 1px solid var(--studio-border);
      background: #FFFFFF;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 14px;
    }
    th, td {
      padding: 16px 20px;
      border-bottom: 1px solid var(--studio-light);
    }
    th {
      background: var(--studio-light);
      font-weight: 600;
      color: var(--ink-primary);
    }
    tr:last-child td { border-bottom: none; }
    .spec-tag {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      background: #EBF5FF;
      color: var(--blue-accent);
    }

    /* Configurator Option Cards */
    .config-box {
      background: var(--studio-light);
      border-radius: 24px;
      padding: 40px;
      margin-top: 48px;
      border: 1px solid rgba(0,0,0,0.05);
    }
    .option-group {
      margin-bottom: 30px;
    }
    .option-group-title {
      font-size: 17px;
      font-weight: 600;
      margin-bottom: 14px;
    }
    .option-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
    }
    .opt-card {
      background: #FFFFFF;
      border: 1px solid var(--studio-border);
      border-radius: 14px;
      padding: 18px;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }
    .opt-card:hover { border-color: var(--ink-secondary); }
    .opt-card.selected {
      border: 2px solid var(--blue-accent);
      padding: 17px;
      background: #FDFDFE;
    }
    .opt-title { font-weight: 600; font-size: 15px; margin-bottom: 4px; }
    .opt-desc { font-size: 13px; color: var(--ink-secondary); line-height: 1.35; }
    .opt-price { font-size: 14px; font-weight: 600; color: var(--ink-primary); margin-top: 10px; }

    /* Shopping Bag Drawer */
    .bag-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(4px);
      z-index: 100;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }
    .bag-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }
    .bag-drawer {
      position: fixed;
      top: 0;
      right: -480px;
      width: 100%;
      max-width: 460px;
      height: 100%;
      background: #FFFFFF;
      z-index: 101;
      box-shadow: -10px 0 30px rgba(0,0,0,0.2);
      transition: right 0.35s cubic-bezier(0.2, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }
    .bag-drawer.open { right: 0; }
    .bag-header {
      padding: 20px 24px;
      border-bottom: 1px solid var(--studio-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .bag-title { font-size: 19px; font-weight: 600; }
    .bag-body {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
    }
    .bag-item {
      display: flex;
      justify-content: space-between;
      padding-bottom: 20px;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--studio-light);
    }
    .bag-footer {
      padding: 24px;
      border-top: 1px solid var(--studio-border);
      background: var(--studio-light);
    }

    /* Printable Quotation Sheet */
    @media print {
      body * { visibility: hidden; }
      #quotationPrintSheet, #quotationPrintSheet * { visibility: visible; }
      #quotationPrintSheet {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        background: #FFFFFF !important;
        color: #000000 !important;
        padding: 40px;
      }
    }

    /* Footer */
    footer {
      background: var(--studio-light);
      border-top: 1px solid var(--studio-border);
      padding: 60px 24px 40px;
      font-size: 12px;
      color: var(--ink-secondary);
    }
    .footer-links a { margin-right: 18px; color: var(--ink-secondary); }
    .footer-links a:hover { color: var(--ink-primary); text-decoration: underline; }
  </style>
</head>
<body>

  <!-- ==================== 1. STICKY FROSTED NAVBAR ==================== -->
  <header class="nav-frosted">
    <div class="container" style="display: flex; align-items: center; justify-content: space-between; height: 100%;">
      <!-- Brand Logo -->
      <a href="#top" style="display: flex; align-items: center; gap: 8px;" aria-label="Syndo Store">
        <svg width="125" height="32" viewBox="0 0 165 42" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="syndoSLogoGrad" x1="2" y1="4" x2="34" y2="38" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#00C2FF"/>
              <stop offset="55%" stop-color="#0077ED"/>
              <stop offset="100%" stop-color="#0047AB"/>
            </linearGradient>
          </defs>
          <path d="M29.5 5H15.5C9.4 5 5 8.9 5 14.3C5 19.6 9.3 22.5 15.6 23.6L22.5 24.7C25.3 25.2 26.8 26.4 26.8 28.5C26.8 30.8 24.7 32.3 21.2 32.3H6.8L4 38.8H22C29.1 38.8 34.2 34.7 34.2 28.7C34.2 23.1 30.1 20.1 23.2 18.9L16.3 17.8C13.7 17.3 12.5 16.2 12.5 14.4C12.5 12.3 14.4 11.2 17.4 11.2H32.2L29.5 5Z" fill="url(#syndoSLogoGrad)"/>
          <text x="39" y="32" fill="#0A1A3A" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Inter', sans-serif" font-weight="700" font-size="30" letter-spacing="-0.03em">yndo</text>
        </svg>
        <span style="font-size: 10px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; background: #E5E5EA; color: #1D1D1F; padding: 2px 7px; border-radius: 999px;" data-i18n="badge_direct">Online Direct</span>
      </a>

      <!-- Desktop Nav Links -->
      <nav style="display: flex; gap: 28px; font-size: 13px; font-weight: 500;">
        <a href="#hero-board" class="nav-link" data-i18n="nav_board">Interactive Board</a>
        <a href="#hero-stand" class="nav-link" data-i18n="nav_stand">Stand TV</a>
        <a href="#hero-dispensing" class="nav-link" data-i18n="nav_dispensing">Smart Dispensing</a>
        <a href="#real-proof" class="nav-link" data-i18n="nav_proof">Real Proof</a>
        <a href="#specs-compare" class="nav-link" data-i18n="nav_specs">Tech Specs</a>
        <a href="#shop-config" class="nav-link" data-i18n="nav_store">Store</a>
      </nav>

      <!-- Right Actions: Language & Bag -->
      <div style="display: flex; align-items: center; gap: 16px;">
        <button id="langToggleBtn" type="button" style="font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px; background: #EFEFF4; color: var(--ink-primary);">
          EN / 简体中文
        </button>

        <button id="openBagBtn" type="button" style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: var(--ink-primary); padding: 4px;" aria-label="Shopping Bag">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          <span id="bagCounter" style="background: var(--ink-primary); color: #FFF; font-size: 11px; font-weight: 700; border-radius: 999px; min-width: 20px; height: 20px; display: inline-flex; align-items: center; justify-content: center; padding: 0 4px;">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ==================== 2. ANNOUNCEMENT RIBBON ==================== -->
  <div id="top" class="ribbon">
    <span data-i18n="ribbon_text">Malaysia Online Direct Flagship &bull; Door-to-Door Nationwide Delivery &bull; Scheduled On-Site Installation</span>
    <a href="#shop-config" data-i18n="ribbon_cta">Order Online Direct &rsaquo;</a>
  </div>

  <!-- ==================== 3. HERO 1: SYNDO INTERACTIVE BOARD ==================== -->
  <section id="hero-board" style="text-align: center; background: #FFFFFF;">
    <div class="container">
      <p class="section-eyebrow" data-i18n="board_eyebrow">65" &bull; 75" &bull; 86" 4K UHD &bull; DUAL OS ANDROID 14 + WINDOWS OPS</p>
      <h1 class="section-title" data-i18n="board_title">Syndo Interactive Board</h1>
      <p class="section-sub" data-i18n="board_sub">Zero-Bonding 4K Touch Display. Powered by Android 14 &amp; Intel OPS.</p>
      <p class="section-price" data-i18n="board_price">From RM 5,999 (Online Direct) &bull; or RM 499.92/mo. for 12 mos.</p>

      <div style="display: flex; align-items: center; justify-content: center; gap: 16px;">
        <a href="#shop-config" class="btn-primary" data-i18n="btn_buy_now">Configure &amp; Buy</a>
        <a href="#specs-compare" class="btn-link" data-i18n="link_compare">Compare specs &rsaquo;</a>
      </div>

      <!-- Real Interactive Board Hardware Simulation -->
      <div class="board-stage select-none">
        <!-- 48MP AI Camera Bar -->
        <div class="board-cam-bar">
          <span class="cam-mic"></span>
          <span class="cam-mic"></span>
          <div class="cam-lens"><div class="cam-pupil"></div></div>
          <span class="cam-mic"></span>
          <span class="cam-mic"></span>
        </div>

        <!-- Brushed Matte Bezel -->
        <div class="board-bezel">
          <div class="board-screen-glass">
            <!-- MODE 1: ANDROID 14 HOME -->
            <div id="boardOsAndroid" class="board-os-view android-wallpaper active">
              <div class="android-topbar">
                <span>AP: SyndoBoard_5G (192.168.1.108)</span>
                <span>Powered by Android 14 &bull; Wi-Fi 6</span>
              </div>
              <div class="android-clock-section">
                <div id="liveClock" class="android-clock">04:33</div>
                <div class="android-date">26-11-2026 &nbsp; PM &nbsp; Thursday</div>
                <div class="android-search">
                  <span>Search files, web, notes...</span>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
                </div>
              </div>
              <div class="android-dock">
                <div class="dock-app" onclick="switchBoardMode('whiteboard')">
                  <div class="dock-icon" style="background: linear-gradient(135deg, #FF3B30, #FF2D55);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFF" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>
                  </div>
                  <span class="dock-label">Whiteboard</span>
                </div>
                <div class="dock-app" onclick="alert('Wireless Cast activated: Scan QR code or use Syndo Cast App to mirror 4 devices simultaneously.')">
                  <div class="dock-icon" style="background: linear-gradient(135deg, #007AFF, #5856D6);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFF" stroke-width="2"><path d="M2 8V6a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-6"/><path d="M2 12a9 9 0 0 1 8 8"/><path d="M2 16a5 5 0 0 1 4 4"/><line x1="2" y1="20" x2="2.01" y2="20"/></svg>
                  </div>
                  <span class="dock-label">Wireless Cast</span>
                </div>
                <div class="dock-app" onclick="switchBoardMode('windows')">
                  <div class="dock-icon" style="background: linear-gradient(135deg, #00C7BE, #30B0C7);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFF" stroke-width="2"><rect x="3" y="3" width="8" height="8"/><rect x="13" y="3" width="8" height="8"/><rect x="3" y="13" width="8" height="8"/><rect x="13" y="13" width="8" height="8"/></svg>
                  </div>
                  <span class="dock-label">Windows OPS</span>
                </div>
                <div class="dock-app" onclick="switchBoardMode('room')">
                  <div class="dock-icon" style="background: linear-gradient(135deg, #34C759, #30D158);">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFF" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                  </div>
                  <span class="dock-label">Room View</span>
                </div>
              </div>
            </div>

            <!-- MODE 2: INTERACTIVE WHITEBOARD -->
            <div id="boardOsWhiteboard" class="board-os-view whiteboard-view">
              <div class="whiteboard-toolbar">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <button type="button" class="wb-btn" onclick="switchBoardMode('android')">&larr; Android Home</button>
                  <span style="font-size: 13px; font-weight: 600; color: #1D1D1F; margin-left: 8px;">Syndo Note Canvas</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="color-swatch active" style="background: #0077ED;" onclick="setPenColor('#0077ED', this)"></span>
                  <span class="color-swatch" style="background: #FF3B30;" onclick="setPenColor('#FF3B30', this)"></span>
                  <span class="color-swatch" style="background: #34C759;" onclick="setPenColor('#34C759', this)"></span>
                  <span class="color-swatch" style="background: #1D1D1F;" onclick="setPenColor('#1D1D1F', this)"></span>
                  <button type="button" class="wb-btn" onclick="clearCanvas()">Clear</button>
                  <button type="button" class="wb-btn" style="background: var(--blue-accent); color: #FFF; border: none;" onclick="downloadCanvas()">Save PNG</button>
                </div>
              </div>
              <div class="canvas-container">
                <canvas id="whiteboardCanvas"></canvas>
              </div>
            </div>

            <!-- MODE 3: WINDOWS 11 PRO OPS -->
            <div id="boardOsWindows" class="board-os-view windows-view">
              <div class="windows-overlay"></div>
              <div class="windows-content">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <div style="background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 6px; font-size: 12px;">
                    Intel Core i7-12700H &bull; 16GB RAM &bull; Windows 11 Pro OPS Module
                  </div>
                  <button type="button" class="wb-btn" onclick="switchBoardMode('android')">Switch to Android 14</button>
                </div>
                <div style="text-align: center; margin: auto;">
                  <h2 style="font-size: 32px; font-weight: 600; text-shadow: 0 2px 8px rgba(0,0,0,0.6);">Seamless Dual-OS OPS Module</h2>
                  <p style="font-size: 15px; opacity: 0.9; margin-top: 6px;">Native Zoom Rooms, Microsoft Teams, Office 365, &amp; CAD with zero lag.</p>
                </div>
                <div class="win-taskbar">
                  <div class="win-icon" title="Windows Start">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="#0078D4"><rect x="3" y="3" width="8" height="8"/><rect x="13" y="3" width="8" height="8"/><rect x="3" y="13" width="8" height="8"/><rect x="13" y="13" width="8" height="8"/></svg>
                  </div>
                  <div class="win-icon" title="Microsoft Teams"><span style="background: #464EB8; width: 18px; height: 18px; border-radius: 4px; display: inline-block;"></span></div>
                  <div class="win-icon" title="Zoom Meetings"><span style="background: #2D8CFF; width: 18px; height: 18px; border-radius: 4px; display: inline-block;"></span></div>
                  <div class="win-icon" title="Microsoft Edge"><span style="background: #0078D7; width: 18px; height: 18px; border-radius: 50%; display: inline-block;"></span></div>
                </div>
              </div>
            </div>

            <!-- MODE 4: REAL CONFERENCE ROOM PHOTO VIEW -->
            <div id="boardOsRoom" class="board-os-view room-view">
              <div style="position: absolute; bottom: 16px; left: 16px; background: rgba(0,0,0,0.7); backdrop-filter: blur(8px); padding: 8px 16px; border-radius: 8px; color: #FFF; font-size: 13px;">
                <strong>Real Boardroom Installation</strong> &bull; Syndo 75" with Mobile Stand in Corporate Meeting Room
              </div>
              <button type="button" class="wb-btn" style="position: absolute; top: 16px; right: 16px;" onclick="switchBoardMode('android')">Back to UI Demo</button>
            </div>

          </div>

          <!-- Chin Badge -->
          <div class="board-chin">
            <span>Syndo</span>
          </div>
        </div>

        <!-- Pill Switchers -->
        <div class="board-pill-bar">
          <button id="pillAndroid" type="button" class="mode-pill active" onclick="switchBoardMode('android')">Android 14 UI</button>
          <button id="pillWhiteboard" type="button" class="mode-pill" onclick="switchBoardMode('whiteboard')">Live Whiteboard Canvas</button>
          <button id="pillWindows" type="button" class="mode-pill" onclick="switchBoardMode('windows')">Windows 11 OPS</button>
          <button id="pillRoom" type="button" class="mode-pill" onclick="switchBoardMode('room')">Real Boardroom Photo</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== 4. HERO 2: SYNDO STAND TV ==================== -->
  <section id="hero-stand" style="background: var(--studio-light); text-align: center;">
    <div class="container">
      <p class="section-eyebrow" data-i18n="stand_eyebrow">32" 4K MOBILE SMART DISPLAY &bull; 6-HOUR BATTERY &bull; OMNI-WHEELS</p>
      <h2 class="section-title" data-i18n="stand_title">Syndo Stand TV</h2>
      <p class="section-sub" data-i18n="stand_sub">Roll it anywhere. Rotate smoothly. Built-in battery and full touch agility.</p>
      <p class="section-price" data-i18n="stand_price">From RM 2,999 (Online Direct) &bull; or RM 249.92/mo. for 12 mos.</p>

      <div style="display: flex; align-items: center; justify-content: center; gap: 16px;">
        <button type="button" class="btn-primary" onclick="openConfig('stand', '32')" data-i18n="btn_buy_stand">Buy Stand TV</button>
        <button type="button" id="togglePivotBtn" class="btn-blue" onclick="toggleStandPivot()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 6px;"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/></svg>
          <span id="pivotBtnLabel">Rotate to Portrait (9:16)</span>
        </button>
      </div>

      <!-- Stand TV 3D Pivot & Gyro Simulation -->
      <div class="stand-stage">
        <div class="stand-pivot-wrapper">
          <div id="standChassis" class="stand-tv-chassis">
            <div class="stand-screen-inner">
              <div id="standGyroUi" class="stand-gyro-content"></div>
            </div>
            <div class="stand-chin-text">Syndo</div>
          </div>
        </div>
        <div class="stand-pole"></div>
        <div class="stand-base"></div>
      </div>
    </div>
  </section>

  <!-- ==================== 5. HERO 3: SMART DISPENSING ==================== -->
  <section id="hero-dispensing" style="background: #FFFFFF;">
    <div class="container" style="text-align: center;">
      <p class="section-eyebrow" data-i18n="disp_eyebrow">HEALTHCARE &amp; PHARMACY AUTOMATION</p>
      <h2 class="section-title" data-i18n="disp_title">Syndo Smart Dispensing</h2>
      <p class="section-sub" data-i18n="disp_sub">Zero-error optical tablet counting, automated vial packaging, and clinical PMS integration.</p>

      <div class="grid-3">
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h3>99.99% Optical Accuracy</h3>
          <p>Multi-angle high-speed machine vision counts odd-shaped tablets, softgels, and translucent capsules without calibration drift.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          </div>
          <h3>Under 3s per Prescription</h3>
          <p>Dramatically reduces patient waiting times in retail pharmacies and outpatient clinics while eliminating human counting fatigue.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          </div>
          <h3>HIS / PMS Seamless Sync</h3>
          <p>Instant API handshake with leading Malaysian clinic management systems (Klinify, Plato, MediCloud) for automated batch records.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== 6. REAL PROOF & SHOWROOM GALLERY ==================== -->
  <section id="real-proof" style="background: var(--studio-light);">
    <div class="container" style="text-align: center;">
      <p class="section-eyebrow" data-i18n="proof_eyebrow">REAL HARDWARE &bull; LIVE INSTALLATIONS</p>
      <h2 class="section-title" data-i18n="proof_title">Engineered for Excellence</h2>
      <p class="section-sub" data-i18n="proof_sub">Actual installations across Malaysian enterprises, healthcare centers, and executive offices.</p>

      <div class="gallery-grid">
        <div class="gallery-item large">
          <img src="assets/53778.jpg" alt="Syndo Interactive Board in Boardroom" loading="lazy" />
          <div class="gallery-caption">Syndo 75" Interactive Board &bull; Corporate Boardroom Installation</div>
        </div>
        <div class="gallery-item">
          <img src="assets/53779.jpg" alt="Syndo Stand TV in Living Room" loading="lazy" />
          <div class="gallery-caption">Syndo Stand TV 32" &bull; Executive Lounge Mobility</div>
        </div>
        <div class="gallery-item">
          <img src="assets/125950.jpg" alt="Syndo CNC Bezel Quality" loading="lazy" />
          <div class="gallery-caption">CNC Aluminum Bezel &bull; Precision "Syndo" Chin Badge</div>
        </div>
        <div class="gallery-item">
          <img src="assets/53771.jpg" alt="Stand TV Android Launcher" loading="lazy" />
          <div class="gallery-caption">Portrait Launcher &bull; EShare, Gemini &amp; Note Suite</div>
        </div>
        <div class="gallery-item">
          <img src="assets/53769.jpg" alt="Quality Wi-Fi Testing" loading="lazy" />
          <div class="gallery-caption">Factory QC &bull; Dual-Band 5GHz Wi-Fi 6 Calibration</div>
        </div>
        <div class="gallery-item">
          <img src="assets/442570.jpg" alt="Android 14 Home UI" loading="lazy" />
          <div class="gallery-caption">Syndo OS 14 &bull; Zero-Bonding 4K Antiglare Glass</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== 7. TECH SPECS & COMPARISON MATRIX ==================== -->
  <section id="specs-compare" style="background: #FFFFFF;">
    <div class="container">
      <div style="text-align: center;">
        <p class="section-eyebrow" data-i18n="specs_eyebrow">TECH SPECS COMPARISON</p>
        <h2 class="section-title" data-i18n="specs_title">Find the Right Syndo for You</h2>
        <p class="section-sub" data-i18n="specs_sub">Detailed specifications across all display sizes and configurations.</p>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Syndo Board 65"</th>
              <th>Syndo Board 75"</th>
              <th>Syndo Board 86"</th>
              <th>Syndo Stand TV 32"</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Target Room Size</strong></td>
              <td>Meeting Room (6-12 pax)</td>
              <td>Boardroom (12-25 pax)</td>
              <td>Auditorium / Hall (25+ pax)</td>
              <td>Mobile / Office / Home</td>
            </tr>
            <tr>
              <td><strong>Display Resolution</strong></td>
              <td><span class="spec-tag">4K UHD (3840 &times; 2160)</span></td>
              <td><span class="spec-tag">4K UHD (3840 &times; 2160)</span></td>
              <td><span class="spec-tag">4K UHD (3840 &times; 2160)</span></td>
              <td><span class="spec-tag">4K Touch Screen</span></td>
            </tr>
            <tr>
              <td><strong>Bonding Technology</strong></td>
              <td>Zero-Bonding 7H Tempered</td>
              <td>Zero-Bonding 7H Tempered</td>
              <td>Zero-Bonding 7H Tempered</td>
              <td>Anti-Glare Capacitive Touch</td>
            </tr>
            <tr>
              <td><strong>Operating System</strong></td>
              <td>Android 14 + Optional OPS Win11</td>
              <td>Android 14 + Optional OPS Win11</td>
              <td>Android 14 + Optional OPS Win11</td>
              <td>Android 13 Smart OS</td>
            </tr>
            <tr>
              <td><strong>AI Camera &amp; Mic</strong></td>
              <td>48MP AI Camera + 8-Mic Array</td>
              <td>48MP AI Camera + 8-Mic Array</td>
              <td>48MP AI Camera + 8-Mic Array</td>
              <td>Integrated Front Cam + Mic</td>
            </tr>
            <tr>
              <td><strong>Audio Output</strong></td>
              <td>2 &times; 20W Hi-Fi Speakers</td>
              <td>2 &times; 20W + Subwoofer</td>
              <td>2 &times; 25W + Subwoofer</td>
              <td>2 &times; 10W Stereo Bass</td>
            </tr>
            <tr>
              <td><strong>Wireless Cast</strong></td>
              <td>4-Screen Split Cast (AirPlay, Miracast)</td>
              <td>4-Screen Split Cast (AirPlay, Miracast)</td>
              <td>4-Screen Split Cast (AirPlay, Miracast)</td>
              <td>EShare + Screen Cast</td>
            </tr>
            <tr>
              <td><strong>Mobility</strong></td>
              <td>Wall Mount / Optional Heavy Trolley</td>
              <td>Wall Mount / Optional Heavy Trolley</td>
              <td>Wall Mount / Optional Heavy Trolley</td>
              <td>5-Wheel Base + 6Hr Battery</td>
            </tr>
            <tr>
              <td><strong>Online Direct Price</strong></td>
              <td><strong>RM 5,999</strong></td>
              <td><strong>RM 7,999</strong></td>
              <td><strong>RM 10,999</strong></td>
              <td><strong>RM 2,999</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ==================== 8. CONFIGURATOR & STORE ==================== -->
  <section id="shop-config" style="background: var(--studio-light);">
    <div class="container">
      <div style="text-align: center;">
        <p class="section-eyebrow" data-i18n="config_eyebrow">CUSTOMIZE YOUR ORDER</p>
        <h2 class="section-title" data-i18n="config_title">Build Your Syndo Package</h2>
        <p class="section-sub" data-i18n="config_sub">Choose screen size, add-on OPS Windows modules, and accessories with instant price calculation.</p>
      </div>

      <div class="config-box">
        <!-- 1. Select Product & Size -->
        <div class="option-group">
          <div class="option-group-title">1. Select Product &amp; Display Size</div>
          <div class="option-cards" id="productOptions">
            <div class="opt-card selected" onclick="selectProduct('board_65', 5999, this)">
              <div class="opt-title">Syndo Board 65"</div>
              <div class="opt-desc">4K Zero-Bonding &bull; Small-to-Mid Rooms</div>
              <div class="opt-price">RM 5,999</div>
            </div>
            <div class="opt-card" onclick="selectProduct('board_75', 7999, this)">
              <div class="opt-title">Syndo Board 75"</div>
              <div class="opt-desc">4K Zero-Bonding &bull; Standard Boardroom</div>
              <div class="opt-price">RM 7,999</div>
            </div>
            <div class="opt-card" onclick="selectProduct('board_86', 10999, this)">
              <div class="opt-title">Syndo Board 86"</div>
              <div class="opt-desc">4K Zero-Bonding &bull; Large Lecture Hall</div>
              <div class="opt-price">RM 10,999</div>
            </div>
            <div class="opt-card" onclick="selectProduct('stand_32', 2999, this)">
              <div class="opt-title">Syndo Stand TV 32"</div>
              <div class="opt-desc">Rotating 4K &bull; Wheeled Pole &bull; Battery</div>
              <div class="opt-price">RM 2,999</div>
            </div>
          </div>
        </div>

        <!-- 2. Select OPS PC Module -->
        <div class="option-group" id="opsOptionGroup">
          <div class="option-group-title">2. Windows OPS PC Module (Optional Dual-OS)</div>
          <div class="option-cards" id="opsOptions">
            <div class="opt-card selected" onclick="selectOps('none', 0, this)">
              <div class="opt-title">Android 14 Native Only</div>
              <div class="opt-desc">Includes Whiteboard, EShare Cast &amp; Apps</div>
              <div class="opt-price">+ RM 0</div>
            </div>
            <div class="opt-card" onclick="selectOps('i5', 1200, this)">
              <div class="opt-title">Intel Core i5 OPS Module</div>
              <div class="opt-desc">16GB RAM &bull; 256GB SSD &bull; Windows 11 Pro</div>
              <div class="opt-price">+ RM 1,200</div>
            </div>
            <div class="opt-card" onclick="selectOps('i7', 1800, this)">
              <div class="opt-title">Intel Core i7 OPS Module</div>
              <div class="opt-desc">16GB RAM &bull; 512GB SSD &bull; Windows 11 Pro</div>
              <div class="opt-price">+ RM 1,800</div>
            </div>
          </div>
        </div>

        <!-- 3. Accessories -->
        <div class="option-group">
          <div class="option-group-title">3. Official Accessories</div>
          <div class="option-cards">
            <div class="opt-card" id="accStandCard" onclick="toggleAccessory('stand', 450, this)">
              <div class="opt-title">Heavy-Duty Mobile Trolley</div>
              <div class="opt-desc">Silent lockable casters &bull; Shelf for OPS/Laptop</div>
              <div class="opt-price">+ RM 450</div>
            </div>
            <div class="opt-card" id="accDongleCard" onclick="toggleAccessory('dongle', 280, this)">
              <div class="opt-title">4K USB Cast Dongle</div>
              <div class="opt-desc">Plug &amp; play 1-click screen mirror for laptops</div>
              <div class="opt-price">+ RM 280</div>
            </div>
            <div class="opt-card" id="accPenCard" onclick="toggleAccessory('pen', 180, this)">
              <div class="opt-title">Smart Dual Stylus Pack</div>
              <div class="opt-desc">Magnetic precision dual-nib styluses (Pair)</div>
              <div class="opt-price">+ RM 180</div>
            </div>
          </div>
        </div>

        <!-- Total Summary Bar -->
        <div style="background: #FFFFFF; border-radius: 18px; padding: 24px 30px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
          <div>
            <div style="font-size: 13px; color: var(--ink-secondary); font-weight: 500;">Calculated Online Direct Total</div>
            <div id="configTotalPrice" style="font-size: 32px; font-weight: 700; color: var(--ink-primary); line-height: 1.1;">RM 5,999</div>
            <div id="configInstallmentPrice" style="font-size: 13px; color: var(--linkblue); font-weight: 500; margin-top: 4px;">or RM 499.92/mo. for 12 mos. with 0% installment</div>
          </div>
          <div style="display: flex; gap: 14px;">
            <button type="button" class="btn-blue" onclick="addCurrentConfigToBag()">Add to Bag</button>
            <button type="button" class="btn-primary" onclick="openQuotationSheet()">Print / Save Quotation</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== 9. SHOPPING BAG DRAWER ==================== -->
  <div id="bagOverlay" class="bag-overlay" onclick="closeBag()"></div>
  <div id="bagDrawer" class="bag-drawer">
    <div class="bag-header">
      <div class="bag-title">Review Your Bag</div>
      <button type="button" onclick="closeBag()" style="font-size: 24px; line-height: 1; color: var(--ink-secondary);">&times;</button>
    </div>
    <div id="bagItemsContainer" class="bag-body">
      <!-- Items dynamically populated -->
      <div id="emptyBagMsg" style="text-align: center; color: var(--ink-secondary); padding: 60px 0;">
        Your shopping bag is empty.
      </div>
    </div>
    <div class="bag-footer">
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 14px; color: var(--ink-secondary);">
        <span>Door-to-Door Delivery (Malaysia)</span>
        <span style="color: var(--success); font-weight: 600;">FREE</span>
      </div>
      <div style="display: flex; justify-content: space-between; margin-bottom: 18px; font-size: 14px; color: var(--ink-secondary);">
        <span>On-Site Professional Installation</span>
        <span style="color: var(--success); font-weight: 600;">FREE</span>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 20px;">
        <span style="font-size: 17px; font-weight: 600;">Total</span>
        <span id="bagGrandTotal" style="font-size: 24px; font-weight: 700; color: var(--ink-primary);">RM 0</span>
      </div>
      <button type="button" class="btn-blue" style="width: 100%; padding: 14px; font-size: 16px;" onclick="checkoutWhatsApp()">
        Order Directly via WhatsApp
      </button>
      <button type="button" class="btn-primary" style="width: 100%; padding: 12px; font-size: 14px; margin-top: 10px;" onclick="openQuotationSheet()">
        Generate Corporate Quotation PDF
      </button>
    </div>
  </div>

  <!-- ==================== 10. PRINTABLE OFFICIAL QUOTATION SHEET ==================== -->
  <div id="quotationPrintSheet" style="display: none; padding: 40px; font-family: -apple-system, sans-serif;">
    <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #000; padding-bottom: 20px;">
      <div>
        <h1 style="font-size: 26px; font-weight: 800; color: #0A1A3A;">PORTLAND ASSETS (MALAYSIA) SDN. BHD.</h1>
        <p style="font-size: 12px; color: #555; margin-top: 4px;">Exclusive Distributor for SyndoTech Malaysia &bull; Co. Reg: 202601004189</p>
        <p style="font-size: 12px; color: #555;">Website: https://syndotech.my &bull; Email: sales@syndotech.my</p>
      </div>
      <div style="text-align: right;">
        <h2 style="font-size: 22px; font-weight: 700; color: #0077ED;">OFFICIAL QUOTATION</h2>
        <p id="quoteRefNumber" style="font-size: 12px; font-weight: 600; margin-top: 4px;">REF: SYN-2026-0891</p>
        <p id="quoteDate" style="font-size: 12px; color: #555;">Date: 27 Nov 2026</p>
      </div>
    </div>

    <div style="margin: 24px 0;">
      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px;">Customer / Organization Information:</h3>
      <p style="font-size: 13px;">Corporate Direct Client &bull; Standard Terms: 100% Door-to-Door Delivery &amp; Testing</p>
    </div>

    <table style="width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 13px;">
      <thead>
        <tr style="background: #F0F2F5; border-bottom: 1px solid #CCC;">
          <th style="padding: 10px; text-align: left;">Item Description</th>
          <th style="padding: 10px; text-align: center;">Qty</th>
          <th style="padding: 10px; text-align: right;">Unit Price (RM)</th>
          <th style="padding: 10px; text-align: right;">Amount (RM)</th>
        </tr>
      </thead>
      <tbody id="quoteTableItems">
        <!-- Dynamically injected -->
      </tbody>
      <tfoot>
        <tr style="border-top: 2px solid #000;">
          <td colspan="3" style="padding: 10px; font-weight: 700; text-align: right;">Subtotal:</td>
          <td id="quoteSubtotal" style="padding: 10px; font-weight: 700; text-align: right;">RM 0</td>
        </tr>
        <tr>
          <td colspan="3" style="padding: 6px 10px; text-align: right; color: #555;">Nationwide Delivery &amp; Setup:</td>
          <td style="padding: 6px 10px; text-align: right; color: #34C759; font-weight: 600;">COMPLIMENTARY</td>
        </tr>
        <tr style="border-top: 1px solid #CCC;">
          <td colspan="3" style="padding: 12px 10px; font-weight: 800; font-size: 16px; text-align: right;">Grand Total:</td>
          <td id="quoteGrandTotal" style="padding: 12px 10px; font-weight: 800; font-size: 18px; text-align: right; color: #0077ED;">RM 0</td>
        </tr>
      </tfoot>
    </table>

    <div style="margin-top: 40px; font-size: 12px; line-height: 1.6; color: #444; border-top: 1px solid #EEE; padding-top: 20px;">
      <p><strong>Terms &amp; Warranty:</strong></p>
      <p>1. 3-Year On-Site Hardware Warranty covering 4K panel, motherboard, and OPS module.</p>
      <p>2. Lead time: 2 - 5 working days within Klang Valley; 3 - 7 working days nationwide.</p>
      <p>3. Quotation valid for 30 calendar days from issue date.</p>
      <div style="display: flex; justify-content: space-between; margin-top: 40px;">
        <div>
          <p>Prepared by:</p>
          <div style="margin-top: 40px; border-top: 1px dashed #777; width: 180px;">SyndoTech Sales Division</div>
        </div>
        <div>
          <p>Confirmed &amp; Accepted by:</p>
          <div style="margin-top: 40px; border-top: 1px dashed #777; width: 180px;">Customer Signature &amp; Stamp</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ==================== 11. FOOTER ==================== -->
  <footer>
    <div class="container">
      <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 30px; margin-bottom: 30px;">
        <div>
          <h4 style="font-size: 14px; font-weight: 700; color: var(--ink-primary); margin-bottom: 10px;">SyndoTech Malaysia</h4>
          <p>Portland Assets (Malaysia) Sdn. Bhd. (202601004189)</p>
          <p>Official Online Direct Flagship Store</p>
          <p style="margin-top: 8px;">Klang Valley Corporate Showroom &bull; Selangor, Malaysia</p>
        </div>
        <div>
          <h4 style="font-size: 14px; font-weight: 700; color: var(--ink-primary); margin-bottom: 10px;">Products</h4>
          <p><a href="#hero-board" style="color: inherit;">Syndo Interactive Board (65" / 75" / 86")</a></p>
          <p><a href="#hero-stand" style="color: inherit;">Syndo Stand TV (32")</a></p>
          <p><a href="#hero-dispensing" style="color: inherit;">Syndo Smart Dispensing Solution</a></p>
        </div>
        <div>
          <h4 style="font-size: 14px; font-weight: 700; color: var(--ink-primary); margin-bottom: 10px;">Support &amp; Inquiries</h4>
          <p>Sales: sales@syndotech.my</p>
          <p>WhatsApp: +60 12-345 6789</p>
          <p>Operating Hours: Mon - Fri (9:00 AM - 6:00 PM)</p>
        </div>
      </div>
      <div style="border-top: 1px solid var(--studio-border); padding-top: 20px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
        <p>&copy; 2026 Portland Assets (Malaysia) Sdn. Bhd. &bull; SyndoTech. All rights reserved.</p>
        <div class="footer-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Sale</a>
          <a href="#">Warranty Guarantee</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==================== JAVASCRIPT LOGIC ==================== -->
  <script>
    // --- 1. STATE & CONFIGURATION ---
    const state = {
      lang: 'en',
      activeBoardMode: 'android',
      standPivotPortrait: false,
      selectedProduct: { id: 'board_65', name: 'Syndo Interactive Board 65"', price: 5999 },
      selectedOps: { id: 'none', name: 'Android 14 Native Only', price: 0 },
      selectedAccessories: {},
      bag: []
    };

    // --- 2. BILINGUAL DICTIONARY ---
    const i18n = {
      en: {
        badge_direct: 'Online Direct',
        nav_board: 'Interactive Board',
        nav_stand: 'Stand TV',
        nav_dispensing: 'Smart Dispensing',
        nav_proof: 'Real Proof',
        nav_specs: 'Tech Specs',
        nav_store: 'Store',
        ribbon_text: 'Malaysia Online Direct Flagship • Door-to-Door Nationwide Delivery • Scheduled On-Site Installation',
        ribbon_cta: 'Order Online Direct ›',
        board_eyebrow: '65" • 75" • 86" 4K UHD • DUAL OS ANDROID 14 + WINDOWS OPS',
        board_title: 'Syndo Interactive Board',
        board_sub: 'Zero-Bonding 4K Touch Display. Powered by Android 14 & Intel OPS.',
        board_price: 'From RM 5,999 (Online Direct) • or RM 499.92/mo. for 12 mos.',
        btn_buy_now: 'Configure & Buy',
        link_compare: 'Compare specs ›',
        stand_eyebrow: '32" 4K MOBILE SMART DISPLAY • 6-HOUR BATTERY • OMNI-WHEELS',
        stand_title: 'Syndo Stand TV',
        stand_sub: 'Roll it anywhere. Rotate smoothly. Built-in battery and full touch agility.',
        stand_price: 'From RM 2,999 (Online Direct) • or RM 249.92/mo. for 12 mos.',
        btn_buy_stand: 'Buy Stand TV',
        disp_eyebrow: 'HEALTHCARE & PHARMACY AUTOMATION',
        disp_title: 'Syndo Smart Dispensing',
        disp_sub: 'Zero-error optical tablet counting, automated vial packaging, and clinical PMS integration.',
        proof_eyebrow: 'REAL HARDWARE • LIVE INSTALLATIONS',
        proof_title: 'Engineered for Excellence',
        proof_sub: 'Actual installations across Malaysian enterprises, healthcare centers, and executive offices.',
        specs_eyebrow: 'TECH SPECS COMPARISON',
        specs_title: 'Find the Right Syndo for You',
        specs_sub: 'Detailed specifications across all display sizes and configurations.',
        config_eyebrow: 'CUSTOMIZE YOUR ORDER',
        config_title: 'Build Your Syndo Package',
        config_sub: 'Choose screen size, add-on OPS Windows modules, and accessories with instant price calculation.'
      },
      zh: {
        badge_direct: '官方直营',
        nav_board: '智能交互平板',
        nav_stand: '随心移动屏',
        nav_dispensing: '智能调剂系统',
        nav_proof: '实拍案例',
        nav_specs: '参数对比',
        nav_store: '在线商城',
        ribbon_text: '马来西亚官方直营旗舰 • 全马门到门顺丰空运/专车送达 • 专业上门安装调试',
        ribbon_cta: '立即在线选购 ›',
        board_eyebrow: '65寸 • 75寸 • 86寸 4K超高清 • 安卓14 + WINDOWS双系统',
        board_title: 'Syndo 智能交互平板',
        board_sub: '4K零贴合防眩触控大屏，搭载Android 14与英特尔OPS双系统架构。',
        board_price: '直营特惠 RM 5,999 起 • 12期免息月付仅 RM 499.92 起',
        btn_buy_now: '立即定制选购',
        link_compare: '对比规格参数 ›',
        stand_eyebrow: '32寸4K可移动智能屏 • 内置6小时电池 • 万向静音轮',
        stand_title: 'Syndo 随心旋转移动屏',
        stand_sub: '自由推移，横竖随心旋转。内置高容量电池，全屏触控畅快交互。',
        stand_price: '直营特惠 RM 2,999 起 • 12期免息月付仅 RM 249.92 起',
        btn_buy_stand: '选购随心屏',
        disp_eyebrow: '医疗门诊与智慧药房自动化',
        disp_title: 'Syndo 智能分药调剂系统',
        disp_sub: '0差错视觉高速药片计数、自动化封口装瓶，无缝对接门诊管理系统。',
        proof_eyebrow: '真实硬件 • 客户实拍案例',
        proof_title: '卓越品质，实机见证',
        proof_sub: '马来西亚众多知名企业会议室、医疗机构与高管办公室真实交付实拍。',
        specs_eyebrow: '技术参数全面对比',
        specs_title: '选择最契合您业务的 Syndo',
        specs_sub: '覆盖各尺寸触控显示屏与移动智能终端的核心参数一览。',
        config_eyebrow: '定制您的专属方案',
        config_title: '选配您的 Syndo 智能套装',
        config_sub: '选择屏幕尺寸、加装 Windows OPS 双系统电脑与官方配件，实时计算直营总价。'
      }
    };

    function toggleLanguage() {
      state.lang = state.lang === 'en' ? 'zh' : 'en';
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (i18n[state.lang] && i18n[state.lang][key]) {
          el.textContent = i18n[state.lang][key];
        }
      });
      document.getElementById('langToggleBtn').textContent = state.lang === 'en' ? 'EN / 简体中文' : '中文 / English';
    }
    document.getElementById('langToggleBtn').addEventListener('click', toggleLanguage);

    // --- 3. INTERACTIVE BOARD SCREEN MODES ---
    function switchBoardMode(mode) {
      state.activeBoardMode = mode;
      document.querySelectorAll('.board-os-view').forEach(v => v.classList.remove('active'));
      document.querySelectorAll('.mode-pill').forEach(p => p.classList.remove('active'));

      if (mode === 'android') {
        document.getElementById('boardOsAndroid').classList.add('active');
        document.getElementById('pillAndroid').classList.add('active');
      } else if (mode === 'whiteboard') {
        document.getElementById('boardOsWhiteboard').classList.add('active');
        document.getElementById('pillWhiteboard').classList.add('active');
        resizeCanvas();
      } else if (mode === 'windows') {
        document.getElementById('boardOsWindows').classList.add('active');
        document.getElementById('pillWindows').classList.add('active');
      } else if (mode === 'room') {
        document.getElementById('boardOsRoom').classList.add('active');
        document.getElementById('pillRoom').classList.add('active');
      }
    }

    // --- 4. WHITEBOARD CANVAS ENGINE ---
    const canvas = document.getElementById('whiteboardCanvas');
    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let penColor = '#0077ED';
    let penWidth = 3;

    function resizeCanvas() {
      const rect = canvas.parentElement.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {
        canvas.width = rect.width;
        canvas.height = rect.height;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
      }
    }
    window.addEventListener('resize', resizeCanvas);

    function setPenColor(color, swatchEl) {
      penColor = color;
      document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
      if (swatchEl) swatchEl.classList.add('active');
    }

    function clearCanvas() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function downloadCanvas() {
      const link = document.createElement('a');
      link.download = 'Syndo-Whiteboard-Drawing.png';
      link.href = canvas.toDataURL('image/png');
      link.click();
    }

    function getCanvasCoordinates(e) {
      const rect = canvas.getBoundingClientRect();
      return {
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
      };
    }

    canvas.addEventListener('pointerdown', (e) => {
      isDrawing = true;
      const { x, y } = getCanvasCoordinates(e);
      ctx.beginPath();
      ctx.moveTo(x, y);
    });

    canvas.addEventListener('pointermove', (e) => {
      if (!isDrawing) return;
      const { x, y } = getCanvasCoordinates(e);
      ctx.strokeStyle = penColor;
      ctx.lineWidth = penWidth;
      ctx.lineTo(x, y);
      ctx.stroke();
    });

    canvas.addEventListener('pointerup', () => { isDrawing = false; });
    canvas.addEventListener('pointercancel', () => { isDrawing = false; });

    // --- 5. STAND TV ROTATION & GYRO CONTROLLER ---
    function toggleStandPivot() {
      state.standPivotPortrait = !state.standPivotPortrait;
      const chassis = document.getElementById('standChassis');
      const label = document.getElementById('pivotBtnLabel');

      if (state.standPivotPortrait) {
        chassis.classList.add('portrait');
        label.textContent = 'Rotate to Landscape (16:9)';
      } else {
        chassis.classList.remove('portrait');
        label.textContent = 'Rotate to Portrait (9:16)';
      }
    }

    // --- 6. LIVE DIGITAL CLOCK ---
    function updateClock() {
      const now = new Date();
      let hours = now.getHours();
      let mins = now.getMinutes();
      hours = hours < 10 ? '0' + hours : hours;
      mins = mins < 10 ? '0' + mins : mins;
      const clockEl = document.getElementById('liveClock');
      if (clockEl) clockEl.textContent = hours + ':' + mins;
    }
    setInterval(updateClock, 1000);
    updateClock();

    // --- 7. CONFIGURATOR & PRICING ENGINE ---
    function selectProduct(id, price, card) {
      state.selectedProduct = {
        id,
        name: card.querySelector('.opt-title').textContent,
        price
      };
      document.querySelectorAll('#productOptions .opt-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');

      // Hide or show OPS options if Stand TV is selected
      const opsGroup = document.getElementById('opsOptionGroup');
      if (id === 'stand_32') {
        opsGroup.style.display = 'none';
        state.selectedOps = { id: 'none', name: 'Integrated Android Only', price: 0 };
      } else {
        opsGroup.style.display = 'block';
      }
      recalculateTotal();
    }

    function selectOps(id, price, card) {
      state.selectedOps = {
        id,
        name: card.querySelector('.opt-title').textContent,
        price
      };
      document.querySelectorAll('#opsOptions .opt-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      recalculateTotal();
    }

    function toggleAccessory(key, price, card) {
      if (state.selectedAccessories[key]) {
        delete state.selectedAccessories[key];
        card.classList.remove('selected');
      } else {
        state.selectedAccessories[key] = {
          name: card.querySelector('.opt-title').textContent,
          price
        };
        card.classList.add('selected');
      }
      recalculateTotal();
    }

    function recalculateTotal() {
      let total = state.selectedProduct.price + state.selectedOps.price;
      for (let k in state.selectedAccessories) {
        total += state.selectedAccessories[k].price;
      }
      document.getElementById('configTotalPrice').textContent = 'RM ' + total.toLocaleString();
      const monthly = (total / 12).toFixed(2);
      document.getElementById('configInstallmentPrice').textContent = 'or RM ' + monthly + '/mo. for 12 mos. with 0% installment';
      return total;
    }

    function openConfig(type, size) {
      const target = document.getElementById('shop-config');
      target.scrollIntoView({ behavior: 'smooth' });
      if (type === 'stand') {
        const standCard = document.querySelector('[onclick*="stand_32"]');
        if (standCard) standCard.click();
      }
    }

    // --- 8. SHOPPING BAG MANAGEMENT ---
    function addCurrentConfigToBag() {
      const item = {
        id: 'SYN-' + Date.now().toString().slice(-6),
        product: state.selectedProduct.name,
        ops: state.selectedOps.price > 0 ? state.selectedOps.name : null,
        accessories: Object.values(state.selectedAccessories).map(a => a.name),
        price: recalculateTotal(),
        qty: 1
      };
      state.bag.push(item);
      updateBagUI();
      openBag();
    }

    function updateBagUI() {
      const counter = document.getElementById('bagCounter');
      counter.textContent = state.bag.length;

      const container = document.getElementById('bagItemsContainer');
      const emptyMsg = document.getElementById('emptyBagMsg');

      if (state.bag.length === 0) {
        emptyMsg.style.display = 'block';
        container.innerHTML = '';
        container.appendChild(emptyMsg);
        document.getElementById('bagGrandTotal').textContent = 'RM 0';
        return;
      }

      emptyMsg.style.display = 'none';
      container.innerHTML = '';

      let grandTotal = 0;
      state.bag.forEach((item, index) => {
        grandTotal += item.price * item.qty;
        const itemEl = document.createElement('div');
        itemEl.className = 'bag-item';
        
        const details = document.createElement('div');
        const title = document.createElement('div');
        title.style.fontWeight = '600';
        title.style.fontSize = '15px';
        title.textContent = item.product;
        details.appendChild(title);

        if (item.ops) {
          const opsText = document.createElement('div');
          opsText.style.fontSize = '12px';
          opsText.style.color = '#6E6E73';
          opsText.textContent = '+ ' + item.ops;
          details.appendChild(opsText);
        }

        if (item.accessories && item.accessories.length > 0) {
          const accText = document.createElement('div');
          accText.style.fontSize = '12px';
          accText.style.color = '#6E6E73';
          accText.textContent = '+ ' + item.accessories.join(', ');
          details.appendChild(accText);
        }

        const priceEl = document.createElement('div');
        priceEl.style.textAlign = 'right';
        const priceText = document.createElement('div');
        priceText.style.fontWeight = '600';
        priceText.textContent = 'RM ' + (item.price * item.qty).toLocaleString();
        
        const removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.style.color = '#FF3B30';
        removeBtn.style.fontSize = '12px';
        removeBtn.style.marginTop = '6px';
        removeBtn.textContent = 'Remove';
        removeBtn.onclick = () => {
          state.bag.splice(index, 1);
          updateBagUI();
        };

        priceEl.appendChild(priceText);
        priceEl.appendChild(removeBtn);

        itemEl.appendChild(details);
        itemEl.appendChild(priceEl);
        container.appendChild(itemEl);
      });

      document.getElementById('bagGrandTotal').textContent = 'RM ' + grandTotal.toLocaleString();
    }

    function openBag() {
      document.getElementById('bagOverlay').classList.add('open');
      document.getElementById('bagDrawer').classList.add('open');
    }

    function closeBag() {
      document.getElementById('bagOverlay').classList.remove('open');
      document.getElementById('bagDrawer').classList.remove('open');
    }
    document.getElementById('openBagBtn').addEventListener('click', openBag);

    // --- 9. WHATSAPP DIRECT ORDER ---
    function checkoutWhatsApp() {
      if (state.bag.length === 0) {
        alert('Your bag is empty! Please configure a Syndo product first.');
        return;
      }

      let message = 'Hi SyndoTech Malaysia! I would like to place an Online Direct Order:\n\n';
      let total = 0;
      state.bag.forEach((item, i) => {
        total += item.price * item.qty;
        message += `${i+1}. ${item.product}\n`;
        if (item.ops) message += `   - OPS: ${item.ops}\n`;
        if (item.accessories.length > 0) message += `   - Accessories: ${item.accessories.join(', ')}\n`;
        message += `   - Price: RM ${item.price.toLocaleString()}\n\n`;
      });
      message += `Total Order: RM ${total.toLocaleString()}\n`;
      message += `Please provide invoice and schedule nationwide installation. Thank you!`;

      const encoded = encodeURIComponent(message);
      window.open(`https://wa.me/60123456789?text=${encoded}`, '_blank', 'noopener,noreferrer');
    }

    // --- 10. OFFICIAL PRINT QUOTATION ---
    function openQuotationSheet() {
      if (state.bag.length === 0) {
        addCurrentConfigToBag();
      }

      const tableBody = document.getElementById('quoteTableItems');
      tableBody.innerHTML = '';
      let subtotal = 0;

      state.bag.forEach((item) => {
        subtotal += item.price * item.qty;
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #EEE';

        let desc = `<strong>${item.product}</strong>`;
        if (item.ops) desc += `<br/><span style="color:#666; font-size:11px;">+ ${item.ops}</span>`;
        if (item.accessories.length > 0) desc += `<br/><span style="color:#666; font-size:11px;">+ ${item.accessories.join(', ')}</span>`;

        tr.innerHTML = `
          <td style="padding: 10px;">${desc}</td>
          <td style="padding: 10px; text-align: center;">${item.qty}</td>
          <td style="padding: 10px; text-align: right;">${item.price.toLocaleString()}</td>
          <td style="padding: 10px; text-align: right;">${(item.price * item.qty).toLocaleString()}</td>
        `;
        tableBody.appendChild(tr);
      });

      document.getElementById('quoteSubtotal').textContent = 'RM ' + subtotal.toLocaleString();
      document.getElementById('quoteGrandTotal').textContent = 'RM ' + subtotal.toLocaleString();
      document.getElementById('quoteRefNumber').textContent = 'REF: SYN-2026-' + Math.floor(1000 + Math.random() * 9000);
      document.getElementById('quoteDate').textContent = 'Date: ' + new Date().toLocaleDateString('en-GB');

      // Trigger Print
      window.print();
    }
  </script>
</body>
</html>
'''

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated successfully: {index_path} ({len(html_content)} bytes)")
