from pathlib import Path

from core import class_css, layer
from ui import widget


def compile_and_make(folder_output: str = 'source'):
    html_output, css_output = widget.compile()

    base_dir = Path(folder_output)
    css_dir = base_dir / 'css'
    css_dir.mkdir(parents=True, exist_ok=True)

    css_links: list[str] = []
    for file, content in css_output.items():
        (css_dir / file).write_text(content, encoding='utf-8')
        css_links.append(f'css/{file}')

    if class_css.Classes.not_empty():
        (css_dir / 'class.css').write_text(class_css.Classes.compile(), encoding='utf-8')
        css_links.append('css/class.css')

    html = layer.get(
        'es',
        'Mi Pagina',
        css_links=css_links,
        body=html_output,
    )
    (base_dir / 'index.html').write_text(html, encoding='utf-8')
