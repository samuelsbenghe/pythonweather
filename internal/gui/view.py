import tkinter as tk


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Weather App")
        self.geometry("800x600")

        self.label = tk.Label(self, text=self.controller.get_data(), font=("Helvetica", 32), pady=20)
        self.label.pack()

        self.button = tk.Button(self, text="Update", command=self.controller.update_data)
        self.button.pack()
