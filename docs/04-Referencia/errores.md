# Catálogo de Diagnósticos y Errores

Este documento recopila las condiciones de error, advertencias de ciclo de vida en memoria, comportamientos límite y anomalías potenciales durante el uso de Lithe, indicando su subsistema de origen, causa fundamental y solución técnica recomendada.

---

## ⚙️ Matriz de Diagnósticos y Condiciones Críticas

| Código | Nivel | Subsistema | Causa Raíz | Solución Técnica |
| :--- | :--- | :--- | :--- | :--- |
| `LITHE_001` | Advertencia | Ciclo de Vida | Widget huérfano (instanciado pero no añadido a ningún `Container` o `Label`). Permanece en `Widget._widgets` y se renderiza en la raíz del documento. | Incluir siempre el widget en la lista `items` del contenedor o en el parámetro `text` del padre. |
| `LITHE_002` | Error Lógico | Identificadores | Widget compartido añadido a múltiples contenedores simultáneamente. Emite el mismo `id` repetido en el HTML. | Instanciar un objeto `Widget` independiente para cada ubicación en la interfaz. |
| `LITHE_003` | Advertencia | Sistema de Estilos | Estilos en línea (`css_styles`) definidos en widgets hijos de un `Label` raíz no se emiten a `styles.css`. | Ubicar el `Label` dentro de un `Container` o aplicar estilos mediante clases globales con `core.Classes`. |
| `LITHE_004` | Advertencia | Sistema de Archivos | Recompilación tras modificar la jerarquía visual deja archivos `.css` huérfanos con IDs de contenedores previos en la carpeta de salida. | Limpiar o vaciar la carpeta de salida (`source/css/`) antes de compilar una nueva versión de la interfaz. |
| `LITHE_005` | Error Sintaxis | Parser Marcadores | Marcador de apertura (ej. `%b`, `%s`) sin su respectivo cierre (`%bc`, `%sc`) en cadenas de texto. Deja etiquetas abiertas en el DOM. | Verificar que todo marcador de formato posea su correspondiente etiqueta de cierre. |
| `LITHE_006` | Advertencia | CSS / Geometría | `Container` instanciado sin dimensiones explícitas adquiere por defecto 200×200 píxeles fijos, provocando desbordamiento de contenido. | Especificar explícitamente `width='auto', height='auto'` cuando se desee ajuste automático al contenido. |
| `LITHE_007` | Advertencia | Estado Global | Ejecución repetida de `main.compile_and_make()` dentro de una misma sesión de Python acumula widgets en memoria sin reiniciar contadores. | Invocar `ui.Widget._widgets.clear()` o reiniciar el intérprete si se ejecuta de forma interactiva. |
| `LITHE_008` | Error Lógico | Clases Globales | Nombre de clase pasado a `core.Classes.add_class()` incluye un punto al inicio (ej. `'.mi-clase'`), generando selectores inválidos como `..mi-clase`. | Pasar el nombre de la clase sin punto inicial (ej. `'mi-clase'`). |

---

## ⚠️ Casos de Borde y Comportamientos de Diseño

### 1. Manejo de Inyección de HTML Literal

Lithe no escapa etiquetas HTML presentes dentro del cuerpo de texto de un `Label`:

```python
# Emite <script> intacto en el DOM
ui.Label("<script>alert('xss')</script>")
```

* **Mitigación:** Si el texto proviene de entradas de usuario no confiables o consultas externas, debe procesarse previamente mediante `html.escape()` antes de suministrarlo a `Label`. Los atributos de widgets, por el contrario, sí están protegidos por el serializador de `core.attrs`.

### 2. Mutación de Diccionarios de Estilo

`Container` modifica directamente el diccionario pasado al parámetro `css_styles` para inyectar `left`, `top`, `width`, `height` y `position`:

```python
estilos_comunes = {'background': 'white'}
c1 = ui.Container(css_styles=estilos_comunes, width=300)
# Ahora estilos_comunes contiene width: '300px'
```

* **Mitigación:** Pasar copias independientes `css_styles=dict(estilos_comunes)` al instanciar múltiples contenedores con estilos base compartidos.
