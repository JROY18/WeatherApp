import sys                                                                                          # To import system variables in python
import requests                                                                                     # To make a request to api using request module
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()                                                                          #super() calls the parent class constructor
        self.city_label = QLabel("Enter city name :",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.teamperature = QLabel("70F",self)
        self.emoji = QLabel("star",self)
        self.description_label = QLabel("Sunny",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.teamperature)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.teamperature.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.emoji.setObjectName("emoji")
        self.teamperature.setObjectName("temperature")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
        QLabel, QPushButton{  
                font-family: calibri;
            }
        QLabel{
                font-size: 40px;
                font-style: italic;
            }
        """)
        


if __name__ == "__main__":
        app = QApplication(sys.argv)
        weather_app = WeatherApp()
        weather_app.show()
        sys.exit(app.exec_())                                                                      # Keeps your app running in a loop until an action is performed for returning exit code
