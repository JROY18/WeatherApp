import sys                                                                                          # To import system variables in python
import requests                                                                                     # To make a request to api using request module
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()                                                                          #super() calls the parent class constructor

if __name__ == "__main__":

        app = QApplication(sys.argv)
        weather_app = WeatherApp()
        weather_app.show()
        sys.exit(app.exec_())                                                                      # Keeps your app running