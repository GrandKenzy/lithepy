from core.css import render_rule


class Classes:
    _classes: dict[str, dict[str, str]] = {}

    @classmethod
    def add_class(cls, name: str, styles: dict[str, str]):
        cls._classes[name] = styles

    @classmethod
    def compile(cls) -> str:
        return ''.join(
            render_rule('.' + name, styles) + '\n\n'
            for name, styles in cls._classes.items()
        )

    @classmethod
    def not_empty(cls) -> bool:
        return len(cls._classes) != 0