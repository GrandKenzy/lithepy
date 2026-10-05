# Widget Image

El widget `Image` (`ui/image.py`) representa imágenes incrustadas (`<img>`). Como elemento vacío en HTML5, no posee etiqueta de cierre (`CLOSE = False`).

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from __future__ import annotations
from typing import Literal
from core.attrs import AttrValue
from ui.widget import Widget

Loading = Literal['lazy', 'eager']
Decoding = Literal['async', 'sync', 'auto']
CrossOrigin = Literal['anonymous', 'use-credentials']

class Image(Widget):
    TAG: str = 'img'
    CLOSE: bool = False

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
    ) -> None: ...
```

### Parámetros del Constructor

| Parámetro | Tipo | Requerido | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `src` | `str` | Sí | — | Ruta relativa o URL absoluta de la imagen. |
| `alt` | `str` | No | `''` | Texto alternativo de accesibilidad. Siempre se emite en el tag. |
| `width` | `int \| str \| None` | No | `None` | Ancho intrínseco (atributo HTML, ej. `120`). |
| `height` | `int \| str \| None` | No | `None` | Alto intrínseco (atributo HTML, ej. `40`). |
| `title` | `str \| None` | No | `None` | Mensaje contextual mostrado al posicionar el cursor. |
| `loading` | `'lazy' \| 'eager' \| None` | No | `None` | Control de carga diferida por el navegador. |
| `decoding` | `'async' \| 'sync' \| 'auto' \| None` | No | `None` | Sugerencia para la decodificación en segundo plano. |
| `srcset` | `str \| None` | No | `None` | Conjunto de fuentes para pantallas de alta densidad o responsivas. |
| `sizes` | `str \| None` | No | `None` | Condiciones de visualización para selección de fuentes en `srcset`. |
| `crossorigin` | `'anonymous' \| 'use-credentials' \| None` | No | `None` | Configuración CORS para la petición del recurso. |
| `css_styles` | `dict[str, str] \| None` | No | `None` | Reglas CSS aplicadas al ID de la imagen. |
| `class_names` | `list[str] \| None` | No | `None` | Clases CSS asignadas a la imagen. |
| `attributes` | `dict[str, AttrValue] \| None` | No | `None` | Atributos adicionales (`data-*`, etc.). |

---

## ⚙️ Dimensiones HTML vs. Estilos CSS

* **Atributos `width` y `height`:** Establecen la relación de aspecto intrínseca del elemento en el HTML sin unidad (ej. `width="120"`). Esto previene saltos acumulativos de diseño (*Cumulative Layout Shift - CLS*) antes de que la imagen descargue.
* **Estilos CSS (`css_styles`):** Controlan el renderizado visual responsivo (ej. `css_styles={'width': '100%', 'height': 'auto'}`).

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Garantía de Accesibilidad (`alt`):** El atributo `alt` siempre se emite, incluso si se pasa vacío (`alt=""`). Esto indica explícitamente a los lectores de pantalla que la imagen es decorativa, cumpliendo con la directiva WCAG 2.1.
2. **Copia de Archivos:** Lithe no mueve ni copia archivos multimedia hacia la carpeta de salida. Las rutas pasadas a `src` deben existir relativamente en la carpeta de destino o servirse desde un servidor web externo.

---

## 💡 Ejemplo de Uso

```python
import ui

logo = ui.Image(
    src='assets/logo.webp',
    alt='Logotipo oficial de la aplicación',
    width=240,
    height=80,
    loading='lazy',
    decoding='async',
    srcset='assets/logo.webp 1x, assets/logo@2x.webp 2x',
    css_styles={'max-width': '100%', 'border-radius': '4px'}
)

print(logo.compile())
```

Salida HTML:

```html
<img id="Image_0___Widget_0" src="assets/logo.webp" alt="Logotipo oficial de la aplicación" width="240" height="80" loading="lazy" decoding="async" srcset="assets/logo.webp 1x, assets/logo@2x.webp 2x">
```
