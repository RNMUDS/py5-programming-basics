"""
乱数 - サイコロシミュレータ
整数の乱数を使用してサイコロを作成します
"""
import py5

dice_value = 1
dice_history = []

def setup():
    py5.size(500, 400)
    py5.background(240, 240, 255)

def draw():
    py5.background(240, 240, 255)
    
    # サイコロの枠を描画
    py5.fill(255)
    py5.stroke(0)
    py5.stroke_weight(3)
    py5.rect(150, 100, 100, 100)
    
    # サイコロの目を描画
    draw_dice_dots(200, 150, dice_value)
    
    # 現在の値を表示
    py5.fill(0)
    py5.text_size(24)
    py5.text(f"出た目: {dice_value}", 170, 250)
    
    # 履歴を表示
    py5.text_size(16)
    py5.text("履歴:", 50, 300)
    if len(dice_history) > 0:
        history_text = " ".join(map(str, dice_history[-10:]))  # 最新10個
        py5.text(history_text, 100, 300)
    
    # 統計を表示
    if len(dice_history) > 0:
        py5.text(f"試行回数: {len(dice_history)}", 50, 330)
        average = sum(dice_history) / len(dice_history)
        py5.text(f"平均: {average:.2f}", 200, 330)
    
    # 操作説明
    py5.text_size(14)
    py5.text("スペースキーでサイコロを振る", 150, 370)

def draw_dice_dots(center_x, center_y, value):
    dot_size = 12
    py5.fill(0)
    py5.no_stroke()
    
    if value == 1:
        py5.circle(center_x, center_y, dot_size)
    elif value == 2:
        py5.circle(center_x - 20, center_y - 20, dot_size)
        py5.circle(center_x + 20, center_y + 20, dot_size)
    elif value == 3:
        py5.circle(center_x - 20, center_y - 20, dot_size)
        py5.circle(center_x, center_y, dot_size)
        py5.circle(center_x + 20, center_y + 20, dot_size)
    elif value == 4:
        py5.circle(center_x - 20, center_y - 20, dot_size)
        py5.circle(center_x + 20, center_y - 20, dot_size)
        py5.circle(center_x - 20, center_y + 20, dot_size)
        py5.circle(center_x + 20, center_y + 20, dot_size)
    elif value == 5:
        py5.circle(center_x - 20, center_y - 20, dot_size)
        py5.circle(center_x + 20, center_y - 20, dot_size)
        py5.circle(center_x, center_y, dot_size)
        py5.circle(center_x - 20, center_y + 20, dot_size)
        py5.circle(center_x + 20, center_y + 20, dot_size)
    elif value == 6:
        py5.circle(center_x - 20, center_y - 20, dot_size)
        py5.circle(center_x + 20, center_y - 20, dot_size)
        py5.circle(center_x - 20, center_y, dot_size)
        py5.circle(center_x + 20, center_y, dot_size)
        py5.circle(center_x - 20, center_y + 20, dot_size)
        py5.circle(center_x + 20, center_y + 20, dot_size)

def key_pressed():
    global dice_value
    if py5.key == ' ':
        dice_value = int(py5.random(1, 7))  # 1-6のランダムな整数
        dice_history.append(dice_value)

py5.run_sketch()