from __future__ import annotations

from typing import Literal

from core.attrs import AttrValue
from ui.label import Label, LabelText

Target = Literal['_self', '_blank', '_parent', '_top']


class Link(Label):
    """Enlace: `<a>`. El texto acepta lo mismo que `Label` (strings, marcadores y widgets)."""

    TAG = 'a'

    def __init__(
        self,
        text: LabelText,
        href: str,
        *,
        target: Target | str | None = None,
        new_tab: bool = False,
        rel: str | None = None,
        download: bool | str = False,
        title: str | None = None,
        hreflang: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        """
        Args:
            text: Contenido del enlace.
            href: URL destino (también '#seccion', 'mailto:...', 'tel:...').
            target: Dónde abrir el enlace.
            new_tab: Atajo para `target='_blank'`.
            rel: Relación con el destino. Si se abre en otra pestaña y no se
                indica, se usa 'noopener noreferrer' por seguridad.
            download: True para descargar el recurso, o un string con el
                nombre de archivo sugerido.
            title: Texto que aparece al pasar el mouse.
            hreflang: Idioma del recurso destino.
        """
        self.href = href
        self.target = '_blank' if new_tab else target
        self.rel = rel
        self.download = download
        self.title = title
        self.hreflang = hreflang
        super().__init__(text, css_styles, class_names, attributes)

    def attributes(self) -> dict[str, AttrValue]:
        rel = self.rel
        if rel is None and self.target == '_blank':
            rel = 'noopener noreferrer'
        return {
            'href': self.href,
            'target': self.target,
            'rel': rel,
            'download': self.download,
            'title': self.title,
            'hreflang': self.hreflang,
        }
