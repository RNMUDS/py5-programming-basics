"""
入れ子構造の基本 - ネストしたループ
二重ループを使用してパターンを作成します
"""
import py5

def setup():
    py5.size(600, 600)
    py5.background(255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("ネストしたループのパターン", 160, 40)
    
    # パターン1: グリッド状の円
    py5.text_size(16)
    py5.text("パターン1: グリッド状の円", 50, 80)
    
    for row in range(5):
        for col in range(8):
            x = 50 + col * 40
            y = 100 + row * 40
            
            # 位置によって色を変化
            red = int(255 * col / 7)
            green = int(255 * row / 4)
            blue = 150
            
            py5.fill(red, green, blue)
            py5.circle(x, y, 25)
    
    # パターン2: 三角形のパターン
    py5.text_size(16)
    py5.fill(0)
    py5.text("パターン2: 三角形のパターン", 350, 80)
    
    for row in range(6):
        for col in range(row + 1):
            x = 400 + col * 30 - row * 15
            y = 100 + row * 30
            
            py5.fill(255 - row * 40, 100 + col * 30, 200)
            py5.rect(x, y, 25, 25)
    
    # パターン3: チェッカーボード
    py5.text_size(16)
    py5.fill(0)
    py5.text("パターン3: チェッカーボード", 50, 320)
    
    square_size = 25
    for row in range(6):
        for col in range(8):
            x = 50 + col * square_size
            y = 340 + row * square_size
            
            # チェッカーパターン
            if (row + col) % 2 == 0:
                py5.fill(0)  # 黒
            else:
                py5.fill(255)  # 白
            
            py5.rect(x, y, square_size, square_size)
    
    # パターン4: 同心円
    py5.text_size(16)
    py5.fill(0)
    py5.text("パターン4: 同心円", 350, 320)
    
    center_x = 450
    center_y = 420
    
    for ring in range(8):
        for segment in range(ring * 4 + 4):
            angle = py5.TWO_PI * segment / (ring * 4 + 4)
            radius = 20 + ring * 15
            
            x = center_x + py5.cos(angle) * radius
            y = center_y + py5.sin(angle) * radius
            
            # 色を角度と半径で変化
            hue = int(255 * angle / py5.TWO_PI)
            saturation = int(255 * ring / 7)
            
            py5.fill(hue, saturation, 255, 150)
            py5.circle(x, y, 8)
    
    # パターン5: フラクタル風のパターン
    py5.text_size(16)
    py5.fill(0)
    py5.text("パターン5: フラクタル風", 50, 520)
    
    for level in range(4):
        for i in range(2 ** level):
            for j in range(2 ** level):
                x = 80 + i * (120 // (2 ** level))
                y = 540 + j * (120 // (2 ** level))
                size = 60 // (2 ** level)
                
                # レベルによって色を変化
                py5.fill(255 - level * 50, 100 + level * 50, 150 + level * 25)
                py5.rect(x, y, size, size)

py5.run_sketch()