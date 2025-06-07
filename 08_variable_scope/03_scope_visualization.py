"""
変数スコープ - スコープの視覚化
変数のスコープを視覚的に理解するためのデモ
"""
import py5

# グローバル変数
global_x = 400
global_y = 100
global_size = 50
execution_log = []

def function_a():
    """関数A - ローカル変数とグローバル変数の混在"""
    # ローカル変数
    local_x = 150
    local_y = 200
    local_size = 30
    
    # グローバル変数の読み取り
    global global_size
    combined_size = local_size + global_size // 2
    
    # 実行ログに追加
    execution_log.append(f"関数A: local_x={local_x}, global_size={global_size}")
    
    return local_x, local_y, combined_size

def function_b(param_x, param_y):
    """関数B - 引数を使用したローカルスコープ"""
    # 引数もローカル変数
    local_color = [param_x % 255, param_y % 255, 150]
    local_message = f"座標({param_x}, {param_y})"
    
    # ネストした関数
    def nested_function():
        nested_value = param_x + param_y
        return nested_value * 2
    
    nested_result = nested_function()
    execution_log.append(f"関数B: param_x={param_x}, nested_result={nested_result}")
    
    return local_color, local_message, nested_result

def function_c():
    """関数C - グローバル変数の変更"""
    global global_x, global_y
    
    # グローバル変数を変更
    old_x, old_y = global_x, global_y
    global_x = (global_x + 10) % 800
    global_y = (global_y + 5) % 300
    
    execution_log.append(f"関数C: ({old_x},{old_y}) → ({global_x},{global_y})")
    
    return old_x, old_y

def demonstrate_variable_shadowing():
    """変数のシャドウイング（隠蔽）を示す関数"""
    global_size = 25  # ローカル変数（グローバル変数を隠す）
    shadow_message = f"ローカルのglobal_size={global_size}"
    
    execution_log.append(f"シャドウイング: {shadow_message}")
    
    return global_size, shadow_message

def setup():
    py5.size(800, 600)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 12)
    py5.text_font(font)

def draw():
    py5.background(245, 245, 250)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("変数スコープの視覚化", 280, 40)
    
    # グローバル変数の表示
    py5.text_size(16)
    py5.text("グローバル変数:", 50, 80)
    py5.text_size(12)
    py5.text(f"global_x = {global_x}", 50, 100)
    py5.text(f"global_y = {global_y}", 50, 120)
    py5.text(f"global_size = {global_size}", 50, 140)
    
    # グローバル変数による図形
    py5.fill(255, 100, 100, 150)
    py5.stroke(255, 0, 0)
    py5.stroke_weight(2)
    py5.circle(global_x, global_y, global_size)
    py5.no_stroke()
    
    # 関数Aの実行結果
    result_a = function_a()
    py5.fill(0)
    py5.text_size(16)
    py5.text("関数A（ローカル変数）:", 300, 80)
    py5.text_size(12)
    py5.text(f"local_x = {result_a[0]}", 300, 100)
    py5.text(f"local_y = {result_a[1]}", 300, 120)
    py5.text(f"combined_size = {result_a[2]}", 300, 140)
    
    # 関数Aによる図形
    py5.fill(100, 255, 100, 150)
    py5.stroke(0, 255, 0)
    py5.stroke_weight(2)
    py5.circle(result_a[0], result_a[1], result_a[2])
    py5.no_stroke()
    
    # 関数Bの実行結果
    result_b = function_b(py5.mouse_x, py5.mouse_y)
    py5.text_size(16)
    py5.text("関数B（引数パラメータ）:", 550, 80)
    py5.text_size(12)
    py5.text(f"param_x = {py5.mouse_x}", 550, 100)
    py5.text(f"param_y = {py5.mouse_y}", 550, 120)
    py5.text(f"nested_result = {result_b[2]}", 550, 140)
    
    # 関数Bによる図形
    py5.fill(result_b[0][0], result_b[0][1], result_b[0][2], 150)
    py5.stroke(100, 100, 255)
    py5.stroke_weight(2)
    py5.rect(py5.mouse_x - 15, py5.mouse_y - 15, 30, 30)
    py5.no_stroke()
    
    # シャドウイングの例
    shadow_result = demonstrate_variable_shadowing()
    py5.fill(0)
    py5.text_size(16)
    py5.text("変数のシャドウイング:", 50, 200)
    py5.text_size(12)
    py5.text(f"グローバル: global_size = {global_size}", 50, 220)
    py5.text(f"ローカル: global_size = {shadow_result[0]}", 50, 240)
    
    # 実行ログの表示
    py5.text_size(14)
    py5.text("実行ログ（最新5件）:", 50, 300)
    py5.text_size(10)
    for i, log in enumerate(execution_log[-5:]):
        py5.text(log, 50, 320 + i * 15)
    
    # スコープの概念図
    py5.text_size(16)
    py5.text("スコープの概念図:", 400, 300)
    
    # グローバルスコープ
    py5.stroke(255, 0, 0)
    py5.stroke_weight(3)
    py5.no_fill()
    py5.rect(420, 320, 300, 200)
    py5.fill(255, 0, 0)
    py5.text_size(12)
    py5.text("グローバルスコープ", 430, 340)
    
    # 関数スコープ
    py5.stroke(0, 255, 0)
    py5.stroke_weight(2)
    py5.no_fill()
    py5.rect(440, 360, 120, 80)
    py5.fill(0, 255, 0)
    py5.text("関数スコープ", 450, 380)
    
    py5.rect(580, 360, 120, 80)
    py5.text("関数スコープ", 590, 380)
    
    # ネストしたスコープ
    py5.stroke(0, 0, 255)
    py5.stroke_weight(1)
    py5.rect(590, 400, 80, 30)
    py5.fill(0, 0, 255)
    py5.text_size(10)
    py5.text("ネストスコープ", 595, 415)
    
    py5.no_stroke()
    
    # 操作説明
    py5.fill(0)
    py5.text_size(12)
    py5.text("操作方法:", 50, 550)
    py5.text("• マウス移動: 関数Bの引数を変更", 50, 565)
    py5.text("• スペース: グローバル変数を変更", 200, 565)
    py5.text("• Cキー: ログをクリア", 350, 565)

def key_pressed():
    global execution_log
    
    if py5.key == ' ':
        function_c()
    elif py5.key == 'c' or py5.key == 'C':
        execution_log.clear()

py5.run_sketch()