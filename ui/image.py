from __future__ import annotations

from typing import Literal

from core.attrs import AttrValue
from ui.widget import Widget

Loading = Literal['lazy', 'eager']
Decoding = Literal['async', 'sync', 'auto']
CrossOrigin = Literal['anonymous', 'use-credentials']


class Image(Widget):
    """Imagen: `<img>`."""

    TAG = 'img'
    CLOSE = False

    def __init__(
        self,
        src: str,
        alt: str = '',
        *,
        width: int | str | None = None,
        height: int | str | None = None,
        title: str | None = None,
        loading: Loading | None = None,
        decoding: Decoding | None = None,
        srcset: str | None = None,
        sizes: str | None = None,
        crossorigin: CrossOrigin | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        """
        Args:
            src: Ruta o URL de la imagen.
            alt: Texto alternativo (accesibilidad / si la imagen no carga).
            width, height: Tamaño intrínseco en píxeles (atributo HTML, sin 'px').
                Para tamaños CSS (%, rem, ...) usa `css_styles`.
            title: Texto que aparece al pasar el mouse.
            loading: 'lazy' difiere la carga hasta que la imagen sea visible.
            decoding: Pista al navegador sobre cómo decodificar.
            srcset, sizes: Imágenes responsivas.
            crossorigin: Política CORS para la petición de la imagen.
        """
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.title = title
        self.loading = loading
        self.decoding = decoding
        self.srcset = srcset
        self.sizes = sizes
        self.crossorigin = crossorigin
        super().__init__(css_styles, class_names, attributes)

    def attributes(self) -> dict[str, AttrValue]:
        return {
            'src': self.src,
            'alt': self.alt,  
            'width': self.width,
            'height': self.height,
            'title': self.title,
            'loading': self.loading,
            'decoding': self.decoding,
            'srcset': self.srcset,
            'sizes': self.sizes,
            'crossorigin': self.crossorigin,
        }
