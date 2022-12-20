
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QCheckBox, QLineEdit, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Campaign Title Generator")

        # Set the window icon
        #self.setWindowIcon(QIcon("icon.png"))

        # Create a combo box for the first part of the title
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["SJ", "TR", "TGWSA", "KOA", "AHHTA", "IIKY", "GUE", "AFB", "SL"])
        self.combo_box.currentTextChanged.connect(self.update_title)

        # Create a check box for the second part of the title
        self.check_box = QCheckBox("P", self)
        self.check_box.stateChanged.connect(self.update_title)

        # Create a line edit for the fourth part of the title
        self.line_edit = QLineEdit(self)
        self.line_edit.textChanged.connect(self.update_title)

       
        # Create a label to display the generated title
        self.label = QLabel(self)

        # Create a button to copy the title to the clipboard
        self.copy_button = QPushButton("Copy title", self)
        self.copy_button.clicked.connect(self.copy_title)

         # Create a button to copy the ESN to the clipboard
        self.esn_button = QPushButton("Copy ESN", self)
        self.esn_button.clicked.connect(self.copy_esn)

        # Create a text edit for the additional text box
        self.text_edit = QTextEdit(self)
        self.text_edit.setLineWrapMode(QTextEdit.NoWrap)

        # Create a button to copy the contents of the text edit to the clipboard
        self.text_edit_copy_button = QPushButton("Copy", self)
        self.text_edit_copy_button.clicked.connect(self.copy_text_edit)


        # Create a button to copy "0.23" to the clipboard
        self.button1 = QPushButton("Copy 0.23", self)
        self.button1.clicked.connect(self.copy_0_23)

        # Create a button to copy "0.18" to the clipboard
        self.button2 = QPushButton("Copy 0.18", self)
        self.button2.clicked.connect(self.copy_0_18)

        # Set up the layout of the user interface
        self.combo_box.move(10, 10)
        self.check_box.move(10, 50)
        self.line_edit.move(10, 90)
        self.label.move(10, 130)
        self.copy_button.move(10, 170)
        self.esn_button.move(120, 170)
        self.text_edit.setGeometry(10, 220, 330, 220)
        self.button1.setGeometry(10, 490, 100, 30)
        self.button2.setGeometry(120, 490, 100, 30)
        self.text_edit_copy_button.setGeometry(10, 450, 50, 30)

        

        
    def update_title(self):
        # Get the selected value from the combo box
        first_part = self.combo_box.currentText()

        # Get the value of the check box
        second_part = "P " if self.check_box.isChecked() else ""

        # Get the value from the line edit
        fourth_part = self.line_edit.text()

        # Generate the full campaign title
        title = f"{first_part} {second_part}SPK G1 {fourth_part}"

        # Update the label with the generated title
        self.label.setText(title)

    def generate_title(self):
        self.update_title()

    def copy_title(self):
        # Check if the label is empty
        if self.label.text():
            # Copy the title to the clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(self.label.text())
        else:
            # Display an alert
            self.label.setText("No title generated yet")

    def copy_esn(self):
    # Create a dictionary that maps the values of the first part to the corresponding items in the array
        esn_dict = {
            "SJ": "B00D8KZH0M",
            "TR": "B00BNPFXK8",
            "TGWSA": "B08NGRJ278",
            "KOA": "B09RN6G8GG",
            "AHHTA": "B00ADAZ7FU",
            "IIKY": "B00RNHE4E6",
            "GUE": "B089FN9Y1Z",
            "AFB": "B0973KK3VD",
            "SL": "B08HG1SHW6"
        }

        esn_dictP = {
            "SJ": "1483982874",
            "TR": "148196156X",
            "TGWSA": "B08PJNXYMS",
            "KOA": "B0B1CHX4QY",
            "AHHTA": "1481125397",
            "IIKY": "150868068X",
            "GUE": "B08B1LN3VK",
            "AFB": "B09F1CVXVK",
            "SL": "B08HGTSXNT"
        }


        # Check if the first part of the title is "SJ" and the second part is empty
        if self.combo_box.currentText() in esn_dict and not self.check_box.isChecked():
            # Get the corresponding ESN from the dictionary
            esn = esn_dict[self.combo_box.currentText()]

            # Copy the ESN to the clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(esn)
        # Check if the first part of the title is "SJ" and the second part is P
        if self.combo_box.currentText() in esn_dictP and self.check_box.isChecked():
            # Get the corresponding ESN from the dictionary
            esn = esn_dictP[self.combo_box.currentText()]

            # Copy the ESN to the clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(esn)    
        else:
            # Display an alert
            esn = "N/A"
    def copy_text_edit(self):
    # Check if the text edit is empty
        if self.text_edit.toPlainText():
            # Copy the contents of the text edit to the clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(self.text_edit.toPlainText())
        else:
            # Display an alert
            self.label.setText("No text to copy")
    def copy_0_23(self):
        # Copy "0.23" to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText("0.23")

    def copy_0_18(self):
        # Copy "0.18" to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText("0.18")

#Main


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(0, 0, 350, 600)
    window.show()
    sys.exit(app.exec_())
    