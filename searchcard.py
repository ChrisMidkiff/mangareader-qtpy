import sys
from PyQt4 import QtGui, QtCore
import requests


class SearchCardView (QtGui.QWidget):
    def __init__(self, parent=None):
        super(SearchCardView, self).__init__(parent)
        self.textQVBoxLayout = QtGui.QVBoxLayout()
        self.textUpQLabel = QtGui.QLabel()
        self.textDownQLabel = QtGui.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QtGui.QHBoxLayout()
        self.iconQLabel = QtGui.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        self.mangaurl = None
        self.index = 0
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setIcon(self, image):
        if 'http' in image:
            infoimage0 = requests.get(image, timeout=10)
            image = QtGui.QImage()
            image.loadFromData(infoimage0.content)
        self.iconQLabel.setPixmap(QtGui.QPixmap(image).scaled(self.iconQLabel.size(), QtCore.Qt.KeepAspectRatio))

    def setUrl(self, text):
        self.mangaurl = text

    def setIndex(self, index):
        self.index = index
