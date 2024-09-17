from PyQt5.QtWidgets import QWidget, QApplication
from layout_quizz import *

app = QApplication([])

window = QWidget()
window.resize(800, 700)
window.setWindowTitle("MemoryCard")
window.setLayout(main_line_quizz)
window.show()

def click_ok():
    if btn_ok.text() == "Відповісти":
        rbGroupBox.hide()
        ansGroupBox.show()
        btn_ok.setText("Наступне питання")
    else:
        rbGroupBox.show()
        ansGroupBox.hide()
        btn_ok.setText("Відповісти")

if btn_menu.clicked:
    menuGroupBox = QGroupBox("Меню")
    main_box3_line = QVBoxLayout()
    btn_test = QPushButton("Почати тестування")
    btn_study = QPushButton("Почати навчання")
    btn_leave = QPushButton("Вийти")
    main_box3_line.addWidget(btn_test, alignment=Qt.AlignCenter)
    main_box3_line.addWidget(btn_study, alignment=Qt.AlignCenter)
    main_box3_line.addWidget(btn_leave, alignment=Qt.AlignCenter)
    menuGroupBox.setLayout(main_box3_line)

btn_ok.clicked.connect(click_ok)

app.exec()




                                                
















