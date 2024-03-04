# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrderWindow(object):
    def setupUi(self, OrderWindow):
        OrderWindow.setObjectName("OrderWindow")
        OrderWindow.resize(1197, 803)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        OrderWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(OrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.leOrderNumber = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.leOrderNumber.setFont(font)
        self.leOrderNumber.setObjectName("leOrderNumber")
        self.horizontalLayout.addWidget(self.leOrderNumber)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.deDateOn = QtWidgets.QDateEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.deDateOn.setFont(font)
        self.deDateOn.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.deDateOn.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.deDateOn.setCalendarPopup(True)
        self.deDateOn.setObjectName("deDateOn")
        self.horizontalLayout.addWidget(self.deDateOn)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.cbOrderState = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cbOrderState.setFont(font)
        self.cbOrderState.setObjectName("cbOrderState")
        self.horizontalLayout.addWidget(self.cbOrderState)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.leCustomer = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.leCustomer.setFont(font)
        self.leCustomer.setObjectName("leCustomer")
        self.horizontalLayout_3.addWidget(self.leCustomer)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.leManager = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.leManager.setFont(font)
        self.leManager.setObjectName("leManager")
        self.horizontalLayout_3.addWidget(self.leManager)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.btnFilter = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFilter.sizePolicy().hasHeightForWidth())
        self.btnFilter.setSizePolicy(sizePolicy)
        self.btnFilter.setMinimumSize(QtCore.QSize(48, 48))
        self.btnFilter.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources/img/filter_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFilter.setIcon(icon)
        self.btnFilter.setIconSize(QtCore.QSize(48, 48))
        self.btnFilter.setCheckable(False)
        self.btnFilter.setObjectName("btnFilter")
        self.horizontalLayout_6.addWidget(self.btnFilter)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setContentsMargins(2, -1, 2, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddGood = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddGood.sizePolicy().hasHeightForWidth())
        self.btnAddGood.setSizePolicy(sizePolicy)
        self.btnAddGood.setMinimumSize(QtCore.QSize(60, 60))
        self.btnAddGood.setToolTipDuration(-1)
        self.btnAddGood.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("sources/img/cart_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddGood.setIcon(icon1)
        self.btnAddGood.setIconSize(QtCore.QSize(48, 48))
        self.btnAddGood.setObjectName("btnAddGood")
        self.verticalLayout.addWidget(self.btnAddGood)
        self.btnViewGood = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnViewGood.sizePolicy().hasHeightForWidth())
        self.btnViewGood.setSizePolicy(sizePolicy)
        self.btnViewGood.setMinimumSize(QtCore.QSize(60, 60))
        self.btnViewGood.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sources/img/cart_full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnViewGood.setIcon(icon2)
        self.btnViewGood.setIconSize(QtCore.QSize(48, 48))
        self.btnViewGood.setObjectName("btnViewGood")
        self.verticalLayout.addWidget(self.btnViewGood)
        self.btnDelGood = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelGood.sizePolicy().hasHeightForWidth())
        self.btnDelGood.setSizePolicy(sizePolicy)
        self.btnDelGood.setMinimumSize(QtCore.QSize(60, 60))
        self.btnDelGood.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("sources/img/cart_empty_bw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelGood.setIcon(icon3)
        self.btnDelGood.setIconSize(QtCore.QSize(48, 48))
        self.btnDelGood.setObjectName("btnDelGood")
        self.verticalLayout.addWidget(self.btnDelGood)
        self.btnReport = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReport.sizePolicy().hasHeightForWidth())
        self.btnReport.setSizePolicy(sizePolicy)
        self.btnReport.setMinimumSize(QtCore.QSize(60, 60))
        self.btnReport.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("sources/img/report1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReport.setIcon(icon4)
        self.btnReport.setIconSize(QtCore.QSize(48, 48))
        self.btnReport.setObjectName("btnReport")
        self.verticalLayout.addWidget(self.btnReport)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 5)
        self.horizontalLayout_7.addWidget(self.frame)
        self.tvGoods = QtWidgets.QTableView(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.tvGoods.setFont(font)
        self.tvGoods.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tvGoods.setProperty("showDropIndicator", False)
        self.tvGoods.setAlternatingRowColors(True)
        self.tvGoods.setCornerButtonEnabled(True)
        self.tvGoods.setObjectName("tvGoods")
        self.horizontalLayout_7.addWidget(self.tvGoods)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_2.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(1, 1)
        OrderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OrderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 21))
        self.menubar.setObjectName("menubar")
        OrderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OrderWindow)
        self.statusbar.setObjectName("statusbar")
        OrderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OrderWindow)
        QtCore.QMetaObject.connectSlotsByName(OrderWindow)

    def retranslateUi(self, OrderWindow):
        _translate = QtCore.QCoreApplication.translate
        OrderWindow.setWindowTitle(_translate("OrderWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("OrderWindow", "Фильтры"))
        self.label.setText(_translate("OrderWindow", "Номер заказа:"))
        self.label_5.setText(_translate("OrderWindow", "Дата оформления:"))
        self.label_6.setText(_translate("OrderWindow", "Статус заказа:"))
        self.label_3.setText(_translate("OrderWindow", "Контрагент:"))
        self.label_7.setText(_translate("OrderWindow", "Менеджер:"))
        self.btnFilter.setToolTip(_translate("OrderWindow", "Агрегация"))
        self.groupBox.setTitle(_translate("OrderWindow", "Товарные позиции"))
        self.btnAddGood.setToolTip(_translate("OrderWindow", "Добавить товар"))
        self.btnViewGood.setToolTip(_translate("OrderWindow", "Просмотр информации по товару"))
        self.btnDelGood.setToolTip(_translate("OrderWindow", "Удалить товар из заказа"))
        self.btnReport.setToolTip(_translate("OrderWindow", "Создать отчет по заказу"))
        self.btnOk.setText(_translate("OrderWindow", "Сохранить"))
        self.btnCancel.setText(_translate("OrderWindow", "Отмена"))
