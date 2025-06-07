"""
関数 - アニメーション関数
アニメーションに使用する関数を作成します
"""
import py5

frame_count = 0

def bounce_position(time, start, end, speed):
    """バウンドする位置を計算する関数"""
    # sin波を使ってバウンドアニメーション
    progress = (py5.sin(time * speed) + 1) / 2  # 0-1の範囲
    return start + (end - start) * progress

def rotate_around_point(center_x, center_y, radius, angle):
    """点の周りを回転する座標を計算する関数"""
    x = center_x + radius * py5.cos(angle)
    y = center_y + radius * py5.sin(angle)
    return x, y

def pulse_size(time, base_size, amplitude, speed):
    """脈動するサイズを計算する関数"""
    return base_size + amplitude * py5.sin(time * speed)

def wave_height(x, time, amplitude, frequency):
    """波の高さを計算する関数"""
    return amplitude * py5.sin(x * frequency + time)

def setup():
    py5.size(600, 400)

def draw():
    global frame_count
    py5.background(20, 20, 40)
    frame_count += 1
    time = frame_count * 0.05
    
    # バウンドするボール
    ball_y = bounce_position(time, 100, 300, 2)
    py5.fill(255, 100, 100)
    py5.circle(150, ball_y, 30)
    
    # 回転する惑星系
    center_x, center_y = 300, 200
    
    # 太陽
    py5.fill(255, 255, 0)
    py5.circle(center_x, center_y, 40)
    
    # 惑星1（近い軌道）
    planet1_x, planet1_y = rotate_around_point(center_x, center_y, 80, time * 2)
    py5.fill(100, 150, 255)
    py5.circle(planet1_x, planet1_y, 15)
    
    # 惑星2（遠い軌道）
    planet2_x, planet2_y = rotate_around_point(center_x, center_y, 120, time)
    py5.fill(255, 150, 100)
    py5.circle(planet2_x, planet2_y, 20)
    
    # 脈動する星
    star_size = pulse_size(time, 15, 10, 3)
    py5.fill(255, 255, 255, 200)
    py5.circle(500, 100, star_size)
    py5.circle(450, 150, pulse_size(time + 1, 12, 8, 2.5))
    py5.circle(520, 180, pulse_size(time + 2, 10, 6, 4))
    
    # 波のパターン
    py5.stroke(100, 255, 255)
    py5.stroke_weight(3)
    py5.no_fill()
    
    py5.begin_shape()
    for x in range(0, 600, 5):
        y = 350 + wave_height(x * 0.01, time * 2, 20, 1)
        py5.vertex(x, y)
    py5.end_shape()
    
    # 情報表示
    py5.fill(255)
    py5.text_size(14)
    py5.text("関数を使ったアニメーション", 10, 25)
    py5.text(f"フレーム: {frame_count}", 10, 45)

py5.run_sketch()