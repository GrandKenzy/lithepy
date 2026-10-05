from __future__ import annotations

from typing import Literal

from core.attrs import AttrValue
from ui.label import Label, LabelText

ButtonType = Literal['button', 'submit', 'reset']


class Button(Label):
    """Botón: `<button>`. El texto acepta lo mismo que `Label` (strings, marcadores y widgets)."""

    TAG = 'button'

    def __init__(
        self,
        text: LabelText,
        *,
        type: ButtonType = 'button',
        name: str | None = None,
        value: str | None = None,
        disabled: bool = False,
        autofocus: bool = False,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        """
        Args:
            text: Contenido del botón.
            type: 'button' (por defecto, no hace nada solo), 'submit' (envía
                el formulario) o 'reset' (lo limpia).
            name, value: Par que se envía con el formulario al presionarlo.
            disabled: Deshabilita el botón.
            autofocus: Recibe el foco al cargar la página.
            form: id del formulario al que pertenece (si está fuera de él).
            title: Texto que aparece al pasar el mouse.

        Eventos como `onclick` se pasan en `attributes`.
        """
        self.type = type
        self.name = name
        self.value = value
        self.disabled = disabled
        self.autofocus = autofocus
        self.form = form
        self.title = title
        super().__init__(text, css_styles, class_names, attributes)

    def attributes(self) -> dict[str, AttrValue]:
        return {
            'type': self.type,
            'name': self.name,
            'value': self.value,
            'disabled': self.disabled,
            'autofocus': self.autofocus,
            'form': self.form,
            'title': self.title,
        }
