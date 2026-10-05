from __future__ import annotations

from core.attrs import AttrValue
from ui.widget import Widget

LabelText = str | Widget | list[Widget | str]


class Label(Widget):
    TAG = 'p'

    def __init__(
        self,
        text: LabelText,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        self.text = text
        super().__init__(css_styles, class_names, attributes)
        self.fix()

    def _parts(self) -> list[Widget | str]:
        return self.text if isinstance(self.text, list) else [self.text]

    def children(self) -> list[Widget]:
        return [c for c in self._parts() if isinstance(c, Widget)]

    def content(self) -> str:

        return ''.join(
            c.compile() if isinstance(c, Widget) else self.format(str(c))
            for c in self._parts()
        )
