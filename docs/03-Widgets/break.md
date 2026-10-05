# Widget Break

El widget `Break` (`ui/br.py`) permite insertar uno o múltiples saltos de línea HTML consecutivos (`<br>`) en el documento.

---

## ⚙️ Especificación Técnica

### Definición y Firma

```python
from ui.widget import Widget

class Break(Widget):
    TAG: str = 'br'

    def __init__(self, count: int = 1) -> None: ...

    def compile(self) -> str:
        return '<br>' * self.count
```

### Parámetros del Constructor

| Parámetro | Tipo | Requerido | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `count` | `int` | No | `1` | Cantidad de etiquetas `<br>` consecutivas a emitir. |

---

## ⚙️ Comportamiento de Renderizado

A diferencia de los widgets convencionales, `Break` sobreescribe directamente `compile()` para generar cadenas repetidas del elemento vacío `<br>`:

* `Break(1).compile()` ──> `'<br>'`
* `Break(3).compile()` ──> `'<br><br><br>'`

Como el retorno consiste en una secuencia directa de etiquetas `<br>`, no incluye atributos `id`, `class` ni genera reglas en las hojas de estilo CSS.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Uso como Widget Raíz:** Si se instancia `Break(5)` fuera de un contenedor, se registrará en `Widget._widgets` y emitirá cinco saltos de línea al nivel raíz del `<body>`. Para espaciar elementos dentro de una sección, siempre debe agregarse a la lista `items` del `Container` correspondiente.
2. **Uso dentro de `Label`:** `Break` puede agregarse como elemento en la lista `text` de un `Label`:
   ```python
   ui.Label(["Primera línea", ui.Break(2), "Segunda línea"])
   ```
   El método `fix()` del `Label` adoptará el `Break`, desregistrándolo de la raíz y renderizando los saltos dentro del párrafo.
3. **Valores Menores o Iguales a Cero:** Si se pasa `count=0` o un número negativo, `compile()` retorna una cadena vacía `""`.

---

## 💡 Ejemplo de Uso

```python
import ui

# Separación visual entre dos secciones dentro de un contenedor
contenedor = ui.Container(
    items=[
        ui.Label("Encabezado de sección"),
        ui.Break(3),
        ui.Label("Contenido posterior con tres saltos de separación")
    ]
)
```
