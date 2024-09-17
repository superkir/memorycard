questions = []
class Question():
    def __init__(self, text, true, false1, false2, false3):
        self.text = text
        self.true = true
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
        questions.append(self)
    
    def show_question(self, lb, rb1, rb2, rb3, rb4):
        lb.setText(self.text)
        rb1.setText(self.true)
        rb2.setText(self.false1)
        rb3.setText(self.false2)
        rb4.setText(self.false3)

Question("В якому році почала gthif світова війна?", "1914", "1896", "1918", "1941")
Question("Який футболіст виграв три Чемпіонати Світу?", "Пеле", "Марадона", "Мессі", "Роналду")
Question("Коли помер Майкл Джексон?", "2009", "2010", "1999", "2012")

