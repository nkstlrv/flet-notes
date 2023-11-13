from flet import (
    UserControl,
    TextField,
    InputBorder,
    Page,
    ControlEvent,
    app,
    ThemeMode,
    WEB_BROWSER
)


class FletNotes(UserControl):

    def __init__(self):
        super().__init__()
        self.textfield = TextField(multiline=True, autofocus=True,
                                   border=InputBorder.NONE, min_lines=40, on_change=self.save_text,
                                   content_padding=30, cursor_color="gray")

    def save_text(self, e: ControlEvent):
        with open("save.txt", "w") as file:
            file.write(self.textfield.value)


    def load_text(self):
        try:
            with open("save.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            self.textfield.hint_text = "Welcome to the Flet Notes"


    def build(self) -> TextField:
        self.textfield.value = self.load_text()
        return self.textfield


def main(page: Page):
    page.title = "Flet Notes"
    page.scroll = True
    page.theme_mode = ThemeMode.SYSTEM
    page.window_width = 500
    page.window_height = 500
    page.add(FletNotes())


if __name__ == "__main__":
    app(target=main)
    # app(target=main, view=WEB_BROWSER)