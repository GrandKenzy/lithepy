# Introducción

Esta sección describe qué es Lithe, qué parte del framework está implementada hoy y cómo está organizado el repositorio.

---

## Propósito

Lithe permite describir una interfaz como un árbol de objetos Python y compilarla a HTML y CSS. Frente a escribir HTML y CSS a mano, aporta:

* **Estructura:** cada elemento es un objeto con parámetros tipados y documentados.
* **Identificadores automáticos:** cada widget recibe un `id` único que enlaza su HTML con su regla CSS.
* **Organización de estilos:** el CSS se reparte automáticamente entre archivos según la jerarquía de contenedores.
* **Valores seguros por defecto:** atributos escapados, `rel="noopener noreferrer"` en enlaces que abren otra pestaña, botones `type="button"`, etc.

El HTML y el CSS generados son archivos de texto normales y pueden editarse manualmente después de la compilación.

---

## Alcance actual

| Componente | Estado |
| :--- | :--- |
| API de widgets (`ui`) | Implementado |
| Generación de HTML y CSS | Implementado |
| Clases CSS globales | Implementado |
| Ventana nativa con WebView del sistema | Planificado |
| Generación de JavaScript y animaciones | Planificado |
| Empaquetado instalable (Windows, Linux, macOS) | Planificado |

Las funcionalidades planificadas se describen en [Visión](../05-Vision/index.md).

---

## Estructura del repositorio

```
lithe/
├── main.py              compile_and_make(): compila y escribe la salida
├── test.py              Script de ejemplo que usa todos los widgets
├── core/
│   ├── __init__.py      Exporta Classes
│   ├── attrs.py         render_attributes(), AttrValue
│   ├── css.py           render_rule()
│   ├── class_css.py     Classes: registro de clases CSS globales
│   └── layer.py         get(): plantilla del documento HTML
├── ui/
│   ├── __init__.py      Exporta todos los widgets y compile()
│   ├── widget.py        Widget (base), FORMAT_MARKERS, compile()
│   ├── label.py         Label, LabelText
│   ├── subs.py          Strong, Bold, Italic, ... (variantes de Label)
│   ├── container.py     Container, css_length()
│   ├── br.py            Break
│   ├── image.py         Image
│   ├── link.py          Link
│   ├── button.py        Button
│   └── inputs.py        InputBase, Input
└── source/              Salida generada por test.py
```

---

## Módulos y Especificaciones

* **[Instalación](instalacion.md):** requisitos de Python y forma de ejecutar el proyecto.
* **[Conceptos](conceptos.md):** modelo mental necesario para usar la API.
* **[Primer proyecto](primer_proyecto.md):** construcción guiada de una página completa.
