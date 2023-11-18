from internal.gui.model import Model
from internal.gui.controller import Controller
from internal.gui.view import View


def main():
    model = Model()
    controller = Controller(model, None)
    view = View(controller)
    controller.view = view
    view.mainloop()


if __name__ == "__main__":
    main()
