# Lithe Framework Documentation (English)

Lithe is a pure Python framework designed to build HTML, CSS, and JavaScript-based desktop applications without bundling Electron. It leverages the operating system's built-in WebViewer component to produce lightweight, high-performance applications.

In its current stage, Lithe provides the **UI generation engine**: a declarative Python widget hierarchy (`ui`) and a core compilation subsystem (`core`) that emits standard HTML5 and modular CSS stylesheets to a target output folder.

---

## ⚙️ Core Architecture Overview

Lithe processes user-defined visual trees in three primary tiers:

| Subsystem | Location | Responsibility |
| :--- | :--- | :--- |
| Widgets | `ui/` | Object-oriented representation of HTML elements (`Label`, `Container`, `Image`, `Link`, `Button`, `Input`, etc.). |
| Core | `core/` | Zero-dependency utilities: CSS rule rendering, HTML attribute escaping, document templating, and global CSS class registry. |
| Pipeline Orchestrator | `main.py` | `compile_and_make()` function coordinating widget compilation and disk serialization. |

Compilation workflow:

```
Python Code (ui.Container, ui.Label, ...)
   │
   ▼
Global Registry Widget._widgets (Root nodes only)
   │  ui.compile()
   ▼
HTML string per root node + CSS dictionary {filename.css: content}
   │  main.compile_and_make()
   ▼
Output Directory:
  ├── index.html
  └── css/
      ├── styles.css
      ├── <Container_id>.css
      └── class.css
```

---

## 📋 Documentation Sections

* **[Architecture & Compilation Pipeline](architecture.md):** Deep dive into the lifecycle, identifier assignment, `fix()` adoption, and CSS compilation.
* **[Widget Catalog & API](widgets.md):** Comprehensive reference for all visual components, parameters, and HTML attributes.
* **[Vision & Roadmap](roadmap.md):** Long-term architectural goals, native WebView runtime, JavaScript macros, animations, and cross-platform packaging.

---

## 📦 Quick Start

From the root directory of the repository, create a Python file `app.py`:

```python
import ui
import main

# Define a root layout container
ui.Container(
    items=[
        ui.Label("Hello, %bLithe%bc!"),
        ui.Button("Click Me", class_names=['btn-primary']),
    ],
    width='auto',
    height='auto',
)

# Compile to static distribution folder
main.compile_and_make('dist')
```

Execute the script:

```bash
python app.py
```

The output will be generated inside `dist/index.html` and `dist/css/`.
