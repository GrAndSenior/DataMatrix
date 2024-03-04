# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LayoutWindow(object):
    def setupUi(self, LayoutWindow):
        LayoutWindow.setObjectName("LayoutWindow")
        LayoutWindow.setWindowModality(QtCore.Qt.WindowModal)
        LayoutWindow.resize(1278, 868)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        LayoutWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LayoutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbImage = QtWidgets.QLabel(self.centralwidget)
        self.lbImage.setText("")
        self.lbImage.setObjectName("lbImage")
        self.horizontalLayout.addWidget(self.lbImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbBlank = QtWidgets.QGroupBox(self.centralwidget)
        self.gbBlank.setObjectName("gbBlank")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbBlank)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.leBack = QtWidgets.QLineEdit(self.gbBlank)
        self.leBack.setMaxLength(255)
        self.leBack.setClearButtonEnabled(False)
        self.leBack.setObjectName("leBack")
        self.horizontalLayout_16.addWidget(self.leBack)
        self.btnOpenBack = QtWidgets.QToolButton(self.gbBlank)
        self.btnOpenBack.setMinimumSize(QtCore.QSize(30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources/img/add_box_3d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenBack.setIcon(icon)
        self.btnOpenBack.setObjectName("btnOpenBack")
        self.horizontalLayout_16.addWidget(self.btnOpenBack)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_29 = QtWidgets.QLabel(self.gbBlank)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_32.addWidget(self.label_29)
        self.leLabelWidth = QtWidgets.QLineEdit(self.gbBlank)
        self.leLabelWidth.setEnabled(True)
        self.leLabelWidth.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leLabelWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leLabelWidth.setObjectName("leLabelWidth")
        self.horizontalLayout_32.addWidget(self.leLabelWidth)
        self.label_38 = QtWidgets.QLabel(self.gbBlank)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_32.addWidget(self.label_38)
        self.leLabelHeight = QtWidgets.QLineEdit(self.gbBlank)
        self.leLabelHeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leLabelHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leLabelHeight.setObjectName("leLabelHeight")
        self.horizontalLayout_32.addWidget(self.leLabelHeight)
        self.horizontalLayout_32.setStretch(0, 3)
        self.horizontalLayout_32.setStretch(1, 1)
        self.horizontalLayout_32.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_27 = QtWidgets.QLabel(self.gbBlank)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_28.addWidget(self.label_27)
        self.leLeft = QtWidgets.QLineEdit(self.gbBlank)
        self.leLeft.setEnabled(True)
        self.leLeft.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leLeft.setMaxLength(4)
        self.leLeft.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leLeft.setObjectName("leLeft")
        self.horizontalLayout_28.addWidget(self.leLeft)
        self.label_32 = QtWidgets.QLabel(self.gbBlank)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_28.addWidget(self.label_32)
        self.leTop = QtWidgets.QLineEdit(self.gbBlank)
        self.leTop.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leTop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leTop.setObjectName("leTop")
        self.horizontalLayout_28.addWidget(self.leTop)
        self.horizontalLayout_28.setStretch(0, 3)
        self.horizontalLayout_28.setStretch(1, 1)
        self.horizontalLayout_28.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_28 = QtWidgets.QLabel(self.gbBlank)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_31.addWidget(self.label_28)
        self.leWidth = QtWidgets.QLineEdit(self.gbBlank)
        self.leWidth.setEnabled(True)
        self.leWidth.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leWidth.setObjectName("leWidth")
        self.horizontalLayout_31.addWidget(self.leWidth)
        self.label_36 = QtWidgets.QLabel(self.gbBlank)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_31.addWidget(self.label_36)
        self.leHeight = QtWidgets.QLineEdit(self.gbBlank)
        self.leHeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leHeight.setObjectName("leHeight")
        self.horizontalLayout_31.addWidget(self.leHeight)
        self.horizontalLayout_31.setStretch(0, 3)
        self.horizontalLayout_31.setStretch(1, 1)
        self.horizontalLayout_31.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_31)
        self.cbText = QtWidgets.QGroupBox(self.gbBlank)
        self.cbText.setCheckable(True)
        self.cbText.setChecked(False)
        self.cbText.setObjectName("cbText")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.cbText)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.cbText)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        self.leSampleText = QtWidgets.QLineEdit(self.cbText)
        self.leSampleText.setEnabled(False)
        self.leSampleText.setMaxLength(20)
        self.leSampleText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leSampleText.setClearButtonEnabled(True)
        self.leSampleText.setObjectName("leSampleText")
        self.horizontalLayout_19.addWidget(self.leSampleText)
        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.cbText)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.sbFontSize = QtWidgets.QSpinBox(self.cbText)
        self.sbFontSize.setEnabled(False)
        self.sbFontSize.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.sbFontSize.setMinimum(1)
        self.sbFontSize.setMaximum(48)
        self.sbFontSize.setProperty("value", 18)
        self.sbFontSize.setObjectName("sbFontSize")
        self.horizontalLayout_15.addWidget(self.sbFontSize)
        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_19 = QtWidgets.QLabel(self.cbText)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_25.addWidget(self.label_19)
        self.cbTextRotate = QtWidgets.QComboBox(self.cbText)
        self.cbTextRotate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbTextRotate.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cbTextRotate.setObjectName("cbTextRotate")
        self.cbTextRotate.addItem("")
        self.cbTextRotate.addItem("")
        self.cbTextRotate.addItem("")
        self.cbTextRotate.addItem("")
        self.horizontalLayout_25.addWidget(self.cbTextRotate)
        self.horizontalLayout_25.setStretch(0, 3)
        self.horizontalLayout_25.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_21 = QtWidgets.QLabel(self.cbText)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_26.addWidget(self.label_21)
        self.cbTextAllign = QtWidgets.QComboBox(self.cbText)
        self.cbTextAllign.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbTextAllign.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cbTextAllign.setObjectName("cbTextAllign")
        self.cbTextAllign.addItem("")
        self.cbTextAllign.addItem("")
        self.cbTextAllign.addItem("")
        self.cbTextAllign.addItem("")
        self.horizontalLayout_26.addWidget(self.cbTextAllign)
        self.horizontalLayout_26.setStretch(0, 3)
        self.horizontalLayout_26.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_25 = QtWidgets.QLabel(self.cbText)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_30.addWidget(self.label_25)
        self.leTextLeft = QtWidgets.QLineEdit(self.cbText)
        self.leTextLeft.setEnabled(False)
        self.leTextLeft.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leTextLeft.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leTextLeft.setObjectName("leTextLeft")
        self.horizontalLayout_30.addWidget(self.leTextLeft)
        self.label_37 = QtWidgets.QLabel(self.cbText)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_30.addWidget(self.label_37)
        self.leTextTop = QtWidgets.QLineEdit(self.cbText)
        self.leTextTop.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.leTextTop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leTextTop.setObjectName("leTextTop")
        self.horizontalLayout_30.addWidget(self.leTextTop)
        self.horizontalLayout_30.setStretch(0, 3)
        self.horizontalLayout_30.setStretch(1, 1)
        self.horizontalLayout_30.setStretch(3, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_30)
        self.verticalLayout_4.addWidget(self.cbText)
        self.verticalLayout.addWidget(self.gbBlank)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnPreView = QtWidgets.QPushButton(self.centralwidget)
        self.btnPreView.setObjectName("btnPreView")
        self.verticalLayout.addWidget(self.btnPreView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnDefault = QtWidgets.QPushButton(self.centralwidget)
        self.btnDefault.setEnabled(True)
        self.btnDefault.setObjectName("btnDefault")
        self.horizontalLayout_3.addWidget(self.btnDefault)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_3.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        LayoutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LayoutWindow)
        QtCore.QMetaObject.connectSlotsByName(LayoutWindow)

    def retranslateUi(self, LayoutWindow):
        _translate = QtCore.QCoreApplication.translate
        LayoutWindow.setWindowTitle(_translate("LayoutWindow", "Настройка параметров макета"))
        self.gbBlank.setTitle(_translate("LayoutWindow", "Настройка параметров макета этикетки:"))
        self.leBack.setPlaceholderText(_translate("LayoutWindow", "Файл шаблона этикетки"))
        self.btnOpenBack.setText(_translate("LayoutWindow", "..."))
        self.label_29.setText(_translate("LayoutWindow", "Размер этикетки:"))
        self.leLabelWidth.setText(_translate("LayoutWindow", "236"))
        self.label_38.setText(_translate("LayoutWindow", "X"))
        self.leLabelHeight.setText(_translate("LayoutWindow", "236"))
        self.label_27.setText(_translate("LayoutWindow", "Положение кода на шаблоне:"))
        self.leLeft.setText(_translate("LayoutWindow", "80"))
        self.label_32.setText(_translate("LayoutWindow", "Х"))
        self.leTop.setText(_translate("LayoutWindow", "80"))
        self.label_28.setText(_translate("LayoutWindow", "Размер кода DataMatrix:"))
        self.leWidth.setText(_translate("LayoutWindow", "100"))
        self.label_36.setText(_translate("LayoutWindow", "X"))
        self.leHeight.setText(_translate("LayoutWindow", "100"))
        self.cbText.setTitle(_translate("LayoutWindow", "Добавить текстовую надпись"))
        self.label_14.setText(_translate("LayoutWindow", "Текст:"))
        self.leSampleText.setText(_translate("LayoutWindow", "21XXXXXXX"))
        self.label_13.setText(_translate("LayoutWindow", "Размер шрифта:"))
        self.label_19.setText(_translate("LayoutWindow", "Вращение, град"))
        self.cbTextRotate.setItemText(0, _translate("LayoutWindow", "0"))
        self.cbTextRotate.setItemText(1, _translate("LayoutWindow", "90"))
        self.cbTextRotate.setItemText(2, _translate("LayoutWindow", "180"))
        self.cbTextRotate.setItemText(3, _translate("LayoutWindow", "270"))
        self.label_21.setText(_translate("LayoutWindow", "Выравнивание"))
        self.cbTextAllign.setItemText(0, _translate("LayoutWindow", "0"))
        self.cbTextAllign.setItemText(1, _translate("LayoutWindow", "90"))
        self.cbTextAllign.setItemText(2, _translate("LayoutWindow", "180"))
        self.cbTextAllign.setItemText(3, _translate("LayoutWindow", "270"))
        self.label_25.setText(_translate("LayoutWindow", "Положение надписи:"))
        self.leTextLeft.setText(_translate("LayoutWindow", "80"))
        self.label_37.setText(_translate("LayoutWindow", " : "))
        self.leTextTop.setText(_translate("LayoutWindow", "80"))
        self.btnPreView.setText(_translate("LayoutWindow", "Просмотр"))
        self.btnDefault.setText(_translate("LayoutWindow", "По умолчанию"))
        self.btnOk.setText(_translate("LayoutWindow", "Применить"))
        self.btnCancel.setText(_translate("LayoutWindow", "Отмена"))
