"""Widgets basados en `<input>`.

`InputBase` concentra lo común a todos los tipos; cada subclase fija su
`INPUT_TYPE` y agrega sus propios atributos. Para nuevos tipos (Checkbox,
Radio, ...) basta con heredar de `InputBase`.
"""
from __future__ import annotations

from typing import Literal

from core.attrs import AttrValue
from ui.widget import Widget


class InputBase(Widget):
    """Base para todos los `<input>`. No se usa directamente."""

    TAG = 'input'
    CLOSE = False
    INPUT_TYPE = 'text'

    def __init__(
        self,
        *,
        name: str | None = None,
        value: str | None = None,
        disabled: bool = False,
        required: bool = False,
        autofocus: bool = False,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        self.name = name
        self.value = value
        self.disabled = disabled
        self.required = required
        self.autofocus = autofocus
        self.form = form
        self.title = title
        super().__init__(css_styles, class_names, attributes)

    def attributes(self) -> dict[str, AttrValue]:
        return {
            'type': self.INPUT_TYPE,
            'name': self.name,
            'value': self.value,
            'disabled': self.disabled,
            'required': self.required,
            'autofocus': self.autofocus,
            'form': self.form,
            'title': self.title,
        }


Autocomplete = Literal['on', 'off', 'name', 'email', 'username', 'tel', 'street-address', 'postal-code', 'country']
InputMode = Literal['none', 'text', 'decimal', 'numeric', 'tel', 'search', 'email', 'url']


class Input(InputBase):
    """Campo de texto de una línea: `<input type="text">`."""

    INPUT_TYPE = 'text'

    def __init__(
        self,
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
        autocomplete: Autocomplete | str | None = None,
        spellcheck: bool | None = None,
        inputmode: InputMode | None = None,
        list: str | None = None,
        form: str | None = None,
        title: str | None = None,
        css_styles: dict[str, str] | None = None,
        class_names: list[str] | None = None,
        attributes: dict[str, AttrValue] | None = None,
    ):
        """
        Args:
            name: Nombre con el que se envía el valor en el formulario.
            value: Valor inicial.
            placeholder: Texto de ayuda cuando está vacío.
            readonly: Se ve y se envía, pero no se puede editar.
            required: Obligatorio para enviar el formulario.
            disabled: Deshabilitado (no se envía).
            autofocus: Recibe el foco al cargar la página.
            minlength, maxlength: Longitud mínima/máxima en caracteres.
            size: Ancho visible en caracteres.
            pattern: Expresión regular que debe cumplir el valor.
                Usa `title` para explicar el formato esperado.
            autocomplete: Pista de autocompletado ('off', 'email', 'name', ...).
            spellcheck: Activa/desactiva el corrector ortográfico.
            inputmode: Teclado sugerido en móviles.
            list: id de un `<datalist>` con sugerencias.
            form: id del formulario al que pertenece (si está fuera de él).
            title: Texto que aparece al pasar el mouse.
        """
        self.placeholder = placeholder
        self.readonly = readonly
        self.minlength = minlength
        self.maxlength = maxlength
        self.size = size
        self.pattern = pattern
        self.autocomplete = autocomplete
        self.spellcheck = spellcheck
        self.inputmode = inputmode
        self.list = list
        super().__init__(
            name=name,
            value=value,
            disabled=disabled,
            required=required,
            autofocus=autofocus,
            form=form,
            title=title,
            css_styles=css_styles,
            class_names=class_names,
            attributes=attributes,
        )

    def attributes(self) -> dict[str, AttrValue]:
        attrs = super().attributes()
        attrs.update({
            'placeholder': self.placeholder,
            'readonly': self.readonly,
            'minlength': self.minlength,
            'maxlength': self.maxlength,
            'size': self.size,
            'pattern': self.pattern,
            'autocomplete': self.autocomplete,
            'spellcheck': None if self.spellcheck is None else str(self.spellcheck).lower(),
            'inputmode': self.inputmode,
            'list': self.list,
        })
        return attrs
