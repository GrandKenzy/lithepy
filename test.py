import ui
import main
import core

core.Classes.add_class(
    'clase1',
    {
        'color': "yellow",
        "font-family": '"Comic Sans MS"',
        "border": "solid 1px white"
    }
)

etiqueta_mixta = ui.Label(
    text=[
        "Hola, %bMundo%bc. ", 
        "Esto es texto normal seguido de un ",
        ui.Strong("componente Strong", class_names=['texto-destacado']),
        " y también puedes anidar otros estilos como ",
        ui.Mark("texto resaltado"), 
        " sin problemas."
    ],
    class_names=['clase1', 'contenedor-texto'],
)

salto = ui.Break(10)

logo = ui.Image('img/logo.png', alt='Logo de Lithe', width=120, height=40, loading='lazy')

parrafo_link = ui.Label([
    "Visita la ",
    ui.Link("documentación de %bHTML%bc", "https://developer.mozilla.org/es/docs/Web/HTML?q=%e2&a=1", new_tab=True),
    " para más detalles.",
])

campo = ui.Input(
    name='usuario',
    placeholder='Tu nombre de usuario',
    required=True,
    maxlength=20,
    autocomplete='username',
    spellcheck=False,
)

boton = ui.Button(
    "Enviar",
    type='submit',
    attributes={'onclick': "alert('Hola')"},
)


container = ui.Container(
    items=[salto, etiqueta_mixta, logo, parrafo_link, campo, boton]
)


main.compile_and_make('source')