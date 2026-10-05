# Lithe

Lithe es un framework ligero en Python puro para crear aplicaciones de escritorio basadas en HTML5, CSS y JavaScript sin empaquetar Electron. En su lugar, utiliza el motor WebViewer integrado del sistema operativo (WebView2 en Windows, WKWebView en macOS y WebKitGTK en Linux).

---

## Características Principales

- **Python Puro:** Sin dependencias externas pesadas ni compilación compleja.
- **Alternativa Ligera a Electron:** Aprovecha el navegador web nativo del sistema operativo, reduciendo drásticamente el consumo de memoria RAM y el tamaño de los instaladores.
- **Árbol de Widgets Declarativo:** Componentes orientados a objetos (`Container`, `Label`, `Button`, `Input`, `Image`, `Link`, etc.) con identificadores únicos y clases CSS automáticas.
- **CSS Modular:** Generación de hojas de estilo separadas por contenedor y soporte para clases globales reutilizables (`core.Classes`).
- **Salida Transparente y Editable:** Todo el HTML y CSS generado es texto estándar y puede inspeccionarse o modificarse manualmente según las necesidades del proyecto.

---

## Inicio Rápido

```python
import ui
import main
import core

# 1. Definir estilos compartidos
core.Classes.add_class('boton-accion', {
    'background': '#2563eb',
    'color': 'white',
    'padding': '10px 16px',
    'border-radius': '6px',
    'border': 'none',
    'cursor': 'pointer'
})

# 2. Construir la interfaz
tarjeta = ui.Container(
    items=[
        ui.Label("Bienvenido a %bLithe%bc"),
        ui.Input(placeholder="Ingresa tu nombre", required=True),
        ui.Button("Continuar", class_names=['boton-accion'])
    ],
    width=360,
    height='auto',
    x=20,
    y=20
)

# 3. Compilar a archivos estáticos
main.compile_and_make('source')
```

Ejecuta tu script con Python 3.10+:

```bash
python app.py
```

El resultado se genera dentro de `source/index.html` y `source/css/`.

---

## Documentación Completa

La documentación técnica exhaustiva del proyecto se encuentra disponible en la carpeta [`docs/`](docs/):

* **[Portada de Documentación](docs/index.md)**
* **[01 - Introducción](docs/01-Introduccion/index.md):** [Instalación](docs/01-Introduccion/instalacion.md), [Conceptos](docs/01-Introduccion/conceptos.md) y [Primer Proyecto](docs/01-Introduccion/primer_proyecto.md).
* **[02 - Arquitectura](docs/02-Arquitectura/index.md):** [Widget Base](docs/02-Arquitectura/widget.md), [Pipeline de Compilación](docs/02-Arquitectura/compilacion.md), [Sistema de Estilos](docs/02-Arquitectura/estilos.md) y [Atributos HTML](docs/02-Arquitectura/atributos.md).
* **[03 - Catálogo de Widgets](docs/03-Widgets/index.md):** [Container](docs/03-Widgets/container.md), [Label](docs/03-Widgets/label.md), [Formato de Texto](docs/03-Widgets/formato_texto.md), [Input](docs/03-Widgets/input.md), [Button](docs/03-Widgets/button.md), [Image](docs/03-Widgets/image.md), [Link](docs/03-Widgets/link.md) y [Break](docs/03-Widgets/break.md).
* **[04 - Referencia Técnica](docs/04-Referencia/index.md):** [Catálogo de API](docs/04-Referencia/api.md) y [Diagnósticos y Errores](docs/04-Referencia/errores.md).
* **[05 - Visión y Hoja de Ruta](docs/05-Vision/index.md):** [Hoja de Ruta](docs/05-Vision/hoja_de_ruta.md) (Runtime nativo, macros JS, empaquetador multiplataforma).
* **[06 - English Documentation](docs/06-English/index.md):** [Architecture](docs/06-English/architecture.md), [Widgets](docs/06-English/widgets.md) and [Roadmap](docs/06-English/roadmap.md).

---

## Licencia

Distribuido bajo licencia MIT.
