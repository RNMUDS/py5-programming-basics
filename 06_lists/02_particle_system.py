"""
リスト - パーティクルシステム
リストを使用してパーティクルを管理します
"""
import py5

particles = []

def setup():
    py5.size(600, 400)
    
    # 初期パーティクルを作成
    for i in range(20):
        create_particle(py5.random(100, 500), py5.random(100, 300))

def create_particle(x, y):
    """新しいパーティクルを作成してリストに追加"""
    particle = {
        'x': x,
        'y': y,
        'vx': py5.random(-3, 3),
        'vy': py5.random(-3, 3),
        'life': 255,
        'size': py5.random(5, 15),
        'color': (py5.random(150, 255), py5.random(100, 255), py5.random(100, 255))
    }
    particles.append(particle)

def update_particles():
    """パーティクルを更新"""
    # 後ろから削除するために逆順でループ
    for i in range(len(particles) - 1, -1, -1):
        particle = particles[i]
        
        # 位置を更新
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        
        # 寿命を減らす
        particle['life'] -= 2
        
        # 重力効果
        particle['vy'] += 0.1
        
        # 境界でバウンド
        if particle['x'] < 0 or particle['x'] > py5.width:
            particle['vx'] *= -0.8
        if particle['y'] < 0 or particle['y'] > py5.height:
            particle['vy'] *= -0.8
        
        # 境界内に収める
        particle['x'] = py5.constrain(particle['x'], 0, py5.width)
        particle['y'] = py5.constrain(particle['y'], 0, py5.height)
        
        # 寿命が尽きたパーティクルを削除
        if particle['life'] <= 0:
            particles.pop(i)

def draw_particles():
    """パーティクルを描画"""
    for particle in particles:
        alpha = particle['life']
        py5.fill(particle['color'][0], particle['color'][1], particle['color'][2], alpha)
        py5.circle(particle['x'], particle['y'], particle['size'])

def draw():
    py5.background(20, 20, 40, 50)  # 軌跡を残すため半透明
    
    update_particles()
    draw_particles()
    
    # 情報表示
    py5.fill(255)
    py5.text_size(14)
    py5.text(f"パーティクル数: {len(particles)}", 10, 25)
    py5.text("マウスクリックで新しいパーティクルを追加", 10, 45)
    
    # パーティクルが少なくなったら自動追加
    if len(particles) < 5:
        create_particle(py5.random(100, 500), py5.random(100, 300))

def mouse_pressed():
    """マウスクリックで新しいパーティクルを追加"""
    for i in range(5):  # 5個のパーティクルを一度に追加
        create_particle(py5.mouse_x + py5.random(-20, 20), 
                       py5.mouse_y + py5.random(-20, 20))

py5.run_sketch()