#создай приложение для запоминания информации

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QRadioButton, QHBoxLayout
from random import shuffle


class Questions():
    def __init__(self, question, right_answer, answer2, answer3, answer4):
        self.question = question
        self.right_answer = right_answer
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4

question_list = []
question_list.append(Questions("Вопрос: Сколько сотрудников D-classа надо чтобы закрутить лампочку в камере scp-173?","Бесконечное множество по скольку их всех убьёт scp-173","10000 D-class","50 D-class","1 D-class"))
question_list.append(Questions("Вопрос: Какую карту доступа нужно получить для побега из комплекса играя за D-class?","Карта менеджера зон","Научного сотрудника","Скан ладони","Никак"))
question_list.append(Questions("Вопрос: Scp-096 это вообще кто?","Скромняга","Кахут","Статуя","Охрана"))
question_list.append(Questions("Вопрос: Кто является первым scp?","Печенька","Капуста","Картошка","Гамбургер"))
question_list.append(Questions("Вопрос: Какая карта доступа является самого высокого уровня?","Карта совета 05","Карта лейтенанта","Карта Командира","Карта учёного"))
question_list.append(Questions("Вопрос: Кто является чумным доктором","Гуманоидное существо","человек","водяной","блоха"))
question_list.append(Questions("Вопрос: Зачем ?","Что","Где","Когда","Почему"))



far = QApplication([])
window = QWidget()
window.resize(600, 600)

number = 0
all_ans = 0
ri_ans = 0

#----------------------------------------------


otv = QPushButton("Закрыть глаза",window)
otv.move(290, 350)
DA = QLabel("Вопрос: Сколько сотрудников D-classа надо чтобы закрутить лампочку в камере?", window)
DA.move(100,20)
#DA,setFixedSize(150,30)


#----------------------------------------------


RadioGroupBox = QGroupBox("Варианты ответа")
rd = QRadioButton("1 D-class",window)
rd.move(50,100)
rd1 = QRadioButton("50 D-class",window)
rd1.move(200,100)
rd2 = QRadioButton("10000 D-class",window)
rd2.move(50,200)
rd3 = QRadioButton("Бесконечное множество по скольку их всех убьёт scp-173",window)
rd3.move(200,200)

#----------------------------------------------

AnsGrup = QGroupBox("Посмотрим кто выжел после эксперимента")
la= QLabel("Правильно или нэйт",window)
ld= QLabel("Ответы",window)
la.move(0,0)
ld.move(200,200)
sled = QPushButton("Бежать дальше", window)
sled.move(200,300)
#----------------------------------------------

def Question():

    
    la.hide()
    ld.hide()
    rd.show()
    rd.show()
    rd1.show()
    rd2.show()
    rd3.show()
    otv.show()
    DA.show()
    sled.hide()
#----------------------------------------------

def Answer():
    sled.show()
    la.show()
    ld.show()
    rd.hide()
    rd1.hide()
    rd2.hide()
    rd3.hide()
    otv.hide()
    DA.hide()

#----------------------------------------------

answer = [rd,rd1, rd2, rd3]


def ask(question, right_answer, answer2, answer3, answer4):
    shuffle(answer)
    answer[0].setText(right_answer)
    answer[1].setText(answer2)
    answer[2].setText(answer3)
    answer[3].setText(answer4)
    DA.setText(question)
    ld.setText(right_answer)
    Question()

def check_answer():
    global all_ans
    global ri_ans
    all_ans += 1
    if answer[0].isChecked():
        ri_ans += 1
        la.setText("Правильно! \n Статистика:"+str(ri_ans)+"/"+str(all_ans))
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            la.setText("Ты вообще играл  \n Статистика:"+str(ri_ans)+"/"+str(all_ans))
    Answer()

def next_question():
    global number
    if number >= len(question_list):
        number = 0
    q = question_list[number]
    ask(q.question,q.right_answer,q.answer2,q.answer3,q.answer4)
    number+=1




window.setWindowTitle("SCP")
next_question()
#ask("Вопрос: Сколько сотрудников D-classа надо чтобы закрутить лампочку в камере?","Бесконечное множество по скольку их всех убьёт scp-173","10000 D-class","50 D-class","1 D-class")
otv.clicked.connect(check_answer)
sled.clicked.connect(next_question)

window.show()
far.exec()