# Clase Base Widget

La clase `Widget` (`ui/widget.py`) es la abstracción fundamental de la jerarquía visual de Lithe. Todo elemento renderizable en el DOM deriva de ella.

---

## ⚙️ Especificación Técnica

### Definición de la Clase

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
```

### Atributos de Instancia

| Atributo | Tipo | Descripción |
| :--- | :--- | :--- |
| `identifier` | `str` | Identificador autogenerado único para el elemento (utilizado como `id` HTML y selector CSS). |
| `styles` | `dict[str, str]` | Diccionario clave-valor con propiedades CSS en línea aplicadas al ID del widget. |
| `class_names` | `list[str]` | Lista de nombres de clases CSS aplicadas al atributo `class` (sin duplicados, orden determinista). |
| `attrs` | `dict[str, AttrValue]` | Diccionario de atributos HTML adicionales proporcionados por el usuario. |
| `struct` | `dict[str, Any]` | Diccionario que contiene las claves `'tag'` (nombre del tag HTML) y `'close'` (booleano de cierre). |

---

## ⚙️ Ciclo de Vida y Registro Global

1. **Autoinscripción:** En el momento de la instanciación (`__init__`), el widget se añade automáticamente a `Widget._widgets`.
2. **Generación de ID (`consume_identifier`):**
   * Mantiene un contador por tipo de clase (`_regs_`) y un contador secuencial global (`_wint`).
   * Patrón generado: `{NombreClase}_{indiceClase}___Widget_{indiceGlobal}`.
3. **Adopción y Reclamación (`fix`):**
   * Cuando un widget contenedor (como `Container` o `Label`) recibe elementos hijos, invoca recursivamente `fix()` sobre ellos.
   * `fix()` retira a los hijos de la lista `Widget._widgets`. De esta manera, `Widget.get_widgets()` contiene únicamente los nodos raíz del árbol DOM.

```
[Instanciación w1] ──> Widget._widgets = [w1]
[Instanciación w2] ──> Widget._widgets = [w1, w2]
[Instanciación c1(items=[w1, w2])]
   └── c1.fix() retira w1 y w2 de Widget._widgets
   └── Resultado: Widget._widgets = [c1]
```

---

## ⚙️ Métodos Principales

| Método | Retorno | Propósito |
| :--- | :--- | :--- |
| `children()` | `list[Widget]` | Devuelve la lista de nodos hijos. En la clase base retorna una lista vacía `[]`. |
| `fix()` | `Self` | Recorre recursivamente `children()` para desregistrarlos de `_widgets`. |
| `add_class(name: str)` | `None` | Agrega una clase CSS si aún no está presente en `class_names`. |
| `set_attribute(name: str, value: AttrValue = True)` | `Self` | Establece un atributo HTML personalizado; admite encadenamiento. |
| `format(*contents: str)` | `str` | Reemplaza marcadores de texto en línea (`%b`, `%s`, etc.) por etiquetas HTML. |
| `attributes()` | `dict[str, AttrValue]` | Gancho para que las subclases suministren atributos nativos (`src`, `href`, `type`, etc.). |
| `content()` | `str` | Retorna el cuerpo interno del tag (entre apertura y cierre). |
| `compile_styles()` | `str` | Retorna la regla CSS `#identifier { ... }` o cadena vacía si `styles` está vacío. |
| `compile()` | `str` | Emite la etiqueta HTML final con atributos escapados y contenido interno. |

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Widgets Sueltos (Fuga de Raíz):** Si se instancia un widget pero se olvida incluirlo en un contenedor, permanecerá en `Widget._widgets` y se renderizará al final del `<body>`.
2. **Reasignación de Hijos Compartidos:** Si un mismo widget se agrega a dos contenedores distintos, el segundo contenedor no causa error, pero el widget se renderizará dos veces en el HTML manteniendo el mismo `id` duplicado en el DOM, lo cual viola la especificación HTML5.
3. **Persistencia en el Intérprete:** Como `_widgets`, `_regs_` y `_wint` son atributos de clase, permanecen en memoria a lo largo del proceso. Si se llama a `compile()` múltiples veces en una misma sesión interactiva sin reiniciar el proceso, los contadores seguirán incrementándose y los widgets anteriores seguirán compilándose a menos que se limpie `Widget._widgets.clear()`.

---

## 💡 Ejemplo de Uso

```python
import ui

# Instanciación y configuración dinámica
widget = ui.Widget(
    styles={'background-color': '#f3f4f6', 'padding': '12px'},
    class_names=['card', 'shadow'],
    attributes={'data-role': 'banner', 'aria-hidden': False}
)

widget.add_class('rounded')
widget.set_attribute('tabindex', 0)

# Compilación HTML
html = widget.compile()
# Retorna: <unknown id="Widget_0___Widget_0" class="card shadow rounded" data-role="banner" aria-hidden="false" tabindex="0"></unknown>

# Compilación CSS
css = widget.compile_styles()
# Retorna:
# #Widget_0___Widget_0 {
#     background-color : #f3f4f6;
#     padding : 12px;
# }
```
