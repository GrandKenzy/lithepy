DEFAULT_METAS = (
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta charset="UTF-8">',
)
DEFAULT_CSS_LINKS = ('styles.css',)


def get(
    lang: str = 'en',
    title: str = 'Document',
    metas: list[str] | None = None,
    css_links: list[str] | None = None,
    body: list[str] | None = None,
) -> str:
    metas = list(DEFAULT_METAS) if metas is None else metas
    css_links = list(DEFAULT_CSS_LINKS) if css_links is None else css_links
    body = body or []

    meta_tags = '\n    '.join(metas)
    link_tags = '\n    '.join(f'<link rel="stylesheet" href="{lnk}">' for lnk in css_links)
    body_html = '\n'.join(body)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    {meta_tags}
    {link_tags}
    <title>{title}</title>
</head>
<body>

{body_html}

</body>
</html>"""
