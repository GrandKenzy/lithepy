# Widget Catalog Reference

This document provides a comprehensive technical reference for all UI components available in the `ui` package of Lithe.

---

## 📋 Component Overview

| Class | HTML Tag | Closing Tag | Description |
| :--- | :--- | :--- | :--- |
| `Container` | `<div>` | Yes | Block-level container with geometry management (`x`, `y`, `width`, `height`). |
| `Label` | `<p>` | Yes | Paragraph element supporting strings, markers, and nested inline widgets. |
| `Strong`, `Bold`, etc. | Various | Yes | 12 inline semantic subclasses of `Label`. |
| `Break` | `<br>` | No | Consecutive line break generator controlled by `count`. |
| `Image` | `<img>` | No | Void image element supporting responsive images and lazy loading. |
| `Link` | `<a>` | Yes | Hyperlink element with automatic tabnabbing security mitigation. |
| `Button` | `<button>` | Yes | Button element defaulting to safe `type="button"`. |
| `Input` | `<input>` | No | Single-line text input field and base class for future input types. |

---

## ⚙️ Detailed Widget Specifications

### 1. `Container` (`ui/container.py`)

```python
ui.Container(
    items: list[Widget] | None = None,
    width: int | str = 200,
    height: int | str = 200,
    x: int | str = 0,
    y: int | str = 0,
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

* **Geometry Mapping:** Automatically injects `position: relative`, `left`, `top`, `width`, and `height` into the container's styles.
* **Reactive Properties:** Exposes `.x`, `.y`, `.width`, and `.height` getters and setters.

### 2. `Label` & Text Formatting (`ui/label.py`, `ui/subs.py`)

```python
ui.Label(
    text: str | Widget | list[Widget | str],
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

* **Compact Text Markers:**
  * `%b...%bc` ──> `<b>...</b>`
  * `%s...%sc` ──> `<strong>...</strong>`
  * `%e...%ec` ──> `<em>...</em>`
  * `%i...%ic` ──> `<i>...</i>`
  * `%u...%uc` ──> `<u>...</u>`
  * `%m...%mc` ──> `<small>...</small>`
  * `%t...%tc` ──> `<s>...</s>`
  * `%d...%dc` ──> `<del>...</del>`
  * `%in...%inc` ──> `<ins>...</ins>`
  * `%sb...%sbc` ──> `<sub>...</sub>`
  * `%sp...%spc` ──> `<sup>...</sup>`
  * `%mk...%mkc` ──> `<mark>...</mark>`
* **Inline Subclasses:** `Strong`, `Bold`, `Italic`, `Emphasis`, `Underline`, `Small`, `Strike`, `Deleted`, `Inserted`, `Subscript`, `Superscript`, and `Mark`.

### 3. `Break` (`ui/br.py`)

```python
ui.Break(count: int = 1)
```

Emits `'<br>' * count` directly, omitting redundant IDs and classes.

### 4. `Image` (`ui/image.py`)

```python
ui.Image(
    src: str,
    alt: str = '',
    *,
    width: int | str | None = None,
    height: int | str | None = None,
    title: str | None = None,
    loading: Literal['lazy', 'eager'] | None = None,
    decoding: Literal['async', 'sync', 'auto'] | None = None,
    srcset: str | None = None,
    sizes: str | None = None,
    crossorigin: Literal['anonymous', 'use-credentials'] | None = None,
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

Always emits `alt` attribute (even if empty) to satisfy accessibility standards.

### 5. `Link` (`ui/link.py`)

```python
ui.Link(
    text: LabelText,
    href: str,
    *,
    target: Literal['_self', '_blank', '_parent', '_top'] | str | None = None,
    new_tab: bool = False,
    rel: str | None = None,
    download: bool | str = False,
    title: str | None = None,
    hreflang: str | None = None,
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

Automatically applies `rel="noopener noreferrer"` whenever `new_tab=True` or `target="_blank"`.

### 6. `Button` (`ui/button.py`)

```python
ui.Button(
    text: LabelText,
    *,
    type: Literal['button', 'submit', 'reset'] = 'button',
    name: str | None = None,
    value: str | None = None,
    disabled: bool = False,
    autofocus: bool = False,
    form: str | None = None,
    title: str | None = None,
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

Defaults to `type="button"` to avoid unintended form submissions.

### 7. `Input` (`ui/inputs.py`)

```python
ui.Input(
    *,
    name: str | None = None,
    value: str | None = None,
    placeholder: str | None = None,
    readonly: bool = False,
    required: bool = False,
    disabled: bool = False,
    autofocus: bool = False,
    minlength: int | None = None,
    maxlength: int | None = None,
    size: int | None = None,
    pattern: str | None = None,
    autocomplete: str | None = None,
    spellcheck: bool | None = None,
    inputmode: str | None = None,
    list: str | None = None,
    form: str | None = None,
    title: str | None = None,
    css_styles: dict[str, str] | None = None,
    class_names: list[str] | None = None,
    attributes: dict[str, AttrValue] | None = None,
)
```

Inherits from `InputBase`. Standardizes text input attributes and normalizes `spellcheck` to string literals.
