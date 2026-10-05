# Catálogo de API

Este documento contiene la especificación formal de todas las clases, funciones y tipos públicos del framework Lithe.

---

## ⚙️ Módulo `main`

### `compile_and_make`

```python
def compile_and_make(folder_output: str = 'source') -> None:
```

Compila la totalidad de los widgets registrados en `Widget._widgets` y guarda el resultado en el directorio indicado.

* **Parámetros:**
  * `folder_output` (`str`): Ruta del directorio de destino. Valor por defecto: `'source'`.
* **Retorno:** `None`.
* **Efectos secundarios:** Crea carpetas en disco, escribe archivos `.css` y el archivo `index.html`.

---

## ⚙️ Paquete `core`

### `core.attrs.render_attributes`

```python
AttrValue = str | int | float | bool | None

def render_attributes(attrs: dict[str, AttrValue]) -> str:
```

Serializa un diccionario en una cadena de atributos HTML5 con valores escapados mediante `html.escape`.

* **Parámetros:**
  * `attrs` (`dict[str, AttrValue]`): Pares atributo-valor.
* **Retorno:** `str` (cadena iniciada con espacio en blanco para cada atributo o cadena vacía si no hay atributos).

---

### `core.css.render_rule`

```python
def render_rule(selector: str, styles: dict[str, str]) -> str:
```

Genera una regla CSS formateada.

* **Parámetros:**
  * `selector` (`str`): Selector CSS (por ejemplo, `#id` o `.clase`).
  * `styles` (`dict[str, str]`): Diccionario propiedad-valor.
* **Retorno:** `str` con el bloque CSS indentado.

---

### `core.class_css.Classes`

Registro centralizado en memoria de clases CSS compartidas.

```python
class Classes:
    _classes: dict[str, dict[str, str]] = {}

    @classmethod
    def add_class(cls, name: str, styles: dict[str, str]) -> None: ...

    @classmethod
    def compile(cls) -> str: ...

    @classmethod
    def not_empty(cls) -> bool: ...
```

---

### `core.layer.get`

```python
def get(
    lang: str = 'en',
    title: str = 'Document',
    metas: list[str] | None = None,
    css_links: list[str] | None = None,
    body: list[str] | None = None,
) -> str:
```

Genera el documento HTML5 completo integrando metadatos, hojas de estilo enlazadas y el cuerpo.

---

## ⚙️ Paquete `ui`

### `ui.widget.Widget`

```python
class Widget:
    TAG: str = 'unknown'
    CLOSE: bool = True

    _regs_: dict[str, int] = {}
    _wint: int = 0
    _widgets: list[Widget] = []

    def __init__(
        self,
        styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...

    @classmethod
    def get_widgets(cls) -> list[Widget]: ...

    def children(self) -> list[Widget]: ...
    def fix(self) -> Self: ...
    def add_class(self, name: str) -> None: ...
    def set_attribute(self, name: str, value: AttrValue = True) -> Self: ...
    def consume_identifier(self) -> str: ...
    def format(self, *contents: str) -> str: ...
    def attributes(self) -> dict[str, AttrValue]: ...
    def content(self) -> str: ...
    def compile_styles(self) -> str: ...
    def compile(self) -> str: ...
```

---

### `ui.widget.compile`

```python
def compile() -> tuple[list[str], dict[str, str]]:
```

Recorre los widgets registrados en `Widget._widgets` y retorna la tupla con los fragmentos HTML y el mapa de hojas de estilo.

---

### `ui.container.Container`

```python
def css_length(value: int | float | str) -> str: ...

class Container(Widget):
    TAG: str = 'div'

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
    ) -> None: ...

    def children(self) -> list[Widget]: ...
    def add(self, item: Widget | list[Widget]) -> Self: ...
    def compile_all_styles(self) -> dict[str, str]: ...

    @property
    def x(self) -> str: ...
    @x.setter
    def x(self, value: int | str) -> None: ...

    @property
    def y(self) -> str: ...
    @y.setter
    def y(self, value: int | str) -> None: ...

    @property
    def width(self) -> str: ...
    @width.setter
    def width(self, value: int | str) -> None: ...

    @property
    def height(self) -> str: ...
    @height.setter
    def height(self, value: int | str) -> None: ...
```

---

### `ui.label.Label` y Subclases

```python
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

Subclases semánticas en `ui/subs.py`:
* `Strong` (`<strong>`)
* `Bold` (`<b>`)
* `Italic` (`<i>`)
* `Emphasis` (`<em>`)
* `Underline` (`<u>`)
* `Small` (`<small>`)
* `Strike` (`<s>`)
* `Deleted` (`<del>`)
* `Inserted` (`<ins>`)
* `Subscript` (`<sub>`)
* `Superscript` (`<sup>`)
* `Mark` (`<mark>`)

---

### `ui.br.Break`

```python
class Break(Widget):
    TAG: str = 'br'

    def __init__(self, count: int = 1) -> None: ...
    def compile(self) -> str: ...
```

---

### `ui.image.Image`

```python
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
        loading: Literal['lazy', 'eager'] | None = None,
        decoding: Literal['async', 'sync', 'auto'] | None = None,
        srcset: str | None = None,
        sizes: str | None = None,
        crossorigin: Literal['anonymous', 'use-credentials'] | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```

---

### `ui.link.Link`

```python
class Link(Label):
    TAG: str = 'a'

    def __init__(
        self,
        text: LabelText,
        href: str,
        *,
        target: Literal['_self', '_blank', '_parent', '_top'] | str | None = None,
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

---

### `ui.button.Button`

```python
class Button(Label):
    TAG: str = 'button'

    def __init__(
        self,
        text: LabelText,
        *,
        type: Literal['button', 'submit', 'reset'] = 'button',
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

---

### `ui.inputs.InputBase` y `ui.inputs.Input`

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
        autocomplete: str | None = None,
        spellcheck: bool | None = None,
        inputmode: str | None = None,
        list: str | None = None,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ) -> None: ...
```
