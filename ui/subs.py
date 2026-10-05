"""Variantes de Label para formato de texto en línea (<strong>, <em>, ...)."""
from ui.label import Label


class Strong(Label):
    TAG = 'strong'


class Bold(Label):
    TAG = 'b'


class Italic(Label):
    TAG = 'i'


class Emphasis(Label):
    TAG = 'em'


class Underline(Label):
    TAG = 'u'


class Small(Label):
    TAG = 'small'


class Strike(Label):
    TAG = 's'


class Deleted(Label):
    TAG = 'del'


class Inserted(Label):
    TAG = 'ins'


class Subscript(Label):
    TAG = 'sub'


class Superscript(Label):
    TAG = 'sup'


class Mark(Label):
    TAG = 'mark'