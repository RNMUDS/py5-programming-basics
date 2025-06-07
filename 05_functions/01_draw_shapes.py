"""
関数の基本 - 図形を描く関数
関数を定義して図形を描画します
"""
import py5

def draw_flower(x, y, size, color):
    """花を描く関数"""
    py5.fill(color[0], color[1], color[2])
    # 花びら
    for angle in range(0, 360, 45):
        petal_x = x + py5.cos(py5.radians(angle)) * size * 0.5
        petal_y = y + py5.sin(py5.radians(angle)) * size * 0.5
        py5.ellipse(petal_x, petal_y, size * 0.6, size * 0.3)
    
    # 花の中心
    py5.fill(255, 255, 0)
    py5.circle(x, y, size * 0.4)

def draw_house(x, y, width, height):
    """家を描く関数"""
    # 土台
    py5.fill(139, 69, 19)
    py5.rect(x, y, width, height)
    
    # 屋根
    py5.fill(178, 34, 34)
    py5.triangle(x - 10, y, x + width/2, y - height/2, x + width + 10, y)
    
    # ドア
    py5.fill(101, 67, 33)
    py5.rect(x + width * 0.3, y + height * 0.4, width * 0.2, height * 0.6)
    
    # 窓
    py5.fill(173, 216, 230)
    py5.rect(x + width * 0.7, y + height * 0.2, width * 0.2, height * 0.2)

def draw_tree(x, y, height):
    """木を描く関数"""
    # 幹
    py5.fill(101, 67, 33)
    trunk_width = height * 0.1
    py5.rect(x - trunk_width/2, y, trunk_width, height * 0.4)
    
    # 葉
    py5.fill(34, 139, 34)
    py5.circle(x, y - height * 0.2, height * 0.6)

def setup():
    py5.size(600, 400)
    py5.background(135, 206, 235)  # 空色
    
    # 地面
    py5.fill(34, 139, 34)
    py5.rect(0, 300, 600, 100)
    
    # 関数を使って図形を描画
    draw_house(100, 200, 80, 100)
    draw_house(400, 180, 100, 120)
    
    draw_tree(250, 300, 80)
    draw_tree(350, 300, 100)
    draw_tree(50, 300, 70)
    
    draw_flower(150, 320, 20, (255, 100, 150))
    draw_flower(180, 330, 15, (255, 150, 100))
    draw_flower(450, 325, 18, (150, 100, 255))
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("関数で描いた風景", 220, 30)

py5.run_sketch()