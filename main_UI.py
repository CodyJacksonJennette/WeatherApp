from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import requests
import new_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(70, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search.setFont(font)
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.getweatherButton = QtWidgets.QPushButton(self.centralwidget)
        self.getweatherButton.clicked.connect(self.get_weather)
        self.getweatherButton.setGeometry(QtCore.QRect(360, 30, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.getweatherButton.setFont(font)
        self.getweatherButton.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.getweatherButton.setObjectName("getweatherButton")
        self.forecastArea = QtWidgets.QWidget(self.centralwidget)
        self.forecastArea.setGeometry(QtCore.QRect(70, 90, 441, 341))
        self.forecastArea.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.forecastArea.setObjectName("forecastArea")
        self.weatherGoesHere = QtWidgets.QLabel(self.forecastArea)
        self.weatherGoesHere.setGeometry(QtCore.QRect(20, 20, 401, 301))
        self.weatherGoesHere.setText("")
        self.weatherGoesHere.setObjectName("weatherGoesHere")
        self.reminderWidget = QtWidgets.QWidget(self.centralwidget)
        self.reminderWidget.setGeometry(QtCore.QRect(540, 30, 181, 401))
        self.reminderWidget.setStyleSheet("")
        self.reminderWidget.setObjectName("reminderWidget")
        self.printButton = QtWidgets.QPushButton(self.reminderWidget)
        self.printButton.setGeometry(QtCore.QRect(20, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.printButton.setFont(font)
        self.printButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.print_forecast)
        self.reminderbg = QtWidgets.QLabel(self.reminderWidget)
        self.reminderbg.setGeometry(QtCore.QRect(6, 2, 171, 401))
        self.reminderbg.setStyleSheet("background-image: url(:/newPrefix/lined-paper.png);")
        self.reminderbg.setText("")
        self.reminderbg.setPixmap(QtGui.QPixmap(":/newPrefix/lined-paper.png"))
        self.reminderbg.setScaledContents(True)
        self.reminderbg.setObjectName("reminderbg")
        self.remindertext = QtWidgets.QLabel(self.reminderWidget)
        self.remindertext.setGeometry(QtCore.QRect(40, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.remindertext.setFont(font)
        self.remindertext.setObjectName("remindertext")
        self.remindersGoHere = QtWidgets.QLabel(self.reminderWidget)
        self.remindersGoHere.setGeometry(QtCore.QRect(40, 50, 121, 281))
        self.remindersGoHere.setText("")
        self.remindersGoHere.setObjectName("remindersGoHere")
        self.reminderbg.raise_()
        self.printButton.raise_()
        self.remindertext.raise_()
        self.remindersGoHere.raise_()
        self.sunbg = QtWidgets.QLabel(self.centralwidget)
        self.sunbg.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.sunbg.setMinimumSize(QtCore.QSize(800, 600))
        self.sunbg.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sunbg.setFont(font)
        self.sunbg.setStyleSheet("")
        self.sunbg.setText("")
        self.sunbg.setPixmap(QtGui.QPixmap(":/newPrefix/sun.jpg"))
        self.sunbg.setScaledContents(True)
        self.sunbg.setObjectName("sunbg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 460, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.sunbg.raise_()
        self.search.raise_()
        self.getweatherButton.raise_()
        self.forecastArea.raise_()
        self.reminderWidget.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getweatherButton.setText(_translate("MainWindow", "Get Weather"))
        self.printButton.setText(_translate("MainWindow", "Print"))
        self.remindertext.setText(_translate("MainWindow", "Reminders..."))
        self.label.setText(_translate("MainWindow", "TIP: Type a city or ZIP Code in the search bar and click \"Get Weather\" to instantly get the current weather conditions! Reminders of items to have on hand to prepare for the weather will be listed on the right side. "))

    def get_weather(self):
        location = self.search.text()
        weather_key = "20184d8f0b1ac6a9146bc617163b1c64"
        base_url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {"appid": weather_key, "q": location}
        response = requests.get(base_url, params=params)
        response_json = response.json()
        latitude = response_json[0]["lat"]
        longitude = response_json[0]["lon"]
        weather_url = "http://api.openweathermap.org/data/2.5/weather"
        weather_params = {"appid": weather_key, "lat": latitude, "lon": longitude, "units": "imperial"}
        weather_response = requests.get(weather_url, params=weather_params)
        forecast = weather_response.json()
        desc = forecast["weather"][0]["description"]
        temp = forecast["main"]["temp"]
        final_output = "City: %s \nConditions: %s \nTemperature (°F): %s" % (location, desc, temp)
        self.weatherGoesHere.setText(final_output)

    # def settings(self):

    def print_forecast(self):
        if self.weatherGoesHere.text() == "":
            print("error")
        else:
            read_file = open("printable_forecast.txt", "r+")
            read_file.truncate(0)
            read_file.close()
            write_file = open("printable_forecast.txt", "w")
            write_file.write(self.weatherGoesHere.text())
            write_file.close()
            os.system("python pdf-generator.py")
            pdf_path = "C:/PYTHON/forecast_pdf.pdf"
            os.startfile(pdf_path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
