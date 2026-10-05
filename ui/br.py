from ui.widget import Widget


class Break(Widget):
    TAG = 'br'

    def __init__(self, count: int = 1):
        self.count = count
        super().__init__()

    def compile(self) -> str:
        return '<br>' * self.count