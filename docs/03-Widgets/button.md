# Widget Button

El widget `Button` (`ui/button.py`) representa botones interactivos (`<button>`). Al heredar de `Label`, su texto admite marcadores y elementos anidados en su interior (iconos o imágenes).

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from __future__ import annotations
from typing import Literal
from core.attrs import AttrValue
from ui.label import Label, LabelText

ButtonType = Literal['button', 'submit', 'reset']

class Button(Label):
    TAG: str = 'button'

    def __init__(
        self,
        text: LabelText,
        *,
        type: ButtonType = 'button',
        name: str | None = None,
        value: str | None = None,
        disabled: bool = False,
        autofocus: bool = False,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```

### Parámetros del Constructor

| Parámetro | Tipo | Requerido | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `text` | `LabelText` | Sí | — | Contenido visible del botón (texto, marcadores o widgets anidados). |
| `type` | `'button' \| 'submit' \| 'reset'` | No | `'button'` | Comportamiento del botón. Por defecto `'button'` previene envíos accidentales. |
| `name` | `str \| None` | No | `None` | Nombre enviado con el formulario si este botón disparó el envío. |
| `value` | `str \| None` | No | `None` | Valor asociado a `name` al enviar el formulario. |
| `disabled` | `bool` | No | `False` | Deshabilita la interacción y el envío. |
| `autofocus` | `bool` | No | `False` | Enfoca automáticamente el botón al cargar la vista. |
| `form` | `str \| None` | No | `None` | Identificador (`id`) del formulario al que pertenece si está fuera del `<form>`. |
| `title` | `str \| None` | No | `None` | Texto de ayuda contextual al pasar el cursor. |
| `css_styles` | `dict[str, str] \| None` | No | `None` | Reglas CSS aplicadas al ID del botón. |
| `class_names` | `list[str] \| None` | No | `None` | Clases CSS asociadas al botón. |
| `attributes` | `dict[str, AttrValue] \| None` | No | `None` | Atributos adicionales (manejadores `onclick`, `data-*`, etc.). |

---

## ⚙️ Comportamiento Seguro por Defecto

En HTML estándar, cualquier etiqueta `<button>` sin el atributo `type` explícito se comporta como `type="submit"`, provocando recargas de página o envíos de formulario no deseados al hacer clic.

Lithe asigna por diseño `type='button'` de forma predeterminada. Para botones que deben enviar datos de formulario, el desarrollador debe indicar explícitamente `type='submit'`.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Botones Deshabilitados (`disabled`):** Si `disabled=True`, el botón emite el atributo booleano ` disabled` y no disparará eventos `onclick` en el navegador.
2. **Botón con Contenido Compuesto:** Es posible anidar una imagen dentro de un botón:
   ```python
   boton_icono = ui.Button([
       ui.Image("iconos/guardar.svg", alt=""),
       " Guardar Cambios"
   ])
   ```

---

## 💡 Ejemplo de Uso

```python
import ui

# Botón de acción con JavaScript en línea
boton_accion = ui.Button(
    "Calcular Totales",
    type='button',
    class_names=['btn', 'btn-primario'],
    css_styles={'cursor': 'pointer', 'font-weight': '600'},
    attributes={'onclick': "console.log('Calculando...')"}
)

# Botón de envío de formulario deshabilitado inicialmente
boton_envio = ui.Button(
    "Enviar Formulario",
    type='submit',
    name='accion',
    value='confirmar',
    disabled=True,
    form='form_registro'
)
```
