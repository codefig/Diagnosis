__author__ = '0code'


from PyQt4.QtCore import *
from PyQt4.QtGui import  *
import sys
import ui_firstpage

class QuestionsPage(QWidget):
    """
        This class opens the dialog for the question page
    """

    def __init__(self,parent=None):
        super(QuestionsPage, self).__init__(parent)
        layout = QGridLayout()
        self.questionPane = QTextEdit()
        self.questionPane.setReadOnly(True)
        self.yesBtn = QPushButton("Yes")
        self.noBtn = QPushButton("No")
        self.nextBtn = QPushButton("Next")

        btnlayout = QGridLayout()
        btnlayout.addWidget(self.yesBtn, 0, 1)
        btnlayout.addWidget(self.noBtn, 0,2)
        btnlayout.addWidget(self.nextBtn,0,3)

        layout.addWidget(self.questionPane, 1, 0)
        layout.addLayout(btnlayout, 2,0)

        #list of questions to be asked
        self.qlist = ["cold","headache","sweat","fatigue","apetite loss",
                      "cough","tommy pain","rashes","light sensitivity",
                      "bitterness","muscle pain","cattarh","fever","purging","vomit","dizziness"]

        #result for malaria and typhoid
        self.malariaResult = [1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1]
        self.typhoidResult = [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1]
        self.illness = "Unknown Ailment"

        #item to keep the current index in the question list
        self.curindex = 0

        #array to hold the user result
        self.userResult = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        #this represents the user key selected either yes or no
        self.key = 0

        self.setWindowTitle("Diagnosis Questions")
        self.setLayout(layout)

        #connect the 3 buttons to the signal to check which was selected
        self.connect(self.yesBtn, SIGNAL("clicked()"), self.check_key_selected)
        self.connect(self.noBtn, SIGNAL("clicked()"), self.check_key_selected)
        self.connect(self.nextBtn, SIGNAL("clicked()"),self.generate_question)

        self.generate_question()

    def generate_question(self):
        """
            this method generates the question using the current question index and
            and checks if the index is not the maximum which indicates there is no
            more questions to be answered then open the result page
        """
        try:
            self.qstring = "Do you experience " + self.qlist[self.curindex] + " ?"
            self.questionPane.setText(self.qstring)
            self.curindex = self.curindex + 1 #increment the curindex counter
        except IndexError:
            self.curindex = 16
            #check the userResult array and the illness
            if self.userResult == self.malariaResult:
                self.illness = "Malaria"
            elif self.userResult == self.typhoidResult:
                self.illness = "Typhoid"
            else:
                self.illness = "Unknown Ailment"
                self.resultPage = ResultPage(self.illness)
                self.hide()
                self.resultPage.show()

    def check_key_selected(self):
        """
            this method checks the key selected by the user to assign the result for that
            index of question, Yes is represented by 1 ans No is 0
        """
        clicker = self.sender()  #the clicker of the button
        #check for the button clicker
        if clicker is None or not isinstance(clicker, QPushButton):
            return False
        else:
            self.key = 1 if clicker.text() ==  "Yes" else 0
            try:
                self.userResult[self.curindex - 1] = self.key #index of userResult[currentquestion index]
            except IndexError:
                #this shows that is the end of the questions
                self.curindex = 16



class ResultPage(QWidget):
    def __init__(self,illness, parent=None):
        super(ResultPage, self).__init__(parent)

        self.illness  = illness

        layout = QGridLayout()

        finalDisplay = QTextEdit()
        finalDisplay.setGeometry(30, 60, 500, 500)
        finalDisplay.setReadOnly(True)
        layout.addWidget(finalDisplay)
        self.setLayout(layout)
        self.setWindowTitle("Results")
        self.setGeometry()

        self.testResult = "According to the Diagnosis is seems you are sufferfing from " + self.illness

        finalDisplay.setText(self.testResult)


class FirstPage(QWidget, ui_firstpage.Ui_firstPage):
    def __init__(self,parent=None):
        super(FirstPage, self).__init__(parent)
        self.setupUi(self )
        self.firstDisplay.setGeometry(30,20,300,180)

        StyleSheet = """
          QPushButton{background-color:#34495e;}
          QPushButton{color:#fff;}
        """

        self.setStyleSheet(StyleSheet)
        self.setWindowIcon(QIcon("c:\Users\0code\My Pictures\flatui.png"))


    @pyqtSignature("")
    def on_startBtn_clicked(self):
        self.questionPage = QuestionsPage()
        self.hide()
        self.questionPage.show()



app = QApplication(sys.argv)
window = FirstPage()
window.show()
app.exec_()