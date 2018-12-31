import sys
from board import board
from functools import partial
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import QSize


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.board=board()
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 30))
        self.clickedx=-1
        self.clickedy=-1
        
        self.buttons=[[QPushButton('Button', self) for x in range(8)] for y in range(8)]
        a=1
        b=1
        indx=0
        indy=0
        for i in self.buttons:
            for j in i:
                try:
                    k="resources/icons/"+self.board.getpiece(indx,indy).id+".png"
                    pixmap = QPixmap(k)
                    j.setText("")
                    j.setIcon(QIcon(pixmap))
                    j.setIconSize(QSize(100,100))
                    j.setStyleSheet("background-color: #bcaaa4")
#                    j.setText(str(self.board.getpiece(indx,indy).side+" "+self.board.getpiece(indx,indy).name))
#                   j.setText(":DDD")
                except (AttributeError):
                    j.setText("")
                j.clicked.connect(partial(self.handleClickCase,indx,indy))
                j.resize(100,100)
                j.move(b, a)
                a=a+100
                indx=indx+1
            a=1
            indx=0
            b=b+100
            indy=indy+1       
        self.turn=QLabel(self)
        self.turn.move(850,10)

        self.turn.setFont(QFont('SansSerif', 25))
        self.turn.setText(self.board.turn+"'s turn")
        self.setGeometry(200, 300, 1024, 800)
        self.setWindowTitle('openChess')    
        self.show()
    def redraw(self,beginx,beginy,endx,endy):
        try:
            k="resources/icons/"+self.board.getpiece(beginx,beginy).id+".png"
            pixmap = QPixmap(k)
            self.buttons[beginy][beginx].setText("")
            self.buttons[beginy][beginx].setIcon(QIcon(pixmap))
            self.buttons[beginy][beginx].setIconSize(QSize(100,100))
            self.buttons[beginy][beginx].setText("")
            self.buttons[beginy][beginx].setStyleSheet("background-color: #bcaaa4")
        except:
            self.buttons[beginy][beginx].setText("")
            self.buttons[beginy][beginx].setIcon(QIcon())
            self.buttons[beginy][beginx].setIconSize(QSize(100,100))
            self.buttons[beginy][beginx].setText("")
            self.buttons[beginy][beginx].setStyleSheet("background-color: #bcaaa4")
        try:
            k="resources/icons/"+self.board.getpiece(endx,endy).id+".png"
            pixmap = QPixmap(k)
            self.buttons[endy][endx].setText("")
            self.buttons[endy][endx].setIcon(QIcon(pixmap))
            self.buttons[endy][endx].setIconSize(QSize(100,100))
            self.buttons[endy][endx].setText("")
            self.buttons[endy][endx].setStyleSheet("background-color: #bcaaa4")
        except:
            self.buttons[endy][endx].setText("")
            self.buttons[endy][endx].setIcon(QIcon())
            self.buttons[endy][endx].setIconSize(QSize(100,100))
            self.buttons[endy][endx].setText("")
            self.buttons[endy][endx].setStyleSheet("background-color: #bcaaa4")

        self.turn.setText(self.board.turn+"'s turn")
    def handleClickCase(self,indx,indy):
        print("clickedx : "+str(self.clickedx))
        print("clickedy : "+str(self.clickedy))
        print("indx : "+str(indx))
        print("indy : "+str(indy))
        if self.clickedx==-1 and self.clickedy==-1:
            print("gr1")
            self.clickedx=indx
            self.clickedy=indy
            self.buttons[self.clickedy][self.clickedx].setStyleSheet("background-color: #00bfa5")

        elif self.board.move(self.clickedx,self.clickedy,indx,indy):
            print("gr2")
            self.redraw(self.clickedx, self.clickedy, indx, indy)
            self.clickedx=-1
            self.clickedy=-1

        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
