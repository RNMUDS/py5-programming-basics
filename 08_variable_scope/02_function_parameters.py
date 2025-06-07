"""
変数スコープ - 関数の引数と戻り値
関数の引数（パラメータ）と戻り値の仕組みを学習します
"""
import py5

# グローバル変数
shapes = []
current_shape = {"type": "circle", "x": 300, "y": 200, "size": 50, "color": [255, 100, 100]}

def create_shape(shape_type, x, y, size, color):
    """新しい図形を作成する関数（引数を使用）"""
    new_shape = {
        "type": shape_type,
        "x": x,
        "y": y,
        "size": size,
        "color": color.copy()  # リストのコピーを作成
    }
    return new_shape

def modify_shape_color(shape, red_change, green_change, blue_change):
    """図形の色を変更する関数（引数で変更量を指定）"""
    # 新しい色を計算（範囲チェック付き）
    new_color = [
        max(0, min(255, shape["color"][0] + red_change)),
        max(0, min(255, shape["color"][1] + green_change)),
        max(0, min(255, shape["color"][2] + blue_change))
    ]
    return new_color

def calculate_distance(x1, y1, x2, y2):
    """2点間の距離を計算する関数"""
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def draw_shape(shape):
    """図形を描画する関数"""
    py5.fill(shape["color"][0], shape["color"][1], shape["color"][2])
    
    if shape["type"] == "circle":
        py5.circle(shape["x"], shape["y"], shape["size"])
    elif shape["type"] == "square":
        py5.rect(shape["x"] - shape["size"]//2, shape["y"] - shape["size"]//2, 
                shape["size"], shape["size"])
    elif shape["type"] == "triangle":
        s = shape["size"] // 2
        py5.triangle(shape["x"], shape["y"] - s, 
                    shape["x"] - s, shape["y"] + s, 
                    shape["x"] + s, shape["y"] + s)

def setup():
    py5.size(800, 600)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 14)
    py5.text_font(font)
    
    # 初期図形をいくつか作成
    global shapes
    shapes.append(create_shape("circle", 150, 150, 60, [255, 100, 100]))
    shapes.append(create_shape("square", 300, 150, 50, [100, 255, 100]))
    shapes.append(create_shape("triangle", 450, 150, 70, [100, 100, 255]))

def draw():
    py5.background(240, 240, 255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("関数の引数と戻り値", 280, 40)
    
    # 保存された図形を描画
    for shape in shapes:
        draw_shape(shape)
    
    # 現在の図形を描画
    draw_shape(current_shape)
    
    # マウスとの距離を計算して表示
    for i, shape in enumerate(shapes):
        distance = calculate_distance(shape["x"], shape["y"], py5.mouse_x, py5.mouse_y)
        py5.fill(0)
        py5.text_size(10)
        py5.text(f"距離: {distance:.1f}", shape["x"] - 20, shape["y"] + shape["size"]//2 + 15)
    
    # 現在の図形の情報表示
    py5.fill(0)
    py5.text_size(16)
    py5.text("現在の図形（パラメータ例）:", 50, 300)
    py5.text_size(12)
    py5.text(f"種類: {current_shape['type']}", 50, 325)
    py5.text(f"位置: ({current_shape['x']}, {current_shape['y']})", 50, 345)
    py5.text(f"サイズ: {current_shape['size']}", 50, 365)
    py5.text(f"色: {current_shape['color']}", 50, 385)
    
    # 関数の説明
    py5.text_size(14)
    py5.text("関数の引数と戻り値の例:", 400, 300)
    py5.text_size(11)
    py5.text("• create_shape(type, x, y, size, color) → 新しい図形", 400, 320)
    py5.text("• modify_shape_color(shape, r, g, b) → 新しい色", 400, 340)
    py5.text("• calculate_distance(x1, y1, x2, y2) → 距離", 400, 360)
    py5.text("• draw_shape(shape) → なし（描画のみ）", 400, 380)
    
    # 操作説明
    py5.text_size(12)
    py5.text("操作方法:", 50, 450)
    py5.text("• 1,2,3キー: 図形タイプ変更", 50, 470)
    py5.text("• ↑↓キー: サイズ変更", 50, 490)
    py5.text("• R,G,Bキー: 色変更", 50, 510)
    py5.text("• スペース: 図形を保存", 50, 530)
    py5.text("• マウス: 図形移動", 50, 550)
    
    # 重要概念の説明
    py5.fill(100, 0, 0)
    py5.text_size(11)
    py5.text("重要: 引数は関数に値を渡すための仕組み", 400, 450)
    py5.text("戻り値は関数から結果を受け取るための仕組み", 400, 470)
    py5.text("引数の変更は元の変数に影響しない（値渡し）", 400, 490)
    py5.text("リストや辞書は参照渡しなので注意が必要", 400, 510)

def key_pressed():
    global current_shape, shapes
    
    if py5.key == '1':
        current_shape["type"] = "circle"
    elif py5.key == '2':
        current_shape["type"] = "square"
    elif py5.key == '3':
        current_shape["type"] = "triangle"
    elif py5.key == py5.UP:
        current_shape["size"] = min(100, current_shape["size"] + 10)
    elif py5.key == py5.DOWN:
        current_shape["size"] = max(20, current_shape["size"] - 10)
    elif py5.key == 'r' or py5.key == 'R':
        current_shape["color"] = modify_shape_color(current_shape, 20, 0, 0)
    elif py5.key == 'g' or py5.key == 'G':
        current_shape["color"] = modify_shape_color(current_shape, 0, 20, 0)
    elif py5.key == 'b' or py5.key == 'B':
        current_shape["color"] = modify_shape_color(current_shape, 0, 0, 20)
    elif py5.key == ' ':
        # 新しい図形を作成して保存
        new_shape = create_shape(current_shape["type"], current_shape["x"], 
                                 current_shape["y"], current_shape["size"], 
                                 current_shape["color"])
        shapes.append(new_shape)

def mouse_moved():
    """マウス移動で現在の図形を移動"""
    global current_shape
    current_shape["x"] = py5.mouse_x
    current_shape["y"] = py5.mouse_y

py5.run_sketch()