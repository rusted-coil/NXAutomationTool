import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)

        # Window設定
        self.resize(1280, 720)
        self.setWindowTitle('NX Automation Tool')

        # サンプルレイアウト
        btn = QPushButton('Hello World PyQt5', self) # ボタンウィジェット作成
        btn.resize(btn.sizeHint()) # ボタンのサイズの自動設定
        btn.move(100, 50) # ボタンの位置設定(ボタンの左上の座標)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
