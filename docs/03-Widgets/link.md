# Widget Link

El widget `Link` (`ui/link.py`) representa enlaces de hipertexto (`<a>`). Hereda de `Label`, por lo que su contenido textual admite marcadores de formato (`%b`, `%s`, ...) y widgets hijos anidados.

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from __future__ import annotations
from typing import Literal
from core.attrs import AttrValue
from ui.label import Label, LabelText

Target = Literal['_self', '_blank', '_parent', '_top']

class Link(Label):
    TAG: str = 'a'

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
    ) -> None: ...
```

### Parámetros del Constructor

| Parámetro | Tipo | Requerido | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `text` | `LabelText` | Sí | — | Contenido visible del enlace (texto simple, marcadores o widgets). |
| `href` | `str` | Sí | — | Destino del enlace (URL web, ruta local, ancla `#seccion`, `mailto:`, `tel:`). |
| `target` | `Target \| str \| None` | No | `None` | Contexto de navegación (`'_blank'`, `'_self'`, etc.). |
| `new_tab` | `bool` | No | `False` | Atajo ergonómico que establece `target='_blank'`. |
| `rel` | `str \| None` | No | `None` | Relación con el destino. |
| `download` | `bool \| str` | No | `False` | Solicita la descarga del archivo. Si es una cadena, sugiere el nombre del archivo. |
| `title` | `str \| None` | No | `None` | Descripción contextual mostrada al pasar el cursor. |
| `hreflang` | `str \| None` | No | `None` | Código de idioma del documento enlazado (ej. `'es'`, `'en'`). |
| `css_styles` | `dict[str, str] \| None` | No | `None` | Reglas CSS aplicadas al ID del enlace. |
| `class_names` | `list[str] \| None` | No | `None` | Clases CSS asociadas al enlace. |
| `attributes` | `dict[str, AttrValue] \| None` | No | `None` | Atributos adicionales. |

---

## ⚙️ Mitigación Automática de Seguridad (`rel`)

Cuando un enlace se abre en una nueva pestaña (`target='_blank'` o `new_tab=True`), la ventana abierta podría tener acceso a `window.opener`, exponiendo a la aplicación a ataques de suplantación de identidad (*tabnabbing*).

Lithe evalúa automáticamente el atributo `rel` durante `attributes()`:

```python
rel = self.rel
if rel is None and self.target == '_blank':
    rel = 'noopener noreferrer'
```

Si el desarrollador no especifica un valor explícito en `rel`, Lithe asigna `'noopener noreferrer'` automáticamente.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Parámetros URL con Caracteres de Formato:** Las URLs que contienen secuencias como `%b`, `%e` o `%s` (comunes en parámetros codificados con *url-encoding*) se preservan intactas en `href` porque el formateador de marcadores solo procesa el contenido textual interno, no los atributos del widget.
2. **Descarga de Archivos (`download`):** Si se asigna `download=True`, se emite el atributo booleano ` download`. Si se asigna `download='reporte.pdf'`, se emite ` download="reporte.pdf"`.

---

## 💡 Ejemplo de Uso

```python
import ui

# Enlace externo seguro con contenido formateado
enlace_documentacion = ui.Link(
    text="Consultar el %bManual de Python%bc",
    href="https://docs.python.org/3/",
    new_tab=True,
    css_styles={'color': '#2563eb', 'text-decoration': 'none'}
)

# Enlace de descarga de archivo local
enlace_descarga = ui.Link(
    text="Descargar Instalador",
    href="binarios/app-setup.zip",
    download="Lithe-Setup.zip",
    class_names=['boton-descarga']
)
```
