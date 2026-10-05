# Architecture and Pipeline Specification

This document details the internal runtime architecture of Lithe, component lifecycle management, and the compilation pipeline from Python objects to static HTML5/CSS artifacts.

---

## ⚙️ Widget Base Class & Lifecycle

All visual components inherit from `Widget` (`ui/widget.py`).

### Key Properties

* `TAG`: HTML element tag name (`'p'`, `'div'`, `'img'`, etc.).
* `CLOSE`: Boolean indicating if the tag requires a closing tag (`True` for `<p>`, `False` for `<img>`).
* `identifier`: Unique deterministic identifier generated at instantiation (`{ClassName}_{typeIndex}___Widget_{globalIndex}`).
* `styles`: Dictionary containing inline CSS rules compiled against the widget's ID selector (`#identifier { ... }`).
* `class_names`: List of CSS class names emitted in deterministic order without duplicates.
* `attrs`: Additional user-defined HTML attributes (`data-*`, `aria-*`, event handlers).

### Adoption Mechanism (`fix`)

1. Upon creation, every widget automatically registers itself into the global class list `Widget._widgets`.
2. When a parent container (such as `Container` or `Label`) receives children, it invokes `self.fix()`.
3. `fix()` recursively traverses child widgets and removes them from `Widget._widgets`.
4. As a result, `Widget.get_widgets()` only ever contains true **root** nodes of the DOM tree.

---

## ⚙️ Modular CSS Resolution

Lithe separates CSS styles across distinct scopes to ensure maintainability:

1. **Per-Widget ID Styles:** Emitted for any root non-container widget into `styles.css`.
2. **Container Modular Styles:** Each `Container` generates its own dedicated CSS file (`{Container.identifier}.css`). This file contains the container's geometry (`left`, `top`, `width`, `height`, `position`) and the rules of all its direct and nested non-container children.
3. **Global Reusable Classes:** Managed statically via `core.Classes.add_class(name, styles)`. Emitted to `css/class.css` when not empty.

### Measurement Units (`css_length`)

Values passed to geometric properties (`width`, `height`, `x`, `y`) are automatically normalized:
* Numerical types (`int`, `float`) receive `'px'` units (e.g., `250` becomes `'250px'`).
* String types (`'100%'`, `'auto'`, `'2rem'`) are preserved as-is.

---

## ⚙️ Attribute Serialization & Security

Attributes are processed via `core.attrs.render_attributes(attrs)`:

* **Boolean attributes:** `True` produces a standalone attribute (e.g., `' required'`), whereas `False` or `None` omits it entirely.
* **XSS Mitigation:** All string, integer, or float values are safely escaped using `html.escape(str(val), quote=True)`, preventing delimiter injection.

---

## ⚠️ Edge Cases

* **Orphan Widgets:** Widgets created without being passed into a parent container remain in `Widget._widgets` and will be emitted as top-level elements in `<body>`.
* **Shared Widget Instances:** Adding the exact same widget instance to two different containers will emit duplicated HTML IDs, violating HTML5 specifications. Always instantiate separate widget objects.
