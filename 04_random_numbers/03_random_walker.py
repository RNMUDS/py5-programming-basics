"""
乱数 - ランダムウォーカー
乱数を使って点がランダムに動き回るシミュレーション
"""
import py5

# ウォーカーの初期位置
walker_x = 250
walker_y = 200
trail = []  # 軌跡を記録

def setup():
    py5.size(500, 400)
    py5.background(20, 20, 40)
    global walker_x, walker_y
    walker_x = py5.width // 2
    walker_y = py5.height // 2
    trail.append((walker_x, walker_y))

def draw():
    # 背景を少し透明にして軌跡を残す
    py5.fill(20, 20, 40, 50)
    py5.rect(0, 0, py5.width, py5.height)
    
    global walker_x, walker_y
    
    # ランダムな方向に移動
    direction = int(py5.random(0, 8))  # 8方向
    step_size = 3
    
    if direction == 0:    # 上
        walker_y -= step_size
    elif direction == 1:  # 右上
        walker_x += step_size
        walker_y -= step_size
    elif direction == 2:  # 右
        walker_x += step_size
    elif direction == 3:  # 右下
        walker_x += step_size
        walker_y += step_size
    elif direction == 4:  # 下
        walker_y += step_size
    elif direction == 5:  # 左下
        walker_x -= step_size
        walker_y += step_size
    elif direction == 6:  # 左
        walker_x -= step_size
    elif direction == 7:  # 左上
        walker_x -= step_size
        walker_y -= step_size
    
    # 境界チェック
    walker_x = py5.constrain(walker_x, 10, py5.width - 10)
    walker_y = py5.constrain(walker_y, 10, py5.height - 10)
    
    # 軌跡に追加
    trail.append((walker_x, walker_y))
    if len(trail) > 200:  # 軌跡の長さを制限
        trail.pop(0)
    
    # 軌跡を描画
    py5.stroke(100, 150, 255, 150)
    py5.stroke_weight(2)
    for i in range(1, len(trail)):
        alpha = int(255 * i / len(trail))  # 徐々に濃くなる
        py5.stroke(100, 150, 255, alpha)
        py5.line(trail[i-1][0], trail[i-1][1], trail[i][0], trail[i][1])
    
    # 現在位置を描画
    py5.fill(255, 100, 100)
    py5.no_stroke()
    py5.circle(walker_x, walker_y, 12)
    
    # 情報表示
    py5.fill(255)
    py5.text_size(14)
    py5.text(f"位置: ({walker_x}, {walker_y})", 10, 25)
    py5.text(f"歩数: {len(trail)}", 10, 45)
    py5.text("Rキーでリセット", 10, 380)

def key_pressed():
    global walker_x, walker_y, trail
    if py5.key == 'r' or py5.key == 'R':
        # リセット
        walker_x = py5.width // 2
        walker_y = py5.height // 2
        trail.clear()
        trail.append((walker_x, walker_y))
        py5.background(20, 20, 40)

py5.run_sketch()