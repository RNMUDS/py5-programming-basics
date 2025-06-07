"""
辞書 - カラーミキサー
辞書を使用して色の配合を管理します
"""
import py5

color_recipes = {}
current_color = [128, 128, 128]
selected_ingredient = None

def setup():
    py5.size(600, 500)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 14)
    py5.text_font(font)
    
    # 基本色の配合レシピ
    global color_recipes
    color_recipes = {
        "オレンジ": {"赤": 255, "緑": 165, "青": 0},
        "紫": {"赤": 128, "緑": 0, "青": 128},
        "ピンク": {"赤": 255, "緑": 192, "青": 203},
        "茶色": {"赤": 139, "緑": 69, "青": 19},
        "金色": {"赤": 255, "緑": 215, "青": 0},
        "水色": {"赤": 173, "緑": 216, "青": 230},
        "ライム": {"赤": 50, "緑": 205, "青": 50},
        "インディゴ": {"赤": 75, "緑": 0, "青": 130}
    }

def draw():
    py5.background(240, 240, 240)
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("カラーミキサー（辞書使用）", 200, 30)
    
    # 現在の色を表示
    py5.fill(current_color[0], current_color[1], current_color[2])
    py5.rect(50, 60, 150, 100)
    py5.fill(0)
    py5.text_size(14)
    py5.text("現在の色", 100, 180)
    py5.text(f"R:{current_color[0]}", 50, 195)
    py5.text(f"G:{current_color[1]}", 100, 195)
    py5.text(f"B:{current_color[2]}", 150, 195)
    
    # RGB調整スライダー
    py5.text("RGB調整:", 250, 80)
    
    # 赤のスライダー
    py5.fill(255, 100, 100)
    py5.rect(250, 90, 200, 20)
    red_pos = py5.map(current_color[0], 0, 255, 250, 450)
    py5.fill(255, 0, 0)
    py5.rect(red_pos - 5, 85, 10, 30)
    py5.fill(0)
    py5.text(f"赤: {current_color[0]}", 460, 105)
    
    # 緑のスライダー
    py5.fill(100, 255, 100)
    py5.rect(250, 120, 200, 20)
    green_pos = py5.map(current_color[1], 0, 255, 250, 450)
    py5.fill(0, 255, 0)
    py5.rect(green_pos - 5, 115, 10, 30)
    py5.fill(0)
    py5.text(f"緑: {current_color[1]}", 460, 135)
    
    # 青のスライダー
    py5.fill(100, 100, 255)
    py5.rect(250, 150, 200, 20)
    blue_pos = py5.map(current_color[2], 0, 255, 250, 450)
    py5.fill(0, 0, 255)
    py5.rect(blue_pos - 5, 145, 10, 30)
    py5.fill(0)
    py5.text(f"青: {current_color[2]}", 460, 165)
    
    # 保存されたレシピを表示
    py5.text_size(16)
    py5.text("保存されたレシピ:", 50, 240)
    
    y = 260
    for color_name, recipe in color_recipes.items():
        # レシピの色サンプル
        py5.fill(recipe["赤"], recipe["緑"], recipe["青"])
        py5.rect(50, y, 60, 30)
        
        # レシピ名
        py5.fill(0)
        py5.text_size(12)
        py5.text(color_name, 120, y + 20)
        
        # RGB値
        py5.text(f"R:{recipe['赤']} G:{recipe['緑']} B:{recipe['青']}", 200, y + 20)
        
        y += 40
    
    # 操作説明
    py5.text_size(12)
    py5.text("操作方法:", 400, 240)
    py5.text("• スライダーをクリックして色を調整", 400, 260)
    py5.text("• Sキーで現在の色を保存", 400, 280)
    py5.text("• レシピをクリックで色を読み込み", 400, 300)
    py5.text("• Rキーでリセット", 400, 320)

def mouse_pressed():
    global current_color
    
    # スライダーの操作
    if 250 <= py5.mouse_x <= 450:
        if 90 <= py5.mouse_y <= 110:  # 赤スライダー
            current_color[0] = int(py5.map(py5.mouse_x, 250, 450, 0, 255))
        elif 120 <= py5.mouse_y <= 140:  # 緑スライダー
            current_color[1] = int(py5.map(py5.mouse_x, 250, 450, 0, 255))
        elif 150 <= py5.mouse_y <= 170:  # 青スライダー
            current_color[2] = int(py5.map(py5.mouse_x, 250, 450, 0, 255))
    
    # レシピの選択
    if 50 <= py5.mouse_x <= 110:
        recipe_index = (py5.mouse_y - 260) // 40
        recipe_names = list(color_recipes.keys())
        if 0 <= recipe_index < len(recipe_names):
            selected_recipe = color_recipes[recipe_names[recipe_index]]
            current_color = [selected_recipe["赤"], selected_recipe["緑"], selected_recipe["青"]]

def key_pressed():
    global current_color, color_recipes
    
    if py5.key == 's' or py5.key == 'S':
        # 現在の色を新しいレシピとして保存
        recipe_name = f"カスタム{len(color_recipes) + 1}"
        color_recipes[recipe_name] = {
            "赤": current_color[0],
            "緑": current_color[1],
            "青": current_color[2]
        }
    elif py5.key == 'r' or py5.key == 'R':
        # リセット
        current_color = [128, 128, 128]

py5.run_sketch()