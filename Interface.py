# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 780))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 680))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 680))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 431, 121))
        self.groupBox_2.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 431, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labeldeltaT = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labeldeltaT.sizePolicy().hasHeightForWidth())
        self.labeldeltaT.setSizePolicy(sizePolicy)
        self.labeldeltaT.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.labeldeltaT.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.labeldeltaT.setObjectName("labeldeltaT")
        self.gridLayout_4.addWidget(self.labeldeltaT, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.T_min = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_min.sizePolicy().hasHeightForWidth())
        self.T_min.setSizePolicy(sizePolicy)
        self.T_min.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.T_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.T_min.setObjectName("T_min")
        self.gridLayout_4.addWidget(self.T_min, 2, 0, 1, 1)
        self.T_max = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_max.sizePolicy().hasHeightForWidth())
        self.T_max.setSizePolicy(sizePolicy)
        self.T_max.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.T_max.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.T_max.setObjectName("T_max")
        self.gridLayout_4.addWidget(self.T_max, 2, 1, 1, 1)
        self.deltaT = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deltaT.sizePolicy().hasHeightForWidth())
        self.deltaT.setSizePolicy(sizePolicy)
        self.deltaT.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.deltaT.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.deltaT.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.deltaT.setObjectName("deltaT")
        self.gridLayout_4.addWidget(self.deltaT, 2, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(11, 386, 421, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.Atoms = QtWidgets.QRadioButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Atoms.sizePolicy().hasHeightForWidth())
        self.Atoms.setSizePolicy(sizePolicy)
        self.Atoms.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.Atoms.setObjectName("Atoms")
        self.gridLayout.addWidget(self.Atoms, 4, 0, 2, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 2, 1)
        self.line_Press = QtWidgets.QLineEdit(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Press.sizePolicy().hasHeightForWidth())
        self.line_Press.setSizePolicy(sizePolicy)
        self.line_Press.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.line_Press.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_Press.setObjectName("line_Press")
        self.gridLayout.addWidget(self.line_Press, 5, 1, 1, 1)
        self.Linear = QtWidgets.QRadioButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Linear.sizePolicy().hasHeightForWidth())
        self.Linear.setSizePolicy(sizePolicy)
        self.Linear.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.Linear.setObjectName("Linear")
        self.gridLayout.addWidget(self.Linear, 2, 0, 2, 1)
        self.NoLinear = QtWidgets.QRadioButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoLinear.sizePolicy().hasHeightForWidth())
        self.NoLinear.setSizePolicy(sizePolicy)
        self.NoLinear.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.NoLinear.setChecked(True)
        self.NoLinear.setObjectName("NoLinear")
        self.gridLayout.addWidget(self.NoLinear, 0, 0, 2, 1)
        self.sym = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sym.sizePolicy().hasHeightForWidth())
        self.sym.setSizePolicy(sizePolicy)
        self.sym.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.sym.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.sym.setObjectName("sym")
        self.gridLayout.addWidget(self.sym, 0, 1, 1, 1)
        self.line_sym = QtWidgets.QLineEdit(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_sym.sizePolicy().hasHeightForWidth())
        self.line_sym.setSizePolicy(sizePolicy)
        self.line_sym.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.line_sym.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_sym.setObjectName("line_sym")
        self.gridLayout.addWidget(self.line_sym, 1, 1, 2, 1)
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(11, 1, 431, 161))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.line_scf = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_scf.sizePolicy().hasHeightForWidth())
        self.line_scf.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(3)
        self.line_scf.setFont(font)
        self.line_scf.setStyleSheet("font: 25 italic 10pt \"Ubuntu\";")
        self.line_scf.setObjectName("line_scf")
        self.gridLayout_2.addWidget(self.line_scf, 1, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.gridLayout_2.addWidget(self.btn1, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.line_dynmat = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_dynmat.sizePolicy().hasHeightForWidth())
        self.line_dynmat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(3)
        self.line_dynmat.setFont(font)
        self.line_dynmat.setStyleSheet("font: 25 italic 10pt \"Ubuntu\";")
        self.line_dynmat.setObjectName("line_dynmat")
        self.gridLayout_2.addWidget(self.line_dynmat, 3, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.gridLayout_2.addWidget(self.btn2, 3, 1, 1, 1)
        self.texto1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.texto1.setGeometry(QtCore.QRect(450, 0, 750, 630))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto1.sizePolicy().hasHeightForWidth())
        self.texto1.setSizePolicy(sizePolicy)
        self.texto1.setMinimumSize(QtCore.QSize(745, 630))
        self.texto1.setMaximumSize(QtCore.QSize(750, 630))
        self.texto1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.texto1.setObjectName("texto1")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 590, 431, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn3 = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.btn3.setObjectName("btn3")
        self.horizontalLayout_2.addWidget(self.btn3)
        self.btn4 = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.btn4.setObjectName("btn4")
        self.horizontalLayout_2.addWidget(self.btn4)
        self.btn5 = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.btn5.setObjectName("btn5")
        self.horizontalLayout_2.addWidget(self.btn5)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 310, 141, 56))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Solid = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Solid.sizePolicy().hasHeightForWidth())
        self.Solid.setSizePolicy(sizePolicy)
        self.Solid.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.Solid.setChecked(True)
        self.Solid.setObjectName("Solid")
        self.gridLayout_3.addWidget(self.Solid, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.Molecule = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Molecule.sizePolicy().hasHeightForWidth())
        self.Molecule.setSizePolicy(sizePolicy)
        self.Molecule.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.Molecule.setObjectName("Molecule")
        self.gridLayout_3.addWidget(self.Molecule, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menuBar.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(parent=self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuView = QtWidgets.QMenu(parent=self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.sobre = QtGui.QAction(parent=MainWindow)
        self.sobre.setObjectName("sobre")
        self.ajuda = QtGui.QAction(parent=MainWindow)
        self.ajuda.setObjectName("ajuda")
        self.fechar = QtGui.QAction(parent=MainWindow)
        self.fechar.setObjectName("fechar")
        self.simetria = QtGui.QAction(parent=MainWindow)
        self.simetria.setObjectName("simetria")
        self.convert = QtGui.QAction(parent=MainWindow)
        self.convert.setObjectName("convert")
        self.tempU = QtGui.QAction(parent=MainWindow)
        self.tempU.setObjectName("tempU")
        self.tempS = QtGui.QAction(parent=MainWindow)
        self.tempS.setObjectName("tempS")
        self.tempH = QtGui.QAction(parent=MainWindow)
        self.tempH.setObjectName("tempH")
        self.tempG = QtGui.QAction(parent=MainWindow)
        self.tempG.setObjectName("tempG")
        self.tempA = QtGui.QAction(parent=MainWindow)
        self.tempA.setObjectName("tempA")
        self.Complete = QtGui.QAction(parent=MainWindow)
        self.Complete.setObjectName("Complete")
        self.menuFile.addAction(self.sobre)
        self.menuFile.addAction(self.ajuda)
        self.menuFile.addAction(self.fechar)
        self.menuTools.addAction(self.simetria)
        self.menuTools.addAction(self.convert)
        self.menuView.addAction(self.tempU)
        self.menuView.addAction(self.tempS)
        self.menuView.addAction(self.tempH)
        self.menuView.addAction(self.tempG)
        self.menuView.addAction(self.tempA)
        self.menuView.addAction(self.Complete)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Termoquimica"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Temperatura (Kelvin)"))
        self.labeldeltaT.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> &Delta; T</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", " T(min)"))
        self.label_4.setText(_translate("MainWindow", " T(max)"))
        self.T_min.setText(_translate("MainWindow", "0"))
        self.T_max.setText(_translate("MainWindow", "1000"))
        self.deltaT.setText(_translate("MainWindow", "10"))
        self.groupBox.setTitle(_translate("MainWindow", "Variáveis moleculares"))
        self.Atoms.setText(_translate("MainWindow", "Átomos/Íons"))
        self.label.setText(_translate("MainWindow", "Pressão (atm)"))
        self.line_Press.setText(_translate("MainWindow", "1"))
        self.Linear.setText(_translate("MainWindow", "Linear"))
        self.NoLinear.setText(_translate("MainWindow", "Não-linear"))
        self.sym.setText(_translate("MainWindow", "Número de simetria"))
        self.line_sym.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Insira o arquivo de saída do cálculo SCF"))
        self.label_7.setText(_translate("MainWindow", "Insira o arquivo de saida do cálculo dynmat.x"))
        self.btn3.setText(_translate("MainWindow", "Calcular"))
        self.btn4.setText(_translate("MainWindow", "Salvar"))
        self.btn5.setText(_translate("MainWindow", "Limpar"))
        self.Solid.setText(_translate("MainWindow", "Sólidos"))
        self.Molecule.setText(_translate("MainWindow", "Moléculas"))
        self.menuFile.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuTools.setTitle(_translate("MainWindow", "Ferramentas"))
        self.menuView.setTitle(_translate("MainWindow", "Visualizar"))
        self.sobre.setText(_translate("MainWindow", "Sobre"))
        self.ajuda.setText(_translate("MainWindow", "Ajuda"))
        self.fechar.setText(_translate("MainWindow", "Fechar"))
        self.simetria.setText(_translate("MainWindow", "Números de simetria"))
        self.convert.setText(_translate("MainWindow", "Fatores de conversão"))
        self.tempU.setText(_translate("MainWindow", "Temperatura x E_interna"))
        self.tempU.setShortcut(_translate("MainWindow", "F7"))
        self.tempS.setText(_translate("MainWindow", "Temperatura x Entropia"))
        self.tempS.setShortcut(_translate("MainWindow", "F8"))
        self.tempH.setText(_translate("MainWindow", "Temperatura x Entalpia"))
        self.tempH.setShortcut(_translate("MainWindow", "F9"))
        self.tempG.setText(_translate("MainWindow", "Temperatura x E_Gibbs"))
        self.tempG.setShortcut(_translate("MainWindow", "F10"))
        self.tempA.setText(_translate("MainWindow", "Temperatura x E_Helmholtz"))
        self.tempA.setShortcut(_translate("MainWindow", "F11"))
        self.Complete.setText(_translate("MainWindow", "Completo"))
        self.Complete.setShortcut(_translate("MainWindow", "F12"))