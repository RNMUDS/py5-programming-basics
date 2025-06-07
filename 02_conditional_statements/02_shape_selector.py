"""
条件分岐 - 図形選択
変数の値によって描画する図形を変更します
"""
import py5

def setup():
    py5.size(400, 400)
    py5.background(240, 248, 255)
    
    # 日本語フォントを設定
    font = py5.create_font('MS ゴシック', 16)
    py5.text_font(font)
    
    # 図形の種類を決める変数
    shape_type = 2
    
    # 描画位置
    x = 200
    y = 200
    size = 80
    
    # 条件分岐で図形を選択
    if shape_type == 1:
        # 円を描画
        py5.fill(255, 100, 100)
        py5.circle(x, y, size)
        shape_name = "円"
    elif shape_type == 2:
        # 四角形を描画
        py5.fill(100, 255, 100)
        py5.rect(x - size//2, y - size//2, size, size)
        shape_name = "四角形"
    elif shape_type == 3:
        # 三角形を描画
        py5.fill(100, 100, 255)
        py5.triangle(x, y - size//2, x - size//2, y + size//2, x + size//2, y + size//2)
        shape_name = "三角形"
    elif shape_type == 4:
        # 星型を描画
        py5.fill(255, 255, 100)
        # 星の頂点を計算
        outer_radius = size // 2
        inner_radius = outer_radius // 2
        py5.begin_shape()
        for i in range(10):
            angle = py5.PI * 2 * i / 10
            if i % 2 == 0:
                px = x + py5.cos(angle) * outer_radius
                py = y + py5.sin(angle) * outer_radius
            else:
                px = x + py5.cos(angle) * inner_radius
                py = y + py5.sin(angle) * inner_radius
            py5.vertex(px, py)
        py5.end_shape(py5.CLOSE)
        shape_name = "星"
    else:
        # デフォルト（楕円）
        py5.fill(255, 100, 255)
        py5.ellipse(x, y, size, size//2)
        shape_name = "楕円"
    
    # 図形名を表示
    py5.fill(0)
    py5.text_size(20)
    py5.text(f"図形: {shape_name}", 150, 320)
    py5.text(f"タイプ: {shape_type}", 150, 350)

py5.run_sketch()