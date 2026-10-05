# Sistema de Estilos CSS

Lithe implementa un generador de hojas de estilo desacoplado que separa las reglas por ámbito: estilos de instancia por identificador único, estilos agrupados por contenedor y clases globales reutilizables.

---

## ⚙️ Especificación Técnica

### Renderizado de Reglas (`core.css.render_rule`)

La función `render_rule` (`core/css.py`) es el formateador universal de bloques de estilo:

```python
def render_rule(selector: str, styles: dict[str, str]) -> str: ...
```

* **Comportamiento:** Transforma un diccionario en una regla CSS formateada con indentación de 4 espacios. Cada propiedad finaliza con `;`.
* **Formato emitido:**
  ```css
  <selector> {
      <propiedad> : <valor>;
  }
  ```

---

## ⚙️ Ámbitos de CSS

### 1. Estilos por Identificador Único (`Widget.compile_styles`)

Cuando un widget recibe `css_styles={'color': 'blue'}`, se genera una regla asociada exclusivamente a su `id`:

```python
# Ejemplo para un widget con ID Label_0___Widget_1
# #Label_0___Widget_1 {
#     color : blue;
# }
```

### 2. Estilos Agrupados por Contenedor (`Container.compile_all_styles`)

Para mantener el CSS modular, `Container` genera su propio archivo `.css`:

* **Nombre de archivo:** `{Container.identifier}.css` (por ejemplo, `Container_0___Widget_4.css`).
* **Contenido:**
  1. La regla CSS del propio contenedor.
  2. Las reglas de todos los widgets hijos directos o descendientes que no sean contenedores y que definan `styles`.
  3. Si un hijo es a su vez otro `Container`, este emite recursivamente su propio archivo `.css` independiente.

### 3. Clases Globales (`core.Classes`)

Ubicado en `core/class_css.py`, proporciona un registro estático para clases CSS reutilizables en cualquier elemento:

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

* **Salida:** Se compila en `css/class.css` cuando `not_empty()` es verdadero.
* **Prefijo:** Añade automáticamente el punto `.` al nombre de la clase como selector (`.nombre_clase { ... }`).

---

## ⚙️ Normalización de Medidas (`css_length`)

En `ui/container.py`, la función auxiliar `css_length` estandariza valores numéricos hacia unidades web válidas:

```python
def css_length(value: int | float | str) -> str:
    if isinstance(value, (int, float)):
        return f'{value}px'
    return value
```

* Si recibe enteros o decimales (`200`, `15.5`), añade automáticamente `'px'`.
* Si recibe cadenas de texto (`'50%'`, `'2rem'`, `'auto'`), las conserva intactas.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Hijos Dentro de `Label`:** Si un elemento en línea (como `Strong` o `Link`) dentro de un `Label` raíz define `css_styles`, su regla CSS no se emite a `styles.css` a menos que el `Label` contenedor esté dentro de un `Container`. Se recomienda estilizar texto en línea usando clases de `core.Classes`.
2. **Nombres de Clases con Caracteres Especiales:** `core.Classes.add_class()` concatena directamente `.` con el nombre proporcionado. No debe incluirse un punto en el argumento `name` (es decir, usar `'boton'`, no `'.boton'`).
3. **Manejo de Sintaxis de Propiedades:** Lithe no valida nombres de propiedades CSS. Si se pasa una clave inválida (por ejemplo, `'color-texto': 'rojo'`), se emitirá tal cual en el CSS sin advertencia en tiempo de ejecución.

---

## 💡 Ejemplo de Uso

```python
import core
import ui
import main

# 1. Definir estilos compartidos
core.Classes.add_class('sombra', {
    'box-shadow': '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
    'border-radius': '8px'
})

# 2. Contenedor con estilos propios y clase
tarjeta = ui.Container(
    items=[
        ui.Label("Contenido estilizado", css_styles={'color': '#1f2937'})
    ],
    width=350,
    height='auto',
    x=10,
    y=10,
    class_names=['sombra']
)

# Compila tarjeta -> css/Container_0___Widget_1.css y css/class.css
main.compile_and_make('salida_estilos')
```
