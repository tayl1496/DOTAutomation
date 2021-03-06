# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from util import scrape, list_to_excel


class Ui_DotAutomation(object):
    def __init__(self, DotAutomation):
        self.centralwidget = QtWidgets.QWidget(DotAutomation)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_layout = QtWidgets.QGridLayout()
        self.step4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.step2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.run_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.step3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.url_input = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.step1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)

    def get_input_items(self):
        text = self.plainTextEdit.toPlainText()
        items = text.split()
        return items

    def _run_btn_clicked(self):
        list_to_excel(scrape(self.url_input.text(), self.get_input_items()))

    def setupUi(self, DotAutomation):
        DotAutomation.setObjectName("DotAutomation")
        DotAutomation.resize(576, 293)
        DotAutomation.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 541, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.grid_layout.setContentsMargins(-1, 1, -1, -1)
        self.grid_layout.setVerticalSpacing(18)
        self.grid_layout.setObjectName("grid_layout")

        self.step4.setObjectName("step4")
        self.grid_layout.addWidget(self.step4, 7, 0, 1, 1)

        self.label.setObjectName("label")
        self.grid_layout.addWidget(self.label, 5, 0, 1, 1)

        self.step2.setObjectName("step2")
        self.grid_layout.addWidget(self.step2, 2, 0, 1, 1)

        self.run_btn.setObjectName("run_btn")
        self.run_btn.clicked.connect(self._run_btn_clicked)
        self.grid_layout.addWidget(self.run_btn, 8, 0, 1, 1)

        self.step3.setObjectName("step3")
        self.grid_layout.addWidget(self.step3, 4, 0, 1, 1)

        self.url_input.setText("")
        self.url_input.setDragEnabled(True)
        self.url_input.setReadOnly(False)
        self.url_input.setClearButtonEnabled(False)
        self.url_input.setObjectName("url_input")
        self.grid_layout.addWidget(self.url_input, 3, 0, 1, 1)

        self.step1.setObjectName("step1")
        self.grid_layout.addWidget(self.step1, 1, 0, 1, 1)

        self.label_2.setObjectName("label_2")
        self.grid_layout.addWidget(self.label_2, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.grid_layout, 0, 0, 1, 1)

        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        DotAutomation.setCentralWidget(self.centralwidget)

        self.retranslateUi(DotAutomation)
        QtCore.QMetaObject.connectSlotsByName(DotAutomation)

    def retranslateUi(self, DotAutomation):
        _translate = QtCore.QCoreApplication.translate
        DotAutomation.setWindowTitle(_translate("DotAutomation", "MainWindow"))
        self.step4.setText(_translate("DotAutomation", "Step 4: Hit Run"))
        self.label.setText(
            _translate("DotAutomation", "Step 3 Note: Separate numbers by a space")
        )
        self.step2.setText(
            _translate("DotAutomation", "Step 2: Enter URL into the box below")
        )
        self.run_btn.setText(_translate("DotAutomation", "Run"))
        self.step3.setText(
            _translate(
                "DotAutomation", "Step 3: Enter part numbers in text box on right"
            )
        )
        self.step1.setToolTip(
            _translate(
                "DotAutomation",
                "It is not item inquiry because that does not have updated "
                "item status",
            )
        )
        self.step1.setText(
            _translate(
                "DotAutomation", "Step 1: Navigate to Inventory Inquiry (I/C Inquiry)"
            )
        )
        self.label_2.setText(_translate("DotAutomation", "Ex) XBU11Z 2804-20 2853-20"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DotAutomation(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("DOT Automation")
    MainWindow.show()
    sys.exit(app.exec_())
