# Primer proyecto

Este tutorial construye una página de inicio de sesión con título, logotipo, formulario y enlace de ayuda. Todos los fragmentos de código son ejecutables desde la raíz del repositorio.

---

## 📋 Paso 1: Crear el script

Crear `login.py` en la raíz del repositorio con los imports necesarios:

```python
import core
import main
import ui
```

* `ui` contiene los widgets.
* `core` contiene `Classes`, el registro de clases CSS globales.
* `main` contiene `compile_and_make()`.

---

## 📋 Paso 2: Definir clases CSS globales

Las clases globales se registran una vez y se reutilizan en cualquier widget mediante `class_names`.

```python
core.Classes.add_class('campo', {
    'display': 'block',
    'width': '100%',
    'margin-bottom': '12px',
    'padding': '8px',
})

core.Classes.add_class('primario', {
    'background': '#2563eb',
    'color': 'white',
    'border': 'none',
    'padding': '10px 16px',
})
```

---

## 📋 Paso 3: Crear los widgets

```python
titulo = ui.Label("%bIniciar sesión%bc", css_styles={'font-size': '24px'})

logo = ui.Image('img/logo.png', alt='Logotipo', width=96, height=96)

usuario = ui.Input(
    name='usuario',
    placeholder='Usuario',
    required=True,
    autocomplete='username',
    class_names=['campo'],
)

codigo = ui.Input(
    name='codigo',
    placeholder='Código de 6 dígitos',
    pattern='[0-9]{6}',
    title='Seis dígitos numéricos',
    maxlength=6,
    inputmode='numeric',
    class_names=['campo'],
)

entrar = ui.Button("Entrar", type='submit', class_names=['primario'])

ayuda = ui.Label([
    "¿Problemas para entrar? ",
    ui.Link("Consulta la ayuda", "https://example.com/ayuda", new_tab=True),
])
```

En este punto los seis widgets son **raíz**: ninguno está dentro de otro. El `Link` no es raíz porque `ayuda` lo contiene.

---

## 📋 Paso 4: Agruparlos en un contenedor

```python
ui.Container(
    items=[titulo, logo, usuario, codigo, entrar, ayuda],
    width=320,
    height='auto',
    x=40,
    y=40,
)
```

Al pasar los widgets a `items`, el contenedor los retira de la lista de raíces. Ahora la única raíz es el contenedor.

`width=320` se convierte en `320px`; `height='auto'` se escribe tal cual. `x` e `y` se traducen a `left` y `top`, con `position: relative`.

---

## 📋 Paso 5: Compilar

```python
main.compile_and_make('login_out')
```

```bash
python login.py
```

---

## 🔍 Resultado

Estructura generada:

```
login_out/
├── index.html
└── css/
    ├── styles.css
    ├── Container_0___Widget_7.css
    └── class.css
```

`styles.css` queda vacío porque el único widget raíz es un `Container`, cuyos estilos van a su propio archivo.

Fragmento de `index.html`:

```html
<div id="Container_0___Widget_7">
    <p id="Label_0___Widget_0"><b>Iniciar sesión</b></p>
    <img id="Image_0___Widget_1" src="img/logo.png" alt="Logotipo" width="96" height="96">
    <input id="Input_0___Widget_2" class="campo" type="text" name="usuario" required placeholder="Usuario" autocomplete="username">
    <input id="Input_1___Widget_3" class="campo" type="text" name="codigo" title="Seis dígitos numéricos" maxlength="6" pattern="[0-9]{6}" inputmode="numeric">
    <button id="Button_0___Widget_4" class="primario" type="submit">Entrar</button>
    <p id="Label_1___Widget_6">¿Problemas para entrar? <a id="Link_0___Widget_5" href="https://example.com/ayuda" target="_blank" rel="noopener noreferrer">Consulta la ayuda</a></p>
</div>
```

Contenido de `css/Container_0___Widget_7.css`:

```css
#Container_0___Widget_7 {
    position : relative;
    left : 40px;
    top : 40px;
    width : 320px;
    height : auto;
}

#Label_0___Widget_0 {
    font-size : 24px;
}

```

---

## ⚠️ Observaciones

1. El formulario no tiene etiqueta `<form>`: Lithe aún no incluye un widget de formulario. El botón `submit` no enviará datos hasta que exista uno; mientras tanto puede añadirse manualmente en el HTML generado.
2. La imagen `img/logo.png` debe existir en `login_out/img/` para mostrarse; Lithe no copia recursos.
3. Los identificadores dependen del orden de creación. Si se crea otro widget antes de `titulo`, todos los números cambian.
