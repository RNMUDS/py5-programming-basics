"""
順次制御 - 文字と数値の表示
変数を使用して計算結果を表示します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(240, 240, 255)
    
    # 数値変数の定義
    a = 10
    b = 5
    
    # 計算結果
    sum_result = a + b
    diff_result = a - b
    mult_result = a * b
    div_result = a / b
    
    # タイトル
    py5.fill(0, 0, 100)
    py5.text_size(20)
    py5.text("計算結果の表示", 120, 50)
    
    # 計算式と結果を表示
    py5.fill(0)
    py5.text_size(16)
    
    py5.text(f"a = {a}", 50, 100)
    py5.text(f"b = {b}", 50, 120)
    
    py5.text(f"a + b = {sum_result}", 50, 160)
    py5.text(f"a - b = {diff_result}", 50, 180)
    py5.text(f"a × b = {mult_result}", 50, 200)
    py5.text(f"a ÷ b = {div_result:.1f}", 50, 220)
    
    # 結果を使って図形を描画
    py5.fill(255, 100, 100)
    py5.circle(300, 120, sum_result * 4)
    
    py5.fill(100, 255, 100)
    py5.rect(250, 160, mult_result * 2, mult_result * 2)
    
    py5.fill(100, 100, 255)
    py5.rect(250, 250, 50, diff_result * 10)
    
    # 説明文
    py5.fill(50)
    py5.text_size(12)
    py5.text("計算結果で図形のサイズが決まります", 50, 350)

py5.run_sketch()