"""
辞書 - 単語カウンター
辞書を使用して文字の出現頻度を視覚化します
"""
import py5

text_input = "Hello Python Programming"
char_count = {}
current_char = 0
animation_speed = 3

def setup():
    py5.size(800, 600)
    count_characters()

def count_characters():
    """文字の出現頻度をカウント"""
    global char_count
    char_count = {}
    
    for char in text_input.lower():
        if char.isalpha():  # アルファベットのみカウント
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

def draw():
    global current_char
    py5.background(240, 248, 255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("文字出現頻度カウンター", 250, 40)
    
    # 入力テキストを表示
    py5.text_size(18)
    py5.text(f"テキスト: \"{text_input}\"", 50, 80)
    
    # 現在処理中の文字をハイライト
    if current_char < len(text_input):
        highlight_x = 140 + current_char * 12
        py5.fill(255, 255, 0, 150)
        py5.rect(highlight_x, 60, 12, 25)
        current_char += animation_speed
    
    # 文字カウントのグラフを描画
    py5.text_size(16)
    py5.text("文字の出現頻度:", 50, 130)
    
    # 辞書をソート（頻度順）
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    x = 50
    y = 160
    max_count = max(char_count.values()) if char_count else 1
    
    for i, (char, count) in enumerate(sorted_chars):
        # バーの高さを計算
        bar_height = int(py5.map(count, 0, max_count, 0, 200))
        
        # 色を頻度に応じて変更
        if count >= max_count * 0.8:
            py5.fill(255, 100, 100)  # 赤（最頻出）
        elif count >= max_count * 0.6:
            py5.fill(255, 200, 100)  # オレンジ
        elif count >= max_count * 0.4:
            py5.fill(255, 255, 100)  # 黄色
        else:
            py5.fill(150, 200, 255)  # 青
        
        # バーを描画
        py5.rect(x, y + 200 - bar_height, 40, bar_height)
        
        # 文字を表示
        py5.fill(0)
        py5.text_size(20)
        py5.text(char.upper(), x + 15, y + 230)
        
        # カウントを表示
        py5.text_size(14)
        py5.text(str(count), x + 15, y + 250)
        
        x += 50
        
        # 行の折り返し
        if x > 700:
            x = 50
            y += 120
    
    # 統計情報
    py5.fill(0)
    py5.text_size(14)
    total_chars = len([c for c in text_input if c.isalpha()])
    unique_chars = len(char_count)
    
    py5.text("統計情報:", 50, 520)
    py5.text(f"総文字数: {total_chars}", 50, 540)
    py5.text(f"ユニーク文字数: {unique_chars}", 200, 540)
    
    if char_count:
        most_common = max(char_count.items(), key=lambda x: x[1])
        py5.text(f"最頻出文字: '{most_common[0]}' ({most_common[1]}回)", 350, 540)
    
    # 操作説明
    py5.text("操作: 1-4キーで異なるテキストを選択, Rキーでリセット", 50, 570)

def key_pressed():
    global text_input, current_char
    
    if py5.key == '1':
        text_input = "Hello Python Programming"
    elif py5.key == '2':
        text_input = "The quick brown fox jumps over the lazy dog"
    elif py5.key == '3':
        text_input = "Python is a powerful programming language"
    elif py5.key == '4':
        text_input = "Data visualization with py5 is amazing"
    elif py5.key == 'r' or py5.key == 'R':
        current_char = 0
    
    # 文字カウントを再計算
    count_characters()
    current_char = 0

py5.run_sketch()