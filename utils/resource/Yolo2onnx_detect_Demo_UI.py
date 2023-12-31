# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Yolo2onnx_detect_Demo_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(640, 480))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 11, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 5, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 12, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/reset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_2.setMinimum(-1)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setProperty("value", -1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 10, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.tab)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.tab)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 4, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.tab_2)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 8, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 9, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_5.addWidget(self.checkBox_4)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(120)
        self.spinBox.setProperty("value", 15)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 7, 0, 1, 3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_8.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_8.addWidget(self.checkBox_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 6, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/screenshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 11, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 15, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setMinimum(0.05)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.05)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_2.setMinimum(0.05)
        self.doubleSpinBox_2.setMaximum(1.0)
        self.doubleSpinBox_2.setSingleStep(0.05)
        self.doubleSpinBox_2.setProperty("value", 0.5)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout.addWidget(self.doubleSpinBox_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.toolButton_6 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_6.setStyleSheet("color:rgb(255, 0, 0)")
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_7.addWidget(self.toolButton_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_3.addWidget(self.toolButton_5, 0, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_2.setAcceptRichText(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_3.addWidget(self.textEdit_2, 1, 0, 1, 3)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.verticalGroupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/unlock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/unlock.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/lock.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_10.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/clear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_9.addWidget(self.verticalGroupBox)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_9.addWidget(self.textBrowser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yolo2onnx detect Demo"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "视频跳帧："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "not flip"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "horizontal"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "vertical"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "horizontal and vertical"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "翻转图像："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "0°"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "+90°"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "-90°"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "180°"))
        self.comboBox.setItemText(0, _translate("MainWindow", "摄像头(0)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "图片/视频(file)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "网络视频流(url)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "屏幕(screen)"))
        self.comboBox.setItemText(4, _translate("MainWindow", "自定义"))
        self.label_5.setText(_translate("MainWindow", "权重路径："))
        self.spinBox_2.setSpecialValueText(_translate("MainWindow", "auto"))
        self.label_12.setText(_translate("MainWindow", "旋转图像:"))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "输入方式："))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "类别："))
        self.label_4.setText(_translate("MainWindow", "文件路径："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "输入"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.checkBox_4.setText(_translate("MainWindow", "录制视频"))
        self.spinBox.setPrefix(_translate("MainWindow", "帧率:"))
        self.checkBox_5.setText(_translate("MainWindow", "打印检测结果"))
        self.checkBox_6.setText(_translate("MainWindow", "打印坐标"))
        self.pushButton.setText(_translate("MainWindow", "截图并保存"))
        self.pushButton_3.setText(_translate("MainWindow", "保存控制台记录"))
        self.label_2.setText(_translate("MainWindow", "保存路径："))
        self.pushButton_2.setText(_translate("MainWindow", "打开存放目录"))
        self.label_7.setText(_translate("MainWindow", "置信度阈值："))
        self.label_10.setText(_translate("MainWindow", "IOU阈值："))
        self.checkBox.setText(_translate("MainWindow", "显示实时帧数"))
        self.checkBox_2.setText(_translate("MainWindow", "显示锚框"))
        self.label_9.setText(_translate("MainWindow", "锚框颜色："))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "输出"))
        self.checkBox_3.setText(_translate("MainWindow", "Enable"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.pushButton_7.setText(_translate("MainWindow", "reload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "script"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "锁定/取消 在底部"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "清空控制台"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
