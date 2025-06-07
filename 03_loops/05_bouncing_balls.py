"""
繰り返し - バウンドするボール
アニメーションループとリストを使用してボールを動かします
"""
import py5

# ボールの情報を格納するリスト
balls = []

def setup():
    py5.size(600, 400)
    
    # 複数のボールを初期化
    for i in range(8):
        ball = {
            'x': py5.random(50, 550),
            'y': py5.random(50, 350),
            'vx': py5.random(-5, 5),
            'vy': py5.random(-5, 5),
            'color': (py5.random(100, 255), py5.random(100, 255), py5.random(100, 255)),
            'size': py5.random(20, 40)
        }
        balls.append(ball)

def draw():
    py5.background(30, 30, 50)
    
    # 各ボールを更新して描画
    for ball in balls:
        # 位置を更新
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        
        # 壁との衝突判定
        if ball['x'] <= ball['size']/2 or ball['x'] >= 600 - ball['size']/2:
            ball['vx'] *= -1
        if ball['y'] <= ball['size']/2 or ball['y'] >= 400 - ball['size']/2:
            ball['vy'] *= -1
        
        # 境界内に収める
        ball['x'] = py5.constrain(ball['x'], ball['size']/2, 600 - ball['size']/2)
        ball['y'] = py5.constrain(ball['y'], ball['size']/2, 400 - ball['size']/2)
        
        # ボールを描画
        py5.fill(ball['color'][0], ball['color'][1], ball['color'][2], 200)
        py5.circle(ball['x'], ball['y'], ball['size'])
        
        # 軌跡を描画（薄く）
        py5.fill(ball['color'][0], ball['color'][1], ball['color'][2], 50)
        py5.circle(ball['x'] - ball['vx'], ball['y'] - ball['vy'], ball['size'] * 0.8)
    
    # 情報表示
    py5.fill(255)
    py5.text_size(14)
    py5.text(f"ボールの数: {len(balls)}", 10, 25)
    py5.text("スペースキーでボールを追加", 10, 45)

def key_pressed():
    if py5.key == ' ':
        # 新しいボールを追加
        new_ball = {
            'x': py5.random(50, 550),
            'y': py5.random(50, 350),
            'vx': py5.random(-5, 5),
            'vy': py5.random(-5, 5),
            'color': (py5.random(100, 255), py5.random(100, 255), py5.random(100, 255)),
            'size': py5.random(20, 40)
        }
        balls.append(new_ball)

py5.run_sketch()