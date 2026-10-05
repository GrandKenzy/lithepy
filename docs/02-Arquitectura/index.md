# Arquitectura del Sistema

Esta sección describe la arquitectura interna de Lithe, el ciclo de vida de los componentes, el pipeline de compilación a HTML/CSS y las dependencias entre módulos.

---

## ⚙️ Visión General y Flujo de Datos

Lithe opera bajo un modelo de árbol de componentes en memoria implementado en Python puro. Los widgets se instancian de manera declarativa, se organizan jerárquicamente y se compilan a archivos estáticos estándar (HTML y CSS).

El flujo de ejecución general consta de cuatro etapas secuenciales:

```
1. Instanciación & Registro
   └── Cada Widget genera un ID único y se registra en Widget._widgets.

2. Ensamblado Jerárquico (fix)
   └── Los contenedores y etiquetas reclaman a sus hijos, retirándolos de Widget._widgets.

3. Compilación en Memoria (ui.compile)
   └── Se evalúa el marcado HTML y se recopilan los bloques CSS por archivo.

4. Emisión a Disco (main.compile_and_make)
   └── Se escribe el árbol de carpetas, archivos .css y el index.html final.
```

---

## ⚙️ Diagrama de Dependencias de Módulos

```
main.py
  ├── ui.widget ──> core.css, core.attrs
  ├── core.class_css ──> core.css
  └── core.layer

ui/
  ├── widget.py (Base, formateador y registro)
  ├── container.py (Hereda de Widget, maneja geometría y recursión CSS)
  ├── label.py (Hereda de Widget, base de texto y anidación)
  ├── subs.py (Hereda de Label, etiquetas semánticas en línea)
  ├── image.py (Hereda de Widget, <img> vacío)
  ├── link.py (Hereda de Label, <a>)
  ├── button.py (Hereda de Label, <button>)
  ├── inputs.py (InputBase y subclase Input, <input> vacío)
  └── br.py (Hereda de Widget, marcado <br>)

core/
  ├── attrs.py (Renderizado y escape de atributos HTML)
  ├── css.py (Renderizado de reglas CSS)
  ├── class_css.py (Gestor estático de clases globales)
  └── layer.py (Plantilla envolvente HTML5)
```

---

## 📋 Módulos y Especificaciones

* **[Widget](widget.md):** Especificación de la clase base `Widget`, asignación de identificadores y mecanismo de adopción jerárquica (`fix()`).
* **[Compilación](compilacion.md):** Detalle técnico de `ui.compile()`, `compile_and_make()` y la plantilla de `core.layer`.
* **[Estilos](estilos.md):** Sistema de resolución CSS por selector de ID, separación por contenedor y clases globales `core.Classes`.
* **[Atributos](atributos.md):** Contrato de atributos HTML, soporte booleano y mitigación de inyecciones mediante escape de entidades.
