"""
条件分岐 - 年齢カテゴリ判定
年齢によって異なるキャラクターを表示します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(255, 250, 240)
    
    # 年齢を設定
    age = 25
    
    # 年齢による条件分岐
    if age < 3:
        # 赤ちゃん
        category = "赤ちゃん"
        # 小さな顔
        py5.fill(255, 220, 177)
        py5.circle(200, 180, 60)
        # 目
        py5.fill(0)
        py5.circle(185, 170, 8)
        py5.circle(215, 170, 8)
        # 口
        py5.circle(200, 190, 6)
        
    elif age < 13:
        # 子供
        category = "子供"
        # 顔
        py5.fill(255, 220, 177)
        py5.circle(200, 180, 80)
        # 目
        py5.fill(0)
        py5.circle(180, 165, 10)
        py5.circle(220, 165, 10)
        # 口（笑顔）
        py5.stroke(0)
        py5.stroke_weight(3)
        py5.no_fill()
        py5.arc(200, 185, 30, 20, 0, py5.PI)
        py5.no_stroke()
        
    elif age < 20:
        # 青少年
        category = "青少年"
        # 顔
        py5.fill(255, 220, 177)
        py5.circle(200, 180, 90)
        # 目
        py5.fill(0)
        py5.circle(175, 165, 12)
        py5.circle(225, 165, 12)
        # 眉毛
        py5.stroke(101, 67, 33)
        py5.stroke_weight(3)
        py5.line(165, 155, 185, 155)
        py5.line(215, 155, 235, 155)
        # 口
        py5.line(190, 195, 210, 195)
        py5.no_stroke()
        
    elif age < 60:
        # 大人
        category = "大人"
        # 顔
        py5.fill(255, 220, 177)
        py5.circle(200, 180, 100)
        # 目
        py5.fill(0)
        py5.circle(170, 165, 14)
        py5.circle(230, 165, 14)
        # 眉毛
        py5.stroke(101, 67, 33)
        py5.stroke_weight(4)
        py5.line(155, 150, 185, 150)
        py5.line(215, 150, 245, 150)
        # 口
        py5.line(185, 200, 215, 200)
        py5.no_stroke()
        # ひげ
        py5.stroke(101, 67, 33)
        py5.stroke_weight(2)
        py5.line(180, 210, 190, 215)
        py5.line(200, 215, 200, 220)
        py5.line(210, 215, 220, 210)
        py5.no_stroke()
        
    else:
        # 高齢者
        category = "高齢者"
        # 顔
        py5.fill(255, 220, 177)
        py5.circle(200, 180, 100)
        # 目
        py5.fill(0)
        py5.circle(170, 165, 12)
        py5.circle(230, 165, 12)
        # 眉毛（白い）
        py5.stroke(200)
        py5.stroke_weight(4)
        py5.line(155, 150, 185, 150)
        py5.line(215, 150, 245, 150)
        # 口
        py5.stroke(0)
        py5.stroke_weight(2)
        py5.line(185, 200, 215, 200)
        py5.no_stroke()
        # しわ
        py5.stroke(180)
        py5.stroke_weight(1)
        py5.line(160, 140, 170, 145)
        py5.line(230, 145, 240, 140)
        py5.no_stroke()
    
    # カテゴリと年齢を表示
    py5.fill(0)
    py5.text_size(24)
    py5.text(f"年齢: {age}歳", 140, 300)
    py5.text(f"カテゴリ: {category}", 120, 330)

py5.run_sketch()