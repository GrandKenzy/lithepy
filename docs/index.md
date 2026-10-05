# Lithe

Lithe es un framework escrito en Python puro para construir interfaces basadas en HTML, CSS y JavaScript a partir de un árbol de objetos Python. El objetivo del proyecto es producir aplicaciones de escritorio ligeras que se rendericen con el componente WebView nativo del sistema operativo, sin empaquetar un navegador completo como hace Electron.

En su estado actual, Lithe implementa la capa de **generación de interfaz**: una API de widgets (`ui`) y un núcleo de utilidades (`core`) que compilan el árbol de widgets a un `index.html` y a un conjunto de hojas de estilo en una carpeta de salida. El proyecto no tiene todavía un número de versión publicado ni se distribuye como paquete instalable; se utiliza desde la raíz del repositorio.

> English version: [06-English](06-English/index.md)

---

## ⚙️ Arquitectura del Sistema

El sistema se organiza en tres bloques:

| Bloque | Ubicación | Responsabilidad |
| :--- | :--- | :--- |
| Widgets | `ui/` | Clases Python que representan elementos HTML (`Label`, `Container`, `Image`, `Link`, `Button`, `Input`, etc.). |
| Núcleo | `core/` | Utilidades sin dependencia de `ui`: generación de reglas CSS, renderizado de atributos HTML, plantilla de documento y registro de clases CSS globales. |
| Orquestación | `main.py` | Función `compile_and_make()`, que compila los widgets y escribe los archivos en disco. |

Flujo de información:

```
Código del usuario
   │  crea widgets (ui.Label, ui.Container, ...)
   ▼
Registro global Widget._widgets   (solo widgets raíz)
   │  ui.compile()
   ▼
HTML por widget raíz + dict {archivo.css: contenido}
   │  main.compile_and_make()
   ▼
<salida>/index.html
<salida>/css/styles.css
<salida>/css/<Container_id>.css
<salida>/css/class.css
```

---

## 📋 Mapa de Documentación

### 1. Introducción
* **[General](01-Introduccion/index.md):** Propósito, alcance actual y estructura del repositorio.
* **[Instalación](01-Introduccion/instalacion.md):** Requisitos y preparación del entorno.
* **[Conceptos](01-Introduccion/conceptos.md):** Árbol de widgets, widgets raíz, identificadores y compilación.
* **[Primer proyecto](01-Introduccion/primer_proyecto.md):** Tutorial paso a paso.

### 2. Arquitectura
* **[General](02-Arquitectura/index.md):** Pipeline de compilación y dependencias entre módulos.
* **[Widget](02-Arquitectura/widget.md):** Clase base, registro global y ciclo de vida.
* **[Compilación](02-Arquitectura/compilacion.md):** `ui.compile()`, `compile_and_make()` y `core.layer`.
* **[Estilos](02-Arquitectura/estilos.md):** CSS por widget, archivos por contenedor y clases globales.
* **[Atributos](02-Arquitectura/atributos.md):** Sistema de atributos HTML y escapado.

### 3. Widgets
* **[General](03-Widgets/index.md):** Catálogo y jerarquía de clases.
* **[Label](03-Widgets/label.md):** Párrafos con contenido mixto.
* **[Formato de texto](03-Widgets/formato_texto.md):** Marcadores `%b`, `%s`, ... y subclases `Strong`, `Bold`, etc.
* **[Container](03-Widgets/container.md):** Agrupación y geometría.
* **[Break](03-Widgets/break.md):** Saltos de línea.
* **[Image](03-Widgets/image.md):** Imágenes.
* **[Link](03-Widgets/link.md):** Enlaces.
* **[Button](03-Widgets/button.md):** Botones.
* **[Input](03-Widgets/input.md):** Campos de texto y base para otros tipos de `<input>`.

### 4. Referencia
* **[General](04-Referencia/index.md):** Índice de la referencia.
* **[API](04-Referencia/api.md):** Firmas completas de todos los módulos públicos.
* **[Errores y limitaciones](04-Referencia/errores.md):** Condiciones de fallo y casos de borde conocidos.

### 5. Visión
* **[General](05-Vision/index.md):** Objetivos del framework y deuda de complejidad.
* **[Hoja de ruta](05-Vision/hoja_de_ruta.md):** Funcionalidades planificadas.

### 6. English
* **[Overview](06-English/index.md):** English documentation home & quick start.
* **[Architecture](06-English/architecture.md):** Internal runtime architecture and compilation pipeline.
* **[Widget Catalog](06-English/widgets.md):** Complete component reference and parameters.
* **[Vision & Roadmap](06-English/roadmap.md):** Framework goals, complexity debt, and planned milestones.

---

## 📦 Inicio Rápido

Desde la raíz del repositorio, crear un archivo `app.py`:

```python
import ui
import main

ui.Container(
    items=[
        ui.Label("Hola, %bLithe%bc."),
        ui.Button("Aceptar"),
    ],
    width='auto',
    height='auto',
)

main.compile_and_make('source')
```

Ejecutar:

```bash
python app.py
```

El resultado se escribe en `source/index.html` y `source/css/`.
