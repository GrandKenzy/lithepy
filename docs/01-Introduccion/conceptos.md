# Conceptos

Este documento explica el modelo de funcionamiento de Lithe. Los detalles de implementación se encuentran en [Arquitectura](../02-Arquitectura/index.md).

---

## ⚙️ Widget

Un widget es una instancia de una subclase de `ui.Widget` que representa un elemento HTML. Cada clase define:

* `TAG`: la etiqueta HTML que genera (`'p'`, `'div'`, `'img'`, ...).
* `CLOSE`: `True` si el elemento tiene etiqueta de cierre (`<p>...</p>`), `False` si es un elemento vacío (`<img>`, `<input>`).

Todos los widgets aceptan tres parámetros comunes:

| Parámetro | Tipo | Efecto |
| :--- | :--- | :--- |
| `css_styles` | `dict[str, str] \| None` | Propiedades CSS propias del widget. Se escriben como una regla `#<id> { ... }`. |
| `class_names` | `list[str] \| None` | Clases CSS. Se escriben en el atributo `class` en el mismo orden, sin duplicados. |
| `attributes` | `dict[str, AttrValue] \| None` | Atributos HTML adicionales (`data-*`, `aria-*`, `onclick`, ...). |

---

## ⚙️ Árbol de widgets y widgets raíz

Los widgets se anidan pasándolos como contenido de otros:

* `Container(items=[...])` contiene cualquier widget.
* `Label([...])` y sus derivados (`Link`, `Button`, `Strong`, ...) aceptan una lista que mezcla texto y widgets.

Cada widget se registra al crearse en una lista global (`Widget._widgets`). Cuando un widget pasa a ser hijo de otro, el padre llama a `fix()`, que lo **retira** de esa lista. Por lo tanto, la lista global contiene únicamente los **widgets raíz**: los que no están dentro de ningún otro.

La compilación recorre solo los widgets raíz, en el orden en que se crearon. Cada raíz compila a su vez a sus hijos.

```python
a = ui.Label("A")            # raíz
b = ui.Label("B")            # raíz
c = ui.Container(items=[b])  # c es raíz; b deja de serlo

# Orden en el HTML: a, c (que contiene a b)
```

**Consecuencia práctica:** cualquier widget creado y no colocado dentro de otro aparece en la página como elemento de primer nivel.

---

## ⚙️ Identificadores

Cada widget recibe un identificador único en el momento de su creación, con el formato:

```
<NombreDeClase>_<n-ésimo de esa clase>___Widget_<n-ésimo global>
```

Ejemplo: el tercer widget creado en el programa, si es el primer `Label`, recibe `Label_0___Widget_2`.

El identificador se usa como atributo `id` del elemento HTML y como selector de su regla CSS (`#Label_0___Widget_2`). Como depende del orden de creación, cambia si se añaden o reordenan widgets antes que él.

---

## ⚙️ Compilación

`main.compile_and_make(carpeta)` ejecuta todo el proceso:

1. `ui.compile()` recorre los widgets raíz y obtiene:
   * una lista de fragmentos HTML (uno por raíz);
   * un diccionario `{nombre_de_archivo.css: contenido}`.
2. Se escribe cada hoja de estilo en `<carpeta>/css/`.
3. Si hay clases globales registradas con `core.Classes`, se escribe `<carpeta>/css/class.css`.
4. `core.layer.get()` envuelve el HTML en un documento completo con los `<link>` a las hojas de estilo, y se escribe `<carpeta>/index.html`.

---

## ⚙️ Dónde terminan los estilos

| Origen | Archivo de salida |
| :--- | :--- |
| `css_styles` de un widget raíz que no es `Container` | `css/styles.css` |
| `css_styles` de un `Container` y de sus hijos directos que no son `Container` | `css/<id_del_container>.css` |
| Clases registradas con `core.Classes.add_class()` | `css/class.css` |

Ver [Estilos](../02-Arquitectura/estilos.md) para el detalle completo, incluidas las limitaciones.

---

## ⚙️ Formato de texto en línea

Los textos de un `Label` (y sus derivados) admiten marcadores que se convierten en etiquetas HTML: `"%bnegrita%bc"` produce `<b>negrita</b>`. Ver [Formato de texto](../03-Widgets/formato_texto.md).
