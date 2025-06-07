"""
辞書の基本 - 学生データベース
辞書を使用して学生の情報を管理します
"""
import py5

def setup():
    py5.size(700, 500)
    py5.background(255)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 16)
    py5.text_font(font)
    
    # 学生データ（辞書）
    students = {
        "田中太郎": {
            "age": 16,
            "grade": "高1",
            "subjects": {
                "数学": 85,
                "英語": 78,
                "国語": 92,
                "理科": 88
            }
        },
        "佐藤花子": {
            "age": 17,
            "grade": "高2",
            "subjects": {
                "数学": 92,
                "英語": 85,
                "国語": 88,
                "理科": 94
            }
        },
        "鈴木一郎": {
            "age": 15,
            "grade": "中3",
            "subjects": {
                "数学": 76,
                "英語": 82,
                "国語": 79,
                "理科": 83
            }
        }
    }
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text("学生データベース（辞書使用）", 220, 30)
    
    y_position = 70
    
    # 各学生の情報を表示
    for name, info in students.items():
        # 学生名
        py5.text_size(18)
        py5.text(f"氏名: {name}", 50, y_position)
        
        # 基本情報
        py5.text_size(14)
        py5.text(f"年齢: {info['age']}歳", 50, y_position + 25)
        py5.text(f"学年: {info['grade']}", 150, y_position + 25)
        
        # 成績表示
        py5.text("成績:", 50, y_position + 50)
        
        x_offset = 100
        total_score = 0
        subject_count = 0
        
        for subject, score in info['subjects'].items():
            # 成績による色分け
            if score >= 90:
                py5.fill(100, 255, 100)  # 緑（優秀）
            elif score >= 80:
                py5.fill(255, 255, 100)  # 黄（良好）
            elif score >= 70:
                py5.fill(255, 200, 100)  # オレンジ（普通）
            else:
                py5.fill(255, 150, 150)  # 薄い赤（要努力）
            
            # 成績のボックス
            py5.rect(x_offset, y_position + 35, 80, 40)
            
            # 科目名と点数
            py5.fill(0)
            py5.text(subject, x_offset + 5, y_position + 50)
            py5.text(f"{score}点", x_offset + 5, y_position + 65)
            
            total_score += score
            subject_count += 1
            x_offset += 90
        
        # 平均点を計算して表示
        average = total_score / subject_count
        py5.text(f"平均点: {average:.1f}点", 500, y_position + 50)
        
        y_position += 120
    
    # 辞書の操作例
    py5.text_size(16)
    py5.text("辞書の操作例:", 50, 420)
    py5.text_size(12)
    py5.text("• キーで値にアクセス: students['田中太郎']['age']", 50, 440)
    py5.text("• ネストした辞書: students['田中太郎']['subjects']['数学']", 50, 455)
    py5.text("• 動的な値の追加・変更が可能", 50, 470)

py5.run_sketch()