"""
入れ子構造 - 複合データ構造
リスト、辞書、関数を組み合わせた複雑なデータ構造
"""
import py5

# 複合データ構造：学校のクラス管理システム
school_data = {
    "school_name": "プログラミング高校",
    "classes": [
        {
            "class_name": "1年A組",
            "teacher": "田中先生",
            "students": [
                {"name": "佐藤太郎", "age": 16, "scores": [85, 92, 78, 88]},
                {"name": "鈴木花子", "age": 15, "scores": [92, 88, 95, 90]},
                {"name": "高橋次郎", "age": 16, "scores": [78, 85, 82, 86]}
            ],
            "subjects": ["数学", "英語", "国語", "理科"]
        },
        {
            "class_name": "2年B組", 
            "teacher": "山田先生",
            "students": [
                {"name": "小林美咲", "age": 17, "scores": [88, 94, 87, 91]},
                {"name": "中村健太", "age": 16, "scores": [82, 79, 88, 85]}
            ],
            "subjects": ["数学", "英語", "国語", "理科"]
        }
    ]
}

selected_class = 0
selected_student = 0

def calculate_class_average(class_data):
    """クラスの平均点を計算する関数"""
    if not class_data["students"]:
        return [0, 0, 0, 0]
    
    subject_totals = [0, 0, 0, 0]
    student_count = len(class_data["students"])
    
    for student in class_data["students"]:
        for i, score in enumerate(student["scores"]):
            subject_totals[i] += score
    
    return [total / student_count for total in subject_totals]

def get_top_student(class_data):
    """クラスの最高得点者を取得する関数"""
    if not class_data["students"]:
        return None
    
    top_student = None
    highest_average = 0
    
    for student in class_data["students"]:
        average = sum(student["scores"]) / len(student["scores"])
        if average > highest_average:
            highest_average = average
            top_student = student
    
    return top_student, highest_average

def setup():
    py5.size(800, 600)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 14)
    py5.text_font(font)

def draw():
    py5.background(245, 245, 250)
    
    # タイトル
    py5.fill(0)
    py5.text_size(24)
    py5.text(f"{school_data['school_name']} - データ管理システム", 200, 40)
    
    # クラス選択
    py5.text_size(16)
    py5.text("クラス選択:", 50, 80)
    
    for i, class_data in enumerate(school_data["classes"]):
        x = 150 + i * 120
        y = 60
        
        # クラス選択ボタン
        if i == selected_class:
            py5.fill(150, 200, 255)
        else:
            py5.fill(220, 220, 220)
        
        py5.rect(x, y, 100, 30)
        py5.fill(0)
        py5.text_size(12)
        py5.text(class_data["class_name"], x + 10, y + 20)
    
    # 選択されたクラスの情報を表示
    current_class = school_data["classes"][selected_class]
    
    py5.text_size(18)
    py5.text(f"クラス: {current_class['class_name']}", 50, 120)
    py5.text_size(14)
    py5.text(f"担任: {current_class['teacher']}", 50, 145)
    py5.text(f"生徒数: {len(current_class['students'])}名", 200, 145)
    
    # 科目一覧
    py5.text("科目:", 350, 145)
    subjects_text = ", ".join(current_class["subjects"])
    py5.text(subjects_text, 390, 145)
    
    # 学生一覧
    py5.text_size(16)
    py5.text("学生一覧:", 50, 180)
    
    y = 200
    for i, student in enumerate(current_class["students"]):
        # 学生選択の背景
        if i == selected_student:
            py5.fill(255, 255, 150)
            py5.rect(45, y - 15, 700, 60)
        
        py5.fill(0)
        py5.text_size(14)
        py5.text(f"{i+1}. {student['name']} (年齢: {student['age']}歳)", 50, y)
        
        # 成績表示
        py5.text("成績:", 250, y)
        for j, (subject, score) in enumerate(zip(current_class["subjects"], student["scores"])):
            x = 300 + j * 80
            py5.text(f"{subject}: {score}", x, y)
        
        # 平均点
        average = sum(student["scores"]) / len(student["scores"])
        py5.text(f"平均: {average:.1f}", 650, y)
        
        y += 65
    
    # クラス統計
    py5.text_size(16)
    py5.text("クラス統計:", 50, y + 20)
    
    class_averages = calculate_class_average(current_class)
    py5.text_size(12)
    py5.text("科目別平均:", 50, y + 45)
    
    for i, (subject, avg) in enumerate(zip(current_class["subjects"], class_averages)):
        x = 150 + i * 80
        py5.text(f"{subject}: {avg:.1f}", x, y + 45)
    
    # 最高得点者
    top_student_data = get_top_student(current_class)
    if top_student_data:
        top_student, top_average = top_student_data
        py5.text(f"最高得点者: {top_student['name']} (平均: {top_average:.1f})", 50, y + 70)
    
    # データ構造の説明
    py5.text_size(14)
    py5.text("データ構造の例:", 450, y + 20)
    py5.text_size(10)
    py5.text("school_data = {", 450, y + 40)
    py5.text("  'school_name': '文字列',", 450, y + 55)
    py5.text("  'classes': [  # リスト", 450, y + 70)
    py5.text("    {  # 辞書", 450, y + 85)
    py5.text("      'students': [  # ネストしたリスト", 450, y + 100)
    py5.text("        {'scores': [...]}  # さらにネスト", 450, y + 115)
    py5.text("      ]", 450, y + 130)
    py5.text("    }", 450, y + 145)
    py5.text("  ]", 450, y + 160)
    py5.text("}", 450, y + 175)
    
    # 操作説明
    py5.text_size(12)
    py5.text("操作方法:", 50, 580)
    py5.text("• 1,2キー: クラス選択", 150, 580)
    py5.text("• ↑↓キー: 学生選択", 280, 580)

def key_pressed():
    global selected_class, selected_student
    
    if py5.key == '1':
        selected_class = 0
        selected_student = 0
    elif py5.key == '2' and len(school_data["classes"]) > 1:
        selected_class = 1
        selected_student = 0
    elif py5.key == py5.UP:
        current_class = school_data["classes"][selected_class]
        selected_student = max(0, selected_student - 1)
    elif py5.key == py5.DOWN:
        current_class = school_data["classes"][selected_class]
        selected_student = min(len(current_class["students"]) - 1, selected_student + 1)

def mouse_pressed():
    """マウスクリックでクラス選択"""
    global selected_class, selected_student
    
    # クラス選択ボタンのクリック判定
    for i in range(len(school_data["classes"])):
        x = 150 + i * 120
        y = 60
        if x <= py5.mouse_x <= x + 100 and y <= py5.mouse_y <= y + 30:
            selected_class = i
            selected_student = 0
            break

py5.run_sketch()