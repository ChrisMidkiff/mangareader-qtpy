# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mangareader.ui'
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
        MainWindow.resize(1071, 1440)
        MainWindow.setStyleSheet(_fromUtf8("QScrollBar:vertical\n"
" {\n"
"     width: 80px;\n"
" }"))
        self.ok = QtGui.QWidget(MainWindow)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.stackedwidget = QtGui.QStackedWidget(self.ok)
        self.stackedwidget.setGeometry(QtCore.QRect(0, 0, 1072, 1440))
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
        self.bg1.setGeometry(QtCore.QRect(0, 0, 1071, 1440))
        self.bg1.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bg1.setFrameShadow(QtGui.QFrame.Raised)
        self.bg1.setObjectName(_fromUtf8("bg1"))
        self.image = QtGui.QLabel(self.bg1)
        self.image.setGeometry(QtCore.QRect(0, 0, 1072, 1440))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../../Downloads/download.png")))
        self.image.setScaledContents(False)
        self.image.setObjectName(_fromUtf8("image"))
        self.pagedock = QtGui.QWidget(self.bg1)
        self.pagedock.setGeometry(QtCore.QRect(0, 1345, 1071, 91))
        self.pagedock.setObjectName(_fromUtf8("pagedock"))
        self.widget_2 = QtGui.QWidget(self.pagedock)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1071, 91))
        self.widget_2.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color: white;\n"
"border : 2px solid #000000\n"
"}"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.pagecount = QtGui.QLabel(self.widget_2)
        self.pagecount.setGeometry(QtCore.QRect(22, 5, 111, 61))
        self.pagecount.setStyleSheet(_fromUtf8("QWidget{\n"
"border: 0px\n"
"}"))
        self.pagecount.setObjectName(_fromUtf8("pagecount"))
        self.pageslider = QtGui.QSlider(self.widget_2)
        self.pageslider.setGeometry(QtCore.QRect(160, 31, 891, 21))
        self.pageslider.setStyleSheet(_fromUtf8("QWidget{\n"
"   border : 0px\n"
"}\n"
"QSlider::groove:horizontal { \n"
"    background-color: white;\n"
"    border: 1px solid #424242; \n"
"    height: 15px; \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: black; \n"
"    border: 2px solid black; \n"
"    width: 16px; \n"
"    height: 30px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 10px;\n"
"}"))
        self.pageslider.setMaximum(24)
        self.pageslider.setPageStep(1)
        self.pageslider.setOrientation(QtCore.Qt.Horizontal)
        self.pageslider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.pageslider.setTickInterval(1)
        self.pageslider.setObjectName(_fromUtf8("pageslider"))
        self.dockbar = QtGui.QWidget(self.centralwidget)
        self.dockbar.setEnabled(True)
        self.dockbar.setGeometry(QtCore.QRect(0, 0, 1071, 101))
        self.dockbar.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-color : white;\n"
"    border : 2px solid #000000\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border : 0;\n"
"}"))
        self.dockbar.setObjectName(_fromUtf8("dockbar"))
        self.layoutWidget = QtGui.QWidget(self.dockbar)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 2, 1071, 102))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.prevchapterbt = QtGui.QPushButton(self.layoutWidget)
        self.prevchapterbt.setMinimumSize(QtCore.QSize(0, 100))
        self.prevchapterbt.setMaximumSize(QtCore.QSize(16777215, 100))
        self.prevchapterbt.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevchapterbt.setIcon(icon)
        self.prevchapterbt.setIconSize(QtCore.QSize(50, 50))
        self.prevchapterbt.setObjectName(_fromUtf8("prevchapterbt"))
        self.horizontalLayout_5.addWidget(self.prevchapterbt)
        self.nextchapterbt = QtGui.QPushButton(self.layoutWidget)
        self.nextchapterbt.setMinimumSize(QtCore.QSize(0, 100))
        self.nextchapterbt.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextchapterbt.setIcon(icon1)
        self.nextchapterbt.setIconSize(QtCore.QSize(50, 50))
        self.nextchapterbt.setObjectName(_fromUtf8("nextchapterbt"))
        self.horizontalLayout_5.addWidget(self.nextchapterbt)
        self.chapterlist = QtGui.QPushButton(self.layoutWidget)
        self.chapterlist.setMinimumSize(QtCore.QSize(0, 100))
        self.chapterlist.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chapterlist.setIcon(icon2)
        self.chapterlist.setIconSize(QtCore.QSize(50, 50))
        self.chapterlist.setStyleSheet(_fromUtf8(""))
        self.chapterlist.setObjectName(_fromUtf8("chapterlist"))
        self.horizontalLayout_5.addWidget(self.chapterlist)
        self.brightnessbt = QtGui.QPushButton(self.layoutWidget)
        self.brightnessbt.setMinimumSize(QtCore.QSize(0, 100))
        self.brightnessbt.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("light.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brightnessbt.setIcon(icon3)
        self.brightnessbt.setIconSize(QtCore.QSize(50, 50))
        self.brightnessbt.setObjectName(_fromUtf8("brightnessbt"))
        self.horizontalLayout_5.addWidget(self.brightnessbt)
        self.searchbt = QtGui.QPushButton(self.layoutWidget)
        self.searchbt.setMinimumSize(QtCore.QSize(0, 100))
        self.searchbt.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchbt.setIcon(icon4)
        self.searchbt.setIconSize(QtCore.QSize(50, 50))
        self.searchbt.setObjectName(_fromUtf8("searchbt"))
        self.horizontalLayout_5.addWidget(self.searchbt)
        self.bookmarkbt = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkbt.setMinimumSize(QtCore.QSize(0, 100))
        self.bookmarkbt.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("bookmarkoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkbt.setIcon(icon5)
        self.bookmarkbt.setIconSize(QtCore.QSize(60, 60))
        self.bookmarkbt.setObjectName(_fromUtf8("bookmarkbt"))
        self.horizontalLayout_5.addWidget(self.bookmarkbt)
        self.homebt = QtGui.QPushButton(self.layoutWidget)
        self.homebt.setMinimumSize(QtCore.QSize(0, 100))
        self.homebt.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebt.setIcon(icon6)
        self.homebt.setIconSize(QtCore.QSize(60, 60))
        self.homebt.setObjectName(_fromUtf8("homebt"))
        self.horizontalLayout_5.addWidget(self.homebt)
        self.bg1.raise_()
        self.dockbutton.raise_()
        self.next.raise_()
        self.prev.raise_()
        self.dockbar.raise_()
        self.stackedwidget.addWidget(self.centralwidget)
        self.centralwidget2 = QtGui.QWidget()
        self.centralwidget2.setEnabled(True)
        self.centralwidget2.setObjectName(_fromUtf8("centralwidget2"))
        self.bg2 = QtGui.QWidget(self.centralwidget2)
        self.bg2.setGeometry(QtCore.QRect(0, -10, 1081, 1440))
        self.bg2.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg2.setObjectName(_fromUtf8("bg2"))
        self.searchlist = QtGui.QListWidget(self.bg2)
        self.searchlist.setGeometry(QtCore.QRect(0, 240, 1071, 691))
        self.searchlist.setStyleSheet(_fromUtf8(""))
        self.searchlist.setObjectName(_fromUtf8("searchlist"))
        self.searchButton = QtGui.QPushButton(self.bg2)
        self.searchButton.setGeometry(QtCore.QRect(430, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"   border: 2px solid #000000\n"
"}"))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mangaSearch = QtGui.QLineEdit(self.bg2)
        self.mangaSearch.setGeometry(QtCore.QRect(20, 120, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mangaSearch.setFont(font)
        self.mangaSearch.setText(_fromUtf8(""))
        self.mangaSearch.setObjectName(_fromUtf8("mangaSearch"))
        self.widget_3 = QtGui.QWidget(self.bg2)
        self.widget_3.setGeometry(QtCore.QRect(1, 10, 1070, 101))
        self.widget_3.setStyleSheet(_fromUtf8("QWidget{\n"
"border: 2px solid #000000\n"
"}\n"
"\n"
"QPushButton{\n"
" border : 0px;\n"
" background-color: transparent\n"
"}"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.layoutWidget1 = QtGui.QWidget(self.widget_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(-3, 0, 1071, 102))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.homebt2 = QtGui.QPushButton(self.layoutWidget1)
        self.homebt2.setMinimumSize(QtCore.QSize(0, 90))
        self.homebt2.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background-color:transparent\n"
"\n"
"}"))
        self.homebt2.setText(_fromUtf8(""))
        self.homebt2.setIcon(icon6)
        self.homebt2.setIconSize(QtCore.QSize(55, 55))
        self.homebt2.setObjectName(_fromUtf8("homebt2"))
        self.horizontalLayout_6.addWidget(self.homebt2)
        self.readerbt = QtGui.QPushButton(self.layoutWidget1)
        self.readerbt.setMinimumSize(QtCore.QSize(0, 95))
        self.readerbt.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("book.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.readerbt.setIcon(icon7)
        self.readerbt.setIconSize(QtCore.QSize(50, 50))
        self.readerbt.setObjectName(_fromUtf8("readerbt"))
        self.horizontalLayout_6.addWidget(self.readerbt)
        self.brightnessbt2 = QtGui.QPushButton(self.layoutWidget1)
        self.brightnessbt2.setMinimumSize(QtCore.QSize(0, 95))
        self.brightnessbt2.setText(_fromUtf8(""))
        self.brightnessbt2.setIcon(icon3)
        self.brightnessbt2.setIconSize(QtCore.QSize(50, 50))
        self.brightnessbt2.setObjectName(_fromUtf8("brightnessbt2"))
        self.horizontalLayout_6.addWidget(self.brightnessbt2)
        self.exitbt2 = QtGui.QPushButton(self.layoutWidget1)
        self.exitbt2.setMinimumSize(QtCore.QSize(0, 95))
        self.exitbt2.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbt2.setIcon(icon8)
        self.exitbt2.setIconSize(QtCore.QSize(50, 50))
        self.exitbt2.setObjectName(_fromUtf8("exitbt2"))
        self.horizontalLayout_6.addWidget(self.exitbt2)
        self.widget = QtGui.QWidget(self.bg2)
        self.widget.setGeometry(QtCore.QRect(0, 932, 1071, 351))
        self.widget.setStyleSheet(_fromUtf8("QPushButton{\n"
"border : 0;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: white;\n"
"}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget2 = QtGui.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 10, 1061, 341))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.keyboard_grid = QtGui.QGridLayout(self.layoutWidget2)
        self.keyboard_grid.setObjectName(_fromUtf8("keyboard_grid"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.key_q = QtGui.QPushButton(self.layoutWidget2)
        self.key_q.setMinimumSize(QtCore.QSize(0, 80))
        self.key_q.setFlat(True)
        self.key_q.setObjectName(_fromUtf8("key_q"))
        self.horizontalLayout.addWidget(self.key_q)
        self.key_w = QtGui.QPushButton(self.layoutWidget2)
        self.key_w.setMinimumSize(QtCore.QSize(0, 80))
        self.key_w.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.key_w.setFlat(True)
        self.key_w.setObjectName(_fromUtf8("key_w"))
        self.horizontalLayout.addWidget(self.key_w)
        self.key_e = QtGui.QPushButton(self.layoutWidget2)
        self.key_e.setMinimumSize(QtCore.QSize(40, 80))
        self.key_e.setBaseSize(QtCore.QSize(40, 0))
        self.key_e.setFlat(True)
        self.key_e.setObjectName(_fromUtf8("key_e"))
        self.horizontalLayout.addWidget(self.key_e)
        self.key_r = QtGui.QPushButton(self.layoutWidget2)
        self.key_r.setMinimumSize(QtCore.QSize(0, 80))
        self.key_r.setFlat(True)
        self.key_r.setObjectName(_fromUtf8("key_r"))
        self.horizontalLayout.addWidget(self.key_r)
        self.key_t = QtGui.QPushButton(self.layoutWidget2)
        self.key_t.setMinimumSize(QtCore.QSize(0, 80))
        self.key_t.setFlat(True)
        self.key_t.setObjectName(_fromUtf8("key_t"))
        self.horizontalLayout.addWidget(self.key_t)
        self.key_y = QtGui.QPushButton(self.layoutWidget2)
        self.key_y.setMinimumSize(QtCore.QSize(0, 80))
        self.key_y.setFlat(True)
        self.key_y.setObjectName(_fromUtf8("key_y"))
        self.horizontalLayout.addWidget(self.key_y)
        self.key_u = QtGui.QPushButton(self.layoutWidget2)
        self.key_u.setMinimumSize(QtCore.QSize(0, 80))
        self.key_u.setFlat(True)
        self.key_u.setObjectName(_fromUtf8("key_u"))
        self.horizontalLayout.addWidget(self.key_u)
        self.key_i = QtGui.QPushButton(self.layoutWidget2)
        self.key_i.setMinimumSize(QtCore.QSize(0, 80))
        self.key_i.setFlat(True)
        self.key_i.setObjectName(_fromUtf8("key_i"))
        self.horizontalLayout.addWidget(self.key_i)
        self.key_o = QtGui.QPushButton(self.layoutWidget2)
        self.key_o.setMinimumSize(QtCore.QSize(0, 80))
        self.key_o.setFlat(True)
        self.key_o.setObjectName(_fromUtf8("key_o"))
        self.horizontalLayout.addWidget(self.key_o)
        self.key_p = QtGui.QPushButton(self.layoutWidget2)
        self.key_p.setMinimumSize(QtCore.QSize(0, 80))
        self.key_p.setFlat(True)
        self.key_p.setObjectName(_fromUtf8("key_p"))
        self.horizontalLayout.addWidget(self.key_p)
        self.keyboard_grid.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.key_num = QtGui.QPushButton(self.layoutWidget2)
        self.key_num.setMinimumSize(QtCore.QSize(0, 60))
        self.key_num.setBaseSize(QtCore.QSize(0, 60))
        self.key_num.setObjectName(_fromUtf8("key_num"))
        self.horizontalLayout_4.addWidget(self.key_num)
        self.key_space = QtGui.QPushButton(self.layoutWidget2)
        self.key_space.setMinimumSize(QtCore.QSize(700, 60))
        self.key_space.setObjectName(_fromUtf8("key_space"))
        self.horizontalLayout_4.addWidget(self.key_space)
        self.key_dotperiod = QtGui.QPushButton(self.layoutWidget2)
        self.key_dotperiod.setMinimumSize(QtCore.QSize(0, 60))
        self.key_dotperiod.setObjectName(_fromUtf8("key_dotperiod"))
        self.horizontalLayout_4.addWidget(self.key_dotperiod)
        self.key_entr = QtGui.QPushButton(self.layoutWidget2)
        self.key_entr.setMinimumSize(QtCore.QSize(0, 60))
        self.key_entr.setObjectName(_fromUtf8("key_entr"))
        self.horizontalLayout_4.addWidget(self.key_entr)
        self.keyboard_grid.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.key_shift = QtGui.QPushButton(self.layoutWidget2)
        self.key_shift.setMinimumSize(QtCore.QSize(0, 80))
        self.key_shift.setStyleSheet(_fromUtf8(""))
        self.key_shift.setFlat(True)
        self.key_shift.setObjectName(_fromUtf8("key_shift"))
        self.horizontalLayout_3.addWidget(self.key_shift)
        self.key_z = QtGui.QPushButton(self.layoutWidget2)
        self.key_z.setMinimumSize(QtCore.QSize(0, 80))
        self.key_z.setObjectName(_fromUtf8("key_z"))
        self.horizontalLayout_3.addWidget(self.key_z)
        self.key_x = QtGui.QPushButton(self.layoutWidget2)
        self.key_x.setMinimumSize(QtCore.QSize(0, 80))
        self.key_x.setObjectName(_fromUtf8("key_x"))
        self.horizontalLayout_3.addWidget(self.key_x)
        self.key_c = QtGui.QPushButton(self.layoutWidget2)
        self.key_c.setMinimumSize(QtCore.QSize(0, 80))
        self.key_c.setObjectName(_fromUtf8("key_c"))
        self.horizontalLayout_3.addWidget(self.key_c)
        self.key_v = QtGui.QPushButton(self.layoutWidget2)
        self.key_v.setMinimumSize(QtCore.QSize(0, 80))
        self.key_v.setObjectName(_fromUtf8("key_v"))
        self.horizontalLayout_3.addWidget(self.key_v)
        self.key_b = QtGui.QPushButton(self.layoutWidget2)
        self.key_b.setMinimumSize(QtCore.QSize(0, 80))
        self.key_b.setObjectName(_fromUtf8("key_b"))
        self.horizontalLayout_3.addWidget(self.key_b)
        self.key_n = QtGui.QPushButton(self.layoutWidget2)
        self.key_n.setMinimumSize(QtCore.QSize(0, 80))
        self.key_n.setObjectName(_fromUtf8("key_n"))
        self.horizontalLayout_3.addWidget(self.key_n)
        self.key_m = QtGui.QPushButton(self.layoutWidget2)
        self.key_m.setMinimumSize(QtCore.QSize(0, 80))
        self.key_m.setObjectName(_fromUtf8("key_m"))
        self.horizontalLayout_3.addWidget(self.key_m)
        self.key_bksp = QtGui.QPushButton(self.layoutWidget2)
        self.key_bksp.setMinimumSize(QtCore.QSize(0, 80))
        self.key_bksp.setObjectName(_fromUtf8("key_bksp"))
        self.horizontalLayout_3.addWidget(self.key_bksp)
        self.keyboard_grid.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.key_a = QtGui.QPushButton(self.layoutWidget2)
        self.key_a.setMinimumSize(QtCore.QSize(0, 80))
        self.key_a.setFlat(True)
        self.key_a.setObjectName(_fromUtf8("key_a"))
        self.horizontalLayout_2.addWidget(self.key_a)
        self.key_s = QtGui.QPushButton(self.layoutWidget2)
        self.key_s.setMinimumSize(QtCore.QSize(0, 80))
        self.key_s.setFlat(True)
        self.key_s.setObjectName(_fromUtf8("key_s"))
        self.horizontalLayout_2.addWidget(self.key_s)
        self.key_d = QtGui.QPushButton(self.layoutWidget2)
        self.key_d.setMinimumSize(QtCore.QSize(0, 80))
        self.key_d.setFlat(True)
        self.key_d.setObjectName(_fromUtf8("key_d"))
        self.horizontalLayout_2.addWidget(self.key_d)
        self.key_f = QtGui.QPushButton(self.layoutWidget2)
        self.key_f.setMinimumSize(QtCore.QSize(0, 80))
        self.key_f.setFlat(True)
        self.key_f.setObjectName(_fromUtf8("key_f"))
        self.horizontalLayout_2.addWidget(self.key_f)
        self.key_g = QtGui.QPushButton(self.layoutWidget2)
        self.key_g.setMinimumSize(QtCore.QSize(0, 80))
        self.key_g.setFlat(True)
        self.key_g.setObjectName(_fromUtf8("key_g"))
        self.horizontalLayout_2.addWidget(self.key_g)
        self.key_h = QtGui.QPushButton(self.layoutWidget2)
        self.key_h.setMinimumSize(QtCore.QSize(0, 80))
        self.key_h.setFlat(True)
        self.key_h.setObjectName(_fromUtf8("key_h"))
        self.horizontalLayout_2.addWidget(self.key_h)
        self.key_j = QtGui.QPushButton(self.layoutWidget2)
        self.key_j.setMinimumSize(QtCore.QSize(0, 80))
        self.key_j.setFlat(True)
        self.key_j.setObjectName(_fromUtf8("key_j"))
        self.horizontalLayout_2.addWidget(self.key_j)
        self.key_k = QtGui.QPushButton(self.layoutWidget2)
        self.key_k.setMinimumSize(QtCore.QSize(0, 80))
        self.key_k.setFlat(True)
        self.key_k.setObjectName(_fromUtf8("key_k"))
        self.horizontalLayout_2.addWidget(self.key_k)
        self.key_l = QtGui.QPushButton(self.layoutWidget2)
        self.key_l.setMinimumSize(QtCore.QSize(0, 80))
        self.key_l.setFlat(True)
        self.key_l.setObjectName(_fromUtf8("key_l"))
        self.horizontalLayout_2.addWidget(self.key_l)
        self.keyboard_grid.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.comicselector = QtGui.QComboBox(self.bg2)
        self.comicselector.setGeometry(QtCore.QRect(800, 190, 251, 41))
        self.comicselector.setObjectName(_fromUtf8("comicselector"))
        self.stackedwidget.addWidget(self.centralwidget2)
        self.centralwidget3 = QtGui.QWidget()
        self.centralwidget3.setStyleSheet(_fromUtf8(""))
        self.centralwidget3.setObjectName(_fromUtf8("centralwidget3"))
        self.infoimage = QtGui.QLabel(self.centralwidget3)
        self.infoimage.setGeometry(QtCore.QRect(810, 100, 231, 301))
        self.infoimage.setText(_fromUtf8(""))
        self.infoimage.setPixmap(QtGui.QPixmap(_fromUtf8("download.png")))
        self.infoimage.setScaledContents(True)
        self.infoimage.setObjectName(_fromUtf8("infoimage"))
        self.infochapters = QtGui.QListWidget(self.centralwidget3)
        self.infochapters.setGeometry(QtCore.QRect(0, 420, 1071, 861))
        self.infochapters.setObjectName(_fromUtf8("infochapters"))
        self.bg3 = QtGui.QWidget(self.centralwidget3)
        self.bg3.setGeometry(QtCore.QRect(-1, -1, 1081, 1301))
        self.bg3.setStyleSheet(_fromUtf8("QWidget{\n"
"   background-color: white\n"
"}"))
        self.bg3.setObjectName(_fromUtf8("bg3"))
        self.widget_4 = QtGui.QWidget(self.bg3)
        self.widget_4.setGeometry(QtCore.QRect(1, 1, 1071, 83))
        self.widget_4.setStyleSheet(_fromUtf8("QWidget{\n"
"border: 2px solid #000000\n"
"}\n"
"\n"
"QPushButton{\n"
"  border: 0px;\n"
"  background-color : transparent\n"
"}"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.layoutWidget3 = QtGui.QWidget(self.widget_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 1071, 82))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.homebt3 = QtGui.QPushButton(self.layoutWidget3)
        self.homebt3.setMinimumSize(QtCore.QSize(0, 80))
        self.homebt3.setText(_fromUtf8(""))
        self.homebt3.setIcon(icon6)
        self.homebt3.setIconSize(QtCore.QSize(55, 55))
        self.homebt3.setObjectName(_fromUtf8("homebt3"))
        self.horizontalLayout_7.addWidget(self.homebt3)
        self.searchbt3 = QtGui.QPushButton(self.layoutWidget3)
        self.searchbt3.setMinimumSize(QtCore.QSize(0, 80))
        self.searchbt3.setText(_fromUtf8(""))
        self.searchbt3.setIcon(icon4)
        self.searchbt3.setIconSize(QtCore.QSize(50, 50))
        self.searchbt3.setObjectName(_fromUtf8("searchbt3"))
        self.horizontalLayout_7.addWidget(self.searchbt3)
        self.readerbt3 = QtGui.QPushButton(self.layoutWidget3)
        self.readerbt3.setMinimumSize(QtCore.QSize(0, 80))
        self.readerbt3.setText(_fromUtf8(""))
        self.readerbt3.setIcon(icon7)
        self.readerbt3.setIconSize(QtCore.QSize(50, 50))
        self.readerbt3.setObjectName(_fromUtf8("readerbt3"))
        self.horizontalLayout_7.addWidget(self.readerbt3)
        self.brightnessbt3 = QtGui.QPushButton(self.layoutWidget3)
        self.brightnessbt3.setMinimumSize(QtCore.QSize(0, 80))
        self.brightnessbt3.setText(_fromUtf8(""))
        self.brightnessbt3.setIcon(icon3)
        self.brightnessbt3.setIconSize(QtCore.QSize(50, 50))
        self.brightnessbt3.setObjectName(_fromUtf8("brightnessbt3"))
        self.horizontalLayout_7.addWidget(self.brightnessbt3)
        self.exitbt3 = QtGui.QPushButton(self.layoutWidget3)
        self.exitbt3.setMinimumSize(QtCore.QSize(0, 80))
        self.exitbt3.setText(_fromUtf8(""))
        self.exitbt3.setIcon(icon8)
        self.exitbt3.setIconSize(QtCore.QSize(50, 50))
        self.exitbt3.setObjectName(_fromUtf8("exitbt3"))
        self.horizontalLayout_7.addWidget(self.exitbt3)
        self.infotext = QtGui.QLabel(self.bg3)
        self.infotext.setGeometry(QtCore.QRect(20, 100, 731, 81))
        self.infotext.setObjectName(_fromUtf8("infotext"))
        self.bookmarkbt2 = QtGui.QPushButton(self.bg3)
        self.bookmarkbt2.setGeometry(QtCore.QRect(30, 250, 361, 61))
        self.bookmarkbt2.setStyleSheet(_fromUtf8("QWidget{\n"
"   border: 2px solid #000000;\n"
"}"))
        self.bookmarkbt2.setObjectName(_fromUtf8("bookmarkbt2"))
        self.bg3.raise_()
        self.infoimage.raise_()
        self.infochapters.raise_()
        self.stackedwidget.addWidget(self.centralwidget3)
        self.centralwidget4 = QtGui.QWidget()
        self.centralwidget4.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-color: white;\n"
"}"))
        self.centralwidget4.setObjectName(_fromUtf8("centralwidget4"))
        self.widget_5 = QtGui.QWidget(self.centralwidget4)
        self.widget_5.setGeometry(QtCore.QRect(1, 0, 1069, 81))
        self.widget_5.setStyleSheet(_fromUtf8("QWidget{\n"
"border: 2px solid #000000\n"
"}\n"
"\n"
"QPushButton{\n"
"  border: 0px;\n"
"  background-color : transparent\n"
"}"))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.layoutWidget4 = QtGui.QWidget(self.widget_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(-2, 0, 1081, 82))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.searchbt3_2 = QtGui.QPushButton(self.layoutWidget4)
        self.searchbt3_2.setMinimumSize(QtCore.QSize(0, 80))
        self.searchbt3_2.setText(_fromUtf8(""))
        self.searchbt3_2.setIcon(icon4)
        self.searchbt3_2.setIconSize(QtCore.QSize(50, 50))
        self.searchbt3_2.setObjectName(_fromUtf8("searchbt3_2"))
        self.horizontalLayout_8.addWidget(self.searchbt3_2)
        self.readerbt3_2 = QtGui.QPushButton(self.layoutWidget4)
        self.readerbt3_2.setMinimumSize(QtCore.QSize(0, 80))
        self.readerbt3_2.setText(_fromUtf8(""))
        self.readerbt3_2.setIcon(icon7)
        self.readerbt3_2.setIconSize(QtCore.QSize(50, 50))
        self.readerbt3_2.setObjectName(_fromUtf8("readerbt3_2"))
        self.horizontalLayout_8.addWidget(self.readerbt3_2)
        self.brightnessbt3_2 = QtGui.QPushButton(self.layoutWidget4)
        self.brightnessbt3_2.setMinimumSize(QtCore.QSize(0, 80))
        self.brightnessbt3_2.setText(_fromUtf8(""))
        self.brightnessbt3_2.setIcon(icon3)
        self.brightnessbt3_2.setIconSize(QtCore.QSize(50, 50))
        self.brightnessbt3_2.setObjectName(_fromUtf8("brightnessbt3_2"))
        self.horizontalLayout_8.addWidget(self.brightnessbt3_2)
        self.exitbt3_2 = QtGui.QPushButton(self.layoutWidget4)
        self.exitbt3_2.setMinimumSize(QtCore.QSize(0, 80))
        self.exitbt3_2.setText(_fromUtf8(""))
        self.exitbt3_2.setIcon(icon8)
        self.exitbt3_2.setIconSize(QtCore.QSize(50, 50))
        self.exitbt3_2.setObjectName(_fromUtf8("exitbt3_2"))
        self.horizontalLayout_8.addWidget(self.exitbt3_2)
        self.bookmarklist = QtGui.QListWidget(self.centralwidget4)
        self.bookmarklist.setGeometry(QtCore.QRect(0, 140, 1071, 1400))
        self.bookmarklist.setStyleSheet(_fromUtf8(""))
        self.bookmarklist.setObjectName(_fromUtf8("bookmarklist"))
        self.label_2 = QtGui.QLabel(self.centralwidget4)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 291, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.no_bookmark = QtGui.QLabel(self.centralwidget4)
        self.no_bookmark.setGeometry(QtCore.QRect(10, 150, 1041, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.no_bookmark.setFont(font)
        self.no_bookmark.setStyleSheet(_fromUtf8("QLabel{\n"
"  text-align: center;\n"
"}"))
        self.no_bookmark.setAlignment(QtCore.Qt.AlignCenter)
        self.no_bookmark.setObjectName(_fromUtf8("no_bookmark"))
        self.stackedwidget.addWidget(self.centralwidget4)
        self.brightness_window = QtGui.QWidget(self.ok)
        self.brightness_window.setGeometry(QtCore.QRect(10, 350, 1050, 311))
        self.brightness_window.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color : white;\n"
" border : 2px solid #000000 \n"
"}\n"
"QPushButton{\n"
"  border : 2px solid #000000\n"
"}"))
        self.brightness_window.setObjectName(_fromUtf8("brightness_window"))
        self.plusbrightness = QtGui.QPushButton(self.brightness_window)
        self.plusbrightness.setGeometry(QtCore.QRect(520, 150, 301, 61))
        self.plusbrightness.setObjectName(_fromUtf8("plusbrightness"))
        self.brightnessslider = QtGui.QSlider(self.brightness_window)
        self.brightnessslider.setGeometry(QtCore.QRect(40, 90, 981, 22))
        self.brightnessslider.setStyleSheet(_fromUtf8("QWidget{\n"
"border :0}\n"
"QSlider::groove:horizontal { \n"
"    background-color: white;\n"
"    border: 1px solid #424242; \n"
"    height: 10px; \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: black; \n"
"    border: 2px solid black; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 10px;\n"
"}"))
        self.brightnessslider.setMaximum(24)
        self.brightnessslider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessslider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.brightnessslider.setTickInterval(1)
        self.brightnessslider.setObjectName(_fromUtf8("brightnessslider"))
        self.exitbrightness = QtGui.QPushButton(self.brightness_window)
        self.exitbrightness.setGeometry(QtCore.QRect(440, 240, 131, 51))
        self.exitbrightness.setObjectName(_fromUtf8("exitbrightness"))
        self.minusbrightness = QtGui.QPushButton(self.brightness_window)
        self.minusbrightness.setGeometry(QtCore.QRect(210, 150, 301, 61))
        self.minusbrightness.setObjectName(_fromUtf8("minusbrightness"))
        self.label = QtGui.QLabel(self.brightness_window)
        self.label.setGeometry(QtCore.QRect(440, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QWidget{\n"
"border :0}"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.ok)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionComics = QtGui.QAction(MainWindow)
        self.actionComics.setObjectName(_fromUtf8("actionComics"))
        self.actionReader = QtGui.QAction(MainWindow)
        self.actionReader.setObjectName(_fromUtf8("actionReader"))
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))

        self.retranslateUi(MainWindow)
        self.stackedwidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "L:A_N:application_ID:MangaReader_PC:N", None))
        self.pagecount.setText(_translate("MainWindow", "1/10", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.mangaSearch.setPlaceholderText(_translate("MainWindow", "manga here", None))
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
        self.bookmarkbt2.setText(_translate("MainWindow", "Add to bookmarks", None))
        self.label_2.setText(_translate("MainWindow", "Bookmarks", None))
        self.no_bookmark.setText(_translate("MainWindow", "You can add your mangas via the search mode", None))
        self.plusbrightness.setText(_translate("MainWindow", "+", None))
        self.exitbrightness.setText(_translate("MainWindow", "OK", None))
        self.minusbrightness.setText(_translate("MainWindow", "-", None))
        self.label.setText(_translate("MainWindow", "Brightness", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionComics.setText(_translate("MainWindow", "Comics", None))
        self.actionReader.setText(_translate("MainWindow", "Reader", None))
        self.actionHome.setText(_translate("MainWindow", "Home", None))

