"""
繰り返し - スパイラルパターン
角度と半径を変化させてスパイラルを描画します
"""
import py5
import math

def setup():
    py5.size(400, 400)
    py5.background(20, 20, 40)
    
    # 中心点
    center_x = 200
    center_y = 200
    
    # スパイラル1（円のスパイラル）
    for i in range(100):
        angle = i * 0.3
        radius = i * 2
        x = center_x + radius * py5.cos(angle)
        y = center_y + radius * py5.sin(angle)
        
        # 色を変化させる
        red = int(255 * py5.sin(i * 0.1))
        green = int(255 * py5.cos(i * 0.1))
        blue = int(255 * py5.sin(i * 0.05))
        
        py5.fill(red, green, blue, 150)
        py5.circle(x, y, 10)
    
    # スパイラル2（線のスパイラル）
    py5.stroke(255, 255, 100, 100)
    py5.stroke_weight(2)
    py5.no_fill()
    
    points = []
    for i in range(200):
        angle = i * 0.2
        radius = i * 1
        x = center_x + radius * py5.cos(angle)
        y = center_y + radius * py5.sin(angle)
        points.append((x, y))
    
    # 点を線で結ぶ
    for i in range(len(points) - 1):
        py5.line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
    
    # タイトル
    py5.fill(255)
    py5.text_size(16)
    py5.text("スパイラルパターン", 10, 30)

py5.run_sketch()