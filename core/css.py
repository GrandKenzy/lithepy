def render_rule(selector: str, styles: dict[str, str]) -> str:
    """Genera una regla CSS: `selector { prop : valor; ... }`."""
    body = ''.join(f'    {k} : {v};\n' for k, v in styles.items())
    return f'{selector} {{\n{body}}}'
