# Programa ejemplo tomado de la pagina oficial del CustomTKinter
#   https://customtkinter.tomschimansky.com/

import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="Tocame!!!", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("Click")

app = App()
app.mainloop()