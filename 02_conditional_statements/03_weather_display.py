"""
条件分岐 - 天気による背景変更
天気の状態によって背景色と図形を変更します
"""
import py5

def setup():
    py5.size(400, 400)
    
    # 天気の状態を設定
    weather = "雨"  # "晴れ", "曇り", "雨", "雪"
    
    # 天気による条件分岐
    if weather == "晴れ":
        # 晴れの日
        py5.background(135, 206, 235)  # 青空
        # 太陽
        py5.fill(255, 255, 0)
        py5.circle(350, 80, 60)
        # 雲（少し）
        py5.fill(255, 255, 255)
        py5.circle(80, 60, 40)
        py5.circle(100, 60, 50)
        message = "今日は晴れです！"
        
    elif weather == "曇り":
        # 曇りの日
        py5.background(169, 169, 169)  # グレー
        # 雲
        py5.fill(105, 105, 105)
        for i in range(5):
            py5.circle(60 + i * 70, 80, 50)
            py5.circle(30 + i * 70, 100, 40)
        message = "今日は曇りです"
        
    elif weather == "雨":
        # 雨の日
        py5.background(70, 70, 70)  # 暗いグレー
        # 雲
        py5.fill(50, 50, 50)
        for i in range(4):
            py5.circle(80 + i * 80, 60, 60)
        # 雨粒
        py5.stroke(0, 0, 255)
        py5.stroke_weight(2)
        for i in range(0, 400, 30):
            for j in range(0, 400, 40):
                py5.line(i, j, i + 5, j + 20)
        py5.no_stroke()
        message = "今日は雨です"
        
    elif weather == "雪":
        # 雪の日
        py5.background(200, 200, 255)  # 薄い青
        # 雲
        py5.fill(220, 220, 220)
        for i in range(4):
            py5.circle(80 + i * 80, 60, 60)
        # 雪
        py5.fill(255)
        for i in range(0, 400, 40):
            for j in range(0, 400, 50):
                py5.circle(i + 10, j + 20, 8)
        message = "今日は雪です"
        
    else:
        # その他
        py5.background(255, 255, 255)
        message = "天気不明"
    
    # メッセージ表示
    py5.fill(0)
    py5.text_size(20)
    py5.text(message, 100, 350)

py5.run_sketch()