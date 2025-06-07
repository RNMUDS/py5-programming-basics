"""
順次制御の基本 - 簡単な図形を描画
基本的な図形描画命令を順番に実行します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(240, 248, 255)
    
    # 円を描画
    py5.fill(255, 100, 100)
    py5.circle(100, 100, 80)
    
    # 四角形を描画
    py5.fill(100, 255, 100)
    py5.rect(200, 50, 100, 80)
    
    # 三角形を描画
    py5.fill(100, 100, 255)
    py5.triangle(150, 200, 100, 300, 200, 300)
    
    # 線を描画
    py5.stroke(255, 0, 0)
    py5.stroke_weight(3)
    py5.line(50, 350, 350, 350)

py5.run_sketch()