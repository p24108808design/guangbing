/* ============================================================
   光饼·舒芙蕾·油柑茶 — 核心交互逻辑
   ============================================================ */

// ====== 全局状态 ======
let cart = [];

// ====== 初始化 ======
document.addEventListener('DOMContentLoaded', function() {
  // 启动画面
  setTimeout(function() {
    var splash = document.getElementById('splash');
    if (splash) { splash.classList.add('hidden'); }
  }, 1400);

  // 恢复购物车
  loadCart();

  // 设置默认日期为今天
  var dateInput = document.getElementById('bookingDate');
  if (dateInput) {
    var today = new Date();
    dateInput.value = today.toISOString().split('T')[0];
    dateInput.min = today.toISOString().split('T')[0];
  }

  updateCartUI();
});

// ====== 分类筛选 ======
function filterCat(cat, btn) {
  // 更新按钮状态
  var pills = document.querySelectorAll('.cat-pill');
  pills.forEach(function(p) { p.classList.remove('active'); });
  if (btn) btn.classList.add('active');

  // 筛选卡片
  var cards = document.querySelectorAll('.prod-card');
  cards.forEach(function(card) {
    if (cat === 'all' || card.getAttribute('data-cat') === cat) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });
}

// ====== 购物车操作 ======
function addToCart(name, priceText, priceNum, imgSrc) {
  cart.push({
    name: name,
    price: priceText,
    priceNum: priceNum,
    img: imgSrc,
    qty: 1,
    id: Date.now() + Math.random()
  });
  saveCart();
  updateCartUI();

  // 飞入动画
  triggerFlyAnimation(event.target, imgSrc);

  // 按钮反馈动画
  var btn = event.target.closest('.add-circle') || event.target;
  btn.classList.add('adding');
  setTimeout(function() { btn.classList.remove('adding'); }, 400);
}

function removeFromCart(id) {
  cart = cart.filter(function(item) { return item.id !== id; });
  saveCart();
  updateCartUI();
}

function changeQty(id, delta) {
  var item = cart.find(function(i) { return i.id === id; });
  if (!item) return;
  item.qty += delta;
  if (item.qty <= 0) {
    removeFromCart(id);
    return;
  }
  saveCart();
  updateCartUI();
}

function clearCart() {
  cart = [];
  saveCart();
  updateCartUI();
}

// ====== 购物车持久化 ======
function saveCart() {
  try { localStorage.setItem('guangbing_cart', JSON.stringify(cart)); } catch(e) {}
}
function loadCart() {
  try {
    var saved = localStorage.getItem('guangbing_cart');
    if (saved) cart = JSON.parse(saved);
  } catch(e) { cart = []; }
}

// ====== 购物车UI更新（三处同步：顶部badge、底部栏、侧边栏）====== 
function updateCartUI() {
  var totalQty = 0;
  var totalPrice = 0;
  cart.forEach(function(item) {
    totalQty += item.qty;
    totalPrice += item.priceNum * item.qty;
  });

  // 1. 顶部导航的角标
  var countEl = document.getElementById('cartCount');
  if (countEl) {
    countEl.textContent = totalQty;
    if (totalQty > 0) countEl.classList.add('show');
    else countEl.classList.remove('show');
  }

  // 2. 底部购物车栏
  var barBadge = document.getElementById('cartBarBadge');
  var barTotal = document.getElementById('cartBarTotal');
  if (barBadge) barBadge.textContent = totalQty;
  if (barTotal) barTotal.textContent = '¥' + totalPrice;

  // 3. 侧边栏内容
  renderCartSheet(totalQty, totalPrice);
}

function renderCartSheet(totalQty, totalPrice) {
  var body = document.getElementById('cartSheetBody');
  var footer = document.getElementById('cartSheetFooter');
  var emptyEl = document.getElementById('cartSheetEmpty');
  var clearBtn = document.getElementById('clearCartBtn');
  var totalEl = document.getElementById('cartSheetTotal');

  if (totalQty === 0) {
    body.innerHTML = '<div class="cart-sheet-empty" id="cartSheetEmpty"><p>购物车是空的</p><span>去选点好吃的吧~</span></div>';
    footer.style.display = 'none';
    if (clearBtn) clearBtn.style.display = 'none';
    return;
  }

  clearBtn.style.display = 'block';
  footer.style.display = 'block';
  if (totalEl) totalEl.textContent = '¥' + totalPrice;

  var html = '';
  cart.forEach(function(item) {
    html += '<div class="cart-item-row">';
    html += '<div class="cart-thumb"><img src="' + item.img + '" alt="" onerror="this.parentElement.style.background=\'#FFF0F3\'"></div>';
    html += '<div class="cart-detail">';
    html += '<div class="cart-item-name">' + item.name + '</div>';
    html += '<div class="cart-item-price">' + item.price + '</div>';
    html += '</div>';
    html += '<div class="cart-qty-box">';
    html += '<button class="qty-btn-s" onclick="changeQty(' + item.id + ',-1)">−</button>';
    html += '<span class="qty-num-s">' + item.qty + '</span>';
    html += '<button class="qty-btn-s" onclick="changeQty(' + item.id + ',1)">+</button>';
    html += '</div></div>';
  });

  body.innerHTML = html;
}

// ====== 购物车面板开关 ======
function toggleCart() {
  var mask = document.getElementById('cartMask');
  var sheet = document.getElementById('cartSheet');
  if (mask && sheet) {
    mask.classList.toggle('show');
    sheet.classList.toggle('show');
    // 重绘body防止iOS滚动穿透
    if (sheet.classList.contains('show')) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
  }
}

// 关闭购物车时恢复滚动
document.addEventListener('click', function(e) {
  if (e.target.id === 'cartMask') {
    document.body.style.overflow = '';
  }
});

// ====== 飞入动画（从按钮位置飞到购物车FAB）====== 
function triggerFlyAnimation(startElem, imgSrc) {
  var flyDot = document.getElementById('flyDot');
  var cartBar = document.getElementById('cartBar');
  if (!flyDot || !cartBar || !startElem) return;

  var startRect = startElem.getBoundingClientRect();
  var endRect = cartBar.getBoundingClientRect();

  // 创建图片元素放入飞球
  flyDot.innerHTML = imgSrc ? ('<img src="' + imgSrc + '" alt="">') : '';
  
  // 起始位置
  flyDot.style.left = (startRect.left + startRect.width / 2 - 16) + 'px';
  flyDot.style.top = (startRect.top + startRect.height / 2 - 16) + 'px';
  flyDot.style.transform = 'scale(1)';
  flyDot.style.opacity = '1';

  // 触发重排后开始动画
  requestAnimationFrame(function() {
    flyDot.style.left = (endRect.left + 22 - 16) + 'px';
    flyDot.style.top = (endRect.top + endRect.height / 2 - 16) + 'px';
    flyDot.style.transform = 'scale(0.2)';
    flyDot.style.opacity = '0.3';

    setTimeout(function() {
      flyDot.style.transition = 'none';
      flyDot.style.transform = '';
      flyDot.style.opacity = '';
      flyDot.innerHTML = '';
    }, 600);
  });
}

// ====== 显示预约弹窗 ======
function showBooking() {
  if (cart.length === 0) {
    alert('请先添加商品到购物车~');
    return;
  }

  // 先关闭购物车
  var mask = document.getElementById('cartMask');
  var sheet = document.getElementById('cartSheet');
  if (mask) mask.classList.remove('show');
  if (sheet) sheet.classList.remove('show');
  document.body.style.overflow = '';

  // 生成订单摘要
  var summary = generateOrderSummary();
  var summaryEl = document.getElementById('orderSummary');
  if (summaryEl) summaryEl.innerHTML = summary;

  // 显示预约弹窗
  var modal = document.getElementById('bookingModal');
  if (modal) modal.classList.add('show');
}

function generateOrderSummary() {
  var itemsHtml = '';
  var total = 0;
  cart.forEach(function(item) {
    itemsHtml += '<div class="item-row"><span>' + item.name + ' ×' + item.qty + '</span><span>' + item.price + '</span></div>';
    total += item.priceNum * item.qty;
  });
  return itemsHtml + '<div style="border-top:1px solid #FFE4EB;margin-top:8px;padding-top:8px;display:flex;justify-content:space-between;font-weight:700;color:#D1456F"><span>合计</span><span>¥' + total + '</span></div>';
}

function closeModal() {
  var modal = document.getElementById('bookingModal');
  if (modal) modal.classList.remove('show');
  document.body.style.overflow = '';
}

// ====== 提交订单 ======
var currentOrderText = '';

function submitOrder() {
  var name = document.getElementById('customerName').value.trim();
  var phone = document.getElementById('customerPhone').value.trim();
  var date = document.getElementById('bookingDate').value;
  var note = document.getElementById('bookingNote').value.trim();

  // 校验
  if (!name) { alert('请填写您的称呼~'); return; }
  if (!phone) { alert('请填写手机号~'); return; }
  if (!/^\d{11}$/.test(phone)) { alert('手机号格式不正确哦~'); return; }
  if (!date) { alert('请选择预约日期~'); return; }

  var slotChecked = document.querySelector('input[name="timeSlot"]:checked');
  if (!slotChecked) { alert('请选择预约时段~'); return; }

  // 生成订单号
  var orderId = 'GB' + Date.now().toString().slice(-8);

  // 构建订单文本（复制用）
  var orderItems = [];
  cart.forEach(function(item) {
    orderItems.push(item.name + ' ×' + item.qty + ' ' + item.price);
  });
  var total = 0;
  cart.forEach(function(item) { total += item.priceNum * item.qty; });

  currentOrderText = [
    '【光饼·舒芙蕾·油柑茶 预约订单】',
    '📦 订单号：' + orderId,
    '👤 称呼：' + name,
    '📱 电话：' + phone,
    '📅 日期：' + date,
    '⏰ 时段：' + slotChecked.value,
    '',
    ...orderItems,
    '',
    '💰 合计：¥' + total,
    note ? ('📝 备注：' + note) : ''
  ].join('\n');

  // 保存到localStorage
  var orders = [];
  try { orders = JSON.parse(localStorage.getItem('guangbing_orders') || '[]'); } catch(e) {}
  orders.unshift({
    orderId: orderId,
    customer: name,
    phone: phone,
    date: date,
    time: slotChecked.value,
    items: cart.map(function(i) { return i.name + '×' + i.qty; }),
    total: total,
    note: note,
    status: 'pending',
    createdAt: new Date().toISOString()
  });
  localStorage.setItem('guangbing_orders', JSON.stringify(orders));

  // 关闭预约弹窗，显示成功弹窗
  closeModal();

  var successIdEl = document.getElementById('successOrderId');
  if (successIdEl) successIdEl.textContent = orderId;

  var successModal = document.getElementById('successModal');
  if (successModal) successModal.classList.add('show');
}

// ====== 复制订单信息 ======
function copyOrderInfo() {
  if (!currentOrderText) return;

  // 尝试使用 Clipboard API
  if (navigator.clipboard) {
    navigator.clipboard.writeText(currentOrderText).then(function() {
      showCopySuccess();
    }).catch(function() {
      fallbackCopy();
    });
  } else {
    fallbackCopy();
  }

  function fallbackCopy() {
    var ta = document.createElement('textarea');
    ta.value = currentOrderText;
    ta.style.cssText = 'position:fixed;left:-9999px;top:-9999px;opacity:0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); showCopySuccess(); } catch(e) { alert('复制失败，请手动长按选择复制'); }
    document.body.removeChild(ta);
  }

  function showCopySuccess() {
    var btn = document.getElementById('copyOrderBtn');
    if (btn) {
      btn.textContent = '✅ 已复制！快去发微信吧~';
      btn.style.background = '#F2F8F4';
      btn.style.borderColor = '#5BB57A';
      btn.style.color = '#2D5A3D';
      setTimeout(function() {
        btn.textContent = '📋 复制订单信息发微信';
        btn.style.background = '';
        btn.style.borderColor = '';
        btn.style.color = '';
      }, 2000);
    }
  }
}

// ====== 返回首页 ======
function closeSuccess() {
  var modal = document.getElementById('successModal');
  if (modal) modal.classList.remove('show');
  document.body.style.overflow = '';

  // 清空购物车
  cart = [];
  saveCart();
  updateCartUI();
  currentOrderText = '';

  // 滚动回顶部
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ====== 详情页占位（暂未实现）======
function showDetail(id) {
  // TODO: 可扩展为产品详情弹窗
  // 目前点击卡片无操作（加购在卡片上直接完成）
}
