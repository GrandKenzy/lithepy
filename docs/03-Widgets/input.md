# Widget Input

El módulo `ui/inputs.py` define la arquitectura de controles de entrada para formularios HTML5, estructurada en la clase base `InputBase` y el componente de campo de texto `Input`.

---

## ⚙️ Especificación Técnica

### 1. Clase Base `InputBase`

`InputBase` unifica el comportamiento de cualquier elemento `<input>` (`CLOSE = False`). Sirve como cimiento para todos los tipos de entrada:

```python
class InputBase(Widget):
    TAG: str = 'input'
    CLOSE: bool = False
    INPUT_TYPE: str = 'text'

    def __init__(
        self,
        *,
        name: str | None = None,
        value: str | None = None,
        disabled: bool = False,
        required: bool = False,
        autofocus: bool = False,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```

### 2. Clase `Input` (Tipo Texto)

`Input` representa campos de entrada de texto de una sola línea (`<input type="text">`):

```python
class Input(InputBase):
    INPUT_TYPE: str = 'text'

    def __init__(
        self,
        *,
        name: str | None = None,
        value: str | None = None,
        placeholder: str | None = None,
        readonly: bool = False,
        required: bool = False,
        disabled: bool = False,
        autofocus: bool = False,
        minlength: int | None = None,
        maxlength: int | None = None,
        size: int | None = None,
        pattern: str | None = None,
        autocomplete: Autocomplete | str | None = None,
        spellcheck: bool | None = None,
        inputmode: InputMode | None = None,
        list: str | None = None,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```

---

## 📋 Parámetros de `Input`

| Parámetro | Tipo | Requerido | Descripción |
| :--- | :--- | :--- | :--- |
| `name` | `str \| None` | No | Nombre del campo con el que se envía el valor en la petición HTTP. |
| `value` | `str \| None` | No | Valor inicial cargado en el campo. |
| `placeholder` | `str \| None` | No | Texto de indicación que se muestra cuando el campo está vacío. |
| `readonly` | `bool` | No | El campo es de solo lectura; su valor no puede editarse pero se envía en el formulario. |
| `required` | `bool` | No | El navegador impide el envío si el campo se encuentra vacío. |
| `disabled` | `bool` | No | Deshabilita el control; el navegador no envía su valor al servidor. |
| `autofocus` | `bool` | No | Otorga foco automático al control tras cargar el documento. |
| `minlength` / `maxlength` | `int \| None` | No | Restricción de longitud mínima y máxima de caracteres permitidos. |
| `size` | `int \| None` | No | Ancho visible del campo en cantidad de caracteres. |
| `pattern` | `str \| None` | No | Expresión regular que el valor debe satisfacer para considerarse válido. |
| `autocomplete` | `str \| None` | No | Sugerencia para el motor de autocompletado (`'off'`, `'username'`, `'email'`, etc.). |
| `spellcheck` | `bool \| None` | No | Control del corrector ortográfico del navegador (`'true'` o `'false'`). |
| `inputmode` | `str \| None` | No | Tipo de teclado virtual en dispositivos móviles (`'numeric'`, `'email'`, `'tel'`, etc.). |
| `list` | `str \| None` | No | Identificador del elemento `<datalist>` con opciones sugeridas. |
| `form` | `str \| None` | No | Identificador del formulario padre cuando el control reside fuera de este. |
| `title` | `str \| None` | No | Mensaje explicativo, útil junto a `pattern` para describir el formato esperado. |

---

## ⚙️ Extensibilidad para Nuevos Tipos de Input

La arquitectura desacoplada de `InputBase` permite crear nuevos controles de formulario fijando el atributo de clase `INPUT_TYPE`:

```python
from ui.inputs import InputBase

class Checkbox(InputBase):
    INPUT_TYPE = 'checkbox'

    def __init__(self, checked: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.checked = checked

    def attributes(self):
        attrs = super().attributes()
        attrs['checked'] = self.checked
        return attrs
```

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Normalización de `spellcheck`:** A diferencia de `disabled` o `required`, `spellcheck` es un atributo enumerado de HTML (`spellcheck="true"` o `spellcheck="false"`). Si se pasa `spellcheck=False`, `Input` lo convierte internamente a la cadena `'false'` para que el serializador de atributos no lo descarte.
2. **Validación de `pattern`:** Los caracteres especiales de expresiones regulares (por ejemplo `pattern="[0-9]{2,4}"`) se escapan de forma segura al serializarse como atributo HTML, evitando rupturas de comillas.

---

## 💡 Ejemplo de Uso

```python
import ui

campo_codigo = ui.Input(
    name='codigo_verificacion',
    placeholder='000-000',
    pattern=r'\d{3}-\d{3}',
    title='Formato requerido: 123-456',
    maxlength=7,
    required=True,
    inputmode='numeric',
    autocomplete='one-time-code',
    spellcheck=False,
    class_names=['input-codigo'],
    css_styles={'letter-spacing': '2px', 'text-align': 'center'}
)
```
