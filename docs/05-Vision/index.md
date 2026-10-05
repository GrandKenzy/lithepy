# Visión del Framework

Este documento expone la visión estratégica y la propuesta de arquitectura de Lithe como plataforma para el desarrollo de aplicaciones de escritorio ligeras y de alto rendimiento.

---

## ⚙️ Propósito y Propuesta de Valor

Lithe está concebido para resolver la sobrecarga de recursos tradicionalmente asociada al desarrollo de interfaces modernas de escritorio:

1. **Reemplazo Ligero de Electron:** En lugar de empaquetar una instancia completa de Chromium y Node.js con cada aplicación (lo que genera ejecutables de cientos de megabytes y alto consumo de memoria RAM), Lithe aprovechará el componente **WebView integrado del sistema operativo**:
   * **Windows:** WebView2 (Microsoft Edge / Blink nativo).
   * **macOS:** WKWebView (WebKit nativo).
   * **Linux:** WebKitGTK.
2. **Python Puro:** El núcleo, las herramientas de compilación y la lógica del desarrollador se mantienen en Python estándar sin dependencias foráneas obligatorias, facilitando la portabilidad y la integración con el ecosistema de ciencia de datos, backend y automatización.
3. **Distribución Multiplataforma:** La meta del framework es incluir un pipeline de empaquetado que genere instaladores y binarios autónomos compatibles con Windows, Linux y macOS.

---

## ⚙️ Deuda de Complejidad y Filosofía de Diseño

### Comparativa: Marcado Manual vs. API de Lithe

Escribir HTML y CSS de forma manual puede parecer inicialmente más directo que aprender la API de un framework en Python. Sin embargo, Lithe asume deliberadamente esta complejidad estructural a cambio de beneficios de ingeniería de software a escala:

* **Estructuración y Tipado:** Interfaces construidas mediante objetos modulares con firmas de tipo comprobables estáticamente, autocompletado en el IDE y reutilización de componentes.
* **Reducción de Integración Manual:** Automatización en la asignación de identificadores, enlaces CSS y división de archivos según la jerarquía de vistas.
* **Automatización y Macros (Planificado):** Generación guiada de scripts JavaScript reactivos, enlaces de eventos bidireccionales y animaciones complejas declaradas desde Python sin escribir código repetitivo.

### Filosofía de Salida Transparente

Lithe no es una caja negra ni un compilador opaco. Toda la salida producida consiste en **HTML5, CSS y JavaScript estándar**.

El desarrollador retiene el control total sobre los artefactos emitidos y puede modificar, auditar y optimizar manualmente los archivos generados para afinar el resultado visual según las necesidades del proyecto.

---

## 📋 Módulos y Especificaciones

* **[Hoja de Ruta](hoja_de_ruta.md):** Planificación por etapas para el desarrollo de las capacidades del runtime nativo, macros de animación y empaquetador multiplataforma.
