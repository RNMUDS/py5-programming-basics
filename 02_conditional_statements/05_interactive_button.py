"""
条件分岐 - インタラクティブなボタン
マウスの位置によってボタンの色が変わります
"""
import py5

button_x = 150
button_y = 200
button_width = 100
button_height = 50

def setup():
    py5.size(400, 400)

def draw():
    py5.background(240, 240, 255)
    
    # マウスがボタンの上にあるかチェック
    if (button_x < py5.mouse_x < button_x + button_width and 
        button_y < py5.mouse_y < button_y + button_height):
        # マウスがボタンの上にある場合
        button_color = (100, 255, 100)  # 緑色
        text_color = (255, 255, 255)    # 白文字
        message = "ボタンにマウスが重なっています！"
    else:
        # マウスがボタンの外にある場合
        button_color = (200, 200, 200)  # グレー
        text_color = (0, 0, 0)          # 黒文字
        message = "ボタンにマウスを重ねてみてください"
    
    # ボタンを描画
    py5.fill(button_color[0], button_color[1], button_color[2])
    py5.stroke(100)
    py5.stroke_weight(2)
    py5.rect(button_x, button_y, button_width, button_height)
    
    # ボタンのテキスト
    py5.fill(text_color[0], text_color[1], text_color[2])
    py5.text_size(16)
    py5.text("クリック", button_x + 20, button_y + 30)
    
    # メッセージを表示
    py5.fill(0)
    py5.text_size(14)
    py5.text(message, 50, 320)
    
    # マウス座標を表示
    py5.text(f"マウス座標: ({py5.mouse_x}, {py5.mouse_y})", 50, 350)
    
    # 境界線を表示（デバッグ用）
    py5.stroke(255, 0, 0)
    py5.stroke_weight(1)
    py5.no_fill()
    py5.rect(button_x - 1, button_y - 1, button_width + 2, button_height + 2)

def mouse_pressed():
    # マウスがボタン内でクリックされた場合
    if (button_x < py5.mouse_x < button_x + button_width and 
        button_y < py5.mouse_y < button_y + button_height):
        print("ボタンがクリックされました！")

py5.run_sketch()