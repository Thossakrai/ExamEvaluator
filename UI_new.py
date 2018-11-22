from PyQt5 import QtGui, QtWidgets, uic
import sys
from  ICPFinalProject import *
import matplotlib.pyplot as plt


class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.MainWindow = uic.loadUi("main.ui")
        self.InstructorButton = self.MainWindow.LogInAsTeacher
        self.InstructorButton.clicked.connect(self.show_instructorpage)
        self.StudentButton = self.MainWindow.LogInAsStudent
        self.StudentButton.clicked.connect(self.show_studentpage)
        self.MainWindow.show()


    def show_instructorpage(self):
        self.InstPage = InstructorPage()

    def show_studentpage(self):
        self.stdPage = StudentPage()


class InstructorPage(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(InstructorPage, self).__init__(parent)
        self.ui = uic.loadUi("teacher.ui")
        self.cancelButton = self.ui.cancelButton
        self.cancelButton.clicked.connect(self.cancel)
        self.ExamName = self.ui.textExamName.text()
        self.ExamCode = self.ui.textRefCode.text()
        self.okayButton = self.ui.okayButton
        self.create = self.ui.radioButton_create
        self.view = self.ui.radioButton_view
        self.okayButton.clicked.connect(lambda : self.okay(self.create.isChecked(), self.view.isChecked()))
        self.ui.show()

    def cancel(self):
        self.ui.close()

    def okay(self, checked_create, checked_view):
        if (checked_create):
            self.create_exam()
            self.ui.close()

        elif (checked_view):
            self.view_exam()
            self.ui.close()


    def create_exam(self):
        self.new_sheet = AnswerSheet(name = self.ui.textExamName.text(),
                                     code = self.ui.textRefCode.text())


    def view_exam(self):
        self.code = self.ui.textRefCode.text()
        self.result, self.correct = Control.analyse(self.code)
        print(self.result, self.correct)
        print(len(self.result))
        self.page = DataVisual(result = self.result, correct = self.correct)

class DataVisual(QtWidgets.QMainWindow):
    def __init__(self, parent=None, result = [], correct= []):
        super(DataVisual, self).__init__(parent)
        self.ui = uic.loadUi("dataanalysis.ui")
        self.score_button = self.ui.HighestScoreButton
        self.accuracy = self.ui.ExamAnalyse
        self.score = StudentCollector(result).getScore()
        self.name = StudentCollector(result).getName()
        self.correct = correctCollector(correct).data
        self.score_button.clicked.connect(self.score_clicked)
        self.accuracy.clicked.connect(self.accuracy_clicked)
        self.ui.show()

    def score_clicked(self):
        print(self.name)
        plt.bar(self.name,self.score, color = "Blue", width = 0.35)
        plt.show()


    def accuracy_clicked(self):
        print(self.correct)
        self.question_num = [x for x in range (1,21)]
        plt.bar(self.question_num, self.correct, color = "Red", width = 0.35)
        plt.show()

class AnswerSheet(QtWidgets.QMainWindow):
    def __init__(self, parent=None, name="", code=""):
        super(AnswerSheet, self).__init__(parent)
        self.ui = uic.loadUi("answerkey.ui")
        self.exam_name = name
        self.exam_id = code
        self.cancelButton = self.ui.cancelButton
        self.saveButton = self.ui.saveButton
        self.saveButton.clicked.connect(self.create_new_answer_sheet)
        self.ui.show()

    def create_new_answer_sheet(self):
        self.ans_list = [self.exam_name,
            self.ui.A1.value(), self.ui.A2.value(), self.ui.A3.value(), self.ui.A4.value(),
            self.ui.A5.value(), self.ui.A6.value(), self.ui.A7.value(), self.ui.A8.value(),
            self.ui.A9.value(), self.ui.A10.value(), self.ui.A11.value(), self.ui.A12.value(),
            self.ui.A13.value(), self.ui.A14.value(), self.ui.A15.value(), self.ui.A16.value(),
            self.ui.A17.value(), self.ui.A18.value(), self.ui.A19.value(), self.ui.A20.value(),
        ]
        self.exam = Sheet(self.exam_name, self.exam_id, self.ans_list)
        Control.generate_new_exam(self.exam.get_ans_list(), self.exam.get_exam_id())
        self.ui.close()


class StudentPage(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(StudentPage, self).__init__(parent)
        self.ui = uic.loadUi("Student.ui")
        self.exam_code = self.ui.RefCode.text()
        self.student_name = self.ui.studentname.text()
        self.okayButton = self.ui.okayButton
        self.okayButton.clicked.connect(self.create_new_answer)
        self.cancelButton =  self.ui.cancelButton
        self.ui.show()

    def create_new_answer(self):
        name = self.ui.studentname.text()
        code = self.ui.RefCode.text()
        self.student_answer = StudentAnswer(name = name, code = code)


class StudentAnswer(QtWidgets.QMainWindow):
    def __init__(self,parent=None, name="", code=""):
        super(StudentAnswer, self).__init__(parent)
        self.ui = uic.loadUi("student_answer.ui")
        self.student_name = name
        self.exam_code = code
        self.saveButton = self.ui.pushButton
        self.cancelButton = self.ui.pushButton_2
        self.saveButton.clicked.connect(self.save_answer)
        self.ui.show()


    def save_answer(self):
        self.answer_list = [self.student_name,
            self.ui.spinBox.value(), self.ui.spinBox_2.value(), self.ui.spinBox_3.value(), self.ui.spinBox_4.value(),
            self.ui.spinBox_5.value(), self.ui.spinBox_6.value(), self.ui.spinBox_7.value(), self.ui.spinBox_8.value(),
            self.ui.spinBox_9.value(), self.ui.spinBox_10.value(), self.ui.spinBox_11.value(), self.ui.spinBox_12.value(),
            self.ui.spinBox_13.value(), self.ui.spinBox_14.value(), self.ui.spinBox_15.value(), self.ui.spinBox_16.value(),
            self.ui.spinBox_17.value(), self.ui.spinBox_18.value(), self.ui.spinBox_19.value(), self.ui.spinBox_20.value(),
        ]
        self.exam = Sheet(self.student_name, self.exam_code, self.answer_list)
        Control.generate_new_answer(self.exam.get_ans_list(), self.exam.get_exam_id())
        self.ui.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    homepage = MainPage()
    app.exec_()
