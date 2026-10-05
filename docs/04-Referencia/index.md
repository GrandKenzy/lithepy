# Referencia Técnica

Esta sección proporciona la especificación formal de la API pública de Lithe, así como la matriz detallada de diagnósticos, limitaciones operativas y casos de borde.

---

## 📋 Módulos y Especificaciones

* **[Catálogo de API](api.md):** Firmas completas, anotaciones de tipo, argumentos y valores de retorno de todas las clases y funciones de `core`, `ui` y `main`.
* **[Catálogo de Diagnósticos y Errores](errores.md):** Matriz de errores, consideraciones de ciclo de vida en memoria, comportamientos límite de serialización y medidas de mitigación.

---

## ⚙️ Estructura de Exportaciones Públicas

### Paquete `ui` (`from ui import ...`)

* **Clases Base:** `Widget`, `Container`, `Label`, `InputBase`
* **Widgets Visuales:** `Break`, `Image`, `Link`, `Button`, `Input`
* **Variantes de Texto:** `Strong`, `Bold`, `Italic`, `Emphasis`, `Underline`, `Small`, `Strike`, `Deleted`, `Inserted`, `Subscript`, `Superscript`, `Mark`
* **Funciones:** `compile`

### Paquete `core` (`from core import ...`)

* **Clases:** `Classes`
* **Módulos Internos:** `core.attrs` (`render_attributes`, `AttrValue`), `core.css` (`render_rule`), `core.layer` (`get`)

### Módulo Principal (`import main`)

* **Funciones:** `compile_and_make`
