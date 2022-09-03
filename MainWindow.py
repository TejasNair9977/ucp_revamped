from PySide6 import QtCore,QtGui,QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 556)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 219, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 92, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 219, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 92, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 219, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 92, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 92, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 92, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 10, 251, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 319))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 11, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 11, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 340, 381, 163))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hrclothdispenser = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.hrclothdispenser.setObjectName("hrclothdispenser")
        self.gridLayout_2.addWidget(self.hrclothdispenser, 3, 1, 1, 1)
        self.pbdispenser = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pbdispenser.setObjectName("pbdispenser")
        self.gridLayout_2.addWidget(self.pbdispenser, 4, 1, 1, 1)
        self.dtpadispenser = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dtpadispenser.setObjectName("dtpadispenser")
        self.gridLayout_2.addWidget(self.dtpadispenser, 5, 0, 1, 1)
        self.gasdispenser = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gasdispenser.setObjectName("gasdispenser")
        self.gridLayout_2.addWidget(self.gasdispenser, 3, 0, 1, 1)
        self.pinger = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pinger.setObjectName("pinger")
        self.gridLayout_2.addWidget(self.pinger, 5, 1, 1, 1)
        self.kidispenser = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.kidispenser.setObjectName("kidispenser")
        self.gridLayout_2.addWidget(self.kidispenser, 4, 0, 1, 1)
        self.automate = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.automate.setObjectName("automate")
        self.gridLayout_2.addWidget(self.automate, 0, 0, 1, 2)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setEnabled(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 160, 251, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout.addWidget(self.label_32)
        self.dial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout.addWidget(self.label_31)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_2.addWidget(self.label_33)
        self.verticalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_2.addWidget(self.verticalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 25))
        self.menubar.setObjectName("menubar")
        self.menuSimulate = QtWidgets.QMenu(self.menubar)
        self.menuSimulate.setObjectName("menuSimulate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_24.setText(_translate("MainWindow", "Air Purification"))
        self.label_27.setText(_translate("MainWindow", "Purification Type:-"))
        self.radioButton.setText(_translate("MainWindow", "Active"))
        self.radioButton_2.setText(_translate("MainWindow", "Passive"))
        self.label_30.setText(_translate("MainWindow", "Negative Ion Discharge"))
        self.label_4.setText(_translate("MainWindow", "SAFE"))
        self.label_5.setText(_translate("MainWindow", "Internal Gas Toxicity:-"))
        self.label_17.setText(_translate("MainWindow", "120rad"))
        self.label_6.setText(_translate("MainWindow", "40%"))
        self.label_11.setText(_translate("MainWindow", "Noise Levels:-"))
        self.label_18.setText(_translate("MainWindow", "550rad"))
        self.label_19.setText(_translate("MainWindow", "External Gas Toxicity:-"))
        self.label_9.setText(_translate("MainWindow", "Water Pressure:-"))
        self.label_15.setText(_translate("MainWindow", "Radiation Counter C;-"))
        self.label_21.setText(_translate("MainWindow", "Temparature:-"))
        self.label_10.setText(_translate("MainWindow", "Clean"))
        self.label_20.setText(_translate("MainWindow", "3%"))
        self.label_7.setText(_translate("MainWindow", "Threat:-"))
        self.label_16.setText(_translate("MainWindow", "Radiation Counter D;-"))
        self.label_12.setText(_translate("MainWindow", "Low"))
        self.label_8.setText(_translate("MainWindow", "None"))
        self.label.setText(_translate("MainWindow", "Radiation Counter A:-"))
        self.label_13.setText(_translate("MainWindow", "Radiation Counter B;-"))
        self.label_22.setText(_translate("MainWindow", "Normal"))
        self.label_2.setText(_translate("MainWindow", "69 rad"))
        self.label_14.setText(_translate("MainWindow", "420rad"))
        self.label_3.setText(_translate("MainWindow", "Safety Level:-"))
        self.label_28.setText(_translate("MainWindow", "Power Output:-"))
        self.label_29.setText(_translate("MainWindow", "69MW"))
        self.hrclothdispenser.setText(_translate("MainWindow", "Heat Resistant Clothes"))
        self.pbdispenser.setText(_translate("MainWindow", "Prussian Blue"))
        self.dtpadispenser.setText(_translate("MainWindow", "DTPA"))
        self.gasdispenser.setText(_translate("MainWindow", "Gas Masks"))
        self.pinger.setText(_translate("MainWindow", "Ping"))
        self.kidispenser.setText(_translate("MainWindow", "Potassium Iodide"))
        self.automate.setText(_translate("MainWindow", "Automate"))
        self.label_23.setText(_translate("MainWindow", "Disnpense:-"))
        self.label_26.setText(_translate("MainWindow", "Error"))
        self.label_25.setText(_translate("MainWindow", "Water Cooling"))
        self.label_32.setText(_translate("MainWindow", "Water Pressure"))
        self.label_31.setText(_translate("MainWindow", "Water Pressure Gauge"))
        self.label_33.setText(_translate("MainWindow", "Water Filteration"))
        self.menuSimulate.setTitle(_translate("MainWindow", "Simulate"))