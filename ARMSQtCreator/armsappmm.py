# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'armsapp.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ARMSApp(object):
    def setupUi(self, ARMSApp):
        ARMSApp.setObjectName("ARMSApp")
        ARMSApp.resize(1520, 1144)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        ARMSApp.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Img/arms_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ARMSApp.setWindowIcon(icon)
        ARMSApp.setAutoFillBackground(False)
        ARMSApp.setStyleSheet("QMainWindow#ARMSApp\n"
"{\n"
"border-image: url(:/Img/arms_fondo.png) 0 0 0 0 stretch stretch;\n"
"background: url(:/Img/arms_fondo.png) no-repeat center center fixed\n"
"}")
        ARMSApp.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralWidget = QtWidgets.QWidget(ARMSApp)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_29.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_29.setSpacing(6)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_34.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_34.setSpacing(6)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        palette = QtGui.QPalette()
        self.tabWidget.setPalette(palette)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabBar::tab\n"
"{\n"
"border: 0px solid white;\n"
"background-color: rgb(41,180,115);\n"
"border-radius: 1px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"margin: 2px;\n"
"width: 30px;\n"
"height: 150px;\n"
"} \n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"background-color:  rgb(24,158,87);\n"
"} \n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"font:  14px;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_2.setStyleSheet("QTabBar::tab\n"
"{\n"
"border: 0px solid white;\n"
"background-color: rgb(41,180,115);\n"
"border-radius: 1px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"margin: 2px;\n"
"width: 150px;\n"
"height: 30px;\n"
"} \n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"background-color:  rgb(24,158,87);\n"
"} \n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"font:  14px;\n"
"}\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_26.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_26.setSpacing(6)
        self.gridLayout_26.setObjectName("gridLayout_26")
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(360, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem1, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_22.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_22.setSpacing(6)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.frame_45 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_45.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_45.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_45.setStyleSheet("font: 11px;\n"
"color: rgb(160, 232, 105);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgba(0,0,0,0);\n"
"")
        self.frame_45.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.frame_45)
        self.gridLayout_57.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_57.setSpacing(6)
        self.gridLayout_57.setObjectName("gridLayout_57")
        spacerItem2 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_57.addItem(spacerItem2, 1, 0, 1, 1)
        self.lineEditClave_2 = QtWidgets.QLineEdit(self.frame_45)
        self.lineEditClave_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditClave_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditClave_2.setObjectName("lineEditClave_2")
        self.gridLayout_57.addWidget(self.lineEditClave_2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_57.addItem(spacerItem3, 0, 2, 1, 1)
        self.lineEditUsuario_2 = QtWidgets.QLineEdit(self.frame_45)
        self.lineEditUsuario_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditUsuario_2.setObjectName("lineEditUsuario_2")
        self.gridLayout_57.addWidget(self.lineEditUsuario_2, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_57.addItem(spacerItem4, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_57.addItem(spacerItem5, 1, 3, 1, 1)
        self.lineEditCEDI_2 = QtWidgets.QLineEdit(self.frame_45)
        self.lineEditCEDI_2.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditCEDI_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditCEDI_2.setObjectName("lineEditCEDI_2")
        self.gridLayout_57.addWidget(self.lineEditCEDI_2, 1, 2, 1, 1)
        self.pushButtonIniciaSesion_2 = QtWidgets.QPushButton(self.frame_45)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonIniciaSesion_2.setPalette(palette)
        self.pushButtonIniciaSesion_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonIniciaSesion_2.setObjectName("pushButtonIniciaSesion_2")
        self.gridLayout_57.addWidget(self.pushButtonIniciaSesion_2, 4, 2, 1, 1)
        self.gridLayout_22.addWidget(self.frame_45, 1, 0, 1, 1)
        self.labelStatusBarCEDI_7 = QtWidgets.QLabel(self.groupBox_2)
        self.labelStatusBarCEDI_7.setMaximumSize(QtCore.QSize(500, 175))
        self.labelStatusBarCEDI_7.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"")
        self.labelStatusBarCEDI_7.setText("")
        self.labelStatusBarCEDI_7.setPixmap(QtGui.QPixmap(":/Img/arete_group.png"))
        self.labelStatusBarCEDI_7.setScaledContents(False)
        self.labelStatusBarCEDI_7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusBarCEDI_7.setObjectName("labelStatusBarCEDI_7")
        self.gridLayout_22.addWidget(self.labelStatusBarCEDI_7, 0, 0, 1, 1)
        self.gridLayout_26.addWidget(self.groupBox_2, 1, 1, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(360, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem7, 2, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_47.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_47.setSpacing(6)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setStyleSheet("background-color: rgba(255,255,255,50);\n"
"margin-top: 0.5em;\n"
"font: bold 18px;\n"
"color: rgb(102,102,102);\n"
"border: 0px solid white;\n"
"padding: 13px;\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_64 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_64.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_64.setSpacing(6)
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_64.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_47.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.frame_43 = QtWidgets.QFrame(self.tab_2)
        self.frame_43.setStyleSheet("border-radius: 0px;")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_43)
        self.gridLayout_23.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_23.setSpacing(6)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.labelStatusBarUser = QtWidgets.QLabel(self.frame_43)
        self.labelStatusBarUser.setObjectName("labelStatusBarUser")
        self.gridLayout_23.addWidget(self.labelStatusBarUser, 4, 0, 1, 1)
        self.progressBarStatus = QtWidgets.QProgressBar(self.frame_43)
        self.progressBarStatus.setProperty("value", 24)
        self.progressBarStatus.setObjectName("progressBarStatus")
        self.gridLayout_23.addWidget(self.progressBarStatus, 5, 0, 1, 1)
        self.labelStatusBarCEDI = QtWidgets.QLabel(self.frame_43)
        self.labelStatusBarCEDI.setObjectName("labelStatusBarCEDI")
        self.gridLayout_23.addWidget(self.labelStatusBarCEDI, 0, 0, 1, 1)
        self.labelStatusBarMensaje = QtWidgets.QLabel(self.frame_43)
        self.labelStatusBarMensaje.setObjectName("labelStatusBarMensaje")
        self.gridLayout_23.addWidget(self.labelStatusBarMensaje, 3, 0, 1, 1)
        self.labelStatusBarEmpresa = QtWidgets.QLabel(self.frame_43)
        self.labelStatusBarEmpresa.setObjectName("labelStatusBarEmpresa")
        self.gridLayout_23.addWidget(self.labelStatusBarEmpresa, 2, 0, 1, 1)
        self.gridLayout_47.addWidget(self.frame_43, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.labelStatusBarCEDI_2 = QtWidgets.QLabel(self.widget)
        self.labelStatusBarCEDI_2.setText("")
        self.labelStatusBarCEDI_2.setPixmap(QtGui.QPixmap(":/Img/arms_logo.png"))
        self.labelStatusBarCEDI_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusBarCEDI_2.setObjectName("labelStatusBarCEDI_2")
        self.verticalLayout_2.addWidget(self.labelStatusBarCEDI_2)
        self.tabWidget.addTab(self.widget, "")
        self.tabInterfase = QtWidgets.QWidget()
        self.tabInterfase.setObjectName("tabInterfase")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.tabInterfase)
        self.gridLayout_55.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_55.setSpacing(6)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tabInterfase)
        self.tabWidget_7.setStyleSheet("QTabBar::tab\n"
"{\n"
"border: 0px solid white;\n"
"background-color: rgb(41,180,115);\n"
"border-radius: 1px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"margin: 2px;\n"
"width: 250px;\n"
"height: 30px;\n"
"} \n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"background-color:  rgb(24,158,87);\n"
"} \n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"font:  14px;\n"
"}\n"
"")
        self.tabWidget_7.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_37.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_37.setSpacing(6)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_8.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_35.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_35.setSpacing(6)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_8)
        self.frame_3.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.radioButtonInterfasePochtecaPedidos = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonInterfasePochtecaPedidos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaPedidos.setChecked(True)
        self.radioButtonInterfasePochtecaPedidos.setObjectName("radioButtonInterfasePochtecaPedidos")
        self.gridLayout_10.addWidget(self.radioButtonInterfasePochtecaPedidos, 0, 0, 1, 1)
        self.radioButtonInterfasePochtecaOperadores = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonInterfasePochtecaOperadores.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaOperadores.setObjectName("radioButtonInterfasePochtecaOperadores")
        self.gridLayout_10.addWidget(self.radioButtonInterfasePochtecaOperadores, 1, 0, 1, 1)
        self.radioButtonInterfasePochtecaDestinos = QtWidgets.QRadioButton(self.frame_3)
        self.radioButtonInterfasePochtecaDestinos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaDestinos.setObjectName("radioButtonInterfasePochtecaDestinos")
        self.gridLayout_10.addWidget(self.radioButtonInterfasePochtecaDestinos, 2, 0, 1, 1)
        self.gridLayout_35.addWidget(self.frame_3, 0, 0, 1, 1)
        self.listWidgetPochtecaFTP = QtWidgets.QListWidget(self.groupBox_8)
        self.listWidgetPochtecaFTP.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.listWidgetPochtecaFTP.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetPochtecaFTP.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidgetPochtecaFTP.setObjectName("listWidgetPochtecaFTP")
        self.gridLayout_35.addWidget(self.listWidgetPochtecaFTP, 0, 1, 2, 1)
        self.frame_27 = QtWidgets.QFrame(self.groupBox_8)
        self.frame_27.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_13.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.radioButtonInterfasePochtecaUrgentes = QtWidgets.QRadioButton(self.frame_27)
        self.radioButtonInterfasePochtecaUrgentes.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaUrgentes.setChecked(False)
        self.radioButtonInterfasePochtecaUrgentes.setObjectName("radioButtonInterfasePochtecaUrgentes")
        self.gridLayout_13.addWidget(self.radioButtonInterfasePochtecaUrgentes, 3, 0, 1, 1)
        self.radioButtonInterfasePochtecaCancelados = QtWidgets.QRadioButton(self.frame_27)
        self.radioButtonInterfasePochtecaCancelados.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaCancelados.setObjectName("radioButtonInterfasePochtecaCancelados")
        self.gridLayout_13.addWidget(self.radioButtonInterfasePochtecaCancelados, 2, 0, 1, 1)
        self.radioButtonInterfasePochtecaOrdinarios = QtWidgets.QRadioButton(self.frame_27)
        self.radioButtonInterfasePochtecaOrdinarios.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaOrdinarios.setObjectName("radioButtonInterfasePochtecaOrdinarios")
        self.gridLayout_13.addWidget(self.radioButtonInterfasePochtecaOrdinarios, 1, 0, 1, 1)
        self.radioButtonInterfasePochtecaTodos = QtWidgets.QRadioButton(self.frame_27)
        self.radioButtonInterfasePochtecaTodos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfasePochtecaTodos.setChecked(True)
        self.radioButtonInterfasePochtecaTodos.setObjectName("radioButtonInterfasePochtecaTodos")
        self.gridLayout_13.addWidget(self.radioButtonInterfasePochtecaTodos, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem8, 4, 0, 1, 1)
        self.gridLayout_35.addWidget(self.frame_27, 1, 0, 1, 1)
        self.pushButtonInterfasePochtecaGenera = QtWidgets.QPushButton(self.groupBox_8)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonInterfasePochtecaGenera.setPalette(palette)
        self.pushButtonInterfasePochtecaGenera.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonInterfasePochtecaGenera.setObjectName("pushButtonInterfasePochtecaGenera")
        self.gridLayout_35.addWidget(self.pushButtonInterfasePochtecaGenera, 2, 1, 1, 1)
        self.gridLayout_37.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_9.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.listWidgetPochtecaHistorial = QtWidgets.QListWidget(self.groupBox_9)
        self.listWidgetPochtecaHistorial.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.listWidgetPochtecaHistorial.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetPochtecaHistorial.setObjectName("listWidgetPochtecaHistorial")
        self.gridLayout_11.addWidget(self.listWidgetPochtecaHistorial, 0, 0, 1, 1)
        self.gridLayout_37.addWidget(self.groupBox_9, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_54.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_54.setSpacing(6)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.groupBox_36 = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox_36.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_36.setObjectName("groupBox_36")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.groupBox_36)
        self.gridLayout_53.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_53.setSpacing(6)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.tableWidgetPochtecaAnadeDe = QtWidgets.QTableWidget(self.groupBox_36)
        self.tableWidgetPochtecaAnadeDe.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetPochtecaAnadeDe.setObjectName("tableWidgetPochtecaAnadeDe")
        self.tableWidgetPochtecaAnadeDe.setColumnCount(0)
        self.tableWidgetPochtecaAnadeDe.setRowCount(0)
        self.gridLayout_53.addWidget(self.tableWidgetPochtecaAnadeDe, 0, 0, 1, 1)
        self.tableWidgetPochtecaAnadeA = QtWidgets.QTableWidget(self.groupBox_36)
        self.tableWidgetPochtecaAnadeA.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetPochtecaAnadeA.setObjectName("tableWidgetPochtecaAnadeA")
        self.tableWidgetPochtecaAnadeA.setColumnCount(0)
        self.tableWidgetPochtecaAnadeA.setRowCount(0)
        self.gridLayout_53.addWidget(self.tableWidgetPochtecaAnadeA, 1, 0, 1, 1)
        self.pushButtonInterfasePochtecaGenera_2 = QtWidgets.QPushButton(self.groupBox_36)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonInterfasePochtecaGenera_2.setPalette(palette)
        self.pushButtonInterfasePochtecaGenera_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonInterfasePochtecaGenera_2.setObjectName("pushButtonInterfasePochtecaGenera_2")
        self.gridLayout_53.addWidget(self.pushButtonInterfasePochtecaGenera_2, 2, 0, 1, 1)
        self.gridLayout_54.addWidget(self.groupBox_36, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_60.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_60.setSpacing(6)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.tableWidgetPochtecaLatLong = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidgetPochtecaLatLong.setMinimumSize(QtCore.QSize(600, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidgetPochtecaLatLong.setPalette(palette)
        self.tableWidgetPochtecaLatLong.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetPochtecaLatLong.setObjectName("tableWidgetPochtecaLatLong")
        self.tableWidgetPochtecaLatLong.setColumnCount(0)
        self.tableWidgetPochtecaLatLong.setRowCount(0)
        self.gridLayout_60.addWidget(self.tableWidgetPochtecaLatLong, 0, 0, 1, 2)
        self.gridLayout_54.addWidget(self.groupBox, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.gridLayout_9.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_5, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_79 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_79.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_79.setSpacing(6)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.tabWidget_8 = QtWidgets.QTabWidget(self.tab_14)
        self.tabWidget_8.setObjectName("tabWidget_8")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_32.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_32.setSpacing(6)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_15)
        self.groupBox_5.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_50.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_50.setSpacing(6)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.dateEditInterfaseSilodisaFecha = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEditInterfaseSilodisaFecha.setStyleSheet("font: 16px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.dateEditInterfaseSilodisaFecha.setWrapping(False)
        self.dateEditInterfaseSilodisaFecha.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateEditInterfaseSilodisaFecha.setProperty("showGroupSeparator", False)
        self.dateEditInterfaseSilodisaFecha.setCalendarPopup(True)
        self.dateEditInterfaseSilodisaFecha.setCurrentSectionIndex(0)
        self.dateEditInterfaseSilodisaFecha.setDate(QtCore.QDate(2017, 9, 20))
        self.dateEditInterfaseSilodisaFecha.setObjectName("dateEditInterfaseSilodisaFecha")
        self.gridLayout_50.addWidget(self.dateEditInterfaseSilodisaFecha, 3, 0, 1, 1)
        self.frame_29 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_29.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_29)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButtonInterfaseSilodisaForaneo = QtWidgets.QRadioButton(self.frame_29)
        self.radioButtonInterfaseSilodisaForaneo.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaForaneo.setObjectName("radioButtonInterfaseSilodisaForaneo")
        self.gridLayout_6.addWidget(self.radioButtonInterfaseSilodisaForaneo, 1, 0, 1, 1)
        self.radioButtonInterfaseSilodisaLocal = QtWidgets.QRadioButton(self.frame_29)
        self.radioButtonInterfaseSilodisaLocal.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaLocal.setChecked(True)
        self.radioButtonInterfaseSilodisaLocal.setObjectName("radioButtonInterfaseSilodisaLocal")
        self.gridLayout_6.addWidget(self.radioButtonInterfaseSilodisaLocal, 0, 0, 1, 1)
        self.gridLayout_50.addWidget(self.frame_29, 1, 0, 1, 1)
        self.frame_30 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_30.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.frame_30)
        self.gridLayout_46.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_46.setSpacing(6)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.radioButtonInterfaseSilodisaReplaneaciones = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaReplaneaciones.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaReplaneaciones.setObjectName("radioButtonInterfaseSilodisaReplaneaciones")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaReplaneaciones, 5, 0, 1, 1)
        self.radioButtonInterfaseSilodisaExtraordinarios = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaExtraordinarios.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaExtraordinarios.setObjectName("radioButtonInterfaseSilodisaExtraordinarios")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaExtraordinarios, 4, 0, 1, 1)
        self.radioButtonInterfaseSilodisaVacunas = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaVacunas.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaVacunas.setObjectName("radioButtonInterfaseSilodisaVacunas")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaVacunas, 3, 0, 1, 1)
        self.radioButtonInterfaseSilodisaSoportes = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaSoportes.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaSoportes.setObjectName("radioButtonInterfaseSilodisaSoportes")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaSoportes, 2, 0, 1, 1)
        self.radioButtonInterfaseSilodisaOrdinarios = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaOrdinarios.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaOrdinarios.setObjectName("radioButtonInterfaseSilodisaOrdinarios")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaOrdinarios, 1, 0, 1, 1)
        self.radioButtonInterfaseSilodisaTodos = QtWidgets.QRadioButton(self.frame_30)
        self.radioButtonInterfaseSilodisaTodos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonInterfaseSilodisaTodos.setChecked(True)
        self.radioButtonInterfaseSilodisaTodos.setObjectName("radioButtonInterfaseSilodisaTodos")
        self.gridLayout_46.addWidget(self.radioButtonInterfaseSilodisaTodos, 0, 0, 1, 1)
        self.gridLayout_50.addWidget(self.frame_30, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 124, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_50.addItem(spacerItem9, 4, 0, 1, 1)
        self.pushButtonInterfaseSilodisaGeneraPedido = QtWidgets.QPushButton(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonInterfaseSilodisaGeneraPedido.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonInterfaseSilodisaGeneraPedido.setFont(font)
        self.pushButtonInterfaseSilodisaGeneraPedido.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonInterfaseSilodisaGeneraPedido.setObjectName("pushButtonInterfaseSilodisaGeneraPedido")
        self.gridLayout_50.addWidget(self.pushButtonInterfaseSilodisaGeneraPedido, 5, 0, 1, 1)
        self.gridLayout_32.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_15)
        self.groupBox_6.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_48.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_48.setSpacing(6)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.listWidgetSilodisaPedidos = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidgetSilodisaPedidos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.listWidgetSilodisaPedidos.setObjectName("listWidgetSilodisaPedidos")
        self.gridLayout_48.addWidget(self.listWidgetSilodisaPedidos, 0, 0, 1, 1)
        self.gridLayout_32.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_59.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_59.setSpacing(6)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.groupBox_37 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_37.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_37.setObjectName("groupBox_37")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.groupBox_37)
        self.gridLayout_56.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_56.setSpacing(6)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.tableWidgetSilodisaAnadeDe = QtWidgets.QTableWidget(self.groupBox_37)
        self.tableWidgetSilodisaAnadeDe.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetSilodisaAnadeDe.setObjectName("tableWidgetSilodisaAnadeDe")
        self.tableWidgetSilodisaAnadeDe.setColumnCount(0)
        self.tableWidgetSilodisaAnadeDe.setRowCount(0)
        self.gridLayout_56.addWidget(self.tableWidgetSilodisaAnadeDe, 0, 0, 1, 1)
        self.tableWidgetSilodisaAnadeA = QtWidgets.QTableWidget(self.groupBox_37)
        self.tableWidgetSilodisaAnadeA.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetSilodisaAnadeA.setObjectName("tableWidgetSilodisaAnadeA")
        self.tableWidgetSilodisaAnadeA.setColumnCount(0)
        self.tableWidgetSilodisaAnadeA.setRowCount(0)
        self.gridLayout_56.addWidget(self.tableWidgetSilodisaAnadeA, 1, 0, 1, 1)
        self.pushButtonInterfasePochtecaGenera_3 = QtWidgets.QPushButton(self.groupBox_37)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonInterfasePochtecaGenera_3.setPalette(palette)
        self.pushButtonInterfasePochtecaGenera_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonInterfasePochtecaGenera_3.setObjectName("pushButtonInterfasePochtecaGenera_3")
        self.gridLayout_56.addWidget(self.pushButtonInterfasePochtecaGenera_3, 2, 0, 1, 1)
        self.gridLayout_59.addWidget(self.groupBox_37, 0, 0, 1, 1)
        self.groupBox_42 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_42.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_42.setObjectName("groupBox_42")
        self.gridLayout_78 = QtWidgets.QGridLayout(self.groupBox_42)
        self.gridLayout_78.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_78.setSpacing(6)
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.tableSilodisaLatLong = QtWidgets.QTableWidget(self.groupBox_42)
        self.tableSilodisaLatLong.setMinimumSize(QtCore.QSize(600, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableSilodisaLatLong.setPalette(palette)
        self.tableSilodisaLatLong.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableSilodisaLatLong.setObjectName("tableSilodisaLatLong")
        self.tableSilodisaLatLong.setColumnCount(0)
        self.tableSilodisaLatLong.setRowCount(0)
        self.gridLayout_78.addWidget(self.tableSilodisaLatLong, 0, 0, 1, 2)
        self.gridLayout_59.addWidget(self.groupBox_42, 0, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_16, "")
        self.gridLayout_79.addWidget(self.tabWidget_8, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_14, "")
        self.gridLayout_55.addWidget(self.tabWidget_7, 0, 0, 1, 1)
        self.labelStatusBarCEDI_4 = QtWidgets.QLabel(self.tabInterfase)
        self.labelStatusBarCEDI_4.setText("")
        self.labelStatusBarCEDI_4.setPixmap(QtGui.QPixmap(":/Img/arms_logo.png"))
        self.labelStatusBarCEDI_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusBarCEDI_4.setObjectName("labelStatusBarCEDI_4")
        self.gridLayout_55.addWidget(self.labelStatusBarCEDI_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabInterfase, "")
        self.tabGeneradorRutasPreferencias = QtWidgets.QWidget()
        self.tabGeneradorRutasPreferencias.setObjectName("tabGeneradorRutasPreferencias")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabGeneradorRutasPreferencias)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelStatusBarCEDI_8 = QtWidgets.QLabel(self.tabGeneradorRutasPreferencias)
        self.labelStatusBarCEDI_8.setText("")
        self.labelStatusBarCEDI_8.setPixmap(QtGui.QPixmap(":/Img/arms_logo.png"))
        self.labelStatusBarCEDI_8.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusBarCEDI_8.setObjectName("labelStatusBarCEDI_8")
        self.gridLayout_4.addWidget(self.labelStatusBarCEDI_8, 3, 0, 1, 2)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tabGeneradorRutasPreferencias)
        self.tabWidget_4.setStyleSheet("QTabBar::tab\n"
"{\n"
"border: 0px solid white;\n"
"background-color: rgb(41,180,115);\n"
"border-radius: 1px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"margin: 2px;\n"
"width: 150px;\n"
"height: 30px;\n"
"} \n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"background-color:  rgb(24,158,87);\n"
"} \n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"font:  14px;\n"
"}\n"
"")
        self.tabWidget_4.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_49.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_49.setSpacing(6)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_10.setMinimumSize(QtCore.QSize(900, 700))
        self.groupBox_10.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_39.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_39.setSpacing(6)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_11.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_30.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_30.setSpacing(6)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.tableWidgetDatosSSPedidos = QtWidgets.QTableWidget(self.groupBox_11)
        self.tableWidgetDatosSSPedidos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSPedidos.setObjectName("tableWidgetDatosSSPedidos")
        self.tableWidgetDatosSSPedidos.setColumnCount(0)
        self.tableWidgetDatosSSPedidos.setRowCount(0)
        self.gridLayout_30.addWidget(self.tableWidgetDatosSSPedidos, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_11, 0, 0, 1, 2)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_12.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_51.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_51.setSpacing(6)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.tableWidgetDatosSSVehiculos = QtWidgets.QTableWidget(self.groupBox_12)
        self.tableWidgetDatosSSVehiculos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSVehiculos.setObjectName("tableWidgetDatosSSVehiculos")
        self.tableWidgetDatosSSVehiculos.setColumnCount(0)
        self.tableWidgetDatosSSVehiculos.setRowCount(0)
        self.gridLayout_51.addWidget(self.tableWidgetDatosSSVehiculos, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_12, 0, 2, 1, 2)
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_13.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_52.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_52.setSpacing(6)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.tableWidgetDatosSSOperadores = QtWidgets.QTableWidget(self.groupBox_13)
        self.tableWidgetDatosSSOperadores.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSOperadores.setObjectName("tableWidgetDatosSSOperadores")
        self.tableWidgetDatosSSOperadores.setColumnCount(0)
        self.tableWidgetDatosSSOperadores.setRowCount(0)
        self.gridLayout_52.addWidget(self.tableWidgetDatosSSOperadores, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_13, 0, 4, 1, 2)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_15.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_65.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_65.setSpacing(6)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.tableWidgetDatosSSDestinos = QtWidgets.QTableWidget(self.groupBox_15)
        self.tableWidgetDatosSSDestinos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSDestinos.setObjectName("tableWidgetDatosSSDestinos")
        self.tableWidgetDatosSSDestinos.setColumnCount(0)
        self.tableWidgetDatosSSDestinos.setRowCount(0)
        self.gridLayout_65.addWidget(self.tableWidgetDatosSSDestinos, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_15, 1, 0, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_16.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_66 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_66.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_66.setSpacing(6)
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.tableWidgetDatosSSPreferencias = QtWidgets.QTableWidget(self.groupBox_16)
        self.tableWidgetDatosSSPreferencias.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSPreferencias.setObjectName("tableWidgetDatosSSPreferencias")
        self.tableWidgetDatosSSPreferencias.setColumnCount(0)
        self.tableWidgetDatosSSPreferencias.setRowCount(0)
        self.gridLayout_66.addWidget(self.tableWidgetDatosSSPreferencias, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_16, 1, 1, 1, 2)
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_17.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_69 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_69.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_69.setSpacing(6)
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.tableWidgetDatosSSTarifario = QtWidgets.QTableWidget(self.groupBox_17)
        self.tableWidgetDatosSSTarifario.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSTarifario.setObjectName("tableWidgetDatosSSTarifario")
        self.tableWidgetDatosSSTarifario.setColumnCount(0)
        self.tableWidgetDatosSSTarifario.setRowCount(0)
        self.gridLayout_69.addWidget(self.tableWidgetDatosSSTarifario, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_17, 1, 3, 1, 2)
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_18.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_58.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_58.setSpacing(6)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.tableWidgetDatosSSCompatibilidad = QtWidgets.QTableWidget(self.groupBox_18)
        self.tableWidgetDatosSSCompatibilidad.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDatosSSCompatibilidad.setObjectName("tableWidgetDatosSSCompatibilidad")
        self.tableWidgetDatosSSCompatibilidad.setColumnCount(0)
        self.tableWidgetDatosSSCompatibilidad.setRowCount(0)
        self.gridLayout_58.addWidget(self.tableWidgetDatosSSCompatibilidad, 0, 0, 1, 1)
        self.gridLayout_39.addWidget(self.groupBox_18, 1, 5, 1, 1)
        self.gridLayout_49.addWidget(self.groupBox_10, 0, 0, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(1014, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_49.addItem(spacerItem10, 1, 0, 1, 1)
        self.pushButtonGeneradorDatosAbreSeleccionados_2 = QtWidgets.QPushButton(self.tab_7)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonGeneradorDatosAbreSeleccionados_2.setPalette(palette)
        self.pushButtonGeneradorDatosAbreSeleccionados_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonGeneradorDatosAbreSeleccionados_2.setObjectName("pushButtonGeneradorDatosAbreSeleccionados_2")
        self.gridLayout_49.addWidget(self.pushButtonGeneradorDatosAbreSeleccionados_2, 1, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_17.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_17.setSpacing(6)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_19.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_14.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frameMotor = QtWidgets.QFrame(self.groupBox_19)
        self.frameMotor.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frameMotor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMotor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMotor.setObjectName("frameMotor")
        self.gridLayout_14.addWidget(self.frameMotor, 0, 0, 1, 2)
        self.gridLayout_17.addWidget(self.groupBox_19, 0, 0, 1, 1)
        self.frame_28 = QtWidgets.QFrame(self.tab_8)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_28.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_28)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumberCostoKg = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoKg.setFont(font)
        self.lcdNumberCostoKg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoKg.setSmallDecimalPoint(False)
        self.lcdNumberCostoKg.setDigitCount(8)
        self.lcdNumberCostoKg.setProperty("value", 1.23)
        self.lcdNumberCostoKg.setObjectName("lcdNumberCostoKg")
        self.gridLayout.addWidget(self.lcdNumberCostoKg, 1, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.frame_28)
        self.label_38.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 0, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.frame_28)
        self.label_43.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 0, 6, 1, 1)
        self.lcdNumberOcupacion = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberOcupacion.setFont(font)
        self.lcdNumberOcupacion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberOcupacion.setSmallDecimalPoint(False)
        self.lcdNumberOcupacion.setDigitCount(8)
        self.lcdNumberOcupacion.setProperty("value", 1.23)
        self.lcdNumberOcupacion.setObjectName("lcdNumberOcupacion")
        self.gridLayout.addWidget(self.lcdNumberOcupacion, 1, 6, 1, 1)
        self.lcdNumberViajes = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberViajes.setFont(font)
        self.lcdNumberViajes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberViajes.setSmallDecimalPoint(False)
        self.lcdNumberViajes.setDigitCount(8)
        self.lcdNumberViajes.setProperty("value", 1.23)
        self.lcdNumberViajes.setObjectName("lcdNumberViajes")
        self.gridLayout.addWidget(self.lcdNumberViajes, 1, 8, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.frame_28)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 0, 4, 1, 1)
        self.lcdNumberCostoPieza = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoPieza.setFont(font)
        self.lcdNumberCostoPieza.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoPieza.setSmallDecimalPoint(False)
        self.lcdNumberCostoPieza.setDigitCount(8)
        self.lcdNumberCostoPieza.setProperty("value", 1.23)
        self.lcdNumberCostoPieza.setObjectName("lcdNumberCostoPieza")
        self.gridLayout.addWidget(self.lcdNumberCostoPieza, 1, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.frame_28)
        self.label_40.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 0, 3, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.frame_28)
        self.label_39.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 0, 2, 1, 1)
        self.lcdNumberKm = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberKm.setFont(font)
        self.lcdNumberKm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberKm.setSmallDecimalPoint(False)
        self.lcdNumberKm.setDigitCount(8)
        self.lcdNumberKm.setProperty("value", 1.23)
        self.lcdNumberKm.setObjectName("lcdNumberKm")
        self.gridLayout.addWidget(self.lcdNumberKm, 1, 7, 1, 1)
        self.lcdNumberCostoM3 = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoM3.setFont(font)
        self.lcdNumberCostoM3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoM3.setSmallDecimalPoint(False)
        self.lcdNumberCostoM3.setDigitCount(8)
        self.lcdNumberCostoM3.setProperty("value", 1.23)
        self.lcdNumberCostoM3.setObjectName("lcdNumberCostoM3")
        self.gridLayout.addWidget(self.lcdNumberCostoM3, 1, 3, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.frame_28)
        self.label_45.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 0, 8, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.frame_28)
        self.label_44.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 0, 7, 1, 1)
        self.lcdNumberCostoTotal = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoTotal.setFont(font)
        self.lcdNumberCostoTotal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoTotal.setSmallDecimalPoint(False)
        self.lcdNumberCostoTotal.setDigitCount(8)
        self.lcdNumberCostoTotal.setProperty("value", 1.23)
        self.lcdNumberCostoTotal.setObjectName("lcdNumberCostoTotal")
        self.gridLayout.addWidget(self.lcdNumberCostoTotal, 1, 5, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_28)
        self.label_42.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 0, 5, 1, 1)
        self.lcdNumberCostoViaje = QtWidgets.QLCDNumber(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoViaje.setFont(font)
        self.lcdNumberCostoViaje.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoViaje.setSmallDecimalPoint(False)
        self.lcdNumberCostoViaje.setDigitCount(8)
        self.lcdNumberCostoViaje.setProperty("value", 1.23)
        self.lcdNumberCostoViaje.setObjectName("lcdNumberCostoViaje")
        self.gridLayout.addWidget(self.lcdNumberCostoViaje, 1, 4, 1, 1)
        self.pushButtonGeneradorMotorGuardar = QtWidgets.QPushButton(self.frame_28)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonGeneradorMotorGuardar.setPalette(palette)
        self.pushButtonGeneradorMotorGuardar.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonGeneradorMotorGuardar.setObjectName("pushButtonGeneradorMotorGuardar")
        self.gridLayout.addWidget(self.pushButtonGeneradorMotorGuardar, 0, 0, 2, 1)
        self.gridLayout_17.addWidget(self.frame_28, 1, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_8, "")
        self.tabGeneradorOtimizaAutomatico = QtWidgets.QWidget()
        self.tabGeneradorOtimizaAutomatico.setObjectName("tabGeneradorOtimizaAutomatico")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabGeneradorOtimizaAutomatico)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tabGeneradorOtimizaAutomatico)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_19.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_21 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_21.setMaximumSize(QtCore.QSize(900, 900))
        self.groupBox_21.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_25.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_25.setSpacing(6)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_21)
        self.groupBox_20.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox_20.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.groupBox_20.setTitle("")
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_20)
        self.label_16.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 7, 0, 1, 4)
        self.radioButtonOptimizaVacios = QtWidgets.QRadioButton(self.groupBox_20)
        self.radioButtonOptimizaVacios.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButtonOptimizaVacios.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaVacios.setChecked(True)
        self.radioButtonOptimizaVacios.setObjectName("radioButtonOptimizaVacios")
        self.gridLayout_2.addWidget(self.radioButtonOptimizaVacios, 11, 0, 1, 2)
        self.lineEditOptimizaAumentarValorMiles = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditOptimizaAumentarValorMiles.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditOptimizaAumentarValorMiles.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOptimizaAumentarValorMiles.setObjectName("lineEditOptimizaAumentarValorMiles")
        self.gridLayout_2.addWidget(self.lineEditOptimizaAumentarValorMiles, 4, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_20)
        self.label_14.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_20)
        self.label_15.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 0, 1, 4)
        self.pushButtonOptimizaAutoViajesMotor = QtWidgets.QPushButton(self.groupBox_20)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOptimizaAutoViajesMotor.setPalette(palette)
        self.pushButtonOptimizaAutoViajesMotor.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOptimizaAutoViajesMotor.setIcon(icon1)
        self.pushButtonOptimizaAutoViajesMotor.setObjectName("pushButtonOptimizaAutoViajesMotor")
        self.gridLayout_2.addWidget(self.pushButtonOptimizaAutoViajesMotor, 12, 3, 1, 2)
        self.lineEditOptimizaCercaniaMaxima = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditOptimizaCercaniaMaxima.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditOptimizaCercaniaMaxima.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOptimizaCercaniaMaxima.setObjectName("lineEditOptimizaCercaniaMaxima")
        self.gridLayout_2.addWidget(self.lineEditOptimizaCercaniaMaxima, 3, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_20)
        self.label_12.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_20)
        self.label_7.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 4)
        self.label_17 = QtWidgets.QLabel(self.groupBox_20)
        self.label_17.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 7, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_20)
        self.label_11.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 3)
        self.lineEditOptimizaAumentarCapacidad = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditOptimizaAumentarCapacidad.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditOptimizaAumentarCapacidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOptimizaAumentarCapacidad.setObjectName("lineEditOptimizaAumentarCapacidad")
        self.gridLayout_2.addWidget(self.lineEditOptimizaAumentarCapacidad, 6, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_20)
        self.label_8.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 10, 1, 1, 1)
        self.radioButtonOptimizaCercanos = QtWidgets.QRadioButton(self.groupBox_20)
        self.radioButtonOptimizaCercanos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaCercanos.setObjectName("radioButtonOptimizaCercanos")
        self.gridLayout_2.addWidget(self.radioButtonOptimizaCercanos, 11, 3, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.groupBox_20)
        self.label_10.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 5, 1, 1)
        self.checkBoxOptimizaIgnoraAcceso = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBoxOptimizaIgnoraAcceso.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxOptimizaIgnoraAcceso.setStyleSheet("QCheckBox {\n"
"background-color: rgba(0,0,0,0);\n"
"font: 14px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 1px;\n"
"margin-top: 0.01em;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}")
        self.checkBoxOptimizaIgnoraAcceso.setObjectName("checkBoxOptimizaIgnoraAcceso")
        self.gridLayout_2.addWidget(self.checkBoxOptimizaIgnoraAcceso, 8, 0, 1, 4)
        self.checkBoxOptimizaIgnoraCompatibilidad = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBoxOptimizaIgnoraCompatibilidad.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxOptimizaIgnoraCompatibilidad.setStyleSheet("QCheckBox {\n"
"background-color: rgba(0,0,0,0);\n"
"font: 14px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 1px;\n"
"margin-top: 0.01em;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}")
        self.checkBoxOptimizaIgnoraCompatibilidad.setObjectName("checkBoxOptimizaIgnoraCompatibilidad")
        self.gridLayout_2.addWidget(self.checkBoxOptimizaIgnoraCompatibilidad, 9, 0, 1, 3)
        self.label_18 = QtWidgets.QLabel(self.groupBox_20)
        self.label_18.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 6, 5, 1, 1)
        self.lineEditOptimizaAumentarPeso = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditOptimizaAumentarPeso.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditOptimizaAumentarPeso.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOptimizaAumentarPeso.setObjectName("lineEditOptimizaAumentarPeso")
        self.gridLayout_2.addWidget(self.lineEditOptimizaAumentarPeso, 7, 4, 1, 1)
        self.lineEditOptimizaAumentarVentanaMinutos = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditOptimizaAumentarVentanaMinutos.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditOptimizaAumentarVentanaMinutos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOptimizaAumentarVentanaMinutos.setObjectName("lineEditOptimizaAumentarVentanaMinutos")
        self.gridLayout_2.addWidget(self.lineEditOptimizaAumentarVentanaMinutos, 5, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_20)
        self.label_13.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.groupBox_20)
        self.label_9.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 3)
        self.lineEditGeneradorOptimizaViajesVacios = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEditGeneradorOptimizaViajesVacios.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditGeneradorOptimizaViajesVacios.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditGeneradorOptimizaViajesVacios.setObjectName("lineEditGeneradorOptimizaViajesVacios")
        self.gridLayout_2.addWidget(self.lineEditGeneradorOptimizaViajesVacios, 2, 4, 1, 1)
        self.pushButtonNuevoViajeV1_6 = QtWidgets.QPushButton(self.groupBox_20)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonNuevoViajeV1_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonNuevoViajeV1_6.setFont(font)
        self.pushButtonNuevoViajeV1_6.setToolTipDuration(3)
        self.pushButtonNuevoViajeV1_6.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNuevoViajeV1_6.setIcon(icon2)
        self.pushButtonNuevoViajeV1_6.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNuevoViajeV1_6.setFlat(False)
        self.pushButtonNuevoViajeV1_6.setObjectName("pushButtonNuevoViajeV1_6")
        self.gridLayout_2.addWidget(self.pushButtonNuevoViajeV1_6, 1, 5, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_20)
        self.comboBox_5.setStyleSheet("background-color: rgb(230,231,232);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 0, 1, 5)
        self.pushButtonOptimiza = QtWidgets.QPushButton(self.groupBox_20)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOptimiza.setPalette(palette)
        self.pushButtonOptimiza.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOptimiza.setObjectName("pushButtonOptimiza")
        self.gridLayout_2.addWidget(self.pushButtonOptimiza, 12, 0, 1, 2)
        self.gridLayout_25.addWidget(self.groupBox_20, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_21, 0, 0, 1, 1)
        self.groupBox_35 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_35.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_35.setObjectName("groupBox_35")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_35)
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.tableWidgetOptimizaResultados = QtWidgets.QTableWidget(self.groupBox_35)
        self.tableWidgetOptimizaResultados.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetOptimizaResultados.setObjectName("tableWidgetOptimizaResultados")
        self.tableWidgetOptimizaResultados.setColumnCount(0)
        self.tableWidgetOptimizaResultados.setRowCount(0)
        self.gridLayout_12.addWidget(self.tableWidgetOptimizaResultados, 0, 0, 1, 2)
        spacerItem13 = QtWidgets.QSpacerItem(248, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem13, 1, 0, 2, 1)
        self.lineEditSSResultados_2 = QtWidgets.QLineEdit(self.groupBox_35)
        self.lineEditSSResultados_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEditSSResultados_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditSSResultados_2.setInputMask("")
        self.lineEditSSResultados_2.setObjectName("lineEditSSResultados_2")
        self.gridLayout_12.addWidget(self.lineEditSSResultados_2, 1, 1, 1, 1)
        self.pushButtonOptimizaAutoGuarda = QtWidgets.QPushButton(self.groupBox_35)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOptimizaAutoGuarda.setPalette(palette)
        self.pushButtonOptimizaAutoGuarda.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOptimizaAutoGuarda.setObjectName("pushButtonOptimizaAutoGuarda")
        self.gridLayout_12.addWidget(self.pushButtonOptimizaAutoGuarda, 2, 1, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_35, 0, 1, 1, 1)
        self.frame_42 = QtWidgets.QFrame(self.tab_3)
        self.frame_42.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_42.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.0em;\n"
"font: 16px;\n"
"color:  rgb(160, 232, 105);\n"
"border: 0px solid white;\n"
"padding: 1;\n"
"")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.frame_42)
        self.gridLayout_41.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_41.setSpacing(6)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.lcdNumberCostoKgAuto = QtWidgets.QLCDNumber(self.frame_42)
        self.lcdNumberCostoKgAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoKgAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoKgAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoKgAuto.setDigitCount(8)
        self.lcdNumberCostoKgAuto.setProperty("value", 1.23)
        self.lcdNumberCostoKgAuto.setObjectName("lcdNumberCostoKgAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoKgAuto, 1, 0, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.frame_42)
        self.label_111.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.gridLayout_41.addWidget(self.label_111, 0, 3, 1, 1)
        self.lcdNumberCostoM3DifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoM3DifAuto.setFont(font)
        self.lcdNumberCostoM3DifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoM3DifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoM3DifAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoM3DifAuto.setDigitCount(8)
        self.lcdNumberCostoM3DifAuto.setProperty("value", 1.23)
        self.lcdNumberCostoM3DifAuto.setObjectName("lcdNumberCostoM3DifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoM3DifAuto, 2, 2, 1, 1)
        self.lcdNumberCostoViajeDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoViajeDifAuto.setFont(font)
        self.lcdNumberCostoViajeDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoViajeDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoViajeDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoViajeDifAuto.setDigitCount(8)
        self.lcdNumberCostoViajeDifAuto.setProperty("value", 1.23)
        self.lcdNumberCostoViajeDifAuto.setObjectName("lcdNumberCostoViajeDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoViajeDifAuto, 2, 3, 1, 1)
        self.lcdNumberOcupacionAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberOcupacionAuto.setFont(font)
        self.lcdNumberOcupacionAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberOcupacionAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberOcupacionAuto.setSmallDecimalPoint(False)
        self.lcdNumberOcupacionAuto.setDigitCount(8)
        self.lcdNumberOcupacionAuto.setProperty("value", 1.23)
        self.lcdNumberOcupacionAuto.setObjectName("lcdNumberOcupacionAuto")
        self.gridLayout_41.addWidget(self.lcdNumberOcupacionAuto, 1, 5, 1, 1)
        self.lcdNumberKmAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberKmAuto.setFont(font)
        self.lcdNumberKmAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberKmAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberKmAuto.setSmallDecimalPoint(False)
        self.lcdNumberKmAuto.setDigitCount(8)
        self.lcdNumberKmAuto.setProperty("value", 1.23)
        self.lcdNumberKmAuto.setObjectName("lcdNumberKmAuto")
        self.gridLayout_41.addWidget(self.lcdNumberKmAuto, 1, 6, 1, 1)
        self.lcdNumberViajesAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberViajesAuto.setFont(font)
        self.lcdNumberViajesAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberViajesAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberViajesAuto.setSmallDecimalPoint(False)
        self.lcdNumberViajesAuto.setDigitCount(8)
        self.lcdNumberViajesAuto.setProperty("value", 1.23)
        self.lcdNumberViajesAuto.setObjectName("lcdNumberViajesAuto")
        self.gridLayout_41.addWidget(self.lcdNumberViajesAuto, 1, 7, 1, 1)
        self.lcdNumberCostoKgDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoKgDifAuto.setFont(font)
        self.lcdNumberCostoKgDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoKgDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoKgDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoKgDifAuto.setDigitCount(8)
        self.lcdNumberCostoKgDifAuto.setProperty("value", 1.23)
        self.lcdNumberCostoKgDifAuto.setObjectName("lcdNumberCostoKgDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoKgDifAuto, 2, 0, 1, 1)
        self.lcdNumberCostoPiezaDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoPiezaDifAuto.setFont(font)
        self.lcdNumberCostoPiezaDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoPiezaDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoPiezaDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoPiezaDifAuto.setDigitCount(8)
        self.lcdNumberCostoPiezaDifAuto.setProperty("value", 1.23)
        self.lcdNumberCostoPiezaDifAuto.setObjectName("lcdNumberCostoPiezaDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoPiezaDifAuto, 2, 1, 1, 1)
        self.lcdNumberCostoTotalDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoTotalDifAuto.setFont(font)
        self.lcdNumberCostoTotalDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoTotalDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoTotalDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoTotalDifAuto.setDigitCount(8)
        self.lcdNumberCostoTotalDifAuto.setProperty("value", 1.23)
        self.lcdNumberCostoTotalDifAuto.setObjectName("lcdNumberCostoTotalDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoTotalDifAuto, 2, 4, 1, 1)
        self.lcdNumberKmDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberKmDifAuto.setFont(font)
        self.lcdNumberKmDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberKmDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberKmDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberKmDifAuto.setDigitCount(8)
        self.lcdNumberKmDifAuto.setProperty("value", 1.23)
        self.lcdNumberKmDifAuto.setObjectName("lcdNumberKmDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberKmDifAuto, 2, 6, 1, 1)
        self.lcdNumberOcupacionDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberOcupacionDifAuto.setFont(font)
        self.lcdNumberOcupacionDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberOcupacionDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberOcupacionDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberOcupacionDifAuto.setDigitCount(8)
        self.lcdNumberOcupacionDifAuto.setProperty("value", 1.23)
        self.lcdNumberOcupacionDifAuto.setObjectName("lcdNumberOcupacionDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberOcupacionDifAuto, 2, 5, 1, 1)
        self.lcdNumberCostoM3Auto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoM3Auto.setFont(font)
        self.lcdNumberCostoM3Auto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoM3Auto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoM3Auto.setSmallDecimalPoint(False)
        self.lcdNumberCostoM3Auto.setDigitCount(8)
        self.lcdNumberCostoM3Auto.setProperty("value", 1.23)
        self.lcdNumberCostoM3Auto.setObjectName("lcdNumberCostoM3Auto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoM3Auto, 1, 2, 1, 1)
        self.label_113 = QtWidgets.QLabel(self.frame_42)
        self.label_113.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.gridLayout_41.addWidget(self.label_113, 0, 5, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.frame_42)
        self.label_112.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.gridLayout_41.addWidget(self.label_112, 0, 4, 1, 1)
        self.lcdNumberCostoViajeAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoViajeAuto.setFont(font)
        self.lcdNumberCostoViajeAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoViajeAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoViajeAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoViajeAuto.setDigitCount(8)
        self.lcdNumberCostoViajeAuto.setProperty("value", 1.23)
        self.lcdNumberCostoViajeAuto.setObjectName("lcdNumberCostoViajeAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoViajeAuto, 1, 3, 1, 1)
        self.lcdNumberCostoTotalAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoTotalAuto.setFont(font)
        self.lcdNumberCostoTotalAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoTotalAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoTotalAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoTotalAuto.setDigitCount(8)
        self.lcdNumberCostoTotalAuto.setProperty("value", 1.23)
        self.lcdNumberCostoTotalAuto.setObjectName("lcdNumberCostoTotalAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoTotalAuto, 1, 4, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.frame_42)
        self.label_71.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.gridLayout_41.addWidget(self.label_71, 0, 2, 1, 1)
        self.lcdNumberViajesDifAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberViajesDifAuto.setFont(font)
        self.lcdNumberViajesDifAuto.setStyleSheet("background-color: rgba(160, 232, 105,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberViajesDifAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberViajesDifAuto.setSmallDecimalPoint(False)
        self.lcdNumberViajesDifAuto.setDigitCount(8)
        self.lcdNumberViajesDifAuto.setProperty("value", 1.23)
        self.lcdNumberViajesDifAuto.setObjectName("lcdNumberViajesDifAuto")
        self.gridLayout_41.addWidget(self.lcdNumberViajesDifAuto, 2, 7, 1, 1)
        self.lcdNumberCostoPiezaAuto = QtWidgets.QLCDNumber(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoPiezaAuto.setFont(font)
        self.lcdNumberCostoPiezaAuto.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoPiezaAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoPiezaAuto.setSmallDecimalPoint(False)
        self.lcdNumberCostoPiezaAuto.setDigitCount(8)
        self.lcdNumberCostoPiezaAuto.setProperty("value", 1.23)
        self.lcdNumberCostoPiezaAuto.setObjectName("lcdNumberCostoPiezaAuto")
        self.gridLayout_41.addWidget(self.lcdNumberCostoPiezaAuto, 1, 1, 1, 1)
        self.label_115 = QtWidgets.QLabel(self.frame_42)
        self.label_115.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_115.setAlignment(QtCore.Qt.AlignCenter)
        self.label_115.setObjectName("label_115")
        self.gridLayout_41.addWidget(self.label_115, 0, 7, 1, 1)
        self.label_114 = QtWidgets.QLabel(self.frame_42)
        self.label_114.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_114.setAlignment(QtCore.Qt.AlignCenter)
        self.label_114.setObjectName("label_114")
        self.gridLayout_41.addWidget(self.label_114, 0, 6, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.frame_42)
        self.label_55.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout_41.addWidget(self.label_55, 0, 0, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.frame_42)
        self.label_70.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.gridLayout_41.addWidget(self.label_70, 0, 1, 1, 1)
        self.gridLayout_19.addWidget(self.frame_42, 1, 0, 1, 2)
        self.tabWidget_6.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_24.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_24.setSpacing(6)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_22.setMaximumSize(QtCore.QSize(700, 16777215))
        self.groupBox_22.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_20.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_20.setSpacing(6)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_22)
        self.comboBox_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_20.addWidget(self.comboBox_2, 0, 0, 1, 2)
        self.pushButtonNuevoViajeV1_3 = QtWidgets.QPushButton(self.groupBox_22)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonNuevoViajeV1_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonNuevoViajeV1_3.setFont(font)
        self.pushButtonNuevoViajeV1_3.setToolTipDuration(3)
        self.pushButtonNuevoViajeV1_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonNuevoViajeV1_3.setIcon(icon2)
        self.pushButtonNuevoViajeV1_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNuevoViajeV1_3.setFlat(False)
        self.pushButtonNuevoViajeV1_3.setObjectName("pushButtonNuevoViajeV1_3")
        self.gridLayout_20.addWidget(self.pushButtonNuevoViajeV1_3, 0, 2, 1, 2)
        self.tableWidgetOptimizaManualResultados = QtWidgets.QTableWidget(self.groupBox_22)
        self.tableWidgetOptimizaManualResultados.setMinimumSize(QtCore.QSize(600, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 98, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidgetOptimizaManualResultados.setPalette(palette)
        self.tableWidgetOptimizaManualResultados.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetOptimizaManualResultados.setObjectName("tableWidgetOptimizaManualResultados")
        self.tableWidgetOptimizaManualResultados.setColumnCount(0)
        self.tableWidgetOptimizaManualResultados.setRowCount(0)
        self.gridLayout_20.addWidget(self.tableWidgetOptimizaManualResultados, 1, 0, 1, 4)
        self.radioButtonOptimizaManualViajes = QtWidgets.QRadioButton(self.groupBox_22)
        self.radioButtonOptimizaManualViajes.setToolTipDuration(3)
        self.radioButtonOptimizaManualViajes.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualViajes.setChecked(True)
        self.radioButtonOptimizaManualViajes.setObjectName("radioButtonOptimizaManualViajes")
        self.gridLayout_20.addWidget(self.radioButtonOptimizaManualViajes, 2, 0, 1, 1)
        self.radioButtonOptimizaManualDestinos = QtWidgets.QRadioButton(self.groupBox_22)
        self.radioButtonOptimizaManualDestinos.setToolTipDuration(3)
        self.radioButtonOptimizaManualDestinos.setStatusTip("")
        self.radioButtonOptimizaManualDestinos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualDestinos.setObjectName("radioButtonOptimizaManualDestinos")
        self.gridLayout_20.addWidget(self.radioButtonOptimizaManualDestinos, 2, 1, 1, 1)
        self.pushButtonOptimizaManualRecargaOptimizado = QtWidgets.QPushButton(self.groupBox_22)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOptimizaManualRecargaOptimizado.setPalette(palette)
        self.pushButtonOptimizaManualRecargaOptimizado.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOptimizaManualRecargaOptimizado.setObjectName("pushButtonOptimizaManualRecargaOptimizado")
        self.gridLayout_20.addWidget(self.pushButtonOptimizaManualRecargaOptimizado, 4, 0, 1, 1)
        self.pushButtonOptimizaManualGuardaResultados = QtWidgets.QPushButton(self.groupBox_22)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOptimizaManualGuardaResultados.setPalette(palette)
        self.pushButtonOptimizaManualGuardaResultados.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOptimizaManualGuardaResultados.setObjectName("pushButtonOptimizaManualGuardaResultados")
        self.gridLayout_20.addWidget(self.pushButtonOptimizaManualGuardaResultados, 4, 1, 1, 2)
        self.pushButtonRecalculaSeleccionados = QtWidgets.QPushButton(self.groupBox_22)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonRecalculaSeleccionados.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonRecalculaSeleccionados.setFont(font)
        self.pushButtonRecalculaSeleccionados.setToolTipDuration(3)
        self.pushButtonRecalculaSeleccionados.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRecalculaSeleccionados.setIcon(icon3)
        self.pushButtonRecalculaSeleccionados.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonRecalculaSeleccionados.setFlat(False)
        self.pushButtonRecalculaSeleccionados.setObjectName("pushButtonRecalculaSeleccionados")
        self.gridLayout_20.addWidget(self.pushButtonRecalculaSeleccionados, 4, 3, 1, 1)
        self.frame_41 = QtWidgets.QFrame(self.groupBox_22)
        self.frame_41.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_41.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.0em;\n"
"font: 16px;\n"
"color:  rgb(160, 232, 105);\n"
"border: 0px solid white;\n"
"padding: 1;\n"
"")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_41)
        self.gridLayout_18.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_18.setSpacing(6)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_54 = QtWidgets.QLabel(self.frame_41)
        self.label_54.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.gridLayout_18.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.frame_41)
        self.label_63.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout_18.addWidget(self.label_63, 0, 1, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.frame_41)
        self.label_64.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_18.addWidget(self.label_64, 0, 2, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.frame_41)
        self.label_65.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.gridLayout_18.addWidget(self.label_65, 0, 3, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.frame_41)
        self.label_66.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_18.addWidget(self.label_66, 0, 4, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.frame_41)
        self.label_67.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.gridLayout_18.addWidget(self.label_67, 0, 5, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.frame_41)
        self.label_68.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.gridLayout_18.addWidget(self.label_68, 0, 6, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.frame_41)
        self.label_69.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.gridLayout_18.addWidget(self.label_69, 0, 7, 1, 1)
        self.lcdNumberCostoKgManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoKgManual.setFont(font)
        self.lcdNumberCostoKgManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.0em;\n"
"margin-top: 0.0em;\n"
"")
        self.lcdNumberCostoKgManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoKgManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoKgManual.setDigitCount(8)
        self.lcdNumberCostoKgManual.setProperty("value", 0.0)
        self.lcdNumberCostoKgManual.setObjectName("lcdNumberCostoKgManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoKgManual, 1, 0, 1, 1)
        self.lcdNumberCostoPiezaManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoPiezaManual.setFont(font)
        self.lcdNumberCostoPiezaManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoPiezaManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoPiezaManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoPiezaManual.setDigitCount(8)
        self.lcdNumberCostoPiezaManual.setProperty("value", 0.0)
        self.lcdNumberCostoPiezaManual.setObjectName("lcdNumberCostoPiezaManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoPiezaManual, 1, 1, 1, 1)
        self.lcdNumberCostoM3Manual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoM3Manual.setFont(font)
        self.lcdNumberCostoM3Manual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoM3Manual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoM3Manual.setSmallDecimalPoint(False)
        self.lcdNumberCostoM3Manual.setDigitCount(8)
        self.lcdNumberCostoM3Manual.setProperty("value", 0.0)
        self.lcdNumberCostoM3Manual.setObjectName("lcdNumberCostoM3Manual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoM3Manual, 1, 2, 1, 1)
        self.lcdNumberCostoViajeManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoViajeManual.setFont(font)
        self.lcdNumberCostoViajeManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoViajeManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoViajeManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoViajeManual.setDigitCount(8)
        self.lcdNumberCostoViajeManual.setProperty("value", 0.0)
        self.lcdNumberCostoViajeManual.setObjectName("lcdNumberCostoViajeManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoViajeManual, 1, 3, 1, 1)
        self.lcdNumberCostoTotalManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoTotalManual.setFont(font)
        self.lcdNumberCostoTotalManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoTotalManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoTotalManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoTotalManual.setDigitCount(8)
        self.lcdNumberCostoTotalManual.setProperty("value", 0.0)
        self.lcdNumberCostoTotalManual.setObjectName("lcdNumberCostoTotalManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoTotalManual, 1, 4, 1, 1)
        self.lcdNumberOcupacionManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberOcupacionManual.setFont(font)
        self.lcdNumberOcupacionManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberOcupacionManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberOcupacionManual.setSmallDecimalPoint(False)
        self.lcdNumberOcupacionManual.setDigitCount(8)
        self.lcdNumberOcupacionManual.setProperty("value", 0.0)
        self.lcdNumberOcupacionManual.setObjectName("lcdNumberOcupacionManual")
        self.gridLayout_18.addWidget(self.lcdNumberOcupacionManual, 1, 5, 1, 1)
        self.lcdNumberKmManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberKmManual.setFont(font)
        self.lcdNumberKmManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberKmManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberKmManual.setSmallDecimalPoint(False)
        self.lcdNumberKmManual.setDigitCount(8)
        self.lcdNumberKmManual.setProperty("value", 0.0)
        self.lcdNumberKmManual.setObjectName("lcdNumberKmManual")
        self.gridLayout_18.addWidget(self.lcdNumberKmManual, 1, 6, 1, 1)
        self.lcdNumberViajesManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberViajesManual.setFont(font)
        self.lcdNumberViajesManual.setStyleSheet("background-color: rgba(31, 170, 94,0);\n"
"\n"
"color: rgb(255,255,255);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 0px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberViajesManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberViajesManual.setSmallDecimalPoint(False)
        self.lcdNumberViajesManual.setDigitCount(8)
        self.lcdNumberViajesManual.setProperty("value", 0.0)
        self.lcdNumberViajesManual.setObjectName("lcdNumberViajesManual")
        self.gridLayout_18.addWidget(self.lcdNumberViajesManual, 1, 7, 1, 1)
        self.lcdNumberCostoKgDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoKgDifManual.setFont(font)
        self.lcdNumberCostoKgDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoKgDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoKgDifManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoKgDifManual.setDigitCount(8)
        self.lcdNumberCostoKgDifManual.setProperty("value", 0.0)
        self.lcdNumberCostoKgDifManual.setObjectName("lcdNumberCostoKgDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoKgDifManual, 2, 0, 1, 1)
        self.lcdNumberCostoPiezaDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoPiezaDifManual.setFont(font)
        self.lcdNumberCostoPiezaDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoPiezaDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoPiezaDifManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoPiezaDifManual.setDigitCount(8)
        self.lcdNumberCostoPiezaDifManual.setProperty("value", 0.0)
        self.lcdNumberCostoPiezaDifManual.setObjectName("lcdNumberCostoPiezaDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoPiezaDifManual, 2, 1, 1, 1)
        self.lcdNumberCostoM3DifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoM3DifManual.setFont(font)
        self.lcdNumberCostoM3DifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoM3DifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoM3DifManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoM3DifManual.setDigitCount(8)
        self.lcdNumberCostoM3DifManual.setProperty("value", 0.0)
        self.lcdNumberCostoM3DifManual.setObjectName("lcdNumberCostoM3DifManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoM3DifManual, 2, 2, 1, 1)
        self.lcdNumberCostoViajeDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoViajeDifManual.setFont(font)
        self.lcdNumberCostoViajeDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoViajeDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoViajeDifManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoViajeDifManual.setDigitCount(8)
        self.lcdNumberCostoViajeDifManual.setProperty("value", 0.0)
        self.lcdNumberCostoViajeDifManual.setObjectName("lcdNumberCostoViajeDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoViajeDifManual, 2, 3, 1, 1)
        self.lcdNumberCostoTotalDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberCostoTotalDifManual.setFont(font)
        self.lcdNumberCostoTotalDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberCostoTotalDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberCostoTotalDifManual.setSmallDecimalPoint(False)
        self.lcdNumberCostoTotalDifManual.setDigitCount(8)
        self.lcdNumberCostoTotalDifManual.setProperty("value", 0.0)
        self.lcdNumberCostoTotalDifManual.setObjectName("lcdNumberCostoTotalDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberCostoTotalDifManual, 2, 4, 1, 1)
        self.lcdNumberOcupacionDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberOcupacionDifManual.setFont(font)
        self.lcdNumberOcupacionDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberOcupacionDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberOcupacionDifManual.setSmallDecimalPoint(False)
        self.lcdNumberOcupacionDifManual.setDigitCount(8)
        self.lcdNumberOcupacionDifManual.setProperty("value", 0.0)
        self.lcdNumberOcupacionDifManual.setObjectName("lcdNumberOcupacionDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberOcupacionDifManual, 2, 5, 1, 1)
        self.lcdNumberKmDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberKmDifManual.setFont(font)
        self.lcdNumberKmDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberKmDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberKmDifManual.setSmallDecimalPoint(False)
        self.lcdNumberKmDifManual.setDigitCount(8)
        self.lcdNumberKmDifManual.setProperty("value", 0.0)
        self.lcdNumberKmDifManual.setObjectName("lcdNumberKmDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberKmDifManual, 2, 6, 1, 1)
        self.lcdNumberViajesDifManual = QtWidgets.QLCDNumber(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberViajesDifManual.setFont(font)
        self.lcdNumberViajesDifManual.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberViajesDifManual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberViajesDifManual.setSmallDecimalPoint(False)
        self.lcdNumberViajesDifManual.setDigitCount(8)
        self.lcdNumberViajesDifManual.setProperty("value", 0.0)
        self.lcdNumberViajesDifManual.setObjectName("lcdNumberViajesDifManual")
        self.gridLayout_18.addWidget(self.lcdNumberViajesDifManual, 2, 7, 1, 1)
        self.gridLayout_20.addWidget(self.frame_41, 5, 0, 1, 4)
        self.lineEditSSResultados_3 = QtWidgets.QLineEdit(self.groupBox_22)
        self.lineEditSSResultados_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEditSSResultados_3.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditSSResultados_3.setInputMask("")
        self.lineEditSSResultados_3.setObjectName("lineEditSSResultados_3")
        self.gridLayout_20.addWidget(self.lineEditSSResultados_3, 3, 0, 1, 4)
        self.radioButtonOptimizaManualPedidos = QtWidgets.QRadioButton(self.groupBox_22)
        self.radioButtonOptimizaManualPedidos.setToolTipDuration(3)
        self.radioButtonOptimizaManualPedidos.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualPedidos.setObjectName("radioButtonOptimizaManualPedidos")
        self.gridLayout_20.addWidget(self.radioButtonOptimizaManualPedidos, 2, 2, 1, 1)
        self.gridLayout_24.addWidget(self.groupBox_22, 0, 0, 3, 1)
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_23.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_23.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_21.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_21.setSpacing(6)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.labelOptimizaManualV1Header = QtWidgets.QLabel(self.groupBox_23)
        self.labelOptimizaManualV1Header.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelOptimizaManualV1Header.setObjectName("labelOptimizaManualV1Header")
        self.gridLayout_21.addWidget(self.labelOptimizaManualV1Header, 0, 0, 1, 5)
        self.tableWidgetOptimizaManualV1 = QtWidgets.QTableWidget(self.groupBox_23)
        self.tableWidgetOptimizaManualV1.setMinimumSize(QtCore.QSize(600, 230))
        self.tableWidgetOptimizaManualV1.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetOptimizaManualV1.setObjectName("tableWidgetOptimizaManualV1")
        self.tableWidgetOptimizaManualV1.setColumnCount(0)
        self.tableWidgetOptimizaManualV1.setRowCount(0)
        self.gridLayout_21.addWidget(self.tableWidgetOptimizaManualV1, 1, 0, 5, 5)
        self.lcdNumberPesoSobranteV1 = QtWidgets.QLCDNumber(self.groupBox_23)
        self.lcdNumberPesoSobranteV1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberPesoSobranteV1.setFont(font)
        self.lcdNumberPesoSobranteV1.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberPesoSobranteV1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberPesoSobranteV1.setSmallDecimalPoint(False)
        self.lcdNumberPesoSobranteV1.setDigitCount(7)
        self.lcdNumberPesoSobranteV1.setProperty("value", 0.0)
        self.lcdNumberPesoSobranteV1.setObjectName("lcdNumberPesoSobranteV1")
        self.gridLayout_21.addWidget(self.lcdNumberPesoSobranteV1, 1, 5, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.groupBox_23)
        self.label_56.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.gridLayout_21.addWidget(self.label_56, 1, 6, 1, 1)
        self.lcdNumberVolumenSobranteV1 = QtWidgets.QLCDNumber(self.groupBox_23)
        self.lcdNumberVolumenSobranteV1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberVolumenSobranteV1.setFont(font)
        self.lcdNumberVolumenSobranteV1.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberVolumenSobranteV1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberVolumenSobranteV1.setSmallDecimalPoint(False)
        self.lcdNumberVolumenSobranteV1.setDigitCount(7)
        self.lcdNumberVolumenSobranteV1.setProperty("value", 0.0)
        self.lcdNumberVolumenSobranteV1.setObjectName("lcdNumberVolumenSobranteV1")
        self.gridLayout_21.addWidget(self.lcdNumberVolumenSobranteV1, 2, 5, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.groupBox_23)
        self.label_57.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_57.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout_21.addWidget(self.label_57, 2, 6, 1, 1)
        self.lcdNumberValorSobranteV1 = QtWidgets.QLCDNumber(self.groupBox_23)
        self.lcdNumberValorSobranteV1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberValorSobranteV1.setFont(font)
        self.lcdNumberValorSobranteV1.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberValorSobranteV1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberValorSobranteV1.setSmallDecimalPoint(False)
        self.lcdNumberValorSobranteV1.setDigitCount(7)
        self.lcdNumberValorSobranteV1.setProperty("value", 0.0)
        self.lcdNumberValorSobranteV1.setObjectName("lcdNumberValorSobranteV1")
        self.gridLayout_21.addWidget(self.lcdNumberValorSobranteV1, 3, 5, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.groupBox_23)
        self.label_58.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_58.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.gridLayout_21.addWidget(self.label_58, 3, 6, 1, 1)
        self.lcdNumberTiempoSobranteV1 = QtWidgets.QLCDNumber(self.groupBox_23)
        self.lcdNumberTiempoSobranteV1.setMinimumSize(QtCore.QSize(0, 20))
        self.lcdNumberTiempoSobranteV1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberTiempoSobranteV1.setFont(font)
        self.lcdNumberTiempoSobranteV1.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberTiempoSobranteV1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberTiempoSobranteV1.setSmallDecimalPoint(False)
        self.lcdNumberTiempoSobranteV1.setDigitCount(7)
        self.lcdNumberTiempoSobranteV1.setProperty("value", 0.0)
        self.lcdNumberTiempoSobranteV1.setObjectName("lcdNumberTiempoSobranteV1")
        self.gridLayout_21.addWidget(self.lcdNumberTiempoSobranteV1, 4, 5, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.groupBox_23)
        self.label_59.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_59.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.gridLayout_21.addWidget(self.label_59, 4, 6, 1, 1)
        self.labelCumpleAccesoV1 = QtWidgets.QLabel(self.groupBox_23)
        self.labelCumpleAccesoV1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelCumpleAccesoV1.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelCumpleAccesoV1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCumpleAccesoV1.setObjectName("labelCumpleAccesoV1")
        self.gridLayout_21.addWidget(self.labelCumpleAccesoV1, 5, 5, 1, 1)
        self.labelCumpleAccesoV1_2 = QtWidgets.QLabel(self.groupBox_23)
        self.labelCumpleAccesoV1_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelCumpleAccesoV1_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelCumpleAccesoV1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCumpleAccesoV1_2.setObjectName("labelCumpleAccesoV1_2")
        self.gridLayout_21.addWidget(self.labelCumpleAccesoV1_2, 5, 6, 1, 1)
        self.lineEditNvoViajeValor = QtWidgets.QLineEdit(self.groupBox_23)
        self.lineEditNvoViajeValor.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeValor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeValor.setObjectName("lineEditNvoViajeValor")
        self.gridLayout_21.addWidget(self.lineEditNvoViajeValor, 6, 0, 1, 1)
        self.lineEditNvoViajeM3 = QtWidgets.QLineEdit(self.groupBox_23)
        self.lineEditNvoViajeM3.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeM3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeM3.setObjectName("lineEditNvoViajeM3")
        self.gridLayout_21.addWidget(self.lineEditNvoViajeM3, 6, 1, 1, 1)
        self.lineEditNvoViajeKg = QtWidgets.QLineEdit(self.groupBox_23)
        self.lineEditNvoViajeKg.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeKg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeKg.setObjectName("lineEditNvoViajeKg")
        self.gridLayout_21.addWidget(self.lineEditNvoViajeKg, 6, 2, 1, 1)
        self.pushButtonNuevoViajeV1 = QtWidgets.QPushButton(self.groupBox_23)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonNuevoViajeV1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonNuevoViajeV1.setFont(font)
        self.pushButtonNuevoViajeV1.setToolTipDuration(3)
        self.pushButtonNuevoViajeV1.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonNuevoViajeV1.setIcon(icon2)
        self.pushButtonNuevoViajeV1.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNuevoViajeV1.setFlat(False)
        self.pushButtonNuevoViajeV1.setObjectName("pushButtonNuevoViajeV1")
        self.gridLayout_21.addWidget(self.pushButtonNuevoViajeV1, 6, 3, 1, 1)
        self.pushButtonBorraV1 = QtWidgets.QPushButton(self.groupBox_23)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonBorraV1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonBorraV1.setFont(font)
        self.pushButtonBorraV1.setToolTipDuration(3)
        self.pushButtonBorraV1.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBorraV1.setIcon(icon4)
        self.pushButtonBorraV1.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonBorraV1.setFlat(False)
        self.pushButtonBorraV1.setObjectName("pushButtonBorraV1")
        self.gridLayout_21.addWidget(self.pushButtonBorraV1, 6, 4, 1, 1)
        self.pushButtonRecalculaV1 = QtWidgets.QPushButton(self.groupBox_23)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonRecalculaV1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonRecalculaV1.setFont(font)
        self.pushButtonRecalculaV1.setToolTipDuration(3)
        self.pushButtonRecalculaV1.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonRecalculaV1.setIcon(icon1)
        self.pushButtonRecalculaV1.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonRecalculaV1.setFlat(False)
        self.pushButtonRecalculaV1.setObjectName("pushButtonRecalculaV1")
        self.gridLayout_21.addWidget(self.pushButtonRecalculaV1, 6, 5, 1, 1)
        self.pushButtonOtimizaV1 = QtWidgets.QPushButton(self.groupBox_23)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOtimizaV1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonOtimizaV1.setFont(font)
        self.pushButtonOtimizaV1.setToolTipDuration(3)
        self.pushButtonOtimizaV1.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOtimizaV1.setIcon(icon3)
        self.pushButtonOtimizaV1.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonOtimizaV1.setFlat(False)
        self.pushButtonOtimizaV1.setObjectName("pushButtonOtimizaV1")
        self.gridLayout_21.addWidget(self.pushButtonOtimizaV1, 6, 6, 1, 1)
        self.labelCumpleAccesoV1_2.raise_()
        self.lineEditNvoViajeValor.raise_()
        self.lcdNumberVolumenSobranteV1.raise_()
        self.tableWidgetOptimizaManualV1.raise_()
        self.lcdNumberValorSobranteV1.raise_()
        self.lcdNumberPesoSobranteV1.raise_()
        self.pushButtonBorraV1.raise_()
        self.pushButtonOtimizaV1.raise_()
        self.label_56.raise_()
        self.pushButtonRecalculaV1.raise_()
        self.lcdNumberTiempoSobranteV1.raise_()
        self.label_59.raise_()
        self.labelOptimizaManualV1Header.raise_()
        self.lineEditNvoViajeM3.raise_()
        self.lineEditNvoViajeKg.raise_()
        self.pushButtonNuevoViajeV1.raise_()
        self.label_57.raise_()
        self.label_58.raise_()
        self.labelCumpleAccesoV1.raise_()
        self.gridLayout_24.addWidget(self.groupBox_23, 0, 1, 1, 1)
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_24.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_24.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_24.setObjectName("groupBox_24")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.groupBox_24)
        self.gridLayout_38.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_38.setSpacing(6)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.labelOptimizaManualV1Header_2 = QtWidgets.QLabel(self.groupBox_24)
        self.labelOptimizaManualV1Header_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelOptimizaManualV1Header_2.setObjectName("labelOptimizaManualV1Header_2")
        self.gridLayout_38.addWidget(self.labelOptimizaManualV1Header_2, 0, 0, 1, 5)
        self.tableWidgetOptimizaManualV1_2 = QtWidgets.QTableWidget(self.groupBox_24)
        self.tableWidgetOptimizaManualV1_2.setMinimumSize(QtCore.QSize(600, 230))
        self.tableWidgetOptimizaManualV1_2.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetOptimizaManualV1_2.setObjectName("tableWidgetOptimizaManualV1_2")
        self.tableWidgetOptimizaManualV1_2.setColumnCount(0)
        self.tableWidgetOptimizaManualV1_2.setRowCount(0)
        self.gridLayout_38.addWidget(self.tableWidgetOptimizaManualV1_2, 1, 0, 5, 5)
        self.lcdNumberPesoSobranteV1_2 = QtWidgets.QLCDNumber(self.groupBox_24)
        self.lcdNumberPesoSobranteV1_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lcdNumberPesoSobranteV1_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberPesoSobranteV1_2.setFont(font)
        self.lcdNumberPesoSobranteV1_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberPesoSobranteV1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberPesoSobranteV1_2.setSmallDecimalPoint(False)
        self.lcdNumberPesoSobranteV1_2.setDigitCount(7)
        self.lcdNumberPesoSobranteV1_2.setProperty("value", 0.0)
        self.lcdNumberPesoSobranteV1_2.setObjectName("lcdNumberPesoSobranteV1_2")
        self.gridLayout_38.addWidget(self.lcdNumberPesoSobranteV1_2, 1, 5, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.groupBox_24)
        self.label_72.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_72.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_38.addWidget(self.label_72, 1, 6, 1, 1)
        self.lcdNumberVolumenSobranteV1_2 = QtWidgets.QLCDNumber(self.groupBox_24)
        self.lcdNumberVolumenSobranteV1_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lcdNumberVolumenSobranteV1_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberVolumenSobranteV1_2.setFont(font)
        self.lcdNumberVolumenSobranteV1_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberVolumenSobranteV1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberVolumenSobranteV1_2.setSmallDecimalPoint(False)
        self.lcdNumberVolumenSobranteV1_2.setDigitCount(7)
        self.lcdNumberVolumenSobranteV1_2.setProperty("value", 0.0)
        self.lcdNumberVolumenSobranteV1_2.setObjectName("lcdNumberVolumenSobranteV1_2")
        self.gridLayout_38.addWidget(self.lcdNumberVolumenSobranteV1_2, 2, 5, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.groupBox_24)
        self.label_60.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_60.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.gridLayout_38.addWidget(self.label_60, 2, 6, 1, 1)
        self.lcdNumberValorSobranteV1_2 = QtWidgets.QLCDNumber(self.groupBox_24)
        self.lcdNumberValorSobranteV1_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lcdNumberValorSobranteV1_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberValorSobranteV1_2.setFont(font)
        self.lcdNumberValorSobranteV1_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberValorSobranteV1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberValorSobranteV1_2.setSmallDecimalPoint(False)
        self.lcdNumberValorSobranteV1_2.setDigitCount(7)
        self.lcdNumberValorSobranteV1_2.setProperty("value", 0.0)
        self.lcdNumberValorSobranteV1_2.setObjectName("lcdNumberValorSobranteV1_2")
        self.gridLayout_38.addWidget(self.lcdNumberValorSobranteV1_2, 3, 5, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.groupBox_24)
        self.label_62.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_62.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.gridLayout_38.addWidget(self.label_62, 3, 6, 1, 1)
        self.lcdNumberTiempoSobranteV1_2 = QtWidgets.QLCDNumber(self.groupBox_24)
        self.lcdNumberTiempoSobranteV1_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lcdNumberTiempoSobranteV1_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumberTiempoSobranteV1_2.setFont(font)
        self.lcdNumberTiempoSobranteV1_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lcdNumberTiempoSobranteV1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberTiempoSobranteV1_2.setSmallDecimalPoint(False)
        self.lcdNumberTiempoSobranteV1_2.setDigitCount(7)
        self.lcdNumberTiempoSobranteV1_2.setProperty("value", 0.0)
        self.lcdNumberTiempoSobranteV1_2.setObjectName("lcdNumberTiempoSobranteV1_2")
        self.gridLayout_38.addWidget(self.lcdNumberTiempoSobranteV1_2, 4, 5, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.groupBox_24)
        self.label_61.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.label_61.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.gridLayout_38.addWidget(self.label_61, 4, 6, 1, 1)
        self.labelCumpleAccesoV1_4 = QtWidgets.QLabel(self.groupBox_24)
        self.labelCumpleAccesoV1_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelCumpleAccesoV1_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelCumpleAccesoV1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCumpleAccesoV1_4.setObjectName("labelCumpleAccesoV1_4")
        self.gridLayout_38.addWidget(self.labelCumpleAccesoV1_4, 5, 5, 1, 1)
        self.labelCumpleAccesoV1_3 = QtWidgets.QLabel(self.groupBox_24)
        self.labelCumpleAccesoV1_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelCumpleAccesoV1_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.labelCumpleAccesoV1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCumpleAccesoV1_3.setObjectName("labelCumpleAccesoV1_3")
        self.gridLayout_38.addWidget(self.labelCumpleAccesoV1_3, 5, 6, 1, 1)
        self.lineEditNvoViajeValor_2 = QtWidgets.QLineEdit(self.groupBox_24)
        self.lineEditNvoViajeValor_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeValor_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeValor_2.setObjectName("lineEditNvoViajeValor_2")
        self.gridLayout_38.addWidget(self.lineEditNvoViajeValor_2, 6, 0, 1, 1)
        self.lineEditNvoViajeM3_2 = QtWidgets.QLineEdit(self.groupBox_24)
        self.lineEditNvoViajeM3_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeM3_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeM3_2.setObjectName("lineEditNvoViajeM3_2")
        self.gridLayout_38.addWidget(self.lineEditNvoViajeM3_2, 6, 1, 1, 1)
        self.lineEditNvoViajeKg_2 = QtWidgets.QLineEdit(self.groupBox_24)
        self.lineEditNvoViajeKg_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 12px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditNvoViajeKg_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNvoViajeKg_2.setObjectName("lineEditNvoViajeKg_2")
        self.gridLayout_38.addWidget(self.lineEditNvoViajeKg_2, 6, 2, 1, 1)
        self.pushButtonNuevoViajeV1_2 = QtWidgets.QPushButton(self.groupBox_24)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonNuevoViajeV1_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonNuevoViajeV1_2.setFont(font)
        self.pushButtonNuevoViajeV1_2.setToolTipDuration(3)
        self.pushButtonNuevoViajeV1_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonNuevoViajeV1_2.setIcon(icon2)
        self.pushButtonNuevoViajeV1_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonNuevoViajeV1_2.setFlat(False)
        self.pushButtonNuevoViajeV1_2.setObjectName("pushButtonNuevoViajeV1_2")
        self.gridLayout_38.addWidget(self.pushButtonNuevoViajeV1_2, 6, 3, 1, 1)
        self.pushButtonBorraV1_2 = QtWidgets.QPushButton(self.groupBox_24)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonBorraV1_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonBorraV1_2.setFont(font)
        self.pushButtonBorraV1_2.setToolTipDuration(3)
        self.pushButtonBorraV1_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonBorraV1_2.setIcon(icon4)
        self.pushButtonBorraV1_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonBorraV1_2.setFlat(False)
        self.pushButtonBorraV1_2.setObjectName("pushButtonBorraV1_2")
        self.gridLayout_38.addWidget(self.pushButtonBorraV1_2, 6, 4, 1, 1)
        self.pushButtonRecalculaV1_2 = QtWidgets.QPushButton(self.groupBox_24)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonRecalculaV1_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonRecalculaV1_2.setFont(font)
        self.pushButtonRecalculaV1_2.setToolTipDuration(3)
        self.pushButtonRecalculaV1_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonRecalculaV1_2.setIcon(icon1)
        self.pushButtonRecalculaV1_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonRecalculaV1_2.setFlat(False)
        self.pushButtonRecalculaV1_2.setObjectName("pushButtonRecalculaV1_2")
        self.gridLayout_38.addWidget(self.pushButtonRecalculaV1_2, 6, 5, 1, 1)
        self.pushButtonOtimizaV1_2 = QtWidgets.QPushButton(self.groupBox_24)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonOtimizaV1_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonOtimizaV1_2.setFont(font)
        self.pushButtonOtimizaV1_2.setToolTipDuration(3)
        self.pushButtonOtimizaV1_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonOtimizaV1_2.setIcon(icon3)
        self.pushButtonOtimizaV1_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonOtimizaV1_2.setFlat(False)
        self.pushButtonOtimizaV1_2.setObjectName("pushButtonOtimizaV1_2")
        self.gridLayout_38.addWidget(self.pushButtonOtimizaV1_2, 6, 6, 1, 1)
        self.tableWidgetOptimizaManualV1_2.raise_()
        self.label_72.raise_()
        self.lcdNumberTiempoSobranteV1_2.raise_()
        self.lcdNumberPesoSobranteV1_2.raise_()
        self.lcdNumberVolumenSobranteV1_2.raise_()
        self.label_61.raise_()
        self.pushButtonOtimizaV1_2.raise_()
        self.lineEditNvoViajeValor_2.raise_()
        self.pushButtonBorraV1_2.raise_()
        self.labelOptimizaManualV1Header_2.raise_()
        self.lcdNumberValorSobranteV1_2.raise_()
        self.labelCumpleAccesoV1_3.raise_()
        self.pushButtonRecalculaV1_2.raise_()
        self.lineEditNvoViajeM3_2.raise_()
        self.lineEditNvoViajeKg_2.raise_()
        self.pushButtonNuevoViajeV1_2.raise_()
        self.label_60.raise_()
        self.label_62.raise_()
        self.labelCumpleAccesoV1_4.raise_()
        self.gridLayout_24.addWidget(self.groupBox_24, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab_4)
        self.frame_2.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.0em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 1;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_15.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_15.setSpacing(6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.radioButtonOptimizaManualViajesEnVeh = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonOptimizaManualViajesEnVeh.setToolTipDuration(3)
        self.radioButtonOptimizaManualViajesEnVeh.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualViajesEnVeh.setChecked(False)
        self.radioButtonOptimizaManualViajesEnVeh.setObjectName("radioButtonOptimizaManualViajesEnVeh")
        self.gridLayout_15.addWidget(self.radioButtonOptimizaManualViajesEnVeh, 0, 0, 1, 1)
        self.radioButtonOptimizaManualDestinosEnVeh = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonOptimizaManualDestinosEnVeh.setToolTipDuration(3)
        self.radioButtonOptimizaManualDestinosEnVeh.setStatusTip("")
        self.radioButtonOptimizaManualDestinosEnVeh.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualDestinosEnVeh.setChecked(True)
        self.radioButtonOptimizaManualDestinosEnVeh.setObjectName("radioButtonOptimizaManualDestinosEnVeh")
        self.gridLayout_15.addWidget(self.radioButtonOptimizaManualDestinosEnVeh, 0, 1, 1, 1)
        self.radioButtonOptimizaManualPedidosEnVeh = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonOptimizaManualPedidosEnVeh.setToolTipDuration(3)
        self.radioButtonOptimizaManualPedidosEnVeh.setStyleSheet("QRadioButton {\n"
"background-color:   rgba(255,0,0,0);\n"
"font: 16px;\n"
"color:rgb(97,98,97);\n"
"padding: 1px;\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(41,180,115);\n"
"    border:                 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.radioButtonOptimizaManualPedidosEnVeh.setObjectName("radioButtonOptimizaManualPedidosEnVeh")
        self.gridLayout_15.addWidget(self.radioButtonOptimizaManualPedidosEnVeh, 0, 2, 1, 1)
        self.gridLayout_24.addWidget(self.frame_2, 2, 1, 1, 1)
        self.tabWidget_6.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_40.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_40.setSpacing(6)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.groupBox_25 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_25.setMaximumSize(QtCore.QSize(12345, 12345))
        self.groupBox_25.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_25.setObjectName("groupBox_25")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_25)
        self.gridLayout_27.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_27.setSpacing(6)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.groupBox_26 = QtWidgets.QGroupBox(self.groupBox_25)
        self.groupBox_26.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_26.setObjectName("groupBox_26")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_26)
        self.gridLayout_16.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.listWidgetAnadePedidos = QtWidgets.QListWidget(self.groupBox_26)
        self.listWidgetAnadePedidos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.listWidgetAnadePedidos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetAnadePedidos.setObjectName("listWidgetAnadePedidos")
        self.gridLayout_16.addWidget(self.listWidgetAnadePedidos, 0, 0, 1, 1)
        self.gridLayout_27.addWidget(self.groupBox_26, 0, 0, 4, 1)
        self.groupBox_27 = QtWidgets.QGroupBox(self.groupBox_25)
        self.groupBox_27.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_27.setObjectName("groupBox_27")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.groupBox_27)
        self.gridLayout_31.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_31.setSpacing(6)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.listWidgetAnadePredespegue_2 = QtWidgets.QListWidget(self.groupBox_27)
        self.listWidgetAnadePredespegue_2.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.listWidgetAnadePredespegue_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidgetAnadePredespegue_2.setObjectName("listWidgetAnadePredespegue_2")
        self.gridLayout_31.addWidget(self.listWidgetAnadePredespegue_2, 0, 0, 1, 1)
        self.gridLayout_27.addWidget(self.groupBox_27, 0, 1, 4, 1)
        self.pushButtonAnadePedidosAnadeResultados_2 = QtWidgets.QPushButton(self.groupBox_25)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonAnadePedidosAnadeResultados_2.setPalette(palette)
        self.pushButtonAnadePedidosAnadeResultados_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonAnadePedidosAnadeResultados_2.setObjectName("pushButtonAnadePedidosAnadeResultados_2")
        self.gridLayout_27.addWidget(self.pushButtonAnadePedidosAnadeResultados_2, 0, 2, 1, 2)
        self.pushButtonAnadePedidosQuitaPredespegue_2 = QtWidgets.QPushButton(self.groupBox_25)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonAnadePedidosQuitaPredespegue_2.setPalette(palette)
        self.pushButtonAnadePedidosQuitaPredespegue_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonAnadePedidosQuitaPredespegue_2.setObjectName("pushButtonAnadePedidosQuitaPredespegue_2")
        self.gridLayout_27.addWidget(self.pushButtonAnadePedidosQuitaPredespegue_2, 2, 2, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 352, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_27.addItem(spacerItem14, 3, 2, 1, 1)
        self.pushButtonGeneradorMotorIniciarMotor_4 = QtWidgets.QPushButton(self.groupBox_25)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonGeneradorMotorIniciarMotor_4.setPalette(palette)
        self.pushButtonGeneradorMotorIniciarMotor_4.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonGeneradorMotorIniciarMotor_4.setObjectName("pushButtonGeneradorMotorIniciarMotor_4")
        self.gridLayout_27.addWidget(self.pushButtonGeneradorMotorIniciarMotor_4, 1, 2, 1, 2)
        self.gridLayout_40.addWidget(self.groupBox_25, 0, 0, 2, 2)
        self.tabWidget_6.addTab(self.tab_6, "")
        self.gridLayout_3.addWidget(self.tabWidget_6, 0, 1, 1, 1)
        self.tabWidget_4.addTab(self.tabGeneradorOtimizaAutomatico, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_44.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_44.setSpacing(6)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.groupBox_28 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_28.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_28.setObjectName("groupBox_28")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.groupBox_28)
        self.gridLayout_43.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_43.setSpacing(6)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.groupBox_29 = QtWidgets.QGroupBox(self.groupBox_28)
        self.groupBox_29.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_29.setObjectName("groupBox_29")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_29)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEditSSResultados_4 = QtWidgets.QLineEdit(self.groupBox_29)
        self.lineEditSSResultados_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEditSSResultados_4.setStyleSheet("background-color: rgb(255,255,255);\n"
"\n"
"font: 16px;\n"
"color: rgb(97,98,97);\n"
"border-color: rgb(26,154,198);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 0px;\n"
"padding: 2px;\n"
"margin-top: 0.01em;\n"
"")
        self.lineEditSSResultados_4.setInputMask("")
        self.lineEditSSResultados_4.setObjectName("lineEditSSResultados_4")
        self.gridLayout_8.addWidget(self.lineEditSSResultados_4, 1, 0, 1, 3)
        self.pushButtonAsignaAutomaticoResultadosOptimizados = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButtonAsignaAutomaticoResultadosOptimizados.setMaximumSize(QtCore.QSize(16777215, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonAsignaAutomaticoResultadosOptimizados.setPalette(palette)
        self.pushButtonAsignaAutomaticoResultadosOptimizados.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonAsignaAutomaticoResultadosOptimizados.setObjectName("pushButtonAsignaAutomaticoResultadosOptimizados")
        self.gridLayout_8.addWidget(self.pushButtonAsignaAutomaticoResultadosOptimizados, 2, 0, 1, 1)
        self.pushButtonAsignaPredespegaSeleccionados = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButtonAsignaPredespegaSeleccionados.setMaximumSize(QtCore.QSize(16777215, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonAsignaPredespegaSeleccionados.setPalette(palette)
        self.pushButtonAsignaPredespegaSeleccionados.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonAsignaPredespegaSeleccionados.setObjectName("pushButtonAsignaPredespegaSeleccionados")
        self.gridLayout_8.addWidget(self.pushButtonAsignaPredespegaSeleccionados, 2, 1, 1, 1)
        self.pushButtonAsignaGuardaRESULTADOS = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButtonAsignaGuardaRESULTADOS.setMaximumSize(QtCore.QSize(16777215, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonAsignaGuardaRESULTADOS.setPalette(palette)
        self.pushButtonAsignaGuardaRESULTADOS.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonAsignaGuardaRESULTADOS.setObjectName("pushButtonAsignaGuardaRESULTADOS")
        self.gridLayout_8.addWidget(self.pushButtonAsignaGuardaRESULTADOS, 2, 2, 1, 1)
        self.tableWidgetAsignaResultadosOptimizados = QtWidgets.QTableWidget(self.groupBox_29)
        self.tableWidgetAsignaResultadosOptimizados.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetAsignaResultadosOptimizados.setObjectName("tableWidgetAsignaResultadosOptimizados")
        self.tableWidgetAsignaResultadosOptimizados.setColumnCount(0)
        self.tableWidgetAsignaResultadosOptimizados.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidgetAsignaResultadosOptimizados, 0, 0, 1, 3)
        self.gridLayout_43.addWidget(self.groupBox_29, 0, 0, 1, 1)
        self.groupBox_31 = QtWidgets.QGroupBox(self.groupBox_28)
        self.groupBox_31.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_31.setObjectName("groupBox_31")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.groupBox_31)
        self.gridLayout_36.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_36.setSpacing(6)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.tableWidgetAsignaVehiculos = QtWidgets.QTableWidget(self.groupBox_31)
        self.tableWidgetAsignaVehiculos.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetAsignaVehiculos.setObjectName("tableWidgetAsignaVehiculos")
        self.tableWidgetAsignaVehiculos.setColumnCount(0)
        self.tableWidgetAsignaVehiculos.setRowCount(0)
        self.gridLayout_36.addWidget(self.tableWidgetAsignaVehiculos, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_31, 0, 1, 2, 1)
        self.groupBox_32 = QtWidgets.QGroupBox(self.groupBox_28)
        self.groupBox_32.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_32.setObjectName("groupBox_32")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.groupBox_32)
        self.gridLayout_42.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_42.setSpacing(6)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.tableWidgetAsignaOperadores = QtWidgets.QTableWidget(self.groupBox_32)
        self.tableWidgetAsignaOperadores.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetAsignaOperadores.setObjectName("tableWidgetAsignaOperadores")
        self.tableWidgetAsignaOperadores.setColumnCount(0)
        self.tableWidgetAsignaOperadores.setRowCount(0)
        self.gridLayout_42.addWidget(self.tableWidgetAsignaOperadores, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_32, 0, 2, 2, 1)
        self.groupBox_30 = QtWidgets.QGroupBox(self.groupBox_28)
        self.groupBox_30.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_30.setObjectName("groupBox_30")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_30)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidgetAsignaPredespegue = QtWidgets.QTableWidget(self.groupBox_30)
        self.tableWidgetAsignaPredespegue.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetAsignaPredespegue.setObjectName("tableWidgetAsignaPredespegue")
        self.tableWidgetAsignaPredespegue.setColumnCount(0)
        self.tableWidgetAsignaPredespegue.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidgetAsignaPredespegue, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_30, 1, 0, 1, 1)
        self.gridLayout_44.addWidget(self.groupBox_28, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_33 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_33.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_33.setObjectName("groupBox_33")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.groupBox_33)
        self.gridLayout_33.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_33.setSpacing(6)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.tableWidgetDespeguePredespegue = QtWidgets.QTableWidget(self.groupBox_33)
        self.tableWidgetDespeguePredespegue.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDespeguePredespegue.setObjectName("tableWidgetDespeguePredespegue")
        self.tableWidgetDespeguePredespegue.setColumnCount(0)
        self.tableWidgetDespeguePredespegue.setRowCount(0)
        self.gridLayout_33.addWidget(self.tableWidgetDespeguePredespegue, 0, 0, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(307, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem15, 1, 0, 1, 1)
        self.pushButtonDespegueDespega_2 = QtWidgets.QPushButton(self.groupBox_33)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonDespegueDespega_2.setPalette(palette)
        self.pushButtonDespegueDespega_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonDespegueDespega_2.setObjectName("pushButtonDespegueDespega_2")
        self.gridLayout_33.addWidget(self.pushButtonDespegueDespega_2, 1, 1, 1, 1)
        self.pushButtonDespegueDespega = QtWidgets.QPushButton(self.groupBox_33)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 158, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonDespegueDespega.setPalette(palette)
        self.pushButtonDespegueDespega.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(24,158,87);\n"
"border-radius: 5px;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"color: rgb(255,255,255);\n"
"} ")
        self.pushButtonDespegueDespega.setObjectName("pushButtonDespegueDespega")
        self.gridLayout_33.addWidget(self.pushButtonDespegueDespega, 2, 1, 1, 1)
        self.labelDespeguePIN = QtWidgets.QLabel(self.groupBox_33)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelDespeguePIN.setFont(font)
        self.labelDespeguePIN.setStyleSheet("color: rgb(97,98,97);\n"
"font: bold 34px;\n"
"")
        self.labelDespeguePIN.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDespeguePIN.setObjectName("labelDespeguePIN")
        self.gridLayout_33.addWidget(self.labelDespeguePIN, 3, 0, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_33, 0, 0, 1, 1)
        self.groupBox_34 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_34.setStyleSheet("background-color: rgb(230,231,232);\n"
"margin-top: 0.5em;\n"
"font: 16px;\n"
"color:  rgb(97,98,97);\n"
"border: 0px solid white;\n"
"padding: 14;\n"
"")
        self.groupBox_34.setObjectName("groupBox_34")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.groupBox_34)
        self.gridLayout_45.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_45.setSpacing(6)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.tableWidgetDespegueDespegados_2 = QtWidgets.QTableWidget(self.groupBox_34)
        self.tableWidgetDespegueDespegados_2.setStyleSheet("font: 11px;\n"
"color: rgb(97,98,97);\n"
"border: 0px solid rgba(143, 234, 79,90);\n"
"background-color: rgb(255,255,255);\n"
"")
        self.tableWidgetDespegueDespegados_2.setObjectName("tableWidgetDespegueDespegados_2")
        self.tableWidgetDespegueDespegados_2.setColumnCount(0)
        self.tableWidgetDespegueDespegados_2.setRowCount(0)
        self.gridLayout_45.addWidget(self.tableWidgetDespegueDespegados_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_34, 0, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.gridLayout_4.addWidget(self.tabWidget_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabGeneradorRutasPreferencias, "")
        self.tabDataScience = QtWidgets.QWidget()
        self.tabDataScience.setObjectName("tabDataScience")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.tabDataScience)
        self.gridLayout_28.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_28.setSpacing(6)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frameDashboards = QtWidgets.QFrame(self.tabDataScience)
        self.frameDashboards.setStyleSheet("background-color: rgba(255,255,255,50);\n"
"margin-top: 0.0em;\n"
"font: 16px;\n"
"color:  rgb(160, 232, 105);\n"
"border: 0px solid white;\n"
"padding: 1px;\n"
"")
        self.frameDashboards.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDashboards.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDashboards.setObjectName("frameDashboards")
        self.gridLayout_28.addWidget(self.frameDashboards, 0, 0, 1, 1)
        self.labelStatusBarCEDI_6 = QtWidgets.QLabel(self.tabDataScience)
        self.labelStatusBarCEDI_6.setMaximumSize(QtCore.QSize(12345, 24))
        self.labelStatusBarCEDI_6.setStyleSheet("border: 0px solid white;\n"
"")
        self.labelStatusBarCEDI_6.setText("")
        self.labelStatusBarCEDI_6.setPixmap(QtGui.QPixmap(":/Img/arms_logo.png"))
        self.labelStatusBarCEDI_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusBarCEDI_6.setObjectName("labelStatusBarCEDI_6")
        self.gridLayout_28.addWidget(self.labelStatusBarCEDI_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabDataScience, "")
        self.gridLayout_34.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_29.addWidget(self.frame, 0, 0, 1, 1)
        ARMSApp.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ARMSApp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1520, 22))
        self.menuBar.setObjectName("menuBar")
        ARMSApp.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(ARMSApp)
        self.mainToolBar.setObjectName("mainToolBar")
        ARMSApp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ARMSApp)
        self.statusBar.setObjectName("statusBar")
        ARMSApp.setStatusBar(self.statusBar)

        self.retranslateUi(ARMSApp)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_8.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(2)
        self.tabWidget_6.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ARMSApp)

    def retranslateUi(self, ARMSApp):
        _translate = QtCore.QCoreApplication.translate
        ARMSApp.setWindowTitle(_translate("ARMSApp", "ARMSApp"))
        self.lineEditClave_2.setPlaceholderText(_translate("ARMSApp", "Clave"))
        self.lineEditUsuario_2.setPlaceholderText(_translate("ARMSApp", "Usuario"))
        self.lineEditCEDI_2.setText(_translate("ARMSApp", "CENADI"))
        self.lineEditCEDI_2.setPlaceholderText(_translate("ARMSApp", "CEDI"))
        self.pushButtonIniciaSesion_2.setText(_translate("ARMSApp", "Iniciar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("ARMSApp", "Acceso"))
        self.textEdit.setHtml(_translate("ARMSApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:64pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:64pt;\">ARMS 3.5</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:64pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Release 3.5.0.0.12</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">12 nov 2017</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Grupo Areté</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Derechos Reservados</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">www.arete.ws</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px; font-weight:600;\"><br /></p></body></html>"))
        self.labelStatusBarUser.setText(_translate("ARMSApp", "user"))
        self.labelStatusBarCEDI.setText(_translate("ARMSApp", "CEDI"))
        self.labelStatusBarMensaje.setText(_translate("ARMSApp", "Mensaje"))
        self.labelStatusBarEmpresa.setText(_translate("ARMSApp", "empresa"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("ARMSApp", "Acerca de ARMS..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("ARMSApp", "Iniciar sesión"))
        self.groupBox_8.setTitle(_translate("ARMSApp", "FTP"))
        self.radioButtonInterfasePochtecaPedidos.setText(_translate("ARMSApp", "Pedidos"))
        self.radioButtonInterfasePochtecaOperadores.setText(_translate("ARMSApp", "Operadores"))
        self.radioButtonInterfasePochtecaDestinos.setText(_translate("ARMSApp", "Destinos"))
        self.radioButtonInterfasePochtecaUrgentes.setText(_translate("ARMSApp", "Urgentes"))
        self.radioButtonInterfasePochtecaCancelados.setText(_translate("ARMSApp", "Cancelados"))
        self.radioButtonInterfasePochtecaOrdinarios.setText(_translate("ARMSApp", "Ordinarios"))
        self.radioButtonInterfasePochtecaTodos.setText(_translate("ARMSApp", "Todos"))
        self.pushButtonInterfasePochtecaGenera.setText(_translate("ARMSApp", "Genera Spreasheet"))
        self.groupBox_9.setTitle(_translate("ARMSApp", "Google SS Generados"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("ARMSApp", "Pedidos/Operadores"))
        self.groupBox_36.setTitle(_translate("ARMSApp", "Añade Nuevas Direcciones (de... a...)"))
        self.pushButtonInterfasePochtecaGenera_2.setText(_translate("ARMSApp", "Añade Direcciones"))
        self.groupBox.setTitle(_translate("ARMSApp", "Resultados añadidos"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("ARMSApp", "Destinos"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_5), _translate("ARMSApp", "Pochteca"))
        self.groupBox_5.setTitle(_translate("ARMSApp", "Genera Google SS"))
        self.radioButtonInterfaseSilodisaForaneo.setText(_translate("ARMSApp", "Foráneo"))
        self.radioButtonInterfaseSilodisaLocal.setText(_translate("ARMSApp", "Local"))
        self.radioButtonInterfaseSilodisaReplaneaciones.setText(_translate("ARMSApp", "Replaneaciones"))
        self.radioButtonInterfaseSilodisaExtraordinarios.setText(_translate("ARMSApp", "Extraordinarios"))
        self.radioButtonInterfaseSilodisaVacunas.setText(_translate("ARMSApp", "Guías de Vacuna"))
        self.radioButtonInterfaseSilodisaSoportes.setText(_translate("ARMSApp", "Soportes de Vida"))
        self.radioButtonInterfaseSilodisaOrdinarios.setText(_translate("ARMSApp", "Ordinarios"))
        self.radioButtonInterfaseSilodisaTodos.setText(_translate("ARMSApp", "Todos"))
        self.pushButtonInterfaseSilodisaGeneraPedido.setText(_translate("ARMSApp", "Genera Archivos Google SS"))
        self.groupBox_6.setTitle(_translate("ARMSApp", "Google SS Generados"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_15), _translate("ARMSApp", "Pedidos/Operadores"))
        self.groupBox_37.setTitle(_translate("ARMSApp", "Añade Nuevas Direcciones (de... a...)"))
        self.pushButtonInterfasePochtecaGenera_3.setText(_translate("ARMSApp", "Añade Direcciones"))
        self.groupBox_42.setTitle(_translate("ARMSApp", "Resultados añadidos"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_16), _translate("ARMSApp", "Destinos"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_14), _translate("ARMSApp", "Silodisa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInterfase), _translate("ARMSApp", "Interfaz"))
        self.groupBox_10.setTitle(_translate("ARMSApp", "Selecciona los Google SS para trabajar"))
        self.groupBox_11.setTitle(_translate("ARMSApp", "Pedidos"))
        self.groupBox_12.setTitle(_translate("ARMSApp", "Vehículos"))
        self.groupBox_13.setTitle(_translate("ARMSApp", "Operadores"))
        self.groupBox_15.setTitle(_translate("ARMSApp", "Destinos"))
        self.groupBox_16.setTitle(_translate("ARMSApp", "Preferencias"))
        self.groupBox_17.setTitle(_translate("ARMSApp", "Tarifario"))
        self.groupBox_18.setTitle(_translate("ARMSApp", "Matriz Compatibilidad"))
        self.pushButtonGeneradorDatosAbreSeleccionados_2.setText(_translate("ARMSApp", "Abre Seleccionados Google SS"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("ARMSApp", "1. Google SS"))
        self.groupBox_19.setTitle(_translate("ARMSApp", "Motor ARMS 3.5"))
        self.label_38.setText(_translate("ARMSApp", "$/Kg"))
        self.label_43.setText(_translate("ARMSApp", "%Ocup"))
        self.label_41.setText(_translate("ARMSApp", "$ Viaje"))
        self.label_40.setText(_translate("ARMSApp", "$/m3"))
        self.label_39.setText(_translate("ARMSApp", "$/Pza"))
        self.label_45.setText(_translate("ARMSApp", "Viajes"))
        self.label_44.setText(_translate("ARMSApp", "Km"))
        self.label_42.setText(_translate("ARMSApp", "$ Tot"))
        self.pushButtonGeneradorMotorGuardar.setText(_translate("ARMSApp", "Abre SS Resultados"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("ARMSApp", "2. Generador Rutas"))
        self.groupBox_21.setTitle(_translate("ARMSApp", "Optimiza los Resultados en forma automática"))
        self.label_16.setText(_translate("ARMSApp", "Aumentar capacidad peso"))
        self.radioButtonOptimizaVacios.setText(_translate("ARMSApp", "Elimina baja Ocupación"))
        self.lineEditOptimizaAumentarValorMiles.setText(_translate("ARMSApp", "0"))
        self.label_14.setText(_translate("ARMSApp", "Minutos"))
        self.label_15.setText(_translate("ARMSApp", "Aumentar capacidad volumen"))
        self.pushButtonOptimizaAutoViajesMotor.setText(_translate("ARMSApp", "Optimiza Motor Viajes"))
        self.lineEditOptimizaCercaniaMaxima.setText(_translate("ARMSApp", "50"))
        self.label_12.setText(_translate("ARMSApp", "Pesos"))
        self.label_7.setText(_translate("ARMSApp", "Ocupación menor al"))
        self.label_17.setText(_translate("ARMSApp", "%"))
        self.label_11.setText(_translate("ARMSApp", "Aumentar valor (miles)"))
        self.lineEditOptimizaAumentarCapacidad.setText(_translate("ARMSApp", "5"))
        self.label_8.setText(_translate("ARMSApp", "%"))
        self.radioButtonOptimizaCercanos.setText(_translate("ARMSApp", " Junta Destinos Cercanos"))
        self.label_10.setText(_translate("ARMSApp", "km"))
        self.checkBoxOptimizaIgnoraAcceso.setText(_translate("ARMSApp", "Ignora restriccion de acceso"))
        self.checkBoxOptimizaIgnoraCompatibilidad.setText(_translate("ARMSApp", "Ignora matriz de compatibilidad"))
        self.label_18.setText(_translate("ARMSApp", "%"))
        self.lineEditOptimizaAumentarPeso.setText(_translate("ARMSApp", "5"))
        self.lineEditOptimizaAumentarVentanaMinutos.setText(_translate("ARMSApp", "15"))
        self.label_13.setText(_translate("ARMSApp", "Aumentar ventana entrega"))
        self.label_9.setText(_translate("ARMSApp", "Cercanía máxima"))
        self.lineEditGeneradorOptimizaViajesVacios.setText(_translate("ARMSApp", "90"))
        self.pushButtonNuevoViajeV1_6.setToolTip(_translate("ARMSApp", "Optimiza"))
        self.pushButtonNuevoViajeV1_6.setText(_translate("ARMSApp", "Abre"))
        self.pushButtonOptimiza.setText(_translate("ARMSApp", "Optimiza"))
        self.groupBox_35.setTitle(_translate("ARMSApp", "Resultados"))
        self.lineEditSSResultados_2.setPlaceholderText(_translate("ARMSApp", "Nombre del Archivo Google SS Resultados"))
        self.pushButtonOptimizaAutoGuarda.setText(_translate("ARMSApp", "Guarda Resultados"))
        self.label_111.setText(_translate("ARMSApp", "$ Viaje"))
        self.label_113.setText(_translate("ARMSApp", "%Ocup"))
        self.label_112.setText(_translate("ARMSApp", "$ Tot"))
        self.label_71.setText(_translate("ARMSApp", "$/m3"))
        self.label_115.setText(_translate("ARMSApp", "Viajes"))
        self.label_114.setText(_translate("ARMSApp", "Km"))
        self.label_55.setText(_translate("ARMSApp", "$/Kg"))
        self.label_70.setText(_translate("ARMSApp", "$/Pza"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_3), _translate("ARMSApp", "Automática"))
        self.groupBox_22.setTitle(_translate("ARMSApp", "Resultados"))
        self.pushButtonNuevoViajeV1_3.setToolTip(_translate("ARMSApp", "Optimiza"))
        self.pushButtonNuevoViajeV1_3.setText(_translate("ARMSApp", "Abre"))
        self.radioButtonOptimizaManualViajes.setToolTip(_translate("ARMSApp", "Viajes"))
        self.radioButtonOptimizaManualViajes.setText(_translate("ARMSApp", "Viajes"))
        self.radioButtonOptimizaManualDestinos.setToolTip(_translate("ARMSApp", "Destinos"))
        self.radioButtonOptimizaManualDestinos.setText(_translate("ARMSApp", "Destinos"))
        self.pushButtonOptimizaManualRecargaOptimizado.setText(_translate("ARMSApp", "Recarga Resultados"))
        self.pushButtonOptimizaManualGuardaResultados.setText(_translate("ARMSApp", "Guarda Resultados"))
        self.pushButtonRecalculaSeleccionados.setToolTip(_translate("ARMSApp", "Recalcula"))
        self.pushButtonRecalculaSeleccionados.setText(_translate("ARMSApp", "Recalcula Viajes Seleccionados"))
        self.label_54.setText(_translate("ARMSApp", "$/Kg"))
        self.label_63.setText(_translate("ARMSApp", "$/Pza"))
        self.label_64.setText(_translate("ARMSApp", "$/m3"))
        self.label_65.setText(_translate("ARMSApp", "$ Viaje"))
        self.label_66.setText(_translate("ARMSApp", "$ Tot"))
        self.label_67.setText(_translate("ARMSApp", "%Ocup"))
        self.label_68.setText(_translate("ARMSApp", "Km"))
        self.label_69.setText(_translate("ARMSApp", "Viajes"))
        self.lineEditSSResultados_3.setPlaceholderText(_translate("ARMSApp", "Nombre del Archivo Google SS Resultados"))
        self.radioButtonOptimizaManualPedidos.setToolTip(_translate("ARMSApp", "Pedidos"))
        self.radioButtonOptimizaManualPedidos.setText(_translate("ARMSApp", "Pedidos"))
        self.groupBox_23.setTitle(_translate("ARMSApp", "Viaje A"))
        self.labelOptimizaManualV1Header.setText(_translate("ARMSApp", "Datos Viaje: FL360, 35T, 14m3, 870Km, $678, Xalapa, Veracruz"))
        self.label_56.setText(_translate("ARMSApp", "Kg (000)"))
        self.label_57.setText(_translate("ARMSApp", "m3"))
        self.label_58.setText(_translate("ARMSApp", "$ (000)"))
        self.label_59.setText(_translate("ARMSApp", "Hrs"))
        self.labelCumpleAccesoV1.setText(_translate("ARMSApp", "Acceso"))
        self.labelCumpleAccesoV1_2.setText(_translate("ARMSApp", "M. Comp."))
        self.lineEditNvoViajeValor.setInputMask(_translate("ARMSApp", "$ (miles)"))
        self.lineEditNvoViajeValor.setText(_translate("ARMSApp", "$ (miles)"))
        self.lineEditNvoViajeM3.setInputMask(_translate("ARMSApp", "m3"))
        self.lineEditNvoViajeM3.setText(_translate("ARMSApp", "m3"))
        self.lineEditNvoViajeKg.setInputMask(_translate("ARMSApp", "Kg(miles)"))
        self.lineEditNvoViajeKg.setText(_translate("ARMSApp", "Kg(miles)"))
        self.pushButtonNuevoViajeV1.setToolTip(_translate("ARMSApp", "Optimiza"))
        self.pushButtonNuevoViajeV1.setText(_translate("ARMSApp", "Nvo Viaje"))
        self.pushButtonBorraV1.setToolTip(_translate("ARMSApp", "Borra"))
        self.pushButtonBorraV1.setText(_translate("ARMSApp", "Borra"))
        self.pushButtonRecalculaV1.setToolTip(_translate("ARMSApp", "Nvo. Viaje"))
        self.pushButtonRecalculaV1.setText(_translate("ARMSApp", "Recalcula"))
        self.pushButtonOtimizaV1.setToolTip(_translate("ARMSApp", "Recalcula"))
        self.pushButtonOtimizaV1.setText(_translate("ARMSApp", "Optimiza"))
        self.groupBox_24.setTitle(_translate("ARMSApp", "Viaje B"))
        self.labelOptimizaManualV1Header_2.setText(_translate("ARMSApp", "Datos Viaje: FL360, 35T, 14m3, 870Km, $678, Xalapa, Veracruz"))
        self.label_72.setText(_translate("ARMSApp", "Kg (000)"))
        self.label_60.setText(_translate("ARMSApp", "m3"))
        self.label_62.setText(_translate("ARMSApp", "$ (000)"))
        self.label_61.setText(_translate("ARMSApp", "Hrs"))
        self.labelCumpleAccesoV1_4.setText(_translate("ARMSApp", "Acceso"))
        self.labelCumpleAccesoV1_3.setText(_translate("ARMSApp", "M. Comp."))
        self.lineEditNvoViajeValor_2.setInputMask(_translate("ARMSApp", "$ (miles)"))
        self.lineEditNvoViajeValor_2.setText(_translate("ARMSApp", "$ (miles)"))
        self.lineEditNvoViajeM3_2.setInputMask(_translate("ARMSApp", "m3"))
        self.lineEditNvoViajeM3_2.setText(_translate("ARMSApp", "m3"))
        self.lineEditNvoViajeKg_2.setInputMask(_translate("ARMSApp", "Kg(miles)"))
        self.lineEditNvoViajeKg_2.setText(_translate("ARMSApp", "Kg(miles)"))
        self.pushButtonNuevoViajeV1_2.setToolTip(_translate("ARMSApp", "Optimiza"))
        self.pushButtonNuevoViajeV1_2.setText(_translate("ARMSApp", "Nvo Viaje"))
        self.pushButtonBorraV1_2.setToolTip(_translate("ARMSApp", "Borra"))
        self.pushButtonBorraV1_2.setText(_translate("ARMSApp", "Borra"))
        self.pushButtonRecalculaV1_2.setToolTip(_translate("ARMSApp", "Nvo. Viaje"))
        self.pushButtonRecalculaV1_2.setText(_translate("ARMSApp", "Recalcula"))
        self.pushButtonOtimizaV1_2.setToolTip(_translate("ARMSApp", "Recalcula"))
        self.pushButtonOtimizaV1_2.setText(_translate("ARMSApp", "Optimiza"))
        self.radioButtonOptimizaManualViajesEnVeh.setToolTip(_translate("ARMSApp", "Viajes"))
        self.radioButtonOptimizaManualViajesEnVeh.setText(_translate("ARMSApp", "Viajes"))
        self.radioButtonOptimizaManualDestinosEnVeh.setToolTip(_translate("ARMSApp", "Destinos"))
        self.radioButtonOptimizaManualDestinosEnVeh.setText(_translate("ARMSApp", "Destinos"))
        self.radioButtonOptimizaManualPedidosEnVeh.setToolTip(_translate("ARMSApp", "Pedidos"))
        self.radioButtonOptimizaManualPedidosEnVeh.setText(_translate("ARMSApp", "Pedidos"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_4), _translate("ARMSApp", "Manual"))
        self.groupBox_25.setTitle(_translate("ARMSApp", "Añade Pedidos SS / Viajes predespegados a Resultados SS"))
        self.groupBox_26.setTitle(_translate("ARMSApp", "Pedidos"))
        self.groupBox_27.setTitle(_translate("ARMSApp", "Predespegue"))
        self.pushButtonAnadePedidosAnadeResultados_2.setText(_translate("ARMSApp", "Añade a Resultados"))
        self.pushButtonAnadePedidosQuitaPredespegue_2.setText(_translate("ARMSApp", "Elimina de Resultados"))
        self.pushButtonGeneradorMotorIniciarMotor_4.setText(_translate("ARMSApp", "Verifica Arcos"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_6), _translate("ARMSApp", "Añade Pedidos"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tabGeneradorOtimizaAutomatico), _translate("ARMSApp", "3. Optimizador"))
        self.groupBox_28.setTitle(_translate("ARMSApp", "Asgina operador y vehículo a un viaje"))
        self.groupBox_29.setTitle(_translate("ARMSApp", "Resultados"))
        self.lineEditSSResultados_4.setPlaceholderText(_translate("ARMSApp", "Nombre del Archivo Google SS Resultados"))
        self.pushButtonAsignaAutomaticoResultadosOptimizados.setText(_translate("ARMSApp", "Asignación Automática"))
        self.pushButtonAsignaPredespegaSeleccionados.setText(_translate("ARMSApp", "Predespega Seleccionados"))
        self.pushButtonAsignaGuardaRESULTADOS.setText(_translate("ARMSApp", "Guarda Resultados"))
        self.groupBox_31.setTitle(_translate("ARMSApp", "Vehículos"))
        self.groupBox_32.setTitle(_translate("ARMSApp", "Operadores"))
        self.groupBox_30.setTitle(_translate("ARMSApp", "Predespegue"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), _translate("ARMSApp", "4. Asignador"))
        self.groupBox_33.setTitle(_translate("ARMSApp", "Predespegue"))
        self.pushButtonDespegueDespega_2.setText(_translate("ARMSApp", "Guarda Modificaciones Seleccionado"))
        self.pushButtonDespegueDespega.setText(_translate("ARMSApp", "Despega"))
        self.labelDespeguePIN.setText(_translate("ARMSApp", "PIN: 123456"))
        self.groupBox_34.setTitle(_translate("ARMSApp", "Despegados"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("ARMSApp", "5. Despegar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneradorRutasPreferencias), _translate("ARMSApp", "Generador Rutas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDataScience), _translate("ARMSApp", "Data Science"))

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ARMSApp = QtWidgets.QMainWindow()
    ui = Ui_ARMSApp()
    ui.setupUi(ARMSApp)
    ARMSApp.show()
    sys.exit(app.exec_())

