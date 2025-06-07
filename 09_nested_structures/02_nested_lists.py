"""
入れ子構造 - ネストしたリスト
二次元リストを使用してデータを管理します
"""
import py5

# 二次元リストでゲームボードを表現
game_board = []
cell_size = 40
board_width = 10
board_height = 8

def setup():
    py5.size(700, 500)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 14)
    py5.text_font(font)
    
    initialize_board()

def initialize_board():
    """ゲームボードを初期化"""
    global game_board
    game_board = []
    
    for row in range(board_height):
        board_row = []
        for col in range(board_width):
            # ランダムな値（0-3）を配置
            value = int(py5.random(0, 4))
            board_row.append(value)
        game_board.append(board_row)

def draw():
    py5.background(240, 240, 255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("ネストしたリスト（二次元配列）", 200, 30)
    
    # ゲームボードを描画
    py5.text_size(16)
    py5.text("ゲームボード（二次元リスト）:", 50, 70)
    
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            x = 50 + col * cell_size
            y = 90 + row * cell_size
            value = game_board[row][col]
            
            # 値によって色を変更
            if value == 0:
                py5.fill(200, 200, 200)  # グレー
            elif value == 1:
                py5.fill(255, 150, 150)  # 薄い赤
            elif value == 2:
                py5.fill(150, 255, 150)  # 薄い緑
            elif value == 3:
                py5.fill(150, 150, 255)  # 薄い青
            
            # セルを描画
            py5.rect(x, y, cell_size, cell_size)
            
            # 値を表示
            py5.fill(0)
            py5.text_size(12)
            py5.text(str(value), x + 15, y + 25)
    
    # リストの構造を表示
    py5.fill(0)
    py5.text_size(14)
    py5.text("リストの構造例:", 500, 100)
    py5.text_size(10)
    
    # 最初の3行だけ表示
    for row in range(min(3, len(game_board))):
        row_text = f"行{row}: {game_board[row]}"
        if len(row_text) > 25:
            row_text = row_text[:25] + "..."
        py5.text(row_text, 500, 120 + row * 15)
    
    # 統計情報
    py5.text_size(14)
    py5.text("統計情報:", 500, 200)
    py5.text_size(12)
    
    # 各値の出現回数をカウント
    counts = [0, 0, 0, 0]
    total_cells = 0
    
    for row in game_board:
        for value in row:
            counts[value] += 1
            total_cells += 1
    
    py5.text(f"総セル数: {total_cells}", 500, 220)
    for i, count in enumerate(counts):
        percentage = (count / total_cells) * 100 if total_cells > 0 else 0
        py5.text(f"値{i}: {count}個 ({percentage:.1f}%)", 500, 240 + i * 15)
    
    # ネストしたリストの操作例
    py5.text_size(14)
    py5.text("ネストしたリストの操作例:", 50, 420)
    py5.text_size(11)
    py5.text("• game_board[行][列] でアクセス", 50, 440)
    py5.text("• len(game_board) で行数", 50, 455)
    py5.text("• len(game_board[0]) で列数", 50, 470)
    py5.text("• for row in game_board: で行を繰り返し", 250, 440)
    py5.text("• for cell in row: でセルを繰り返し", 250, 455)
    
    # 操作説明
    py5.text_size(12)
    py5.text("操作方法:", 500, 320)
    py5.text("• クリック: セルの値を変更", 500, 340)
    py5.text("• スペース: ボードをリセット", 500, 360)
    py5.text("• 1-4キー: 特定の値でフィル", 500, 380)

def mouse_pressed():
    """マウスクリックでセルの値を変更"""
    # クリック位置がボード内かチェック
    if 50 <= py5.mouse_x <= 50 + board_width * cell_size and \
       90 <= py5.mouse_y <= 90 + board_height * cell_size:
        
        # セルの位置を計算
        col = int((py5.mouse_x - 50) // cell_size)
        row = int((py5.mouse_y - 90) // cell_size)
        
        # 範囲チェック
        if 0 <= row < len(game_board) and 0 <= col < len(game_board[row]):
            # 値を循環させる（0→1→2→3→0）
            game_board[row][col] = (game_board[row][col] + 1) % 4

def key_pressed():
    global game_board
    
    if py5.key == ' ':
        # ボードをリセット
        initialize_board()
    elif py5.key in ['1', '2', '3', '4']:
        # 特定の値でボードを埋める
        fill_value = int(py5.key) - 1
        for row in range(len(game_board)):
            for col in range(len(game_board[row])):
                game_board[row][col] = fill_value

py5.run_sketch()