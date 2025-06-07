"""
順次制御 - 色のグラデーション
変数を使用して順次的に色を変更します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(0)
    
    # 変数を定義
    r = 255
    g = 0
    b = 0
    
    # 赤から黄色への変化
    py5.fill(r, g, b)
    py5.rect(50, 50, 80, 80)
    
    g = 128
    py5.fill(r, g, b)
    py5.rect(150, 50, 80, 80)
    
    g = 255
    py5.fill(r, g, b)
    py5.rect(250, 50, 80, 80)
    
    # 黄色から緑への変化
    r = 128
    py5.fill(r, g, b)
    py5.rect(50, 150, 80, 80)
    
    r = 0
    py5.fill(r, g, b)
    py5.rect(150, 150, 80, 80)
    
    # 緑から青への変化
    g = 128
    b = 128
    py5.fill(r, g, b)
    py5.rect(250, 150, 80, 80)
    
    g = 0
    b = 255
    py5.fill(r, g, b)
    py5.rect(50, 250, 80, 80)
    
    # 青から紫への変化
    r = 128
    py5.fill(r, g, b)
    py5.rect(150, 250, 80, 80)
    
    r = 255
    py5.fill(r, g, b)
    py5.rect(250, 250, 80, 80)

py5.run_sketch()