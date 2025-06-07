"""
乱数の基本 - ランダムな色の円
random関数を使用してランダムな色の図形を描画します
"""
import py5

def setup():
    py5.size(600, 400)
    py5.background(255)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 16)
    py5.text_font(font)
    
    # ランダムな位置にランダムな色の円を描画
    for i in range(50):
        # ランダムな位置
        x = py5.random(50, 550)
        y = py5.random(50, 350)
        
        # ランダムな色
        r = py5.random(0, 255)
        g = py5.random(0, 255)
        b = py5.random(0, 255)
        
        # ランダムなサイズ
        size = py5.random(10, 50)
        
        py5.fill(r, g, b, 150)
        py5.circle(x, y, size)
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("ランダムな色とサイズの円", 170, 30)

def mouse_pressed():
    # マウスクリックで再描画
    py5.background(255)
    
    # 新しいランダムパターンを生成
    for i in range(50):
        x = py5.random(50, 550)
        y = py5.random(50, 350)
        r = py5.random(0, 255)
        g = py5.random(0, 255)
        b = py5.random(0, 255)
        size = py5.random(10, 50)
        
        py5.fill(r, g, b, 150)
        py5.circle(x, y, size)
    
    # タイトルを再描画
    py5.fill(0)
    py5.text_size(20)
    py5.text("ランダムな色とサイズの円", 170, 30)
    py5.text_size(14)
    py5.text("クリックで再生成", 250, 380)

py5.run_sketch()