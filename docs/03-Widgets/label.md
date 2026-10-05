# Widget Label

El widget `Label` (`ui/label.py`) representa párrafos de texto (`<p>`) y actúa como la base para cualquier elemento que contenga texto enriquecido o componentes anidados en línea.

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from __future__ import annotations
from core.attrs import AttrValue
from ui.widget import Widget

LabelText = str | Widget | list[Widget | str]

class Label(Widget):
    TAG: str = 'p'

    def __init__(
        self,
        text: LabelText,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```

### Parámetros del Constructor

| Parámetro | Tipo | Requerido | Descripción |
| :--- | :--- | :--- | :--- |
| `text` | `LabelText` | Sí | Cadena simple, instancia de `Widget` o lista heterogénea de textos y widgets. |
| `css_styles` | `dict[str, str] \| None` | No | Reglas CSS aplicadas al ID del párrafo (`#Label_X___Widget_Y`). |
| `class_names` | `list[str] \| None` | No | Clases CSS asignadas al elemento. |
| `attributes` | `dict[str, AttrValue] \| None` | No | Atributos HTML adicionales para la etiqueta `<p>`. |

---

## ⚙️ Procesamiento de Contenido

El método `content()` procesa los fragmentos contenidos en `self.text` distinguiendo el tipo de dato:

```python
def content(self) -> str:
    return ''.join(
        c.compile() if isinstance(c, Widget) else self.format(str(c))
        for c in self._parts()
    )
```

1. **Fragmentos de Texto (`str`):** Se evalúan a través de `self.format()`, lo que permite sustituir marcadores como `%b` o `%s` por sus etiquetas correspondientes.
2. **Nodos Hijos (`Widget`):** Se compilan invocando directamente su método `compile()`. Esto garantiza que los atributos de los hijos (como enlaces con caracteres `%` en URLs) nunca sean alterados por el formateador de marcadores.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Auto-adopción (`fix`):** El constructor de `Label` ejecuta `self.fix()`. Cualquier widget pasado dentro de la lista `text` es retirado automáticamente de la lista global `Widget._widgets`, evitando que se renderice duplicado fuera del párrafo.
2. **Uso de HTML sin Procesar:** Si un string dentro de `text` contiene etiquetas HTML literales (por ejemplo, `"<span class='badge'>Nuevo</span>"`), Lithe las emitirá sin escapar en el cuerpo del párrafo. Si se requiere texto seguro proveniente de usuarios no confiables, debe sanitizarse externamente.
3. **Párrafos Vacíos:** Pasar `text=""` o `text=[]` genera un marcado `<p id="..."></p>` válido.

---

## 💡 Ejemplo de Uso

```python
import ui

# Mezcla de cadenas, marcadores y widgets anidados
parrafo = ui.Label(
    text=[
        "Bienvenido a ",
        ui.Strong("Lithe Framework"),
        ". Lee la ",
        ui.Link("guía rápida", "https://ejemplo.com/docs", new_tab=True),
        " para comenzar con %bPython%bc."
    ],
    class_names=['lead', 'texto-principal'],
    css_styles={'line-height': '1.6', 'color': '#333333'}
)

print(parrafo.compile())
```

Salida HTML generada:

```html
<p id="Label_0___Widget_2" class="lead texto-principal">Bienvenido a <strong id="Strong_0___Widget_0">Lithe Framework</strong>. Lee la <a id="Link_0___Widget_1" href="https://ejemplo.com/docs" target="_blank" rel="noopener noreferrer">guía rápida</a> para comenzar con <b>Python</b>.</p>
```
