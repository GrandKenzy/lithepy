# Widget Container

El widget `Container` (`ui/container.py`) representa divisiones en bloque (`<div>`). Es el componente central para estructurar layouts, posicionar elementos en la interfaz y modularizar hojas de estilo.

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from __future__ import annotations
from core.attrs import AttrValue
from ui.widget import Widget

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
```

### Parámetros del Constructor

| Parámetro | Tipo | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- |
| `items` | `list[Widget] \| None` | `None` | Lista ordenada de widgets hijos contenidos. |
| `width` | `int \| str` | `200` | Ancho del contenedor. Si es numérico se convierte a píxeles (`'200px'`). |
| `height` | `int \| str` | `200` | Alto del contenedor. Si es numérico se convierte a píxeles (`'200px'`). |
| `x` | `int \| str` | `0` | Desplazamiento horizontal (mapeado a `left` en CSS). |
| `y` | `int \| str` | `0` | Desplazamiento vertical (mapeado a `top` en CSS). |
| `css_styles` | `dict[str, str] \| None` | `None` | Reglas CSS adicionales aplicadas al contenedor. |
| `class_names` | `list[str] \| None` | `None` | Clases CSS asignadas al contenedor. |
| `attributes` | `dict[str, AttrValue] \| None` | `None` | Atributos HTML adicionales para el `<div>`. |

---

## ⚙️ Geometría y Posicionamiento

Al inicializarse, `Container` inyecta automáticamente en `self.styles`:

* `position`: Si no fue especificado previamente en `css_styles`, se establece por defecto como `'relative'`. Esto asegura que las propiedades `left` y `top` surtan efecto inmediato en el navegador.
* `left`: Calculado mediante `css_length(x)`.
* `top`: Calculado mediante `css_length(y)`.
* `width`: Calculado mediante `css_length(width)`.
* `height`: Calculado mediante `css_length(height)`.

### Propiedades Reactivas (`getters` y `setters`)

El contenedor expone propiedades dinámicas para ajustar la geometría después de su creación:

```python
contenedor = ui.Container(width=100, height=50)
contenedor.x = 20       # Actualiza self.styles['left'] = '20px'
contenedor.width = '80%' # Actualiza self.styles['width'] = '80%'
print(contenedor.width)  # Retorna: '80%'
```

---

## ⚙️ Jerarquía y Compilación Modular de CSS

### Método `add`

```python
def add(self, item: Widget | list[Widget]) -> Self: ...
```

Permite añadir uno o varios widgets tras la instanciación. Mantiene el orden de inserción estricto, evita duplicados y ejecuta automáticamente `self.fix()` sobre los nuevos elementos para retirarlos de la lista global de raíces.

### Compilación Modular (`compile_all_styles`)

A diferencia de otros widgets, `Container` no mezcla sus estilos en `styles.css`. En su lugar:

1. Crea una entrada `{Container.identifier}.css` en el diccionario de estilos.
2. Agrega sus propias reglas geométricas y de estilo.
3. Concatena los estilos de todos sus hijos directos que definan `styles` (a excepción de otros `Container`).
4. Si contiene subcontenedores, invoca recursivamente su método `compile_all_styles()`, generando un archivo CSS separado por cada subcontenedor.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Mutación de Diccionarios Externos:** El constructor aplica mutación sobre el diccionario pasado en `css_styles` mediante `css_styles['width'] = ...`. Si se pasa un diccionario compartido entre múltiples widgets, se recomienda pasar una copia `dict(estilos)`.
2. **Dimensiones Automáticas:** Si se requiere que el contenedor se ajuste naturalmente a su contenido sin altura fija, debe especificarse explícitamente `width='auto', height='auto'`, ya que los valores por defecto son `200` y `200`.

---

## 💡 Ejemplo de Uso

```python
import ui

panel = ui.Container(
    width='100%',
    height='auto',
    x=0,
    y=0,
    css_styles={'padding': '20px', 'background-color': '#fafafa'},
    class_names=['panel-principal']
)

panel.add([
    ui.Label("Título del Panel", css_styles={'font-size': '20px'}),
    ui.Button("Acción", class_names=['btn-primario'])
])
```
