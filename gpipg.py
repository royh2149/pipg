from const_values import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Victim import Victim


class GPIPG(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        # specify dimensions
        self.setFixedWidth(WIDTH)
        self.setFixedHeight(HEIGHT)

        self.vbox = QVBoxLayout()  # main layout
        self.form = QFormLayout()  # the details' form
        self.form.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # create a title and add it to the main layout
        self.title = QLabel("<font color=blue>Enter Victim's Creds</font>")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(title_font)
        self.vbox.addWidget(self.title, Qt.AlignCenter)

        # add an instructing label to the main layout
        self.instruction = QLabel("<font color=green size=5><u><i>Leave fields blank to ignore</u></i></font>")
        self.instruction.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.instruction, Qt.AlignCenter)

        # add the rows of the various details to the form
        self.fname = QLineEdit()
        self.form.addRow(QLabel("<b>First Name:</b>"), self.fname)

        self.lname = QLineEdit()
        self.form.addRow(QLabel("<b>Last Name:</b>"), self.lname)

        self.moren = QLineEdit()
        self.form.addRow(QLabel("<b>More Names (name1,name2,...):</b>"), self.moren)

        self.email = QLineEdit()
        self.form.addRow(QLabel("<b>Email:</b>"), self.email)

        self.date_picker = QDateEdit()
        self.date_checkbox = QCheckBox("Use date?")  # to specify whether the date should be used
        hbox = QHBoxLayout()
        hbox.addWidget(self.date_picker)
        hbox.addWidget(self.date_checkbox)
        self.form.addRow(QLabel("<b>Birth Date:</b>"), hbox)

        self.pets = QLineEdit()
        self.form.addRow(QLabel("<b>Pets (pet1,pet2,...):</b>"), self.pets)

        self.file_output = QLineEdit()
        self.form.addRow(QLabel("<b>Output to file? Leave empty to ignore</b>"), self.file_output)

        self.reverse = QComboBox()
        self.reverse.addItems(["Yes", "No"])
        self.form.addRow(QLabel("<b>Reverse?<b>"), self.reverse)

        self.vbox.addLayout(self.form, Qt.AlignCenter)  # add the form to the main layout, centered

        # create the submit button
        self.submit = QPushButton("Generate Passwords")
        self.submit.clicked.connect(self.call_generate_passwords)
        self.vbox.addWidget(self.submit, Qt.AlignCenter)

        self.setLayout(self.vbox)

    def call_generate_passwords(self):
        victim = Victim()  # create the new victim

        # add the credentials. Strip each from spaces and update only those that were filled by the user
        victim.first_name = EMPTY if self.fname.text().strip() == "" else self.fname.text().lower().strip()
        victim.last_name = EMPTY if self.lname.text().strip() == "" else self.lname.text().lower().strip()
        victim.more_names = EMPTY if self.moren.text().strip() == "" else self.moren.text().lower().split(",")
        victim.email = EMPTY if self.email.text().strip() == "" else self.email.text().strip().lower().split("@")[0]
        victim.pets = EMPTY if self.pets.text().strip() == "" else self.pets.text().lower().split(",")

        # determine the entered date and whether it should be used to generate the passwords
        date_str = str(self.date_picker.date().day()) + "/" + str(self.date_picker.date().month()) + "/" + str(self.date_picker.date().year())
        victim.birth_date = EMPTY if not self.date_checkbox.isChecked() else date_str

        # decide whether the results should be saved in a file
        output_to_file = self.file_output.text().strip() != ""  # output result to file filename provided

        # generate the passwords
        passwords = victim.generate_passwords(self.reverse.currentText() == "Yes")

        # write the passwords to a file if necessary
        if output_to_file:
            output_file = open(self.file_output.text(), "w")  # open the file in write mode
            output_file.write(passwords)  # write the passwords to the file
            output_file.close()  # close the handle to the file

        # show the password on the graphical window
        viewer = PasswordsViewer(self.stacked_widget, passwords)
        self.stacked_widget.addWidget(viewer)
        self.stacked_widget.setCurrentWidget(viewer)


class PasswordsViewer(QWidget):
    def __init__(self, stacked_widget: QStackedWidget, passwords: str):
        super().__init__()
        self.stacked_widget = stacked_widget

        # specify dimensions
        self.setFixedWidth(WIDTH)
        self.setFixedHeight(HEIGHT)

        self.vbox = QVBoxLayout()  # create the main layout

        # add a title
        self.title = QLabel("<font color=blue>Your Passwords are Ready!</font>")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(title_font)
        self.vbox.addWidget(self.title, Qt.AlignCenter)

        # create the widget that shows the passwords
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)  # restrict editing
        self.text_view.setText(passwords)  # show the passwords
        self.vbox.addWidget(self.text_view, Qt.AlignCenter)

        # add a back and copy to clipboard buttons
        self.buttons = QHBoxLayout()
        self.back = QPushButton("Back")
        self.back.clicked.connect(lambda: self.stacked_widget.removeWidget(self))  # return to the previous window

        self.copy = QPushButton("Copy to Clipboard")
        self.copy.clicked.connect(self.copy_to_clipboard)
        self.buttons.addWidget(self.back)
        self.buttons.addWidget(self.copy)

        self.vbox.addLayout(self.buttons)  # add the new buttons to the layout
        self.setLayout(self.vbox)

    def copy_to_clipboard(self):  # copy the text_view text to the user's clipboard (Ctrl+A, Ctrl+C)
        QApplication.clipboard().setText(self.text_view.toPlainText())


if __name__ == '__main__':
    # create the application and add an icon
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)  # exit the program when the app is closed
    app.setWindowIcon(QIcon("lock_icon.png"))  # add an icon

    stackedWidget = QStackedWidget()  # create the stacked screen

    # set screen dimensions
    stackedWidget.setFixedWidth(WIDTH)
    stackedWidget.setFixedHeight(HEIGHT)

    # add a title
    stackedWidget.setWindowTitle(APP_NAME)

    mainWindow = GPIPG(stackedWidget)  # create the home screen

    # run the app
    stackedWidget.addWidget(mainWindow)
    stackedWidget.show()
    sys.exit(app.exec_())
