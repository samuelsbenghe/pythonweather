class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_data(self):
        return self.model.data

    def update_data(self):
        self.model.data = "Button Clicked!"
        self.view.label.config(text=self.get_data())