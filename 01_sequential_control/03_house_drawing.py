"""
順次制御 - 家の絵を描く
複数の図形を組み合わせて家を描画します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(135, 206, 235)  # 空色
    
    # 地面
    py5.fill(34, 139, 34)  # 緑
    py5.rect(0, 300, 400, 100)
    
    # 家の土台
    py5.fill(139, 69, 19)  # 茶色
    py5.rect(150, 200, 100, 100)
    
    # 屋根
    py5.fill(178, 34, 34)  # 赤
    py5.triangle(140, 200, 200, 150, 260, 200)
    
    # ドア
    py5.fill(101, 67, 33)  # 濃い茶色
    py5.rect(175, 250, 20, 50)
    
    # ドアノブ
    py5.fill(255, 215, 0)  # 金色
    py5.circle(190, 275, 4)
    
    # 窓
    py5.fill(173, 216, 230)  # 水色
    py5.rect(210, 220, 25, 25)
    
    # 窓枠
    py5.stroke(101, 67, 33)
    py5.stroke_weight(2)
    py5.line(222, 220, 222, 245)
    py5.line(210, 232, 235, 232)
    py5.no_stroke()
    
    # 太陽
    py5.fill(255, 255, 0)  # 黄色
    py5.circle(350, 80, 40)
    
    # 雲
    py5.fill(255, 255, 255)  # 白
    py5.circle(80, 60, 30)
    py5.circle(100, 60, 40)
    py5.circle(120, 60, 30)

py5.run_sketch()