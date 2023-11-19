import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



root = customtkinter.CTk()
root.geometry("500x350")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry1 = customtkinter.CTkEntry(master= frame, placeholder_text="List Name")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master= frame, placeholder_text="Leads")
entry2.pack(pady=12, padx=10)

root.mainloop()