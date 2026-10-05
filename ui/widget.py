from __future__ import annotations

from typing import Any

from core.attrs import AttrValue, render_attributes
from core.css import render_rule

FORMAT_MARKERS: tuple[tuple[str, str], ...] = (
    ('%inc', '</ins>'),
    ('%sbc', '</sub>'),
    ('%spc', '</sup>'),
    ('%mkc', '</mark>'),

    ('%sc', '</strong>'),
    ('%bc', '</b>'),
    ('%ec', '</em>'),
    ('%ic', '</i>'),
    ('%uc', '</u>'),
    ('%mc', '</small>'),
    ('%tc', '</s>'),
    ('%dc', '</del>'),
    ('%in', '<ins>'),
    ('%sb', '<sub>'),
    ('%sp', '<sup>'),
    ('%mk', '<mark>'),

    # Marcadores de 2 caracteres
    ('%s', '<strong>'),
    ('%b', '<b>'),
    ('%e', '<em>'),
    ('%i', '<i>'),
    ('%u', '<u>'),
    ('%m', '<small>'),
    ('%t', '<s>'),
    ('%d', '<del>'),
)


class Widget:
    TAG = 'unknown'
    CLOSE = True 

    _regs_: dict[str, int] = {}
    _wint = 0
    _widgets: list[Widget] = []

    def __init__(
        self,
        styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None:
        self.identifier = self.consume_identifier()
        self.styles = styles or {}
        self.class_names: list[str] = list(dict.fromkeys(class_names or ()))
        self.attrs: dict[str, AttrValue] = dict(attributes or {})
        self.struct: dict[str, Any] = {
            'tag': self.TAG,
            'close': self.CLOSE,
        }

        Widget._widgets.append(self)

    @classmethod
    def get_widgets(cls) -> list[Widget]:
        return cls._widgets

    def children(self) -> list[Widget]:
        return []

    def fix(self):
        """Quita a los hijos de la lista global para que solo se compile la raíz."""
        for c in self.children():
            c.fix()
            if c in self._widgets:
                self._widgets.remove(c)
        return self

    def add_class(self, name: str):
        if name not in self.class_names:
            self.class_names.append(name)

    def set_attribute(self, name: str, value: AttrValue = True):
        self.attrs[name] = value
        return self

    def consume_identifier(self) -> str:
        w = Widget._wint
        c = self.__class__.__name__

        i = Widget._regs_.get(c, 0)
        Widget._regs_[c] = i + 1
        Widget._wint += 1
        return f'{c}_{i}___Widget_{w}'

    # --- Compilación -----------------------------------------------------

    def format(self, *contents: str) -> str:
        content = ''.join(contents)
        for marker, tag in FORMAT_MARKERS:
            content = content.replace(marker, tag)
        return content

    def attributes(self) -> dict[str, AttrValue]:
        """Atributos HTML propios del widget. Las subclases lo sobrescriben."""
        return {}

    def content(self) -> str:
        return ''

    def compile_styles(self) -> str:
        if not self.styles:
            return ''
        return render_rule('#' + self.identifier, self.styles)

    def compile(self) -> str:
        tag = self.struct['tag']

        attrs: dict[str, AttrValue] = {'id': self.identifier}
        if self.class_names:
            attrs['class'] = ' '.join(self.class_names)
        attrs.update(self.attributes())
        attrs.update(self.attrs) 

        opening = f'<{tag}{render_attributes(attrs)}>'
        if not self.struct['close']:
            return opening
        return f'{opening}{self.content()}</{tag}>'


def compile() -> tuple[list[str], dict[str, str]]:
    from ui.container import Container

    html: list[str] = []
    styles: dict[str, str] = {'styles.css': ''}

    for w in Widget.get_widgets():
        html.append(w.compile())

        if isinstance(w, Container):
            styles.update(w.compile_all_styles())
        else:
            styles['styles.css'] += w.compile_styles() + '\n\n'

    return html, styles
