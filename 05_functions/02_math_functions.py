"""
関数 - 数学関数
計算を行う関数を作成します
"""
import py5

def calculate_circle_area(radius):
    """円の面積を計算する関数"""
    return py5.PI * radius * radius

def calculate_triangle_area(base, height):
    """三角形の面積を計算する関数"""
    return base * height / 2

def calculate_rectangle_area(width, height):
    """四角形の面積を計算する関数"""
    return width * height

def draw_shape_with_area(shape_type, x, y, *params):
    """図形を描いて面積を表示する関数"""
    if shape_type == "circle":
        radius = params[0]
        area = calculate_circle_area(radius)
        py5.fill(255, 150, 150, 150)
        py5.circle(x, y, radius * 2)
        py5.fill(0)
        py5.text(f"円\n半径: {radius}\n面積: {area:.1f}", x - 30, y + radius + 20)
        
    elif shape_type == "triangle":
        base, height = params
        area = calculate_triangle_area(base, height)
        py5.fill(150, 255, 150, 150)
        py5.triangle(x - base/2, y + height/2, x + base/2, y + height/2, x, y - height/2)
        py5.fill(0)
        py5.text(f"三角形\n底辺: {base}\n高さ: {height}\n面積: {area:.1f}", x - 30, y + height/2 + 20)
        
    elif shape_type == "rectangle":
        width, height = params
        area = calculate_rectangle_area(width, height)
        py5.fill(150, 150, 255, 150)
        py5.rect(x - width/2, y - height/2, width, height)
        py5.fill(0)
        py5.text(f"四角形\n幅: {width}\n高さ: {height}\n面積: {area:.1f}", x - 30, y + height/2 + 20)

def setup():
    py5.size(700, 500)
    py5.background(255)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 16)
    py5.text_font(font)
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("図形の面積計算", 280, 30)
    
    # 各図形を描画
    py5.text_size(12)
    draw_shape_with_area("circle", 120, 120, 50)
    draw_shape_with_area("triangle", 350, 120, 80, 60)
    draw_shape_with_area("rectangle", 550, 120, 70, 50)
    
    # より大きな図形
    draw_shape_with_area("circle", 120, 320, 70)
    draw_shape_with_area("triangle", 350, 320, 100, 80)
    draw_shape_with_area("rectangle", 550, 320, 90, 70)
    
    # 計算例を表示
    py5.text_size(14)
    py5.text("関数を使った面積計算の例:", 50, 450)
    py5.text("円: π × r²", 50, 470)
    py5.text("三角形: 底辺 × 高さ ÷ 2", 200, 470)
    py5.text("四角形: 幅 × 高さ", 400, 470)

py5.run_sketch()