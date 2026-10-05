from html import escape

AttrValue = str | int | float | bool | None


def render_attributes(attrs: dict[str, AttrValue]) -> str:
    """Convierte un dict en atributos HTML escapados.

    - `None` / `False` -> se omite el atributo.
    - `True`           -> atributo booleano sin valor (p. ej. `disabled`).
    - Otro valor       -> `clave="valor"` (con el valor escapado).
    """
    parts: list[str] = []
    for key, value in attrs.items():
        if value is None or value is False:
            continue
        if value is True:
            parts.append(f' {key}')
        else:
            parts.append(f' {key}="{escape(str(value), quote=True)}"')
    return ''.join(parts)
