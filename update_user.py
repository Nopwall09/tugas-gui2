from user import user
from role import role
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def getdatarole(self):
        data = role.select_data()
        self.role.addItems(data)

    def cari_user(self):
        username = self.cari.text()
        result = user.cari_user(username)
        if result:
            self.nama.setText(result[0])
            self.usn.setText(username)
            self.pw.setText(result[1])
            index = self.role.findText(result[2])
            self.role.setCurrentIndex(index)
        else:
            QtWidgets.QMessageBox.warning(None, "Tidak Ditemukan", f"User '{username}' tidak ditemukan.")

    def update_user(self):
        nama = self.nama.text()
        usn = self.usn.text()
        pw = self.pw.text()
        role_val = self.role.currentText()
        user.update_user(nama, usn, pw, role_val)
        QtWidgets.QMessageBox.information(None, "Berhasil", f"User '{usn}' berhasil diupdate.")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 420)
        MainWindow.setMinimumSize(QtCore.QSize(500, 420))
        MainWindow.setMaximumSize(QtCore.QSize(500, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.cari = QtWidgets.QLineEdit(self.centralwidget)
        self.cari.setGeometry(QtCore.QRect(20, 90, 200, 28))
        self.cari.setPlaceholderText("Cari Username")

        self.btnCari = QtWidgets.QPushButton(self.centralwidget)
        self.btnCari.setGeometry(QtCore.QRect(230, 90, 80, 28))
        self.btnCari.setText("Cari")
        self.btnCari.setObjectName("btnCari")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 130, 461, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")

        self.namaLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namaLabel)

        self.nama = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nama.setObjectName("nama")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nama)

        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)

        self.usn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usn.setObjectName("usn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usn)

        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)

        self.pw = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pw.setObjectName("pw")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pw)

        self.roleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roleLabel)

        self.role = QtWidgets.QComboBox(self.formLayoutWidget)
        self.role.setObjectName("role")
        self.role.addItems(["admin", "kasir"])
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.role)

        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(200, 310, 93, 28))
        self.submit.setStyleSheet("#submit {\n"
            "background-color: #0078d7;\n"
            "color: white;\n"
            "border-radius: 10px;\n"
            "border: none;\n"
            "padding: 6px 15px;\n"
        "}\n"
        "#submit:hover {\n"
            "background-color: #005fa3;\n"
        "}")
        self.submit.setObjectName("submit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnCari.clicked.connect(self.cari_user)
        self.submit.clicked.connect(self.update_user)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form User"))
        self.submit.setText(_translate("MainWindow", "Update"))
        self.namaLabel.setText(_translate("MainWindow", "Nama"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.roleLabel.setText(_translate("MainWindow", "Role"))
        self.label.setText(_translate("MainWindow", "Form User"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
