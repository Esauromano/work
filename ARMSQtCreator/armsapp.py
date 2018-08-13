# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'destinoPoch.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ARMSApp(object):
    def setupUi(self, ARMSApp):
        ARMSApp.setObjectName("ARMSApp")
        ARMSApp.resize(1400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ARMSApp.sizePolicy().hasHeightForWidth())
        ARMSApp.setSizePolicy(sizePolicy)
        ARMSApp.setMinimumSize(QtCore.QSize(800, 600))
        ARMSApp.setMaximumSize(QtCore.QSize(1906, 2000))
        ARMSApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        ARMSApp.setAutoFillBackground(False)
        ARMSApp.setStyleSheet("\n"
"QMainWindow#ARMSApp {\n"
"border-image: url(:/IMG5/3fonodo_3.jpg) 0 0 0 0 stretch stretch;}\n"
"\n"
"\n"
"contentsMargin 0,0,0,0;\n"
"font: 11pt \"Arial Narrow\";\n"
"background-color: transparent;\n"
"padding: 3px;\n"
"margin: 2px;\n"
"padding-bottom: 0px;")
        ARMSApp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        ARMSApp.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralWidget = QtWidgets.QWidget(ARMSApp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMaximumSize(QtCore.QSize(1920, 1200))
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("QProgressBar{\n"
"border: 0px;\n"
"border-radius: 5px;\n"
"text-align: center;}\n"
"\n"
"QProgressBar::chunk {\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border:none;\n"
"width: 5px;\n"
"height: 5px;}\n"
"\n"
"QGroupBox{\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border: none;\n"
"border-radius: 12px;\n"
"padding:6px;}\n"
"\n"
"QLabel{\n"
"color: rgba(190, 219, 189, 255);\n"
"background:transparent;\n"
"border: none;\n"
"font: 12pt \"Arial Narrow\";\n"
"border-radius: 12px;\n"
"padding:2px;}\n"
"\n"
"QTableView {\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border: none;\n"
"border-radius: 12px;\n"
"font: 10pt \"Arial Narrow\";\n"
"gridline-color: rgba(190, 219, 189,33);}\n"
"\n"
"QTableView::item:focus {\n"
"color: rgb(135, 171, 141);\n"
"background: white;\n"
"border: none;\n"
"width: 25px;\n"
"height: 25px;}\n"
"\n"
"QTableView::item:selected, QTableView::item:selected:!active {\n"
"color: rgb(173, 197, 113);\n"
"background: white;\n"
"border: none;\n"
"width: 25px;\n"
"height: 25px;}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"background:transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QTableView QTableCornerButton {\n"
"background:transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"color: rgba(190, 219, 189,255);;\n"
"background:transparent;\n"
"border: 0px dotted rgba(190, 219, 189, 255);\n"
"text-align: center;\n"
"font: 9pt \"Arial Narrow\";\n"
"height: 22px;\n"
"width: 40px;}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"background-color: transparent;\n"
"color: rgb(135, 171, 141);\n"
"padding: 2px;\n"
"font: 13pt \"Roboto\";\n"
"width:150px;\n"
"height:17;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"background-color: transparent;\n"
"border:0px;\n"
"margin:0 auto;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:  rgb(190, 219, 189);\n"
"background:rgba(190, 219, 189, 75);\n"
"border: 1px solid rgba(190, 219, 189, 33);\n"
"border-radius: 12px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background:rgba(190, 219, 189, 88);\n"
"border: 1px solid rgba(190, 219, 189, 33);\n"
"border-radius: 12px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"QLineEdit{\n"
"color:  rgb(190, 219, 189);\n"
"background:rgba(190, 219, 189, 33);\n"
"border: none;\n"
"border-radius: 12px;\n"
"width: 200px;\n"
"height: 30px;}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"image: url(:/IMG5/checkbox_check.png);}\n"
"QCheckBox::indicator:unchecked {\n"
"image: url(:/IMG5/checkbox_uncheck.png);}\n"
"\n"
"\n"
"QRadioButton::indicator::checked {\n"
"image: url(:/IMG5/radiobutton_check.png);}\n"
"QRadioButton::indicator::unchecked {\n"
"image: url(:/IMG5/radiobutton_uncheck.png);}\n"
"\n"
"QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"border: none;\n"
"border-radius: 12px;}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"color: rgb(190, 219, 189);\n"
"background:transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QComboBox{\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border: none;\n"
"border-radius: 12px;\n"
"width: 200px;\n"
"height: 30px;}\n"
"\n"
"QComboBox:on\n"
"{\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border:none;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"border: none;\n"
"border-radius: 12px;}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(:/IMG5/3dropdown.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"top: 1px;\n"
"left: 1px;\n"
"}\n"
"QComboBox::item:selected, QTableView::item:selected:!active {\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"}\n"
"QComboBox::item {\n"
"color: white;\n"
"background:rgba(190, 219, 189, 33);\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"border: 2px rgba(190, 219, 189, 100);\n"
"background:rgba(190, 219, 189, 33);\n"
"height: 15px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"background:rgba(190, 219, 189, 111);\n"
"min-width: 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: 0px solid rgb(68, 92, 53);\n"
"background:rgba(190, 219, 189, 33);\n"
"width: 15px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background:rgba(190, 219, 189, 111);\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"width: 3px;\n"
"height: 3px;\n"
"background:rgba(190, 219, 189, 33);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 0px solid rgb(68, 92, 53);\n"
"width: 3px;\n"
"height: 3px;\n"
"background:rgba(190, 219, 189, 33);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"padding-bottom: 0px;")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_10.setContentsMargins(0, 11, 0, 0)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("background: rgba(96,103,125,222);\n"
"color: white;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setContentsMargins(0, 0, 11, 0)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setMaximumSize(QtCore.QSize(600, 16777215))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_13.addWidget(self.progressBar, 0, 0, 1, 1)
        self.labelProgress = QtWidgets.QLabel(self.groupBox_3)
        self.labelProgress.setStyleSheet("")
        self.labelProgress.setObjectName("labelProgress")
        self.gridLayout_13.addWidget(self.labelProgress, 0, 1, 1, 1)
        self.empreCedi = QtWidgets.QLabel(self.groupBox_3)
        self.empreCedi.setMaximumSize(QtCore.QSize(180, 16777215))
        self.empreCedi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.empreCedi.setObjectName("empreCedi")
        self.gridLayout_13.addWidget(self.empreCedi, 0, 2, 1, 1)
        self.user = QtWidgets.QLabel(self.groupBox_3)
        self.user.setMaximumSize(QtCore.QSize(150, 16777215))
        self.user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user.setObjectName("user")
        self.gridLayout_13.addWidget(self.user, 0, 3, 1, 1)
        self.version = QtWidgets.QLabel(self.groupBox_3)
        self.version.setMaximumSize(QtCore.QSize(80, 16777215))
        self.version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.gridLayout_13.addWidget(self.version, 0, 4, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget1Principal = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget1Principal.sizePolicy().hasHeightForWidth())
        self.tabWidget1Principal.setSizePolicy(sizePolicy)
        self.tabWidget1Principal.setMaximumSize(QtCore.QSize(1920, 1200))
        self.tabWidget1Principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget1Principal.setStyleSheet("QTabWidget::pane {\n"
"    border: 0px dotted white;\n"
"    background-color: transparent;\n"
"}\n"
"QTabBar::tab {\n"
"margin: 2px;\n"
"background: rgba(96, 103, 125, 123);\n"
"color: white;\n"
"padding: 5px;\n"
"font: 12pt \"Roboto\";\n"
"width:110px;\n"
"height:17px;\n"
"text-alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"margin: 2px;\n"
"font-weight: bold;\n"
"background-color: rgba(111,93,104,123);\n"
"text-alignment: center;\n"
"}\n"
"QTabBar::tab::disabled\n"
"{\n"
"margin: 2px;\n"
"font-weight: bold;\n"
"color: transparent;\n"
"background-color: transparent;\n"
"text-alignment: center;\n"
"}\n"
"\n"
"")
        self.tabWidget1Principal.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget1Principal.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget1Principal.setIconSize(QtCore.QSize(64, 64))
        self.tabWidget1Principal.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget1Principal.setUsesScrollButtons(False)
        self.tabWidget1Principal.setObjectName("tabWidget1Principal")
        self.iniciar = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iniciar.sizePolicy().hasHeightForWidth())
        self.iniciar.setSizePolicy(sizePolicy)
        self.iniciar.setMaximumSize(QtCore.QSize(12345, 12345))
        self.iniciar.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px dotted white;\n"
"    background-color: transparent;\n"
"}\n"
"QTabBar::tab {\n"
"margin: 2px;\n"
"background: rgba(96, 103, 125, 123);\n"
"color: white;\n"
"padding: 5px;\n"
"font: 12pt \"Roboto\";\n"
"width:110px;\n"
"height:17px;\n"
"text-alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"margin: 2px;\n"
"font-weight: bold;\n"
"background-color: rgba(111,93,104,123);\n"
"text-alignment: center;\n"
"}\n"
"QTabBar::tab::disabled\n"
"{\n"
"margin: 2px;\n"
"font-weight: bold;\n"
"color: transparent;\n"
"background-color: transparent;\n"
"text-alignment: center;\n"
"}\n"
"\n"
"")
        self.iniciar.setObjectName("iniciar")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.iniciar)
        self.gridLayout_42.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_42.setSpacing(6)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.frame = QtWidgets.QFrame(self.iniciar)
        self.frame.setStyleSheet("background:transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.frame_48 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_48.setMaximumSize(QtCore.QSize(520, 600))
        self.frame_48.setStyleSheet("border: 0px dotted white;\n"
"background:rgba(96,103,125,222);")
        self.frame_48.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_48)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG5/3logo_iniciosesion.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 2, 1, 1)
        self.editCEDI_3 = QtWidgets.QLineEdit(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editCEDI_3.sizePolicy().hasHeightForWidth())
        self.editCEDI_3.setSizePolicy(sizePolicy)
        self.editCEDI_3.setMinimumSize(QtCore.QSize(0, 0))
        self.editCEDI_3.setStyleSheet("QLineEdit{\n"
"background:rgba(255,255,255,123);\n"
"border: none;\n"
"padding-left:5px;\n"
"color: black;\n"
"font: 12pt \"Roboto\";\n"
"margin: 2px;\n"
"width: 200px;\n"
"height: 30px;}\n"
"")
        self.editCEDI_3.setObjectName("editCEDI_3")
        self.gridLayout_9.addWidget(self.editCEDI_3, 1, 1, 1, 1)
        self.editUsuario_3 = QtWidgets.QLineEdit(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editUsuario_3.sizePolicy().hasHeightForWidth())
        self.editUsuario_3.setSizePolicy(sizePolicy)
        self.editUsuario_3.setStyleSheet("QLineEdit{\n"
"background:rgba(255,255,255,123);\n"
"border: none;\n"
"padding-left:5px;\n"
"color: black;\n"
"font: 12pt \"Roboto\";\n"
"margin: 2px;\n"
"width: 200px;\n"
"height: 30px;}\n"
"")
        self.editUsuario_3.setObjectName("editUsuario_3")
        self.gridLayout_9.addWidget(self.editUsuario_3, 2, 1, 1, 1)
        self.editClave_3 = QtWidgets.QLineEdit(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClave_3.sizePolicy().hasHeightForWidth())
        self.editClave_3.setSizePolicy(sizePolicy)
        self.editClave_3.setStyleSheet("QLineEdit{\n"
"background:rgba(255,255,255,123);\n"
"border: none;\n"
"padding-left:5px;\n"
"color: black;\n"
"font: 12pt \"Roboto\";\n"
"margin: 2px;\n"
"width: 200px;\n"
"height: 30px;}\n"
"")
        self.editClave_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editClave_3.setObjectName("editClave_3")
        self.gridLayout_9.addWidget(self.editClave_3, 3, 1, 1, 1)
        self.btnLogin_3 = QtWidgets.QPushButton(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin_3.sizePolicy().hasHeightForWidth())
        self.btnLogin_3.setSizePolicy(sizePolicy)
        self.btnLogin_3.setMaximumSize(QtCore.QSize(12345, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 133, 143, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnLogin_3.setPalette(palette)
        self.btnLogin_3.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.btnLogin_3.setCheckable(True)
        self.btnLogin_3.setObjectName("btnLogin_3")
        self.gridLayout_9.addWidget(self.btnLogin_3, 4, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_48, 0, 1, 1, 1)
        self.gridLayout_42.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget1Principal.addTab(self.iniciar, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(425, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 0, 1, 1)
        self.logo_footer_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_footer_4.sizePolicy().hasHeightForWidth())
        self.logo_footer_4.setSizePolicy(sizePolicy)
        self.logo_footer_4.setMinimumSize(QtCore.QSize(420, 420))
        self.logo_footer_4.setMaximumSize(QtCore.QSize(420, 420))
        self.logo_footer_4.setStyleSheet("background:transparent;\n"
"")
        self.logo_footer_4.setPixmap(QtGui.QPixmap("IMG5/3logo_iniciosesion_2.png"))
        self.logo_footer_4.setScaledContents(True)
        self.logo_footer_4.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_footer_4.setObjectName("logo_footer_4")
        self.gridLayout_8.addWidget(self.logo_footer_4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(455, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 2, 1, 1)
        self.logo_footer = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_footer.sizePolicy().hasHeightForWidth())
        self.logo_footer.setSizePolicy(sizePolicy)
        self.logo_footer.setMinimumSize(QtCore.QSize(0, 0))
        self.logo_footer.setMaximumSize(QtCore.QSize(12345, 40))
        self.logo_footer.setStyleSheet("font: 17PT \"Roboto\";\n"
"color:white;\n"
"background:transparent;\n"
"\n"
"")
        self.logo_footer.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_footer.setObjectName("logo_footer")
        self.gridLayout_8.addWidget(self.logo_footer, 1, 0, 1, 3)
        self.tabWidget1Principal.addTab(self.tab, "")
        self.interfaz = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interfaz.sizePolicy().hasHeightForWidth())
        self.interfaz.setSizePolicy(sizePolicy)
        self.interfaz.setMaximumSize(QtCore.QSize(12345, 12345))
        self.interfaz.setObjectName("interfaz")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.interfaz)
        self.gridLayout_29.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_29.setSpacing(6)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.groupBox_2 = QtWidgets.QGroupBox(self.interfaz)
        self.groupBox_2.setStyleSheet("background:transparent;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_20.sizePolicy().hasHeightForWidth())
        self.groupBox_20.setSizePolicy(sizePolicy)
        self.groupBox_20.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_20.setMaximumSize(QtCore.QSize(12345, 12345))
        self.groupBox_20.setStyleSheet("background:transparent;")
        self.groupBox_20.setTitle("")
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_20)
        self.frame_3.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_3.setStyleSheet("background:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButtonInterfasePochtecaPedidos = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonInterfasePochtecaPedidos.setStyleSheet("color:white;")
        self.radioButtonInterfasePochtecaPedidos.setChecked(True)
        self.radioButtonInterfasePochtecaPedidos.setObjectName("radioButtonInterfasePochtecaPedidos")
        self.gridLayout_3.addWidget(self.radioButtonInterfasePochtecaPedidos, 0, 0, 1, 1)
        self.btnFiltroFechas = QtWidgets.QPushButton(self.frame_3)
        self.btnFiltroFechas.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.btnFiltroFechas.setObjectName("btnFiltroFechas")
        self.gridLayout_3.addWidget(self.btnFiltroFechas, 4, 0, 1, 1)
        self.radioButtonInterfasePochtecaOperadores = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonInterfasePochtecaOperadores.setStyleSheet("color:white;")
        self.radioButtonInterfasePochtecaOperadores.setObjectName("radioButtonInterfasePochtecaOperadores")
        self.gridLayout_3.addWidget(self.radioButtonInterfasePochtecaOperadores, 2, 0, 1, 1)
        self.frame_27 = QtWidgets.QFrame(self.frame_3)
        self.frame_27.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_27.setStyleSheet("background:transparent; margin-top:0px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_12.setContentsMargins(0, 0, 11, 11)
        self.gridLayout_12.setHorizontalSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.filtrarFechas = QtWidgets.QCheckBox(self.frame_27)
        self.filtrarFechas.setStyleSheet("color:white;")
        self.filtrarFechas.setObjectName("filtrarFechas")
        self.gridLayout_12.addWidget(self.filtrarFechas, 1, 0, 1, 1)
        self.dateEditPochteca = QtWidgets.QDateEdit(self.frame_27)
        self.dateEditPochteca.setStyleSheet("font: 16px;\n"
"color: rgb(255,255,255);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(70,70,70);")
        self.dateEditPochteca.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.dateEditPochteca.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEditPochteca.setCalendarPopup(True)
        self.dateEditPochteca.setDate(QtCore.QDate(2089, 1, 1))
        self.dateEditPochteca.setObjectName("dateEditPochteca")
        self.gridLayout_12.addWidget(self.dateEditPochteca, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_27, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 183))
        self.frame_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_2.setStyleSheet("margin-left:0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_14.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.radioButtonInterfasePochtecaTodos = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonInterfasePochtecaTodos.setStyleSheet("color:white; padding-left:0px;")
        self.radioButtonInterfasePochtecaTodos.setChecked(True)
        self.radioButtonInterfasePochtecaTodos.setObjectName("radioButtonInterfasePochtecaTodos")
        self.gridLayout_14.addWidget(self.radioButtonInterfasePochtecaTodos, 0, 0, 1, 1)
        self.radioButtonInterfasePochtecaCancelados = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonInterfasePochtecaCancelados.setStyleSheet("color:white; padding-left:0px;")
        self.radioButtonInterfasePochtecaCancelados.setObjectName("radioButtonInterfasePochtecaCancelados")
        self.gridLayout_14.addWidget(self.radioButtonInterfasePochtecaCancelados, 1, 0, 1, 1)
        self.radioButtonInterfasePochtecaOrdinarios = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonInterfasePochtecaOrdinarios.setStyleSheet("color:white; padding-left:0px;")
        self.radioButtonInterfasePochtecaOrdinarios.setObjectName("radioButtonInterfasePochtecaOrdinarios")
        self.gridLayout_14.addWidget(self.radioButtonInterfasePochtecaOrdinarios, 2, 0, 1, 1)
        self.radioButtonInterfasePochtecaUrgentes = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonInterfasePochtecaUrgentes.setStyleSheet("color:white; padding-left:0px;")
        self.radioButtonInterfasePochtecaUrgentes.setChecked(False)
        self.radioButtonInterfasePochtecaUrgentes.setObjectName("radioButtonInterfasePochtecaUrgentes")
        self.gridLayout_14.addWidget(self.radioButtonInterfasePochtecaUrgentes, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.pushButtonInterfasePochtecaGenera = QtWidgets.QPushButton(self.groupBox_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInterfasePochtecaGenera.sizePolicy().hasHeightForWidth())
        self.pushButtonInterfasePochtecaGenera.setSizePolicy(sizePolicy)
        self.pushButtonInterfasePochtecaGenera.setMaximumSize(QtCore.QSize(12345, 40))
        self.pushButtonInterfasePochtecaGenera.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.pushButtonInterfasePochtecaGenera.setObjectName("pushButtonInterfasePochtecaGenera")
        self.gridLayout.addWidget(self.pushButtonInterfasePochtecaGenera, 3, 1, 1, 2)
        self.listWidgetPochtecaFTP = QtWidgets.QListWidget(self.groupBox_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetPochtecaFTP.sizePolicy().hasHeightForWidth())
        self.listWidgetPochtecaFTP.setSizePolicy(sizePolicy)
        self.listWidgetPochtecaFTP.setMinimumSize(QtCore.QSize(500, 0))
        self.listWidgetPochtecaFTP.setStyleSheet("QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"font: 12pt \"Roboto\";\n"
"border: 0.5px dotted white;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"font: 12pt \"Roboto\";\n"
"color: white;\n"
"background:rgb(111,93,104,222);\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.listWidgetPochtecaFTP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidgetPochtecaFTP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidgetPochtecaFTP.setObjectName("listWidgetPochtecaFTP")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaFTP.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaFTP.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaFTP.addItem(item)
        self.gridLayout.addWidget(self.listWidgetPochtecaFTP, 0, 2, 2, 1)
        self.abrirLocal = QtWidgets.QPushButton(self.groupBox_20)
        self.abrirLocal.setMaximumSize(QtCore.QSize(16777215, 40))
        self.abrirLocal.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.abrirLocal.setObjectName("abrirLocal")
        self.gridLayout.addWidget(self.abrirLocal, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_20, 0, 0, 1, 1)
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.groupBox_21.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_21.setMaximumSize(QtCore.QSize(12345, 16777215))
        self.groupBox_21.setStyleSheet("background:transparent;")
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_22.setContentsMargins(20, 25, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.listWidgetPochtecaHistorial = QtWidgets.QListWidget(self.groupBox_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetPochtecaHistorial.sizePolicy().hasHeightForWidth())
        self.listWidgetPochtecaHistorial.setSizePolicy(sizePolicy)
        self.listWidgetPochtecaHistorial.setStyleSheet("QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"font: 12pt \"Roboto\";\n"
"border: 0.5px dotted white;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"font: 12pt \"Roboto\";\n"
"color: white;\n"
"background:rgb(111,93,104,222);\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.listWidgetPochtecaHistorial.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidgetPochtecaHistorial.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidgetPochtecaHistorial.setObjectName("listWidgetPochtecaHistorial")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPochtecaHistorial.addItem(item)
        self.gridLayout_22.addWidget(self.listWidgetPochtecaHistorial, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_21, 0, 1, 1, 1)
        self.gridLayout_29.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget1Principal.addTab(self.interfaz, "")
        self.DestinosFTP = QtWidgets.QWidget()
        self.DestinosFTP.setObjectName("DestinosFTP")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.DestinosFTP)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.DestinosFTP)
        self.groupBox.setMinimumSize(QtCore.QSize(800, 600))
        self.groupBox.setStyleSheet("background:transparent;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_23 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        self.groupBox_23.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_23.setMaximumSize(QtCore.QSize(12345, 12345))
        self.groupBox_23.setStyleSheet("background:transparent;")
        self.groupBox_23.setObjectName("groupBox_23")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_23)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listDestinos = QtWidgets.QListWidget(self.groupBox_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listDestinos.sizePolicy().hasHeightForWidth())
        self.listDestinos.setSizePolicy(sizePolicy)
        self.listDestinos.setMinimumSize(QtCore.QSize(500, 0))
        self.listDestinos.setStyleSheet("QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"font: 12pt \"Roboto\";\n"
"border: 0.5px dotted white;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"font: 12pt \"Roboto\";\n"
"color: white;\n"
"background:rgb(111,93,104,222);\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.listDestinos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listDestinos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listDestinos.setObjectName("listDestinos")
        self.verticalLayout_2.addWidget(self.listDestinos)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_23)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSyncDestinos = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSyncDestinos.sizePolicy().hasHeightForWidth())
        self.btnSyncDestinos.setSizePolicy(sizePolicy)
        self.btnSyncDestinos.setMaximumSize(QtCore.QSize(12345, 40))
        self.btnSyncDestinos.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.btnSyncDestinos.setObjectName("btnSyncDestinos")
        self.horizontalLayout_2.addWidget(self.btnSyncDestinos)
        self.abrirLocal_2 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abrirLocal_2.sizePolicy().hasHeightForWidth())
        self.abrirLocal_2.setSizePolicy(sizePolicy)
        self.abrirLocal_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.abrirLocal_2.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.abrirLocal_2.setObjectName("abrirLocal_2")
        self.horizontalLayout_2.addWidget(self.abrirLocal_2)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.gridLayout_4.addWidget(self.groupBox_23, 0, 0, 1, 1)
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy)
        self.groupBox_22.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_22.setMaximumSize(QtCore.QSize(12345, 16777215))
        self.groupBox_22.setStyleSheet("background:transparent;")
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tablePochtecaLatLong = QtWidgets.QListWidget(self.groupBox_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablePochtecaLatLong.sizePolicy().hasHeightForWidth())
        self.tablePochtecaLatLong.setSizePolicy(sizePolicy)
        self.tablePochtecaLatLong.setStyleSheet("QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"font: 12pt \"Roboto\";\n"
"border: 0.5px dotted white;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"font: 12pt \"Roboto\";\n"
"color: white;\n"
"background:rgb(111,93,104,222);\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.tablePochtecaLatLong.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablePochtecaLatLong.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablePochtecaLatLong.setObjectName("tablePochtecaLatLong")
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong.addItem(item)
        self.gridLayout_5.addWidget(self.tablePochtecaLatLong, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_22)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.tablePochtecaLatLong_2 = QtWidgets.QListWidget(self.groupBox_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablePochtecaLatLong_2.sizePolicy().hasHeightForWidth())
        self.tablePochtecaLatLong_2.setSizePolicy(sizePolicy)
        self.tablePochtecaLatLong_2.setStyleSheet("QListWidget{\n"
"color: white;\n"
"background:transparent;\n"
"font: 12pt \"Roboto\";\n"
"border: 0.5px dotted white;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"font: 12pt \"Roboto\";\n"
"color: white;\n"
"background:rgb(111,93,104,222);\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.tablePochtecaLatLong_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablePochtecaLatLong_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablePochtecaLatLong_2.setObjectName("tablePochtecaLatLong_2")
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tablePochtecaLatLong_2.addItem(item)
        self.gridLayout_5.addWidget(self.tablePochtecaLatLong_2, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_22, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget1Principal.addTab(self.DestinosFTP, "")
        self.DestinosDB = QtWidgets.QWidget()
        self.DestinosDB.setObjectName("DestinosDB")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.DestinosDB)
        self.gridLayout_15.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_15.setSpacing(6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.DestinosDB)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"color: white;\n"
"background: rgba(96, 103, 125, 222);\n"
"font: 11pt \"Roboto\";\n"
"border: 1px dotted white;\n"
"gridline-color: rgb(187,203,209);\n"
"}\n"
"\n"
"QTableWidget::item:selected:active {\n"
"background: white;\n"
"color:black;\n"
"padding:0px;\n"
"margin:0px;\n"
"width: 25px;\n"
"height: 25px;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"font: 11pt \"Roboto\";\n"
"color:  white;\n"
"background:rgba(255,255,255,222);\n"
"border: none;\n"
"border-radius: 0px;\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"border: 0px;\n"
"background:rgba(188,188,188,255);\n"
"height: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"background:rgba(96,103,125,88);\n"
"min-width: 7px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"border: 0px;\n"
"background:rgba(188,188,188,255);\n"
"width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:rgba(96,103,125,88);\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"font: 9pt \"Roboto\";\n"
"color: white;\n"
"background: rgba(96, 103, 125, 222);\n"
"align: center;\n"
"height: 22px;\n"
"width: 40px;\n"
"qproperty-alignment: AlignCenter;\n"
"gridline-color: rgba(187,203,209,222);\n"
"border: 0.5px dotted rgb(187,203,222);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"background: rgba(96, 103, 125, 222);\n"
"gridline-color: rgba(187,203,209,222);\n"
"}\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.mapFrame = QtWidgets.QFrame(self.DestinosDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapFrame.sizePolicy().hasHeightForWidth())
        self.mapFrame.setSizePolicy(sizePolicy)
        self.mapFrame.setMinimumSize(QtCore.QSize(800, 300))
        self.mapFrame.setStyleSheet("color: rgba(173, 197, 113, 255);\n"
"background: transparent;\n"
"border: 2px solid rgba(255, 0, 0, 255);\n"
"font: 15pt \"Arial Narrow\";")
        self.mapFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapFrame.setObjectName("mapFrame")
        self.verticalLayout.addWidget(self.mapFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cargarDestinosDB = QtWidgets.QPushButton(self.DestinosDB)
        self.cargarDestinosDB.setMaximumSize(QtCore.QSize(16777215, 40))
        self.cargarDestinosDB.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.cargarDestinosDB.setObjectName("cargarDestinosDB")
        self.horizontalLayout.addWidget(self.cargarDestinosDB)
        self.mandarDestinosDB = QtWidgets.QPushButton(self.DestinosDB)
        self.mandarDestinosDB.setMaximumSize(QtCore.QSize(16777215, 40))
        self.mandarDestinosDB.setStyleSheet("QPushButton{\n"
"font:11pt \"Roboto\";\n"
"background:rgba(150, 133, 143, 133);\n"
"margin: 5px;\n"
"color:  rgb(255,255,255);\n"
"border: 1px solid rgb(150, 133, 143);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"font: 11pt \"Roboto\";\n"
"margin: 5px;\n"
"color: rgb(255,255,255);\n"
"background:rgba(198,168,184,222);\n"
"border: 0px solid rgba(190, 219, 189, 33);\n"
"border-radius: 5px;\n"
"width: 200px;\n"
"height: 40px;}")
        self.mandarDestinosDB.setObjectName("mandarDestinosDB")
        self.horizontalLayout.addWidget(self.mandarDestinosDB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_15.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tabWidget1Principal.addTab(self.DestinosDB, "")
        self.gridLayout_10.addWidget(self.tabWidget1Principal, 0, 0, 1, 1)
        ARMSApp.setCentralWidget(self.centralWidget)

        self.retranslateUi(ARMSApp)
        self.tabWidget1Principal.setCurrentIndex(1)
        self.listWidgetPochtecaFTP.setCurrentRow(0)
        self.listWidgetPochtecaHistorial.setCurrentRow(0)
        self.tablePochtecaLatLong.setCurrentRow(0)
        self.tablePochtecaLatLong_2.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(ARMSApp)

    def retranslateUi(self, ARMSApp):
        _translate = QtCore.QCoreApplication.translate
        ARMSApp.setWindowTitle(_translate("ARMSApp", "ARMS-Exchange"))
        self.labelProgress.setText(_translate("ARMSApp", "TextLabel"))
        self.empreCedi.setText(_translate("ARMSApp", "TextLabel"))
        self.user.setText(_translate("ARMSApp", "TextLabel"))
        self.version.setText(_translate("ARMSApp", "TextLabel"))
        self.editCEDI_3.setText(_translate("ARMSApp", "CENADI"))
        self.editCEDI_3.setPlaceholderText(_translate("ARMSApp", "CEDI"))
        self.editUsuario_3.setPlaceholderText(_translate("ARMSApp", "Usuario"))
        self.editClave_3.setPlaceholderText(_translate("ARMSApp", "Clave"))
        self.btnLogin_3.setText(_translate("ARMSApp", "INICIAR"))
        self.tabWidget1Principal.setTabText(self.tabWidget1Principal.indexOf(self.iniciar), _translate("ARMSApp", "Iniciar"))
        self.logo_footer.setText(_translate("ARMSApp", "A R M S"))
        self.tabWidget1Principal.setTabText(self.tabWidget1Principal.indexOf(self.tab), _translate("ARMSApp", "Areté"))
        self.radioButtonInterfasePochtecaPedidos.setText(_translate("ARMSApp", "Pedidos"))
        self.btnFiltroFechas.setText(_translate("ARMSApp", "Buscar"))
        self.radioButtonInterfasePochtecaOperadores.setText(_translate("ARMSApp", "Operadores"))
        self.filtrarFechas.setText(_translate("ARMSApp", "Seleccione aqui para filtar por fecha"))
        self.radioButtonInterfasePochtecaTodos.setText(_translate("ARMSApp", "Todos"))
        self.radioButtonInterfasePochtecaCancelados.setText(_translate("ARMSApp", "Cancelados"))
        self.radioButtonInterfasePochtecaOrdinarios.setText(_translate("ARMSApp", "Ordinarios"))
        self.radioButtonInterfasePochtecaUrgentes.setText(_translate("ARMSApp", "Urgentes"))
        self.pushButtonInterfasePochtecaGenera.setText(_translate("ARMSApp", "Generar desde el FTP"))
        __sortingEnabled = self.listWidgetPochtecaFTP.isSortingEnabled()
        self.listWidgetPochtecaFTP.setSortingEnabled(False)
        item = self.listWidgetPochtecaFTP.item(0)
        item.setText(_translate("ARMSApp", "Archivo AA"))
        item = self.listWidgetPochtecaFTP.item(1)
        item.setText(_translate("ARMSApp", "Archivo BB"))
        item = self.listWidgetPochtecaFTP.item(2)
        item.setText(_translate("ARMSApp", "Archivo CC"))
        self.listWidgetPochtecaFTP.setSortingEnabled(__sortingEnabled)
        self.abrirLocal.setText(_translate("ARMSApp", "Generar desde archivo local"))
        self.groupBox_21.setTitle(_translate("ARMSApp", "SpreadSheets generados"))
        __sortingEnabled = self.listWidgetPochtecaHistorial.isSortingEnabled()
        self.listWidgetPochtecaHistorial.setSortingEnabled(False)
        item = self.listWidgetPochtecaHistorial.item(0)
        item.setText(_translate("ARMSApp", "Archivo AA"))
        item = self.listWidgetPochtecaHistorial.item(1)
        item.setText(_translate("ARMSApp", "Archivo BB"))
        item = self.listWidgetPochtecaHistorial.item(2)
        item.setText(_translate("ARMSApp", "Archivo CC"))
        self.listWidgetPochtecaHistorial.setSortingEnabled(__sortingEnabled)
        self.tabWidget1Principal.setTabText(self.tabWidget1Principal.indexOf(self.interfaz), _translate("ARMSApp", "Generar SS"))
        self.groupBox_23.setTitle(_translate("ARMSApp", "Destinos en el FTP"))
        self.btnSyncDestinos.setText(_translate("ARMSApp", "Sincronizar archivo seleccionado"))
        self.abrirLocal_2.setText(_translate("ARMSApp", "Destinos desde archivo local"))
        self.groupBox_22.setTitle(_translate("ARMSApp", "Coordenadas encontradas"))
        __sortingEnabled = self.tablePochtecaLatLong.isSortingEnabled()
        self.tablePochtecaLatLong.setSortingEnabled(False)
        item = self.tablePochtecaLatLong.item(0)
        item.setText(_translate("ARMSApp", "Archivo AA"))
        item = self.tablePochtecaLatLong.item(1)
        item.setText(_translate("ARMSApp", "Archivo BB"))
        item = self.tablePochtecaLatLong.item(2)
        item.setText(_translate("ARMSApp", "Archivo CC"))
        self.tablePochtecaLatLong.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ARMSApp", "Coordenadas no encontradas, corregir texto"))
        __sortingEnabled = self.tablePochtecaLatLong_2.isSortingEnabled()
        self.tablePochtecaLatLong_2.setSortingEnabled(False)
        item = self.tablePochtecaLatLong_2.item(0)
        item.setText(_translate("ARMSApp", "Archivo AA"))
        item = self.tablePochtecaLatLong_2.item(1)
        item.setText(_translate("ARMSApp", "Archivo BB"))
        item = self.tablePochtecaLatLong_2.item(2)
        item.setText(_translate("ARMSApp", "Archivo CC"))
        self.tablePochtecaLatLong_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget1Principal.setTabText(self.tabWidget1Principal.indexOf(self.DestinosFTP), _translate("ARMSApp", "Destinos FTP"))
        self.cargarDestinosDB.setText(_translate("ARMSApp", "Recargar destinos"))
        self.mandarDestinosDB.setText(_translate("ARMSApp", "Mandar a base de datos"))
        self.tabWidget1Principal.setTabText(self.tabWidget1Principal.indexOf(self.DestinosDB), _translate("ARMSApp", "Destinos DB"))

import ARMSQtCreator.img5_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ARMSApp = QtWidgets.QMainWindow()
    ui = Ui_ARMSApp()
    ui.setupUi(ARMSApp)
    ARMSApp.show()
    sys.exit(app.exec_())

