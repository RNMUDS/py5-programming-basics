"""
繰り返し - 虹色のストライプ
while文を使用して虹色のストライプを描画します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(255)
    
    # 虹の色を定義
    rainbow_colors = [
        (255, 0, 0),    # 赤
        (255, 165, 0),  # オレンジ
        (255, 255, 0),  # 黄色
        (0, 255, 0),    # 緑
        (0, 0, 255),    # 青
        (75, 0, 130),   # 藍
        (148, 0, 211)   # 紫
    ]
    
    # for文で虹色ストライプ（横）
    stripe_height = 40
    for i in range(len(rainbow_colors)):
        color = rainbow_colors[i]
        y = 50 + i * stripe_height
        py5.fill(color[0], color[1], color[2])
        py5.rect(50, y, 300, stripe_height)
    
    # while文で虹色ストライプ（縦）
    i = 0
    stripe_width = 30
    while i < len(rainbow_colors):
        color = rainbow_colors[i]
        x = 80 + i * stripe_width
        py5.fill(color[0], color[1], color[2], 150)  # 半透明
        py5.rect(x, 100, stripe_width, 200)
        i += 1
    
    # タイトル
    py5.fill(0)
    py5.text_size(16)
    py5.text("虹色のストライプパターン", 120, 30)

py5.run_sketch()