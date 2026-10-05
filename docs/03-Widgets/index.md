# Catálogo de Widgets

Esta sección documenta la totalidad de los componentes visuales disponibles en el módulo `ui` de Lithe, detallando sus firmas, parámetros admitidos, etiquetas HTML generadas y casos de uso.

---

## ⚙️ Taxonomía y Jerarquía de Clases

Todos los elementos visuales derivan de la clase base `Widget`:

```
Widget (ui/widget.py)
  ├── Container (ui/container.py) ──> Contenedor en bloque <div>
  ├── Break (ui/br.py)            ──> Salto de línea <br>
  ├── Image (ui/image.py)         ──> Imagen embebida <img>
  ├── InputBase (ui/inputs.py)    ──> Elemento base para formularios <input>
  │     └── Input                 ──> Campo de texto <input type="text">
  └── Label (ui/label.py)         ──> Texto y contenedor en línea <p>
        ├── Link (ui/link.py)     ──> Enlace hipertexto <a>
        ├── Button (ui/button.py) ──> Botón interactivo <button>
        └── Variantes de formato de texto (ui/subs.py):
              ├── Strong          ──> <strong>
              ├── Bold            ──> <b>
              ├── Italic          ──> <i>
              ├── Emphasis        ──> <em>
              ├── Underline       ──> <u>
              ├── Small           ──> <small>
              ├── Strike          ──> <s>
              ├── Deleted         ──> <del>
              ├── Inserted        ──> <ins>
              ├── Subscript       ──> <sub>
              ├── Superscript     ──> <sup>
              └── Mark            ──> <mark>
```

---

## 📋 Resumen de Componentes

| Widget | Etiqueta | Cierre | Responsabilidad Principal |
| :--- | :--- | :--- | :--- |
| **[Container](container.md)** | `<div>` | Sí | Estructuración en bloque, posicionamiento (`x`, `y`, `width`, `height`) y agrupación de estilos. |
| **[Label](label.md)** | `<p>` | Sí | Párrafo base con soporte para texto enriquecido, marcadores y elementos anidados. |
| **[Formato de Texto](formato_texto.md)** | Varios | Sí | 12 variantes de `Label` para estilización semántica y marcadores rápidos (`%b`, `%s`, etc.). |
| **[Break](break.md)** | `<br>` | No | Inserción de saltos de línea repetibles mediante el parámetro `count`. |
| **[Image](image.md)** | `<img>` | No | Renderizado de imágenes con soporte para carga diferida (`loading`) y atributos responsivos. |
| **[Link](link.md)** | `<a>` | Sí | Enlace hipertexto con mitigación de seguridad automática (`noopener noreferrer`). |
| **[Button](button.md)** | `<button>` | Sí | Botón interactivo seguro por defecto (`type="button"`). |
| **[Input](input.md)** | `<input>` | No | Entrada de texto de una línea y clase base extensible para futuros tipos de control. |
