from PyQt5 import QtGui, QtWidgets, uic
import sys
import  ICPFinalProject

class MainPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.MainWindow = uic.loadUi("PythonProject1.ui")
        IClogo = QtWidgets.QLabel()
        IClogo.setPixmap(QtGui.QPixmap("ic_logo_flat_hi.png"))
        self.MainWindow.LayoutLogo.addWidget(IClogo)
        # BG = QtWidgets.QLabel()
        # BG.setPixmap(QtGui.QPixmap("Home.jpg"))
        # self.ui.bg.addWidget(BG)
        self.InstructorButton = self.MainWindow.LogInAsTeacher
        self.InstructorButton.clicked.connect(self.show_instructorpage)
        self.StudentButton = self.MainWindow.LogInAsStudent
        self.StudentButton.clicked.connect(self.show_studentpage)


        self.MainWindow.show()




    def show_instructorpage(self):
        self.InstPage = InstructorPage()
        #self.MainWindow.hide()

    def show_studentpage(self):
        self.stdPage = StudentPage()
        # self.MainWindow.hide()


class InstructorPage(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(InstructorPage, self).__init__(parent)
        self.ui = uic.loadUi("teacher.ui")
        self.cancelButton = self.ui.cancelButton
        self.cancelButton.clicked.connect(self.cancel)
        self.ExamName = self.ui.textExamName
        self.ExamCode = self.ui.textRefCode
        self.okayButton = self.ui.okayButton
        self.okayButton.clicked.connect(self.okay)
        self.create = self.ui.radioButton_create
        self
        self.ui.show()

    def create_exam(self):
        pass

    def cancel(self):
        self.ui.close()

    def okay(self):
        sender = self.sender()
        if sender.text() == 'Okay':
            pass



class StudentPage(QtWidgets.QMainWindow):
    def __init__(self):
        self.ui = uic.loadUi("Student.ui")
        self.ui.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    homepage = MainPage()
    app.exec_()
