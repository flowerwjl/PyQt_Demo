from ui import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from function import *


class MainUI(Ui_Form):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        self.pushButton.clicked.connect(self.convert)
        MainWindow.show()
        sys.exit(app.exec_())

    def convert(self):
        pictureName, _ = QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "选取视频文件", "C:/", "Video files (*.avi *.mp4 *.mov *.wmv *.mkv)")
        video_path = pictureName

        self.path.setText(video_path)
        result1 = my_interface1(video_path)
        result2 = my_interface2(video_path)
        self.xinfang.setText(result1)
        self.xinlv.setText(result2)
        self.plainTextEdit.setPlainText("输出文件成功: "+video_path+"output.mp4")
