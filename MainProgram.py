import sys
import os
from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class MainScreen():
    def showSplashScreen(self):
        self.pix=QPixmap("parking.jpg")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()


def showSetupWindow():
    mainScreen.splassh.close()
    installWindow.show()


def showLoginWindow():
    mainScreen.splassh.close()
    login.showLoginScreen()



app=QApplication(sys.argv)
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(2000,showLoginWindow)
else:
    QTimer.singleShot(2000,showSetupWindow)


sys.exit(app.exec_())
