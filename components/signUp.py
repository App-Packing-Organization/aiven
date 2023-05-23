import sys
sys.path.add('/home/ketolumin/Dev/aiven')

import assets.bg_rcs
import assets.icon_rcs
import modules.db_manager as db
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog

# Do not UNIQUE the password
class SignUpGUI(QDialog):
    def __init__(self):
        super(SignUpGUI, self).__init__()
        uic.loadUi('../assets/signup_ui.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.login_button_.clicked.connect(self.verify_results)

    def verify_results(self):
        username = self.username_field_.text()
        password = self.password_field_.text()
        re_enter_password = self.repassword_field.text()

        # check if not empty
        if password == "" or re_enter_password == "":
            show_error_dialog(self, "Please fill in all fields.")
            return

        # check if password is the same
        if password != re_enter_password:
            show_error_dialog(self, "Passwords do not match.")
            return

        if not db.create_user(username, password):
            show_error_dialog(self, "Username already exists.")


def show_error_dialog(parent, message):
    error_dialog = QMessageBox(parent)
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(message)
    error_dialog.exec()


def main():
    app = QApplication([])
    window = SignUpGUI()
    app.exec()


if __name__ == '__main__':
    main()