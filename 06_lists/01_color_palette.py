"""
リストの基本 - カラーパレット
リストを使用して色のパレットを管理します
"""
import py5

def setup():
    py5.size(600, 400)
    py5.background(255)
    
    # 色のリスト
    colors = [
        (255, 100, 100),  # 赤
        (100, 255, 100),  # 緑
        (100, 100, 255),  # 青
        (255, 255, 100),  # 黄色
        (255, 100, 255),  # マゼンタ
        (100, 255, 255),  # シアン
        (255, 165, 0),    # オレンジ
        (128, 0, 128),    # 紫
    ]
    
    # 色の名前のリスト
    color_names = [
        "赤", "緑", "青", "黄色",
        "マゼンタ", "シアン", "オレンジ", "紫"
    ]
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("カラーパレット（リスト使用）", 180, 30)
    
    # 色のパレットを描画
    for i in range(len(colors)):
        color = colors[i]
        name = color_names[i]
        
        # 色のサンプル
        x = 50 + (i % 4) * 130
        y = 80 + (i // 4) * 120
        
        py5.fill(color[0], color[1], color[2])
        py5.rect(x, y, 100, 60)
        
        # 色の名前
        py5.fill(0)
        py5.text_size(14)
        py5.text(name, x + 10, y + 80)
        
        # RGB値
        py5.text_size(10)
        py5.text(f"R:{color[0]}", x + 5, y + 95)
        py5.text(f"G:{color[1]}", x + 35, y + 95)
        py5.text(f"B:{color[2]}", x + 65, y + 95)
    
    # リストの操作例を表示
    py5.fill(0)
    py5.text_size(14)
    py5.text("リストの操作例:", 50, 320)
    py5.text(f"色の数: {len(colors)}", 50, 340)
    py5.text(f"最初の色: {colors[0]}", 50, 360)
    py5.text(f"最後の色: {colors[-1]}", 250, 360)

py5.run_sketch()