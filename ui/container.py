from __future__ import annotations

from core.attrs import AttrValue
from ui.widget import Widget


def css_length(value: int | float | str) -> str:
    """Convierte números a píxeles (200 -> '200px'); los strings se dejan tal cual ('50%')."""
    if isinstance(value, (int, float)):
        return f'{value}px'
    return value


class Container(Widget):
    TAG = 'div'

    def __init__(
        self,
        items: list[Widget] | None = None,
        width: int | str = 200,
        height: int | str = 200,
        x: int | str = 0,
        y: int | str = 0,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        css_styles = css_styles or {}
        css_styles.setdefault('position', 'relative')
        css_styles['left'] = css_length(x)
        css_styles['top'] = css_length(y)
        css_styles['width'] = css_length(width)
        css_styles['height'] = css_length(height)

        self.items: list[Widget] = []
        super().__init__(css_styles, class_names, attributes)
        self.add(items or [])


    def children(self) -> list[Widget]:
        return list(self.items)

    def add(self, item: Widget | list[Widget]):
        """Agrega uno o varios widgets conservando el orden e ignorando duplicados."""
        for w in item if isinstance(item, list) else [item]:
            if w not in self.items:
                self.items.append(w)
        self.fix()
        return self


    def content(self) -> str:
        return '\n' + ''.join(f'    {c.compile()}\n' for c in self.children())

    def compile_all_styles(self) -> dict[str, str]:
        """Devuelve {archivo.css: contenido} para este contenedor y sus subcontenedores."""
        content = self.compile_styles() + '\n'
        styles: dict[str, str] = {}
        for c in self.children():
            if isinstance(c, Container):
                styles.update(c.compile_all_styles())
            elif rule := c.compile_styles():
                content += rule + '\n'

        styles[f'{self.identifier}.css'] = content
        return styles


    @property
    def x(self) -> str:
        return self.styles.get('left', '0px')

    @x.setter
    def x(self, value: int | str):
        self.styles['left'] = css_length(value)

    @property
    def y(self) -> str:
        return self.styles.get('top', '0px')

    @y.setter
    def y(self, value: int | str):
        self.styles['top'] = css_length(value)

    @property
    def width(self) -> str:
        return self.styles.get('width', '0px')

    @width.setter
    def width(self, value: int | str):
        self.styles['width'] = css_length(value)

    @property
    def height(self) -> str:
        return self.styles.get('height', '0px')

    @height.setter
    def height(self, value: int | str):
        self.styles['height'] = css_length(value)