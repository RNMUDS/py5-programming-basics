"""
変数スコープの基本 - グローバル変数とローカル変数
関数内外での変数の扱いを学習します
"""
import py5

# グローバル変数
global_counter = 0
global_color = [255, 100, 100]
message = "グローバル変数の値"

def increase_global():
    """グローバル変数を増加させる関数"""
    global global_counter, global_color
    global_counter += 1
    # 色を変更
    global_color[0] = (global_color[0] + 10) % 255
    global_color[1] = (global_color[1] + 5) % 255
    global_color[2] = (global_color[2] + 15) % 255

def local_function():
    """ローカル変数を使用する関数"""
    local_counter = 100  # ローカル変数
    local_message = "これはローカル変数"
    local_color = [100, 255, 100]
    
    return local_counter, local_message, local_color

def demonstrate_scope():
    """スコープの違いを示す関数"""
    # ローカル変数
    local_var = "関数内のローカル変数"
    
    # グローバル変数にアクセス
    global message
    original_message = message
    message = "関数内で変更されたグローバル変数"
    
    return local_var, original_message

def setup():
    py5.size(700, 500)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 14)
    py5.text_font(font)

def draw():
    py5.background(240, 240, 255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("変数スコープの学習", 230, 40)
    
    # グローバル変数の表示
    py5.text_size(18)
    py5.text("グローバル変数:", 50, 80)
    
    py5.text_size(14)
    py5.text(f"global_counter = {global_counter}", 50, 105)
    py5.text(f"global_color = {global_color}", 50, 125)
    py5.text(f"message = \"{message}\"", 50, 145)
    
    # グローバル変数による図形描画
    py5.fill(global_color[0], global_color[1], global_color[2])
    py5.circle(400, 120, 50 + global_counter * 2)
    
    # ローカル変数の例
    local_result = local_function()
    py5.fill(0)
    py5.text_size(18)
    py5.text("ローカル変数（関数から返された値）:", 50, 200)
    
    py5.text_size(14)
    py5.text(f"local_counter = {local_result[0]}", 50, 225)
    py5.text(f"local_message = \"{local_result[1]}\"", 50, 245)
    py5.text(f"local_color = {local_result[2]}", 50, 265)
    
    # ローカル変数による図形描画
    py5.fill(local_result[2][0], local_result[2][1], local_result[2][2])
    py5.circle(400, 250, 60)
    
    # スコープの違いの実演
    scope_result = demonstrate_scope()
    py5.fill(0)
    py5.text_size(18)
    py5.text("スコープの違い:", 50, 320)
    
    py5.text_size(14)
    py5.text(f"関数内のローカル変数: \"{scope_result[0]}\"", 50, 345)
    py5.text(f"元のグローバル変数: \"{scope_result[1]}\"", 50, 365)
    py5.text(f"変更後のグローバル変数: \"{message}\"", 50, 385)
    
    # 操作説明
    py5.text_size(16)
    py5.text("操作方法:", 50, 430)
    py5.text_size(12)
    py5.text("• スペースキー: グローバル変数を変更", 50, 450)
    py5.text("• Rキー: リセット", 50, 465)
    
    # 重要な概念の説明
    py5.fill(100, 0, 0)
    py5.text_size(12)
    py5.text("重要: グローバル変数は関数外で定義され、どこからでもアクセス可能", 350, 350)
    py5.text("ローカル変数は関数内でのみ有効", 350, 370)
    py5.text("global キーワードで関数内からグローバル変数を変更可能", 350, 390)

def key_pressed():
    global global_counter, global_color, message
    
    if py5.key == ' ':
        increase_global()
    elif py5.key == 'r' or py5.key == 'R':
        # リセット
        global_counter = 0
        global_color = [255, 100, 100]
        message = "グローバル変数の値"

py5.run_sketch()