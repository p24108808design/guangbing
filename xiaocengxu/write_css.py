#!/usr/bin/env python3
"""写入大师级CSS样式"""
css = """/* ===== 光饼·舒芙蕾·油柑茶 — 大师级UI ===== */
:root {
  --pink: #E8849C; --pink-deep: #C85A78; --pink-light: #FFF0F3; --pink-bg: #FFF5F7;
  --orange: #F0A060; --orange-light: #FFF5EE;
  --green: #5BB57A; --green-light: #EEF7F1;
  --text: #2D2B2A; --text-sub: #8B8680; --text-hint: #B5B0A8;
  --bg: #FAF8F6; --card: #FFFFFF; --border: #F0ECE8; --border-light: #F7F5F2;
  --shadow-sm: 0 2px 8px rgba(45,43,42,0.04);
  --shadow-md: 0 4px 16px rgba(45,43,42,0.08);
  --shadow-lg: 0 8px 32px rgba(45,43,42,0.12);
  --shadow-pink: 0 4px 20px rgba(232,132,156,0.25);
  --r-sm: 8px; --r-md: 14px; --r-lg: 20px; --r-xl: 28px;
  --font: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-tap-highlight-color: transparent; }
body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; -webkit-font-smoothing: antialiased; }

/* 启动画面 */
.splash { position: fixed; inset: 0; z-index: 9999; background: linear-gradient(160deg, #FFF0F3 0%, #FFE0E8 50%, #FFD0E0 100%); display: flex; align-items: center; justify-content: center; transition: opacity 0.5s, visibility 0.5s; }
.splash.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
.splash-mascot { font-size: 64px; animation: splashBounce 1.2s ease-in-out infinite; }
@keyframes splashBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-16px); } }
.splash-brand { font-size: 22px; font-weight: 900; color: var(--pink-deep); margin-top: 16px; letter-spacing: 2px; }
.splash-slogan { font-size: 12px; color: var(--pink); letter-spacing: 4px; margin-top: 6px; font-weight: 300; }
.splash-loading { margin-top: 28px; width: 120px; height: 3px; background: rgba(232,132,156,0.2); border-radius: 2px; margin-left: auto; margin-right: auto; overflow: hidden; }
.splash-bar { width: 40%; height: 100%; border-radius: 2px; background: var(--pink); animation: splashLoad 1.5s ease-in-out infinite; }
@keyframes splashLoad { 0% { transform: translateX(-100%); } 100% { transform: translateX(350%); } }

/* 英雄区 */
.hero { position: relative; background: linear-gradient(160deg, #E8849C 0%, #D4687E 40%, #C85A78 100%); padding: 48px 20px 60px; text-align: center; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.15) 0%, transparent 50%), radial-gradient(circle at 80% 70%, rgba(255,255,255,0.1) 0%, transparent 40%); }
.hero-content { position: relative; z-index: 1; }
.hero-avatar { width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 14px; border: 3px solid rgba(255,255,255,0.8); overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.15); background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 40px; }
.hero-avatar img { width: 100%; height: 100%; object-fit: cover; }
.hero-title { font-size: 24px; font-weight: 900; color: white; letter-spacing: 2px; text-shadow: 0 2px 8px rgba(0,0,0,0.15); }
.hero-slogan { font-size: 11px; color: rgba(255,255,255,0.85); letter-spacing: 5px; margin-top: 6px; font-weight: 300; }
.hero-desc { font-size: 14px; color: rgba(255,255,255,0.95); margin-top: 8px; font-weight: 500; }
.hero-tags { display: flex; gap: 8px; justify-content: center; margin-top: 14px; flex-wrap: wrap; }
.hero-tag { font-size: 11px; color: white; background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); padding: 5px 12px; border-radius: 20px; font-weight: 500; }
.hero-wave { position: absolute; bottom: -1px; left: 0; right: 0; line-height: 0; }
.hero-wave svg { width: 100%; height: 40px; }

/* 制作时间说明 */
.time-card { margin: -20px 16px 0; position: relative; z-index: 2; background: white; border-radius: var(--r-lg); box-shadow: var(--shadow-md); padding: 14px 16px; display: flex; align-items: flex-start; gap: 10px; animation: slideUp 0.6s ease-out; }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.time-card-icon { font-size: 22px; flex-shrink: 0; margin-top: 2px; }
.time-card-body { flex: 1; min-width: 0; }
.time-card-title { font-size: 13px; font-weight: 700; color: var(--text); }
.time-card-items { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px; }
.time-item { font-size: 11px; color: var(--pink-deep); background: var(--pink-light); padding: 3px 8px; border-radius: 6px; font-weight: 500; }
.time-item b { font-weight: 700; }
.time-card-tip { font-size: 11px; color: var(--text-hint); margin-top: 8px; padding-top: 8px; border-top: 1px dashed var(--border); }

/* 分类导航 */
.cat-nav { position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-light); padding: 10px 0; }
.cat-nav-inner { display: flex; gap: 8px; padding: 0 16px; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
.cat-nav-inner::-webkit-scrollbar { display: none; }
.cat-btn { flex-shrink: 0; padding: 8px 16px; border-radius: 20px; border: 1.5px solid var(--border); background: white; font-size: 13px; font-weight: 600; color: var(--text-sub); cursor: pointer; transition: all 0.25s; white-space: nowrap; font-family: var(--font); }
.cat-btn:active { transform: scale(0.96); }
.cat-btn.active { background: linear-gradient(135deg, var(--pink), var(--pink-deep)); color: white; border-color: transparent; box-shadow: var(--shadow-pink); }

/* 产品区域 */
.products { padding: 16px; }
.cat-section { margin-bottom: 28px; }
.section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 16px; padding: 0 4px; }
.section-icon { font-size: 20px; }
.section-title { font-size: 18px; font-weight: 800; color: var(--text); }
.section-sub { font-size: 12px; color: var(--text-hint); font-weight: 500; }

/* 产品卡片 */
.product-card { background: white; border-radius: var(--r-lg); overflow: hidden; box-shadow: var(--shadow-sm); margin-bottom: 16px; transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94); cursor: pointer; position: relative; }
.product-card:active { transform: scale(0.98); box-shadow: var(--shadow-md); }
.product-card.featured { box-shadow: var(--shadow-md); }
.product-card.featured::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--pink), var(--orange), var(--pink)); z-index: 1; }
.product-img-wrap { position: relative; overflow: hidden; height: 200px; background: var(--pink-light); }
.product-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
.product-card:active .product-img { transform: scale(1.05); }
.product-badge { position: absolute; top: 12px; left: 12px; font-size: 11px; padding: 4px 10px; border-radius: 12px; font-weight: 700; backdrop-filter: blur(10px); }
.product-badge.hot { background: rgba(240,96,96,0.9); color: white; }
.product-badge.new { background: rgba(232,132,156,0.9); color: white; }
.product-tag { position: absolute; top: 12px; right: 12px; font-size: 10px; padding: 3px 8px; border-radius: 8px; font-weight: 600; }
.product-tag.new { background: var(--pink-light); color: var(--pink-deep); }
.product-prep { position: absolute; bottom: 10px; right: 10px; font-size: 11px; background: rgba(0,0,0,0.55); color: white; padding: 3px 10px; border-radius: 10px; backdrop-filter: blur(6px); font-weight: 500; }
.product-info { padding: 16px; }
.product-name-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.product-name { font-size: 16px; font-weight: 700; color: var(--text); line-height: 1.3; }
.product-desc { font-size: 12.5px; color: var(--text-sub); line-height: 1.5; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.product-price-row { display: flex; align-items: center; justify-content: space-between; }
.product-price { display: flex; align-items: baseline; gap: 4px; flex-wrap: wrap; }
.price-current { font-size: 20px; font-weight: 900; color: var(--pink-deep); font-variant-numeric: tabular-nums; }
.price-spec { font-size: 11px; color: var(--text-hint); font-weight: 500; }
.price-original { font-size: 12px; color: var(--text-hint); text-decoration: line-through; margin-left: 6px; }
.add-btn { width: 36px; height: 36px; border-radius: 50%; border: none; background: linear-gradient(135deg, var(--pink), var(--pink-deep)); color: white; font-size: 20px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: var(--shadow-pink); transition: all 0.2s; flex-shrink: 0; }
.add-btn:active { transform: scale(0.9); }

/* 底部导航 */
.bottom-nav { position: fixed; bottom: 0; left: 0; right: 0; z-index: 200; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 1px solid var(--border-light); display: flex; padding: 6px 0; padding-bottom: env(safe-area-inset-bottom); }
.bottom-nav-btn { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; border: none; background: none; padding: 6px 0; cursor: pointer; color: var(--text-hint); font-size: 10px; font-weight: 500; font-family: var(--font); position: relative; transition: color 0.2s; }
.bottom-nav-btn.active { color: var(--pink-deep); }
.nav-icon { font-size: 20px; }
.cart-btn .cart-badge { position: absolute; top: 2px; right: 50%; margin-right: -18px; background: var(--pink); color: white; font-size: 10px; font-weight: 700; min-width: 16px; height: 16px; border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 0 4px; }

/* 购物车面板 */
.cart-overlay { position: fixed; inset: 0; background: rgba(45,43,42,0.4); z-index: 300; opacity: 0; visibility: hidden; transition: all 0.3s; }
.cart-overlay.show { opacity: 1; visibility: visible; }
.cart-panel { position: fixed; top: 0; right: 0; bottom: 0; width: 85%; max-width: 360px; background: white; z-index: 301; transform: translateX(100%); transition: transform 0.35s; box-shadow: -4px 0 24px rgba(0,0,0,0.1); display: flex; flex-direction: column; }
.cart-panel.show { transform: translateX(0); }
.cart-header { display: flex; align-items: center; justify-content: space-between; padding: 18px 16px; border-bottom: 1px solid var(--border-light); }
.cart-header h3 { font-size: 16px; font-weight: 700; }
.cart-close { width: 32px; height: 32px; border-radius: 50%; border: none; background: var(--bg); font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
.cart-items { flex: 1; overflow-y: auto; padding: 12px; }
.cart-empty { text-align: center; padding: 48px 0; color: var(--text-hint); }
.cart-empty-icon { font-size: 40px; margin-bottom: 12px; opacity: 0.5; }
.cart-empty-hint { font-size: 12px; margin-top: 6px; }
.cart-item { display: flex; gap: 12px; padding: 12px; background: var(--bg); border-radius: var(--r-md); margin-bottom: 8px; align-items: center; }
.cart-item-name { font-size: 14px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cart-item-spec { font-size: 11px; color: var(--text-hint); margin-top: 2px; }
.cart-item-price { font-size: 14px; font-weight: 700; color: var(--pink-deep); margin-top: 4px; }
.cart-item-qty { display: flex; align-items: center; gap: 8px; }
.qty-btn { width: 28px; height: 28px; border-radius: 50%; border: 1.5px solid var(--border); background: white; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: 600; color: var(--text); }
.qty-num { font-size: 14px; font-weight: 600; min-width: 20px; text-align: center; }
.cart-footer { padding: 14px 16px; border-top: 1px solid var(--border-light); background: white; }
.cart-total-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.cart-total { font-size: 22px; font-weight: 900; color: var(--pink-deep); }
.cart-checkout { width: 100%; padding: 14px; border-radius: var(--r-md); border: none; background: linear-gradient(135deg, var(--pink), var(--pink-deep)); color: white; font-size: 16px; font-weight: 700; cursor: pointer; box-shadow: var(--shadow-pink); font-family: var(--font); }
.cart-checkout:active { transform: scale(0.98); }

/* 预约弹窗 */
.modal-overlay { position: fixed; inset: 0; background: rgba(45,43,42,0.5); z-index: 500; display: none; align-items: flex-end; justify-content: center; }
.modal-overlay.show { display: flex; }
.modal { background: white; width: 100%; max-width: 500px; max-height: 90vh; border-radius: var(--r-xl) var(--r-xl) 0 0; overflow-y: auto; animation: modalSlideUp 0.35s; }
@keyframes modalSlideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
.modal-header { display: flex; align-items: center; justify-content: space-between; padding: 18px 20px; position: sticky; top: 0; background: white; z-index: 1; border-bottom: 1px solid var(--border-light); }
.modal-header h3 { font-size: 17px; font-weight: 700; }
.modal-close { width: 32px; height: 32px; border-radius: 50%; border: none; background: var(--bg); font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
.modal-body { padding: 20px; }
.order-summary { background: var(--pink-bg); border-radius: var(--r-md); padding: 14px; margin-bottom: 18px; font-size: 13px; line-height: 1.8; }
.time-notice { background: var(--green-light); border-radius: var(--r-sm); padding: 12px 14px; margin-bottom: 18px; font-size: 12px; line-height: 1.7; color: #2D5A3D; }
.time-notice strong { color: var(--green); }
.form-group { margin-bottom: 18px; }
.form-group label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
.form-group input, .form-group textarea { width: 100%; padding: 12px 14px; border: 1.5px solid var(--border); border-radius: var(--r-sm); font-size: 14px; font-family: var(--font); transition: border-color 0.2s; background: white; }
.form-group input:focus, .form-group textarea:focus { outline: none; border-color: var(--pink); box-shadow: 0 0 0 3px rgba(232,132,156,0.15); }
.time-slots { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.time-slot { display: flex; align-items: center; gap: 6px; padding: 10px 12px; border: 1.5px solid var(--border); border-radius: var(--r-sm); cursor: pointer; font-size: 13px; transition: all 0.2s; }
.time-slot:has(input:checked) { border-color: var(--pink); background: var(--pink-light); color: var(--pink-deep); font-weight: 600; }
.time-slot input { display: none; }
.submit-btn { width: 100%; padding: 16px; border-radius: var(--r-md); border: none; background: linear-gradient(135deg, var(--pink), var(--pink-deep)); color: white; font-size: 16px; font-weight: 700; cursor: pointer; box-shadow: var(--shadow-pink); font-family: var(--font); margin-top: 8px; }
.submit-btn:active { transform: scale(0.98); }

/* 成功弹窗 */
.success-modal { text-align: center; padding: 40px 24px; }
.success-icon { font-size: 56px; margin-bottom: 16px; }
.success-modal h3 { font-size: 20px; font-weight: 800; color: var(--text); margin-bottom: 8px; }
.success-order-id { font-size: 13px; color: var(--text-sub); margin-bottom: 24px; }
.success-order-id span { color: var(--pink-deep); font-weight: 700; font-size: 15px; }
.success-steps { display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 24px; flex-wrap: wrap; }
.step { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-sub); }
.step-num { width: 22px; height: 22px; border-radius: 50%; background: var(--pink-light); color: var(--pink-deep); font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.step-arrow { color: var(--text-hint); font-size: 12px; }
.copy-btn { width: 100%; padding: 14px; border-radius: var(--r-md); border: 2px solid var(--pink); background: var(--pink-light); color: var(--pink-deep); font-size: 15px; font-weight: 700; cursor: pointer; margin-bottom: 16px; font-family: var(--font); transition: all 0.2s; }
.copy-btn:active { background: var(--pink); color: white; }
.wechat-guide { background: var(--bg); border-radius: var(--r-sm); padding: 12px; margin-bottom: 16px; }
.wechat-guide p { font-size: 13px; color: var(--text-sub); }
.wechat-guide .hint { font-size: 11px; color: var(--text-hint); margin-top: 4px; }
.back-btn { width: 100%; padding: 12px; border-radius: var(--r-md); border: 1.5px solid var(--pink); background: white; color: var(--pink-deep); font-size: 15px; font-weight: 600; cursor: pointer; font-family: var(--font); }

/* 滚动渐现 */
.product-card { opacity: 0; transform: translateY(20px); animation: fadeInUp 0.5s ease-out forwards; }
.product-card:nth-child(1) { animation-delay: 0.05s; }
.product-card:nth-child(2) { animation-delay: 0.1s; }
.product-card:nth-child(3) { animation-delay: 0.15s; }
.product-card:nth-child(4) { animation-delay: 0.2s; }
.product-card:nth-child(5) { animation-delay: 0.25s; }
@keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }

@media (min-width: 420px) {
  .products { max-width: 420px; margin: 0 auto; }
  .time-card { max-width: 388px; margin-left: auto; margin-right: auto; }
}
"""
with open("D:/xiaocengxu/style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("✅ CSS写入成功")
print(f"📊 文件大小: {len(css)} 字节")
print(f"🎨 包含特性: 启动画面、英雄区、卡片设计、购物车、弹窗、动画")
