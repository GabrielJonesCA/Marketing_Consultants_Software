import sys
import customtkinter

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("Campaign Title Generator")

        # Create a combo box for the first part of the title
        self.combo_box = customtkinter.CTkComboBox(self, values=["SJ", "TR", "TGWSA", "KOA", "AHHTA", "IIKY", "GUE", "AFB", "SL"])
        self.combo_box.bind("<<ComboboxSelected>>", self.update_title)

        # Create a check box for the second part of the title
        self.check_box = customtkinter.CTkCheckBox(self, text="P")
        self.check_box.bind("<Button-1>", self.update_title)

        # Create a line edit for the fourth part of the title
        self.line_edit = customtkinter.CTkEntry(self)
        self.line_edit.bind("<KeyRelease>", self.update_title)

        # Create a label to display the generated title
        self.label = customtkinter.CTkLabel(self)

        # Create a button to copy the title to the clipboard
        self.copy_button = customtkinter.CTkButton(self, text="Copy title", command=self.copy_title)

        # Create a button to copy the ESN to the clipboard
        self.esn_button = customtkinter.CTkButton(self, text="Copy ESN", command=self.copy_esn)

        # Create a text edit for the additional text box
        self.text_edit = customtkinter.CTkTextbox(self, width=40, height=10)
        self.text_edit.bind("<KeyRelease>", self.update_title)  
        
        # Create a button to copy the contents of the text edit to the clipboard
        self.text_edit_copy_button = customtkinter.CTkButton(self, text="Copy", command=self.copy_text_edit)

        # Create a button to copy "0.23" to the clipboard
        self.button1 = customtkinter.CTkButton(self, text="Copy 0.23", command=self.copy_0_23)

        #layout of the user interface
        self.combo_box.grid(row=0, column=0, padx=10, pady=10)
        self.check_box.grid(row=1, column=0, padx=10, pady=10)
        self.line_edit.grid(row=2, column=0, padx=10, pady=10)
        self.label.grid(row=3, column=0, padx=10, pady=10)
        self.copy_button.grid(row=4, column=0, padx=10, pady=10)
        self.esn_button.grid(row=4, column=1, padx=10, pady=10)
        self.text_edit.grid(row=5, column=0, padx=10, pady=10)
        self.button1.grid(row=6, column=0, padx=10, pady=10)
        self.text_edit_copy_button.grid(row=6, column=1, padx=10, pady=10)

    def update_title(self, event=None):
        # Get the selected value from the combo box
        first_part = self.combo_box.get()

        # Get the value of the check box
        second_part = "P " if self.check_box.is_selected() else ""

        # Get the value from the line edit
        fourth_part = self.line_edit.get()

        # Generate the full title
        title = f"{first_part} {second_part}SPK G1 {fourth_part}"

        # Update the label with the generated title
        self.label.set_text(title)

    def copy_title(self):
        # Check if the label is empty
        if self.label.get_text():
            # Copy the title to the clipboard
            self.clipboard_set_text(self.label.get_text())
        else:
            # Display an alert
            self.label.set_text("No title generated yet")

    def copy_esn(self):
        esn_dict = {
            "SJ": "B00D8KZH0M",
            "TR": "B00BNPFXK8",
            "TGWSA": "B08NGRJ278",
            "KOA": "B09RN6G8GG",
            
        }

        esn_dictP = {
            "SJ": "1483982874",
            "TR": "148196156X",
            "TGWSA": "B08PJNXYMS",
            "KOA": "B0B1CHX4QY",
            
        }

        current_text = self.combo_box.get()

        if current_text in esn_dict and not self.check_box.is_selected():
            esn = esn_dict[current_text]
            self.clipboard_set_text(esn)
        elif current_text in esn_dictP and self.check_box.is_selected():
            esn = esn_dictP[current_text]
            self.clipboard_set_text(esn)
        else:
            self.label.set_text("N/A")

    def copy_text_edit(self):
        # Check if the text edit is empty
        if self.text_edit.get("1.0", "end-1c"):
            # Copy the contents of the text edit to the clipboard
            self.clipboard_set_text(self.text_edit.get("1.0", "end-1c"))
        else:
            # Display an alert
            self.label.set_text("No text to copy")

    def copy_0_23(self):

        self.clipboard_set_text("0.23")


if __name__ == "__main__":
    app = customtkinter.CTk()
    window = MainWindow()
    window.geometry("350x600")
    window.mainloop()
    sys.exit()
