"""
リスト - ソートの視覚化
リストのソート処理を視覚的に表示します
"""
import py5

numbers = []
sorting = False
current_i = 0
current_j = 0

def setup():
    py5.size(800, 400)
    generate_random_list()

def generate_random_list():
    """ランダムなリストを生成"""
    global numbers, sorting, current_i, current_j
    numbers = []
    for i in range(40):
        numbers.append(py5.random(10, 300))
    sorting = False
    current_i = 0
    current_j = 0

def bubble_sort_step():
    """バブルソートの1ステップを実行"""
    global current_i, current_j, sorting
    
    if current_i < len(numbers) - 1:
        if current_j < len(numbers) - current_i - 1:
            # 隣接する要素を比較
            if numbers[current_j] > numbers[current_j + 1]:
                # 交換
                numbers[current_j], numbers[current_j + 1] = numbers[current_j + 1], numbers[current_j]
            current_j += 1
        else:
            current_i += 1
            current_j = 0
    else:
        sorting = False  # ソート完了

def draw():
    py5.background(240, 240, 255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("バブルソートの視覚化", 300, 30)
    
    # リストの状態を描画
    bar_width = py5.width / len(numbers)
    for i in range(len(numbers)):
        x = i * bar_width
        height = numbers[i]
        
        # 現在比較中の要素を色分け
        if sorting and (i == current_j or i == current_j + 1):
            if numbers[i] > numbers[min(i + 1, len(numbers) - 1)] and i == current_j:
                py5.fill(255, 100, 100)  # 交換される要素（赤）
            else:
                py5.fill(255, 255, 100)  # 比較中の要素（黄）
        elif sorting and i > len(numbers) - current_i - 1:
            py5.fill(100, 255, 100)  # ソート済み（緑）
        else:
            py5.fill(100, 150, 255)  # 未ソート（青）
        
        py5.rect(x, py5.height - height - 50, bar_width - 2, height)
        
        # インデックスを表示（最初の10個のみ）
        if i < 10:
            py5.fill(0)
            py5.text_size(10)
            py5.text(str(i), x + 2, py5.height - 35)
    
    # ソートの進行状況
    if sorting:
        bubble_sort_step()
        py5.fill(0)
        py5.text_size(14)
        py5.text(f"比較中: インデックス {current_j} と {current_j + 1}", 50, 360)
        py5.text(f"ソート進行: {current_i + 1}/{len(numbers) - 1} パス", 50, 380)
    else:
        py5.fill(0)
        py5.text_size(16)
        py5.text("ソート完了！", 350, 360)
    
    # 操作説明
    py5.text_size(12)
    py5.text("スペース: ソート開始/停止  R: リセット", 50, 60)
    
    # 統計情報
    py5.text(f"要素数: {len(numbers)}", 600, 60)
    py5.text(f"最小値: {min(numbers):.1f}", 600, 80)
    py5.text(f"最大値: {max(numbers):.1f}", 600, 100)

def key_pressed():
    global sorting
    if py5.key == ' ':
        sorting = not sorting
    elif py5.key == 'r' or py5.key == 'R':
        generate_random_list()

py5.run_sketch()