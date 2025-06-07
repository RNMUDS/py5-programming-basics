"""
条件分岐の基本 - 条件によって色を変える
if文を使用して条件に応じて色を変更します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(255)
    
    # 変数を定義
    score = 85
    
    # スコアによって色を変える
    if score >= 90:
        color = (255, 215, 0)  # 金色（優秀）
        grade = "優秀"
    elif score >= 80:
        color = (255, 165, 0)  # オレンジ（良好）
        grade = "良好"
    elif score >= 70:
        color = (255, 255, 0)  # 黄色（普通）
        grade = "普通"
    elif score >= 60:
        color = (135, 206, 235)  # 水色（合格）
        grade = "合格"
    else:
        color = (255, 0, 0)  # 赤（不合格）
        grade = "不合格"
    
    # 結果を表示
    py5.fill(color[0], color[1], color[2])
    py5.circle(200, 150, 100)
    
    # テキスト表示
    py5.fill(0)
    py5.text_size(20)
    py5.text(f"スコア: {score}", 140, 250)
    py5.text(f"評価: {grade}", 150, 280)
    
    # 条件説明
    py5.text_size(14)
    py5.text("90以上: 金色（優秀）", 50, 320)
    py5.text("80以上: オレンジ（良好）", 50, 340)
    py5.text("70以上: 黄色（普通）", 50, 360)
    py5.text("60以上: 水色（合格）", 50, 380)

py5.run_sketch()