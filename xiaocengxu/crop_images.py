#!/usr/bin/env python3
"""智能裁剪产品图片 - 聚焦食品主体"""
from PIL import Image, ImageFilter
import os

IMG_DIR = "D:/xiaocengxu/images"
OUT_DIR = "D:/xiaocengxu/images/cropped"

os.makedirs(OUT_DIR, exist_ok=True)

# 每张图的裁剪参数 (left, top, right, bottom) 比例 0-1
# 根据图片构图手动调整，聚焦食品主体
CROP_CONFIG = {
    "img-durian-cheese.jpg":   (0.15, 0.10, 0.85, 0.90),  # 榴莲芝士饼 - 去掉四周多余
    "img-durian-cheese2.jpg":  (0.20, 0.15, 0.80, 0.85),  # 榴莲芝士饼另一角度
    "img-matcha-durian.jpg":   (0.10, 0.05, 0.90, 0.95),  # 抹茶榴莲 - 绿色拉丝主体
    "img-guangbing.jpg":       (0.08, 0.12, 0.92, 0.88),  # 光饼 - 去掉红底边缘
    "img-guokui.jpg":          (0.12, 0.08, 0.88, 0.92),  # 锅盔 - 聚焦切面
    "img-vanilla-souffle.jpg": (0.18, 0.05, 0.82, 0.90),  # 原味舒芙蕾 - 蓬松主体
    "img-matcha-souffle.jpg":  (0.15, 0.10, 0.85, 0.88),  # 抹茶舒芙蕾
    "img-choco-souffle.jpg":   (0.20, 0.08, 0.80, 0.92),  # 巧克力舒芙蕾
    "img-strawberry-souffle.jpg": (0.10, 0.05, 0.90, 0.90), # 草莓舒芙蕾
    "img-souffle-hero.jpg":    (0.22, 0.12, 0.78, 0.88),  # 舒芙蕾主图
    "img-yougan-drink.jpg":    (0.25, 0.15, 0.75, 0.85),  # 油柑饮品 - 聚焦杯子
}

def smart_crop(img_path, output_path, crop_ratio):
    """智能裁剪图片，聚焦主体"""
    img = Image.open(img_path)
    w, h = img.size
    
    # 转换为RGB (处理RGBA或P模式)
    if img.mode in ('RGBA', 'P'):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # 应用裁剪比例
    left   = int(w * crop_ratio[0])
    top    = int(h * crop_ratio[1])
    right  = int(w * crop_ratio[2])
    bottom = int(h * crop_ratio[3])
    
    img_cropped = img.crop((left, top, right, bottom))
    
    # 统一缩放到 800x600 (4:3) 适合移动端展示
    img_cropped = img_cropped.resize((800, 600), Image.LANCZOS)
    
    # 轻微锐化，让食品更有食欲
    img_cropped = img_cropped.filter(ImageFilter.SHARPEN)
    
    img_cropped.save(output_path, 'JPEG', quality=92)
    print(f"✅ 裁剪完成: {os.path.basename(output_path)} ({img_cropped.size[0]}x{img_cropped.size[1]})")

def add_subtle_watermark(img_path, output_path):
    """添加微妙的水印效果（可选）"""
    # 暂时不添加水印，保持图片干净
    pass

if __name__ == "__main__":
    print("🖼️  开始智能裁剪产品图片...")
    for fname, ratio in CROP_CONFIG.items():
        src = os.path.join(IMG_DIR, fname)
        dst = os.path.join(OUT_DIR, fname)
        if os.path.exists(src):
            smart_crop(src, dst, ratio)
        else:
            print(f"⚠️  文件不存在: {src}")
    
    print(f"\n📁 裁剪后的图片保存在: {OUT_DIR}")
    print(f"📊 共处理 {len(CROP_CONFIG)} 张图片")
