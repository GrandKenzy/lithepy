# Pipeline de Compilación

Este documento detalla el proceso de transformación que convierte el grafo de objetos en memoria en archivos HTML5 y CSS en el sistema de archivos.

---

## ⚙️ Especificación Técnica

El proceso de compilación consta de tres niveles de abstracción:

```
ui.widget.compile()  ──> Retorna tupla (fragmentos_html, mapa_css)
        │
        ▼
main.compile_and_make() ──> Coordina guardado de archivos y clases globales
        │
        ▼
core.layer.get()     ──> Ensambla el documento HTML completo
```

---

## ⚙️ 1. Compilación de Widgets (`ui.compile`)

Ubicado en `ui/widget.py`, evalúa los nodos raíz registrados:

```python
def compile() -> tuple[list[str], dict[str, str]]: ...
```

* **Retorno:**
  * `html: list[str]`: Lista de cadenas con el HTML compilado de cada elemento en `Widget.get_widgets()`.
  * `styles: dict[str, str]`: Mapa `{nombre_archivo: contenido_css}`.
* **Comportamiento:**
  * Inicializa `styles['styles.css'] = ''`.
  * Si el elemento es una instancia de `Container`, invoca `w.compile_all_styles()` y actualiza el diccionario con las hojas de estilo del contenedor y sus subcontenedores.
  * Si no es `Container`, anexa la regla de `w.compile_styles()` a `styles['styles.css']`.

---

## ⚙️ 2. Orquestador de Archivos (`main.compile_and_make`)

Ubicado en `main.py`, gestiona la persistencia en disco:

```python
def compile_and_make(folder_output: str = 'source') -> None: ...
```

### Parámetros

| Parámetro | Tipo | Requerido | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `folder_output` | `str` | No | `'source'` | Directorio de destino para la salida estática. |

### Flujo de Ejecución

1. Invoca `widget.compile()`.
2. Resuelve la ruta base mediante `pathlib.Path(folder_output)` y crea `folder_output/css/`.
3. Itera sobre cada clave de `css_output`, guarda el archivo `.css` y registra su ruta relativa (`css/<archivo>`).
4. Si `core.Classes.not_empty()` es verdadero, compila las clases globales en `folder_output/css/class.css` y agrega el enlace.
5. Invoca `core.layer.get()` pasando los enlaces CSS y los fragmentos de cuerpo HTML.
6. Escribe el documento final en `folder_output/index.html` con codificación UTF-8.

---

## ⚙️ 3. Generador del Documento HTML (`core.layer.get`)

Ubicado en `core/layer.py`, construye el documento HTML5 base:

```python
def get(
    lang: str = 'en',
    title: str = 'Document',
    metas: list[str] | None = None,
    css_links: list[str] | None = None,
    body: list[str] | None = None,
) -> str: ...
```

### Parámetros y Valores por Defecto

| Parámetro | Tipo | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- |
| `lang` | `str` | `'en'` | Código de idioma para el atributo `<html lang="...">`. |
| `title` | `str` | `'Document'` | Contenido de la etiqueta `<title>`. |
| `metas` | `list[str] \| None` | Meta tags por defecto (`viewport` y `charset="UTF-8"`). |
| `css_links` | `list[str] \| None` | `['styles.css']` si no se especifica. |
| `body` | `list[str] \| None` | `[]` | Lista de fragmentos HTML a intercalar dentro de `<body>`. |

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Orden de los `<link>` en `<head>`:** `compile_and_make` enlaza las hojas de estilo en el orden en que son generadas: primero las hojas de `Container` y `styles.css`, y por último `class.css`. La cascada de CSS otorga mayor prioridad a las reglas finales si la especificidad de los selectores coincide.
2. **Manejo de Enlaces Vacíos:** Si ningún widget raíz genera reglas CSS, `styles.css` se crea vacío en disco y se vincula en el `<head>` de todos modos.
3. **Soporte de Recursos Estáticos:** `compile_and_make()` no copia imágenes, fuentes ni scripts referenciados en los widgets (por ejemplo rutas en `Image(src='...')`). Estos deben copiarse manualmente o ubicarse de antemano dentro de la carpeta de destino.

---

## 💡 Ejemplo de Uso

```python
import ui
import main
import core

# Registro de clase global
core.Classes.add_class('alerta', {'color': 'red', 'font-weight': 'bold'})

# Elemento visual
ui.Container(
    items=[
        ui.Label("Operación crítica", class_names=['alerta']),
        ui.Button("Confirmar")
    ],
    width=300,
    height=120
)

# Compilación completa hacia directorio personalizado
main.compile_and_make('dist_app')
```
