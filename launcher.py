from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox, QGroupBox,QButtonGroup,QTextEdit,QLineEdit,QListWidget , QInputDialog,QFileDialog
from PyQt5.QtGui import QPixmap
import os
import sys
import subprocess
app = QApplication([])
win = QWidget()
def pick_file():
    global level_path, status_label
    path,_=QFileDialog.getOpenFileName(None,'Открыть уровень','','Exel (*.xlsx)')
    if path:
        level_path = path
def launh_game():
    args=[sys.executable,'newgame.py']
    if level_path:
        args.append(level_path)
    subprocess.Popen(args)
#кнопки
list1 = QListWidget()
name = QLabel('Платформер')
name.setAlignment(Qt.AlignCenter)
text = QLabel('Выберете Exel-файл с уровнем или запустите встроенный')
play = QPushButton('Играть')
two = QPushButton('Открыть .xlsx')
win.resize(250,250)
level_path = None
status_label = None
#линии
layout1 = QVBoxLayout()
layout3 = QHBoxLayout()
#работа с виджетами
layout1.addWidget(name)
layout1.addWidget(text)
layout1.addLayout(layout3)
layout3.addWidget(two)
layout3.addWidget(play)
#изображение
win.setLayout(layout1)
play.clicked.connect(launh_game)
two.clicked.connect(pick_file)
win.show()
app.exec()