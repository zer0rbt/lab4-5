# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SA.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ResultsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ResultsGroupBox.setGeometry(QtCore.QRect(10, 470, 441, 181))
        self.ResultsGroupBox.setObjectName("ResultsGroupBox")
        self.BestGene = QtWidgets.QPlainTextEdit(self.ResultsGroupBox)
        self.BestGene.setEnabled(True)
        self.BestGene.setGeometry(QtCore.QRect(10, 20, 421, 151))
        self.BestGene.setReadOnly(True)
        self.BestGene.setCenterOnScroll(False)
        self.BestGene.setObjectName("BestGene")
        self.IterationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.IterationGroupBox.setGeometry(QtCore.QRect(10, 310, 441, 141))
        self.IterationGroupBox.setObjectName("IterationGroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.IterationGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 421, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.IterationCount = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IterationCount.sizePolicy().hasHeightForWidth())
        self.IterationCount.setSizePolicy(sizePolicy)
        self.IterationCount.setObjectName("IterationCount")
        self.horizontalLayout_2.addWidget(self.IterationCount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Set1iterationCount = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Set1iterationCount.setObjectName("Set1iterationCount")
        self.horizontalLayout_3.addWidget(self.Set1iterationCount)
        self.Set10iterationCount = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Set10iterationCount.setObjectName("Set10iterationCount")
        self.horizontalLayout_3.addWidget(self.Set10iterationCount)
        self.Set100iterationCount = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Set100iterationCount.setObjectName("Set100iterationCount")
        self.horizontalLayout_3.addWidget(self.Set100iterationCount)
        self.Set1000iterationCount = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Set1000iterationCount.setObjectName("Set1000iterationCount")
        self.horizontalLayout_3.addWidget(self.Set1000iterationCount)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.TableGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TableGroupBox.setGeometry(QtCore.QRect(460, 10, 661, 641))
        self.TableGroupBox.setObjectName("TableGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TableGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.TableGroupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.TableGroupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.TableGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.TableGroupBox)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.TableGroupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.SettingsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SettingsGroupBox.setGeometry(QtCore.QRect(10, 10, 441, 271))
        self.SettingsGroupBox.setObjectName("SettingsGroupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.SettingsGroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(15, 10, 421, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.funcQLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcQLE.sizePolicy().hasHeightForWidth())
        self.funcQLE.setSizePolicy(sizePolicy)
        self.funcQLE.setObjectName("funcQLE")
        self.horizontalLayout_6.addWidget(self.funcQLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.GeneAmountQLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GeneAmountQLE.sizePolicy().hasHeightForWidth())
        self.GeneAmountQLE.setSizePolicy(sizePolicy)
        self.GeneAmountQLE.setObjectName("GeneAmountQLE")
        self.horizontalLayout_5.addWidget(self.GeneAmountQLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.LocalMinL = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.LocalMinL.setObjectName("LocalMinL")
        self.horizontalLayout_9.addWidget(self.LocalMinL)
        self.LocalMinQLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocalMinQLE.sizePolicy().hasHeightForWidth())
        self.LocalMinQLE.setSizePolicy(sizePolicy)
        self.LocalMinQLE.setObjectName("LocalMinQLE")
        self.horizontalLayout_9.addWidget(self.LocalMinQLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.GlobalMinL = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.GlobalMinL.setObjectName("GlobalMinL")
        self.horizontalLayout_11.addWidget(self.GlobalMinL)
        self.GlobalMinQLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GlobalMinQLE.sizePolicy().hasHeightForWidth())
        self.GlobalMinQLE.setSizePolicy(sizePolicy)
        self.GlobalMinQLE.setObjectName("GlobalMinQLE")
        self.horizontalLayout_11.addWidget(self.GlobalMinQLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.bound0QLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bound0QLE.sizePolicy().hasHeightForWidth())
        self.bound0QLE.setSizePolicy(sizePolicy)
        self.bound0QLE.setObjectName("bound0QLE")
        self.horizontalLayout_10.addWidget(self.bound0QLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.bound1QLE = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bound1QLE.sizePolicy().hasHeightForWidth())
        self.bound1QLE.setSizePolicy(sizePolicy)
        self.bound1QLE.setObjectName("bound1QLE")
        self.horizontalLayout_8.addWidget(self.bound1QLE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
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
        self.ResultsGroupBox.setTitle(_translate("MainWindow", "Результаты"))
        self.IterationGroupBox.setTitle(_translate("MainWindow", "Итерации"))
        self.label_2.setText(_translate("MainWindow", "Количество итераций:"))
        self.Set1iterationCount.setText(_translate("MainWindow", "1"))
        self.Set10iterationCount.setText(_translate("MainWindow", "10"))
        self.Set100iterationCount.setText(_translate("MainWindow", "100"))
        self.Set1000iterationCount.setText(_translate("MainWindow", "1000"))
        self.pushButton_3.setText(_translate("MainWindow", "Рассчитать"))
        self.TableGroupBox.setTitle(_translate("MainWindow", "Таблица генов"))
        self.pushButton_2.setText(_translate("MainWindow", "Предыдущая"))
        self.label.setText(_translate("MainWindow", "Итерация:"))
        self.pushButton.setText(_translate("MainWindow", "Следующая"))
        self.SettingsGroupBox.setTitle(_translate("MainWindow", "Настройки"))
        self.label_5.setText(_translate("MainWindow", "Функция:"))
        self.label_4.setText(_translate("MainWindow", "Количество агентов:"))
        self.LocalMinL.setText(_translate("MainWindow", "Влияние собственного минимума"))
        self.GlobalMinL.setText(_translate("MainWindow", "Влияние глобального минимума"))
        self.label_9.setText(_translate("MainWindow", "Минимальное значение координаты:"))
        self.label_7.setText(_translate("MainWindow", "Максимальное значение координаты:"))
