# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vieta\OneDrive\Documents\mangareader\mangareader.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1072, 1350)
        MainWindow.setStyleSheet(_fromUtf8("QScrollBar:vertical\n"
" {\n"
"     width: 80px;\n"
" }"))
        self.stackedwidget = QtGui.QStackedWidget(MainWindow)
        self.stackedwidget.setStyleSheet(_fromUtf8(""))
        self.stackedwidget.setObjectName(_fromUtf8("stackedwidget"))
        self.centralwidget = QtGui.QWidget()
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dockbutton = QtGui.QPushButton(self.centralwidget)
        self.dockbutton.setGeometry(QtCore.QRect(0, 1140, 1072, 141))
        self.dockbutton.setMinimumSize(QtCore.QSize(0, 80))
        self.dockbutton.setText(_fromUtf8(""))
        self.dockbutton.setAutoRepeatDelay(299)
        self.dockbutton.setFlat(True)
        self.dockbutton.setObjectName(_fromUtf8("dockbutton"))
        self.next = QtGui.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(250, 0, 831, 1190))
        self.next.setText(_fromUtf8(""))
        self.next.setFlat(True)
        self.next.setObjectName(_fromUtf8("next"))
        self.prev = QtGui.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(0, 0, 250, 1190))
        self.prev.setText(_fromUtf8(""))
        self.prev.setFlat(True)
        self.prev.setObjectName(_fromUtf8("prev"))
        self.bg1 = QtGui.QFrame(self.centralwidget)
        self.bg1.setGeometry(QtCore.QRect(0, 0, 1071, 1291))
        self.bg1.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bg1.setFrameShadow(QtGui.QFrame.Raised)
        self.bg1.setObjectName(_fromUtf8("bg1"))
        self.image = QtGui.QLabel(self.bg1)
        self.image.setGeometry(QtCore.QRect(0, 0, 1072, 1290))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../../Downloads/download.png")))
        self.image.setScaledContents(True)
        self.image.setObjectName(_fromUtf8("image"))
        self.dockbar = QtGui.QWidget(self.centralwidget)
        self.dockbar.setEnabled(True)
        self.dockbar.setGeometry(QtCore.QRect(0, 1180, 1071, 111))
        self.dockbar.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-color : white\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border : 0;\n"
"}"))
        self.dockbar.setObjectName(_fromUtf8("dockbar"))
        self.layoutWidget_2 = QtGui.QWidget(self.dockbar)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1071, 82))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.brightnessbt = QtGui.QPushButton(self.layoutWidget_2)
        self.brightnessbt.setMinimumSize(QtCore.QSize(0, 80))
        self.brightnessbt.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("light.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brightnessbt.setIcon(icon)
        self.brightnessbt.setIconSize(QtCore.QSize(50, 50))
        self.brightnessbt.setObjectName(_fromUtf8("brightnessbt"))
        self.gridLayout.addWidget(self.brightnessbt, 0, 3, 1, 1)
        self.prevchapterbt = QtGui.QPushButton(self.layoutWidget_2)
        self.prevchapterbt.setMinimumSize(QtCore.QSize(0, 80))
        self.prevchapterbt.setMaximumSize(QtCore.QSize(16777215, 80))
        self.prevchapterbt.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevchapterbt.setIcon(icon1)
        self.prevchapterbt.setIconSize(QtCore.QSize(50, 50))
        self.prevchapterbt.setObjectName(_fromUtf8("prevchapterbt"))
        self.gridLayout.addWidget(self.prevchapterbt, 0, 0, 1, 1)
        self.nextchapterbt = QtGui.QPushButton(self.layoutWidget_2)
        self.nextchapterbt.setMinimumSize(QtCore.QSize(0, 80))
        self.nextchapterbt.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextchapterbt.setIcon(icon2)
        self.nextchapterbt.setIconSize(QtCore.QSize(50, 50))
        self.nextchapterbt.setObjectName(_fromUtf8("nextchapterbt"))
        self.gridLayout.addWidget(self.nextchapterbt, 0, 1, 1, 1)
        self.chapterlist = QtGui.QPushButton(self.layoutWidget_2)
        self.chapterlist.setMinimumSize(QtCore.QSize(0, 80))
        self.chapterlist.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chapterlist.setIcon(icon3)
        self.chapterlist.setIconSize(QtCore.QSize(50, 50))
        self.chapterlist.setObjectName(_fromUtf8("chapterlist"))
        self.gridLayout.addWidget(self.chapterlist, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.brightnessbt.raise_()
        self.nextchapterbt.raise_()
        self.chapterlist.raise_()
        self.pushButton_5.raise_()
        self.prevchapterbt.raise_()
        self.brightness_window = QtGui.QWidget(self.centralwidget)
        self.brightness_window.setGeometry(QtCore.QRect(10, 320, 1051, 311))
        self.brightness_window.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color : white\n"
"}"))
        self.brightness_window.setObjectName(_fromUtf8("brightness_window"))
        self.brightnessslider = QtGui.QSlider(self.brightness_window)
        self.brightnessslider.setGeometry(QtCore.QRect(30, 80, 981, 22))
        self.brightnessslider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessslider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.brightnessslider.setTickInterval(12)
        self.brightnessslider.setObjectName(_fromUtf8("brightnessslider"))
        self.label = QtGui.QLabel(self.brightness_window)
        self.label.setGeometry(QtCore.QRect(430, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.exitbrightness = QtGui.QPushButton(self.brightness_window)
        self.exitbrightness.setGeometry(QtCore.QRect(430, 240, 131, 51))
        self.exitbrightness.setObjectName(_fromUtf8("exitbrightness"))
        self.minusbrightness = QtGui.QPushButton(self.brightness_window)
        self.minusbrightness.setGeometry(QtCore.QRect(200, 140, 301, 61))
        self.minusbrightness.setObjectName(_fromUtf8("minusbrightness"))
        self.plusbrightness = QtGui.QPushButton(self.brightness_window)
        self.plusbrightness.setGeometry(QtCore.QRect(510, 140, 301, 61))
        self.plusbrightness.setObjectName(_fromUtf8("plusbrightness"))
        self.bg1.raise_()
        self.dockbutton.raise_()
        self.dockbar.raise_()
        self.next.raise_()
        self.prev.raise_()
        self.brightness_window.raise_()
        self.stackedwidget.addWidget(self.centralwidget)
        self.centralwidget2 = QtGui.QWidget()
        self.centralwidget2.setEnabled(True)
        self.centralwidget2.setObjectName(_fromUtf8("centralwidget2"))
        self.mangaSearch = QtGui.QLineEdit(self.centralwidget2)
        self.mangaSearch.setGeometry(QtCore.QRect(20, 10, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.mangaSearch.setFont(font)
        self.mangaSearch.setText(_fromUtf8(""))
        self.mangaSearch.setObjectName(_fromUtf8("mangaSearch"))
        self.searchButton = QtGui.QPushButton(self.centralwidget2)
        self.searchButton.setGeometry(QtCore.QRect(440, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.widget = QtGui.QWidget(self.centralwidget2)
        self.widget.setGeometry(QtCore.QRect(10, 920, 1071, 351))
        self.widget.setStyleSheet(_fromUtf8("QPushButton{\n"
"border : 0;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: white;\n"
"}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1061, 341))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.keyboard_grid = QtGui.QGridLayout(self.layoutWidget)
        self.keyboard_grid.setObjectName(_fromUtf8("keyboard_grid"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.key_q = QtGui.QPushButton(self.layoutWidget)
        self.key_q.setMinimumSize(QtCore.QSize(0, 80))
        self.key_q.setFlat(True)
        self.key_q.setObjectName(_fromUtf8("key_q"))
        self.horizontalLayout.addWidget(self.key_q)
        self.key_w = QtGui.QPushButton(self.layoutWidget)
        self.key_w.setMinimumSize(QtCore.QSize(0, 80))
        self.key_w.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.key_w.setFlat(True)
        self.key_w.setObjectName(_fromUtf8("key_w"))
        self.horizontalLayout.addWidget(self.key_w)
        self.key_e = QtGui.QPushButton(self.layoutWidget)
        self.key_e.setMinimumSize(QtCore.QSize(40, 80))
        self.key_e.setBaseSize(QtCore.QSize(40, 0))
        self.key_e.setFlat(True)
        self.key_e.setObjectName(_fromUtf8("key_e"))
        self.horizontalLayout.addWidget(self.key_e)
        self.key_r = QtGui.QPushButton(self.layoutWidget)
        self.key_r.setMinimumSize(QtCore.QSize(0, 80))
        self.key_r.setFlat(True)
        self.key_r.setObjectName(_fromUtf8("key_r"))
        self.horizontalLayout.addWidget(self.key_r)
        self.key_t = QtGui.QPushButton(self.layoutWidget)
        self.key_t.setMinimumSize(QtCore.QSize(0, 80))
        self.key_t.setFlat(True)
        self.key_t.setObjectName(_fromUtf8("key_t"))
        self.horizontalLayout.addWidget(self.key_t)
        self.key_y = QtGui.QPushButton(self.layoutWidget)
        self.key_y.setMinimumSize(QtCore.QSize(0, 80))
        self.key_y.setFlat(True)
        self.key_y.setObjectName(_fromUtf8("key_y"))
        self.horizontalLayout.addWidget(self.key_y)
        self.key_u = QtGui.QPushButton(self.layoutWidget)
        self.key_u.setMinimumSize(QtCore.QSize(0, 80))
        self.key_u.setFlat(True)
        self.key_u.setObjectName(_fromUtf8("key_u"))
        self.horizontalLayout.addWidget(self.key_u)
        self.key_i = QtGui.QPushButton(self.layoutWidget)
        self.key_i.setMinimumSize(QtCore.QSize(0, 80))
        self.key_i.setFlat(True)
        self.key_i.setObjectName(_fromUtf8("key_i"))
        self.horizontalLayout.addWidget(self.key_i)
        self.key_o = QtGui.QPushButton(self.layoutWidget)
        self.key_o.setMinimumSize(QtCore.QSize(0, 80))
        self.key_o.setFlat(True)
        self.key_o.setObjectName(_fromUtf8("key_o"))
        self.horizontalLayout.addWidget(self.key_o)
        self.key_p = QtGui.QPushButton(self.layoutWidget)
        self.key_p.setMinimumSize(QtCore.QSize(0, 80))
        self.key_p.setFlat(True)
        self.key_p.setObjectName(_fromUtf8("key_p"))
        self.horizontalLayout.addWidget(self.key_p)
        self.keyboard_grid.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.key_num = QtGui.QPushButton(self.layoutWidget)
        self.key_num.setMinimumSize(QtCore.QSize(0, 60))
        self.key_num.setBaseSize(QtCore.QSize(0, 60))
        self.key_num.setObjectName(_fromUtf8("key_num"))
        self.horizontalLayout_4.addWidget(self.key_num)
        self.key_space = QtGui.QPushButton(self.layoutWidget)
        self.key_space.setMinimumSize(QtCore.QSize(700, 60))
        self.key_space.setObjectName(_fromUtf8("key_space"))
        self.horizontalLayout_4.addWidget(self.key_space)
        self.key_dotperiod = QtGui.QPushButton(self.layoutWidget)
        self.key_dotperiod.setMinimumSize(QtCore.QSize(0, 60))
        self.key_dotperiod.setObjectName(_fromUtf8("key_dotperiod"))
        self.horizontalLayout_4.addWidget(self.key_dotperiod)
        self.key_entr = QtGui.QPushButton(self.layoutWidget)
        self.key_entr.setMinimumSize(QtCore.QSize(0, 60))
        self.key_entr.setObjectName(_fromUtf8("key_entr"))
        self.horizontalLayout_4.addWidget(self.key_entr)
        self.keyboard_grid.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.key_shift = QtGui.QPushButton(self.layoutWidget)
        self.key_shift.setMinimumSize(QtCore.QSize(0, 80))
        self.key_shift.setStyleSheet(_fromUtf8(""))
        self.key_shift.setFlat(True)
        self.key_shift.setObjectName(_fromUtf8("key_shift"))
        self.horizontalLayout_3.addWidget(self.key_shift)
        self.key_z = QtGui.QPushButton(self.layoutWidget)
        self.key_z.setMinimumSize(QtCore.QSize(0, 80))
        self.key_z.setObjectName(_fromUtf8("key_z"))
        self.horizontalLayout_3.addWidget(self.key_z)
        self.key_x = QtGui.QPushButton(self.layoutWidget)
        self.key_x.setMinimumSize(QtCore.QSize(0, 80))
        self.key_x.setObjectName(_fromUtf8("key_x"))
        self.horizontalLayout_3.addWidget(self.key_x)
        self.key_c = QtGui.QPushButton(self.layoutWidget)
        self.key_c.setMinimumSize(QtCore.QSize(0, 80))
        self.key_c.setObjectName(_fromUtf8("key_c"))
        self.horizontalLayout_3.addWidget(self.key_c)
        self.key_v = QtGui.QPushButton(self.layoutWidget)
        self.key_v.setMinimumSize(QtCore.QSize(0, 80))
        self.key_v.setObjectName(_fromUtf8("key_v"))
        self.horizontalLayout_3.addWidget(self.key_v)
        self.key_b = QtGui.QPushButton(self.layoutWidget)
        self.key_b.setMinimumSize(QtCore.QSize(0, 80))
        self.key_b.setObjectName(_fromUtf8("key_b"))
        self.horizontalLayout_3.addWidget(self.key_b)
        self.key_n = QtGui.QPushButton(self.layoutWidget)
        self.key_n.setMinimumSize(QtCore.QSize(0, 80))
        self.key_n.setObjectName(_fromUtf8("key_n"))
        self.horizontalLayout_3.addWidget(self.key_n)
        self.key_m = QtGui.QPushButton(self.layoutWidget)
        self.key_m.setMinimumSize(QtCore.QSize(0, 80))
        self.key_m.setObjectName(_fromUtf8("key_m"))
        self.horizontalLayout_3.addWidget(self.key_m)
        self.key_bksp = QtGui.QPushButton(self.layoutWidget)
        self.key_bksp.setMinimumSize(QtCore.QSize(0, 80))
        self.key_bksp.setObjectName(_fromUtf8("key_bksp"))
        self.horizontalLayout_3.addWidget(self.key_bksp)
        self.keyboard_grid.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.key_a = QtGui.QPushButton(self.layoutWidget)
        self.key_a.setMinimumSize(QtCore.QSize(0, 80))
        self.key_a.setFlat(True)
        self.key_a.setObjectName(_fromUtf8("key_a"))
        self.horizontalLayout_2.addWidget(self.key_a)
        self.key_s = QtGui.QPushButton(self.layoutWidget)
        self.key_s.setMinimumSize(QtCore.QSize(0, 80))
        self.key_s.setFlat(True)
        self.key_s.setObjectName(_fromUtf8("key_s"))
        self.horizontalLayout_2.addWidget(self.key_s)
        self.key_d = QtGui.QPushButton(self.layoutWidget)
        self.key_d.setMinimumSize(QtCore.QSize(0, 80))
        self.key_d.setFlat(True)
        self.key_d.setObjectName(_fromUtf8("key_d"))
        self.horizontalLayout_2.addWidget(self.key_d)
        self.key_f = QtGui.QPushButton(self.layoutWidget)
        self.key_f.setMinimumSize(QtCore.QSize(0, 80))
        self.key_f.setFlat(True)
        self.key_f.setObjectName(_fromUtf8("key_f"))
        self.horizontalLayout_2.addWidget(self.key_f)
        self.key_g = QtGui.QPushButton(self.layoutWidget)
        self.key_g.setMinimumSize(QtCore.QSize(0, 80))
        self.key_g.setFlat(True)
        self.key_g.setObjectName(_fromUtf8("key_g"))
        self.horizontalLayout_2.addWidget(self.key_g)
        self.key_h = QtGui.QPushButton(self.layoutWidget)
        self.key_h.setMinimumSize(QtCore.QSize(0, 80))
        self.key_h.setFlat(True)
        self.key_h.setObjectName(_fromUtf8("key_h"))
        self.horizontalLayout_2.addWidget(self.key_h)
        self.key_j = QtGui.QPushButton(self.layoutWidget)
        self.key_j.setMinimumSize(QtCore.QSize(0, 80))
        self.key_j.setFlat(True)
        self.key_j.setObjectName(_fromUtf8("key_j"))
        self.horizontalLayout_2.addWidget(self.key_j)
        self.key_k = QtGui.QPushButton(self.layoutWidget)
        self.key_k.setMinimumSize(QtCore.QSize(0, 80))
        self.key_k.setFlat(True)
        self.key_k.setObjectName(_fromUtf8("key_k"))
        self.horizontalLayout_2.addWidget(self.key_k)
        self.key_l = QtGui.QPushButton(self.layoutWidget)
        self.key_l.setMinimumSize(QtCore.QSize(0, 80))
        self.key_l.setFlat(True)
        self.key_l.setObjectName(_fromUtf8("key_l"))
        self.horizontalLayout_2.addWidget(self.key_l)
        self.keyboard_grid.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.bg2 = QtGui.QWidget(self.centralwidget2)
        self.bg2.setGeometry(QtCore.QRect(0, -10, 1081, 1301))
        self.bg2.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg2.setObjectName(_fromUtf8("bg2"))
        self.searchlist = QtGui.QListWidget(self.bg2)
        self.searchlist.setGeometry(QtCore.QRect(0, 140, 1071, 791))
        self.searchlist.setStyleSheet(_fromUtf8(""))
        self.searchlist.setObjectName(_fromUtf8("searchlist"))
        self.bg2.raise_()
        self.mangaSearch.raise_()
        self.searchButton.raise_()
        self.widget.raise_()
        self.stackedwidget.addWidget(self.centralwidget2)
        self.centralwidget3 = QtGui.QWidget()
        self.centralwidget3.setStyleSheet(_fromUtf8(""))
        self.centralwidget3.setObjectName(_fromUtf8("centralwidget3"))
        self.infoimage = QtGui.QLabel(self.centralwidget3)
        self.infoimage.setGeometry(QtCore.QRect(800, 80, 241, 321))
        self.infoimage.setText(_fromUtf8(""))
        self.infoimage.setPixmap(QtGui.QPixmap(_fromUtf8("download.png")))
        self.infoimage.setScaledContents(True)
        self.infoimage.setObjectName(_fromUtf8("infoimage"))
        self.infotext = QtGui.QLabel(self.centralwidget3)
        self.infotext.setGeometry(QtCore.QRect(20, 80, 731, 81))
        self.infotext.setObjectName(_fromUtf8("infotext"))
        self.infochapters = QtGui.QListView(self.centralwidget3)
        self.infochapters.setGeometry(QtCore.QRect(0, 420, 1071, 861))
        self.infochapters.setObjectName(_fromUtf8("infochapters"))
        self.bg3 = QtGui.QWidget(self.centralwidget3)
        self.bg3.setGeometry(QtCore.QRect(-1, -1, 1081, 1301))
        self.bg3.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg3.setObjectName(_fromUtf8("bg3"))
        self.bg3.raise_()
        self.infoimage.raise_()
        self.infotext.raise_()
        self.infochapters.raise_()
        self.stackedwidget.addWidget(self.centralwidget3)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionComics = QtGui.QAction(MainWindow)
        self.actionComics.setObjectName(_fromUtf8("actionComics"))
        self.actionReader = QtGui.QAction(MainWindow)
        self.actionReader.setObjectName(_fromUtf8("actionReader"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionComics)
        self.menuFile.addAction(self.actionReader)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "L:A_N:application_ID:MangaReader", None))
        self.label.setText(_translate("MainWindow", "Brightness", None))
        self.exitbrightness.setText(_translate("MainWindow", "OK", None))
        self.minusbrightness.setText(_translate("MainWindow", "-", None))
        self.plusbrightness.setText(_translate("MainWindow", "+", None))
        self.mangaSearch.setPlaceholderText(_translate("MainWindow", "manga here", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.key_q.setText(_translate("MainWindow", "q", None))
        self.key_w.setText(_translate("MainWindow", "w", None))
        self.key_e.setText(_translate("MainWindow", "e", None))
        self.key_r.setText(_translate("MainWindow", "r", None))
        self.key_t.setText(_translate("MainWindow", "t", None))
        self.key_y.setText(_translate("MainWindow", "y", None))
        self.key_u.setText(_translate("MainWindow", "u", None))
        self.key_i.setText(_translate("MainWindow", "i", None))
        self.key_o.setText(_translate("MainWindow", "o", None))
        self.key_p.setText(_translate("MainWindow", "p", None))
        self.key_num.setText(_translate("MainWindow", "123", None))
        self.key_space.setText(_translate("MainWindow", "space", None))
        self.key_dotperiod.setText(_translate("MainWindow", ".", None))
        self.key_entr.setText(_translate("MainWindow", "enter", None))
        self.key_shift.setText(_translate("MainWindow", "shift", None))
        self.key_z.setText(_translate("MainWindow", "z", None))
        self.key_x.setText(_translate("MainWindow", "x", None))
        self.key_c.setText(_translate("MainWindow", "c", None))
        self.key_v.setText(_translate("MainWindow", "v", None))
        self.key_b.setText(_translate("MainWindow", "b", None))
        self.key_n.setText(_translate("MainWindow", "n", None))
        self.key_m.setText(_translate("MainWindow", "m", None))
        self.key_bksp.setText(_translate("MainWindow", "bksp", None))
        self.key_a.setText(_translate("MainWindow", "a", None))
        self.key_s.setText(_translate("MainWindow", "s", None))
        self.key_d.setText(_translate("MainWindow", "d", None))
        self.key_f.setText(_translate("MainWindow", "f", None))
        self.key_g.setText(_translate("MainWindow", "g", None))
        self.key_h.setText(_translate("MainWindow", "h", None))
        self.key_j.setText(_translate("MainWindow", "j", None))
        self.key_k.setText(_translate("MainWindow", "k", None))
        self.key_l.setText(_translate("MainWindow", "l", None))
        self.infotext.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionComics.setText(_translate("MainWindow", "Comics", None))
        self.actionReader.setText(_translate("MainWindow", "Reader", None))

