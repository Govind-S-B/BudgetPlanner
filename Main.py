import sqlite3
import sys
import os
import glob
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from ui_main import Ui_MainWindow # IMPORT GUI FILE


class DBloader():

    index = 0
    previous_index = 0 # for reverting changes
    db = None

    @staticmethod
    def dblist():
        os.chdir(r'.\Databases')
        x = glob.glob('*.db')
        os.chdir(r'..\\')

        return x

    @staticmethod
    def dbconnect(profile):
        os.chdir(r'.\Databases')
        DBloader.db = sqlite3.connect(profile)
        os.chdir(r'..\\')

        print(DBloader.db)
        return DBloader.db


class MainWindow(QMainWindow):
    EXIT_CODE_REBOOT = -123 #restart functionality

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() # so here i think the gui is inside this main window
        self.ui.setupUi(self)

        if len(DBloader.dblist()) == 0:
            self.ui.circle_button.setText("+")
            self.ui.profile_text.setText("Please make a new profile")
            self.ui.New_button.hide()
            self.ui.next_arrow.hide()
            self.ui.prev_arrow.hide()
        else :
            DBloader.index = 0
            self.ui.circle_button.setText(DBloader.dblist()[DBloader.index][0].upper())
            self.ui.profile_text.setText(DBloader.dblist()[DBloader.index][0:-3].upper())

            self.btn_grp = QButtonGroup()
            self.btn_grp.setExclusive(True)

            tempvar = 0 # made for int id for buttons in the app drawer like thing
            for x in DBloader.dblist():
                self.construct_buttons(tempvar)
                tempvar += 1
            del tempvar

            self.ui.app_drawer_layout.itemAt(DBloader.index).widget().setStyleSheet("QPushButton {\n"
        "    border:none;\n"
        "    border-radius:4px;\n"
        "    \n"
        "    background-color: rgb(255, 87, 51 );\n"
        "    \n"
        "}\n")

            self.btn_grp.buttonClicked.connect(self.on_click)


        #LABEL HOVER

        def hover_on(event):
            self.ui.profile_text.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(248, 255, 0, 255), stop:0.702381 rgba(58, 213, 159, 255));")

        def hover_off(event):
            self.ui.profile_text.setStyleSheet("color: rgb(255, 255, 255);")

        self.ui.circle_button.enterEvent = hover_on
        self.ui.circle_button.leaveEvent = hover_off

        self.ui.next_arrow.clicked.connect(self.next_click)
        self.ui.prev_arrow.clicked.connect(self.prev_click)


        self.ui.circle_button.clicked.connect(self.profile_click)

        self.ui.New_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.Profile_name_Field.returnPressed.connect(self.LineEditDone)


        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def LineEditDone(self):
        DBloader.dbconnect(self.ui.Profile_name_Field.text() + ".db")
        self.ui.stackedWidget.setCurrentIndex(2)


    def profile_click(self):  # called when the main button is pressed
        if len(DBloader.dblist()) == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else :
            DBloader.dbconnect(DBloader.dblist()[DBloader.index])
            self.ui.stackedWidget.setCurrentIndex(2)

    def keyPressEvent(self,e): #restart
        if (e.key() == Qt.Key_F5):
            qApp.exit( MainWindow.EXIT_CODE_REBOOT )

    def setIndex(self):
        # reverting
        self.ui.app_drawer_layout.itemAt(DBloader.previous_index).widget().setStyleSheet("QPushButton {\n"
    "    border:none;\n"
    "    border-radius:4px;\n"
    "    \n"
    "    background-color: rgba(242, 243, 244,255);\n"
    "    \n"
    "}\n"
    "\n"
    "QPushButton:hover {\n"
    "    background-color: rgba(242, 243, 244,150);\n"
    "    \n"
    "}")

        #applying
        self.ui.circle_button.setText(DBloader.dblist()[DBloader.index][0].upper())
        self.ui.profile_text.setText(DBloader.dblist()[DBloader.index][0:-3].upper())
        self.ui.app_drawer_layout.itemAt(DBloader.index).widget().setStyleSheet("QPushButton {\n"
    "    border:none;\n"
    "    border-radius:4px;\n"
    "    \n"
    "    background-color: rgb(255, 87, 51 );\n"
    "    \n"
    "}\n")

    def on_click(self):
    	DBloader.previous_index = DBloader.index
    	DBloader.index = self.btn_grp.checkedId()
    	self.setIndex()

    def prev_click(self):
        if DBloader.index != 0:
            DBloader.previous_index = DBloader.index
            DBloader.index -= 1
        else:
            DBloader.previous_index = DBloader.index
            DBloader.index = (len(DBloader.dblist())-1)

        self.setIndex()

    def next_click(self):
        if DBloader.index < (len(DBloader.dblist())-1):
            DBloader.previous_index = DBloader.index
            DBloader.index += 1
        else :
            DBloader.previous_index = DBloader.index
            DBloader.index = 0

        self.setIndex()


    def construct_buttons(self,i):
        self.ui.button1 = QtWidgets.QPushButton()
        self.ui.button1.setMaximumSize(QtCore.QSize(9, 9))
        self.ui.button1.setToolTipDuration(-1)
        self.ui.button1.setStyleSheet("QPushButton {\n"
    "    border:none;\n"
    "    border-radius:4px;\n"
    "    \n"
    "    background-color: rgba(242, 243, 244,255);\n"
    "    \n"
    "}\n"
    "\n"
    "QPushButton:hover {\n"
    "    background-color: rgba(242, 243, 244,150);\n"
    "    \n"
    "}")
        self.ui.button1.setText("")
        self.ui.button1.setObjectName("button1")

        self.ui.button1.setCheckable(True)
        self.ui.app_drawer_layout.addWidget(self.ui.button1)
        self.btn_grp.addButton(self.ui.button1,i)





#_________________________________________________________________________________
GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0284091, y1:0.045, x2:0.960227, y2:0.972, stop:0 rgba(75, 108, 183, 255), stop:0.806818 rgba(24, 40, 72, 255)); border-radius: 0px;")
            self.ui.bt_maximise.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0284091, y1:0.045, x2:0.960227, y2:0.972, stop:0 rgba(75, 108, 183, 255), stop:0.806818 rgba(24, 40, 72, 255)); border-radius: 10px;")
            self.ui.bt_maximise.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.bt_maximise.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.bt_minimise.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.bt_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")



    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
#_________________________________________________________________________________





if __name__ == "__main__":
    currentExitCode = MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        a = QApplication(sys.argv)
        w = MainWindow()
        w.show()
        currentExitCode = a.exec_()
        a = None  # delete the QApplication object
