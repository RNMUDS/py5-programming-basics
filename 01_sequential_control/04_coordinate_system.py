"""
順次制御 - 座標系の理解
座標を変更しながら図形を配置します
"""
import py5

def setup():
    py5.size(500, 500)
    py5.background(255)
    
    # 座標軸を描画
    py5.stroke(200)
    py5.stroke_weight(1)
    # 縦線
    for x in range(0, 501, 50):
        py5.line(x, 0, x, 500)
    # 横線
    for y in range(0, 501, 50):
        py5.line(0, y, 500, y)
    
    py5.no_stroke()
    
    # 左上から右下に向かって円を配置
    x = 25
    y = 25
    py5.fill(255, 0, 0, 150)
    py5.circle(x, y, 30)
    
    x = 75
    y = 75
    py5.fill(255, 100, 0, 150)
    py5.circle(x, y, 30)
    
    x = 125
    y = 125
    py5.fill(255, 200, 0, 150)
    py5.circle(x, y, 30)
    
    x = 175
    y = 175
    py5.fill(100, 255, 0, 150)
    py5.circle(x, y, 30)
    
    x = 225
    y = 225
    py5.fill(0, 255, 100, 150)
    py5.circle(x, y, 30)
    
    x = 275
    y = 275
    py5.fill(0, 100, 255, 150)
    py5.circle(x, y, 30)
    
    x = 325
    y = 325
    py5.fill(100, 0, 255, 150)
    py5.circle(x, y, 30)
    
    x = 375
    y = 375
    py5.fill(200, 0, 255, 150)
    py5.circle(x, y, 30)
    
    # タイトルテキスト
    py5.fill(0)
    py5.text_size(16)
    py5.text("座標系の学習", 10, 480)

py5.run_sketch()