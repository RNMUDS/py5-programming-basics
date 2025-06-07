"""
繰り返しの基本 - 円のパターン
for文を使用して複数の円を描画します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(255)
    
    # for文で円を描画
    for i in range(5):
        x = 50 + i * 70
        y = 100
        py5.fill(255 - i * 40, 100 + i * 30, 100 + i * 20)
        py5.circle(x, y, 50)
    
    # 縦方向にも円を描画
    for j in range(4):
        x = 200
        y = 150 + j * 50
        py5.fill(100 + j * 30, 255 - j * 40, 150)
        py5.circle(x, y, 40)
    
    # グリッド状に小さな円を描画
    for row in range(3):
        for col in range(6):
            x = 50 + col * 30
            y = 300 + row * 30
            py5.fill(100 + col * 20, 150, 200 + row * 20)
            py5.circle(x, y, 20)
    
    # 説明テキスト
    py5.fill(0)
    py5.text_size(14)
    py5.text("for文で描いた円のパターン", 10, 20)

py5.run_sketch()