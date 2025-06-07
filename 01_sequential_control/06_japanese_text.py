"""
順次制御 - 日本語テキスト描画
フォントを設定して日本語文字を表示します
"""
import py5

def setup():
    py5.size(900, 600)
    py5.background(240, 248, 255)
    
    # 日本語フォントを作成
    font_large = py5.create_font('MS ゴシック', 48)
    font_medium = py5.create_font('MS ゴシック', 24)
    font_small = py5.create_font('MS ゴシック', 16)
    
    # 大きなタイトル
    py5.text_font(font_large)
    py5.fill(50, 50, 150)
    py5.text("py5で日本語プログラミング", 150, 100)
    
    # 中サイズのテキスト
    py5.text_font(font_medium)
    py5.fill(255, 0, 0)
    py5.text("こんにちは、世界！", 200, 180)
    
    py5.fill(0, 150, 0)
    py5.text("プログラミングは楽しい", 180, 220)
    
    py5.fill(150, 0, 150)
    py5.text("視覚的に学習しよう", 200, 260)
    
    # 様々な日本語表現
    py5.text_font(font_small)
    py5.fill(0)
    
    greetings = [
        "おはよう（朝の挨拶）",
        "こんにちは（昼の挨拶）",
        "こんばんは（夜の挨拶）",
        "ありがとう（感謝）",
        "すみません（謝罪）",
        "がんばって（応援）"
    ]
    
    py5.text("日本語の表現例:", 50, 330)
    
    for i, greeting in enumerate(greetings):
        py5.fill(50 + i * 30, 100, 200 - i * 20)
        py5.text(f"• {greeting}", 70, 360 + i * 25)
    
    # 数字の表現
    py5.fill(0)
    py5.text("数字の表現:", 450, 330)
    
    numbers = [
        "いち（1）", "に（2）", "さん（3）", 
        "よん（4）", "ご（5）", "ろく（6）",
        "なな（7）", "はち（8）", "きゅう（9）", "じゅう（10）"
    ]
    
    for i, number in enumerate(numbers):
        if i < 5:
            py5.text(f"• {number}", 470, 360 + i * 25)
        else:
            py5.text(f"• {number}", 620, 360 + (i-5) * 25)
    
    # 色の名前
    py5.text("色の名前:", 50, 520)
    
    colors = [
        ("あか（赤）", (255, 0, 0)),
        ("あお（青）", (0, 0, 255)),
        ("きいろ（黄色）", (255, 255, 0)),
        ("みどり（緑）", (0, 255, 0)),
        ("むらさき（紫）", (128, 0, 128))
    ]
    
    for i, (color_name, color_rgb) in enumerate(colors):
        # 色の四角形
        py5.fill(color_rgb[0], color_rgb[1], color_rgb[2])
        py5.rect(70 + i * 140, 540, 30, 20)
        
        # 色の名前
        py5.fill(0)
        py5.text(color_name, 110 + i * 140, 555)

py5.run_sketch()