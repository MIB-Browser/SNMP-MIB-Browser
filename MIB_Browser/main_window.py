# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './QtUI/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1542, 1020)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./QtUI/../resources/willow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mibTreeWidget = QtWidgets.QWidget(self.centralwidget)
        self.mibTreeWidget.setGeometry(QtCore.QRect(0, 0, 550, 971))
        self.mibTreeWidget.setObjectName("mibTreeWidget")
        self.snmpLabel = QtWidgets.QLabel(self.mibTreeWidget)
        self.snmpLabel.setGeometry(QtCore.QRect(0, 0, 550, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.snmpLabel.setFont(font)
        self.snmpLabel.setAutoFillBackground(False)
        self.snmpLabel.setStyleSheet("background-color: rgb(153, 180, 209);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 180, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.snmpLabel.setObjectName("snmpLabel")
        self.treeView = QtWidgets.QTreeView(self.mibTreeWidget)
        self.treeView.setGeometry(QtCore.QRect(0, 45, 550, 926))
        self.treeView.setIndentation(10)
        self.treeView.setAnimated(False)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1542, 24))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_operations = QtWidgets.QMenu(self.menubar)
        self.menu_operations.setObjectName("menu_operations")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.menu_bookmarks = QtWidgets.QMenu(self.menubar)
        self.menu_bookmarks.setObjectName("menu_bookmarks")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadMibs = QtWidgets.QAction(MainWindow)
        self.actionLoadMibs.setObjectName("actionLoadMibs")
        self.menu_file.addAction(self.actionLoadMibs)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_operations.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_bookmarks.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.snmpLabel.setText(_translate("MainWindow", "SNMP OIDs"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.menu_operations.setTitle(_translate("MainWindow", "Operations"))
        self.menu_tools.setTitle(_translate("MainWindow", "Tools"))
        self.menu_bookmarks.setTitle(_translate("MainWindow", "Bookmarks"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.actionLoadMibs.setText(_translate("MainWindow", "Load MIBs"))
