from PyQt5.QtWidgets import (QPushButton, QRadioButton, QLabel, QApplication, QSpinBox, QGroupBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

app = QApplication([])

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)

lable1 = QLabel("Яблуко")
rbGroupBox = QGroupBox("Варіанти відповідей")
btn_ok = QPushButton("Відповісти")
button_group = QButtonGroup()

rb1 = QRadioButton("Apple")
rb2 = QRadioButton("Dog")
rb3 = QRadioButton("Muc")
rb4 = QRadioButton("Sup")
button_group.addButton(rb1)
button_group.addButton(rb2)
button_group.addButton(rb3)
button_group.addButton(rb4)

main_box_line = QHBoxLayout()
box_line1 = QVBoxLayout()
box_line2 = QVBoxLayout()
box_line1.addWidget(rb1)
box_line1.addWidget(rb2)
box_line2.addWidget(rb3)
box_line2.addWidget(rb4)
main_box_line.addLayout(box_line1)
main_box_line.addLayout(box_line2)
rbGroupBox.setLayout(main_box_line)

rbGroupBox.hide()

ansGroupBox = QGroupBox("Результати тесту")
main_box2_line = QVBoxLayout()
result_lb = QLabel("Правильно")
right_ans_lb = QLabel("apple")
main_box2_line.addWidget(result_lb, alignment=Qt.AlignTop)
main_box2_line.addWidget(right_ans_lb, alignment=Qt.AlignCenter)
main_box2_line.addWidget(right_ans_lb)
ansGroupBox.setLayout(main_box2_line)

menuGroupBox = QGroupBox("Меню")
main_box3_line = QVBoxLayout()
btn_test = QPushButton("Почати тестування")
btn_study = QPushButton("Почати навчання")
btn_leave = QPushButton("Вийти")
main_box3_line.addWidget(btn_test, alignment=Qt.AlignCenter)
main_box3_line.addWidget(btn_study, alignment=Qt.AlignCenter)
main_box3_line.addWidget(btn_leave, alignment=Qt.AlignCenter)
menuGroupBox.setLayout(main_box3_line)
menuGroupBox.hide()

main_line_quizz = QVBoxLayout()
line1_quizz = QHBoxLayout()

line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

main_line_quizz.addLayout(line1_quizz, stretch=1)
main_line_quizz.addWidget(lable1, alignment=Qt.AlignCenter, stretch=1)
main_line_quizz.addWidget(rbGroupBox, stretch=5)
main_line_quizz.addWidget(ansGroupBox, stretch=5)
main_line_quizz.addWidget(menuGroupBox, stretch=5)
main_line_quizz.addWidget(btn_ok, stretch=1)

def button():
    window.show()
    window.setWindowTitle("Результат")
    
window = QWidget()
window.resize(600, 500)

def button1():
    window.show()
    window.setWindowTitle("Відпочинок")

window = QWidget()
window.resize(600, 500)

def button2():
    window.show()
    window.setWindowTitle("Меню")





window = QWidget()
window.resize(600, 500)

btn_ok.clicked.connect(button)
btn_rest.clicked.connect(button1)
btn_menu.clicked.connect(button2)