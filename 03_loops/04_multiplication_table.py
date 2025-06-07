"""
繰り返し - 九九の表
二重ループを使用して九九の表を作成します
"""
import py5

def setup():
    py5.size(600, 500)
    py5.background(255)
    
    # タイトル
    py5.fill(0)
    py5.text_size(20)
    py5.text("九九の表", 250, 30)
    
    # 表のヘッダー
    py5.text_size(14)
    py5.text("×", 30, 70)
    
    # 列のヘッダー（1-9）
    for i in range(1, 10):
        py5.text(str(i), 30 + i * 50, 70)
    
    # 九九の表を描画
    for row in range(1, 10):
        # 行のヘッダー
        py5.text(str(row), 30, 70 + row * 30)
        
        for col in range(1, 10):
            result = row * col
            x = 30 + col * 50
            y = 70 + row * 30
            
            # 結果によって色を変える
            if result <= 20:
                py5.fill(100, 255, 100)  # 薄い緑
            elif result <= 40:
                py5.fill(255, 255, 100)  # 黄色
            elif result <= 60:
                py5.fill(255, 200, 100)  # オレンジ
            else:
                py5.fill(255, 100, 100)  # 薄い赤
            
            # 背景の四角形
            py5.rect(x - 15, y - 15, 30, 20)
            
            # 計算結果
            py5.fill(0)
            py5.text(str(result), x - 5, y)
    
    # 説明
    py5.text_size(12)
    py5.text("色分け: 緑(1-20), 黄(21-40), オレンジ(41-60), 赤(61-81)", 50, 450)

py5.run_sketch()