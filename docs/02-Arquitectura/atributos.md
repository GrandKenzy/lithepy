# Sistema de Atributos HTML

Lithe cuenta con un subsistema centralizado de serialización de atributos (`core/attrs.py`) diseñado para garantizar seguridad contra inyecciones XSS y conformidad estricta con la sintaxis HTML5.

---

## ⚙️ Especificación Técnica

### Definición de Tipos y Firma

```python
from html import escape

AttrValue = str | int | float | bool | None

def render_attributes(attrs: dict[str, AttrValue]) -> str: ...
```

### Reglas de Renderizado

| Tipo de Valor | Entrada de Ejemplo | Salida Renderizada | Explicación |
| :--- | :--- | :--- | :--- |
| `None` | `{'title': None}` | `""` (vacío) | El atributo se omite completamente del tag. |
| `False` | `{'disabled': False}` | `""` (vacío) | Los atributos booleanos falsos no se emiten. |
| `True` | `{'required': True}` | `" required"` | Emite el atributo booleano sin valor asignado. |
| `str`, `int`, `float` | `{'maxlength': 10}` | `' maxlength="10"'` | Emite `clave="valor"` con el valor sanitizado. |

---

## ⚙️ Sanitización y Seguridad (Escape HTML)

Todos los valores que se serializan como cadenas pasan obligatoriamente por:

```python
escape(str(value), quote=True)
```

Esto sustituye automáticamente los caracteres potencialmente peligrosos por sus entidades HTML correspondientes:

* `&` ──> `&amp;`
* `<` ──> `&lt;`
* `>` ──> `&gt;`
* `"` ──> `&quot;`
* `'` ──> `&#x27;`

Esto previene roturas de sintaxis en valores que contienen comillas o símbolos de comparación (por ejemplo, parámetros URL o expresiones regulares en `pattern`).

---

## ⚙️ Gestión Dinámica desde Widgets

Cualquier instancia de `Widget` expone la interfaz para modificar atributos:

1. **Parámetro del Constructor:** Mediante el argumento `attributes`:
   ```python
   btn = ui.Button("Guardar", attributes={'data-id': '42', 'aria-busy': False})
   ```
2. **Método Encadenable `set_attribute`:**
   ```python
   btn.set_attribute('disabled', True).set_attribute('title', 'Procesando...')
   ```

### Prevalencia y Prioridad

En la llamada a `Widget.compile()`, los atributos se fusionan en el siguiente orden estricto:

```python
attrs = {'id': self.identifier}
if self.class_names:
    attrs['class'] = ' '.join(self.class_names)
attrs.update(self.attributes())    # Atributos nativos del widget (ej. src, href)
attrs.update(self.attrs)           # Atributos personalizados pasados por el usuario
```

> ⚠️ Los atributos proporcionados por el usuario en `self.attrs` sobreescriben los atributos calculados por el widget, permitiendo ajustar o anular cualquier comportamiento por defecto.

---

## ⚠️ Consideraciones Críticas y Casos de Borde

1. **Atributos Enumerados vs. Booleanos:** En HTML existen atributos que no son booleanos sino enumerados, como `spellcheck="true"` o `spellcheck="false"`. Pasar `spellcheck=False` a `render_attributes` omitiría el atributo en lugar de emitir `' spellcheck="false"'`. Por esta razón, widgets como `Input` normalizan internamente estos campos a cadenas de texto antes de pasarlos al serializador.
2. **Eventos JavaScript en Línea:** Si se pasa un manejador como `attributes={'onclick': "alert('ok')"}` las comillas simples se convierten en `&#x27;`. Los navegadores modernos decodifican la entidad antes de ejecutar el script en el contexto del atributo, permitiendo que el script funcione correctamente.

---

## 💡 Ejemplo de Uso

```python
from core.attrs import render_attributes

atributos = {
    'id': 'usuario_input',
    'type': 'text',
    'required': True,
    'disabled': False,
    'placeholder': 'Ingrese su nombre & apellido',
    'data-limite': 50
}

cadena_html = render_attributes(atributos)
# Retorna:
# ' id="usuario_input" type="text" required placeholder="Ingrese su nombre &amp; apellido" data-limite="50"'
```
