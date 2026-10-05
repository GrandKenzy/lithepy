# Formato de Texto en Línea

Lithe ofrece dos mecanismos complementarios para estilizar fragmentos de texto en línea: **marcadores compactos** (`%b`, `%s`, ...) y **subclases de Label** (`Strong`, `Mark`, etc.).

---

## ⚙️ 1. Sintaxis de Marcadores Compactos

Los marcadores permiten dar formato dentro de cadenas literales sin necesidad de instanciar objetos adicionales. Se procesan a través de `Widget.format()` utilizando la tabla ordenada `FORMAT_MARKERS`.

> ⚙️ **Principio de Reemplazo:** Los marcadores se evalúan en orden decreciente de longitud (4 caracteres, luego 3, luego 2) para evitar que delimitadores cortos capturen prefijos de marcadores más largos.

### Tabla Completa de Marcadores

| Formato Semántico | Marcador Apertura | Marcador Cierre | Etiqueta HTML |
| :--- | :--- | :--- | :--- |
| **Negrita semántica** | `%s` | `%sc` | `<strong>...</strong>` |
| **Negrita tipográfica** | `%b` | `%bc` | `<b>...</b>` |
| **Énfasis semántico** | `%e` | `%ec` | `<em>...</em>` |
| **Cursiva tipográfica** | `%i` | `%ic` | `<i>...</i>` |
| **Subrayado** | `%u` | `%uc` | `<u>...</u>` |
| **Texto pequeño** | `%m` | `%mc` | `<small>...</small>` |
| **Tachado** | `%t` | `%tc` | `<s>...</s>` |
| **Texto eliminado** | `%d` | `%dc` | `<del>...</del>` |
| **Texto insertado** | `%in` | `%inc` | `<ins>...</ins>` |
| **Subíndice** | `%sb` | `%sbc` | `<sub>...</sub>` |
| **Superíndice** | `%sp` | `%spc` | `<sup>...</sup>` |
| **Resaltado** | `%mk` | `%mkc` | `<mark>...</mark>` |

---

## ⚙️ 2. Subclases de `Label` (`ui/subs.py`)

Para fragmentos que requieren un identificador propio, clases CSS específicas o estilos en línea, se utilizan las subclases de `Label`:

```python
class Strong(Label): TAG = 'strong'
class Bold(Label): TAG = 'b'
class Italic(Label): TAG = 'i'
class Emphasis(Label): TAG = 'em'
class Underline(Label): TAG = 'u'
class Small(Label): TAG = 'small'
class Strike(Label): TAG = 's'
class Deleted(Label): TAG = 'del'
class Inserted(Label): TAG = 'ins'
class Subscript(Label): TAG = 'sub'
class Superscript(Label): TAG = 'sup'
class Mark(Label): TAG = 'mark'
```

Todas las clases heredan la firma y el comportamiento de `Label`:

```python
sub = ui.Strong("Texto destacado", class_names=['alerta'], css_styles={'color': 'red'})
```

---

## 📋 Comparativa: Marcadores vs. Widgets

| Característica | Marcadores (`%b...%bc`) | Subclases de `Label` (`Bold(...)`) |
| :--- | :--- | :--- |
| **Identificador (`id`) generado** | No | Sí (`#Strong_0___Widget_1`) |
| **Soporte de clases (`class_names`)** | No | Sí |
| **Soporte de estilos propios (`css_styles`)** | No | Sí |
| **Atributos personalizados (`attributes`)** | No | Sí |
| **Verbosidad en código** | Mínima | Declarativa |
| **Uso recomendado** | Formato de lectura simple | Elementos interactivos o estilizados |

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Marcadores sin Cerrar:** Si se omite el marcador de cierre (por ejemplo `"Texto %bnegrita"` sin `%bc`), la etiqueta `<b>` quedará abierta en el HTML, afectando la renderización de los elementos subsiguientes.
2. **Escape del Carácter `%`:** Si un texto contiene un signo de porcentaje seguido de una letra reservada (por ejemplo `"El descuento es del 20%b para socios"`), se transformará involuntariamente en `<b>`. Para evitarlo, separar los caracteres o utilizar la subclase correspondiente.

---

## 💡 Ejemplo de Uso

```python
import ui

texto = ui.Label([
    "Texto con %bnegrita%bc y %mkresaltado%mkc mediante marcadores, junto a un ",
    ui.Mark("resaltado interactivo", class_names=['resaltado-amarillo'], attributes={'title': 'Nota clave'}),
    " y una fórmula con H",
    ui.Subscript("2"),
    "O."
])

print(texto.compile())
```
