# Hoja de Ruta y Funcionalidades Planificadas

Este documento detalla las etapas de desarrollo previstas para evolucionar Lithe desde su estado actual de generador estático hasta un entorno completo de desarrollo de aplicaciones nativas de escritorio.

---

## ⚙️ Estado de Implementación por Fases

```
[Fase 1: Generador UI] ────> [Fase 2: Macros JS] ────> [Fase 3: Runtime WebView] ────> [Fase 4: Empaquetador]
  (Completado)                 (Planificado)             (Planificado)                  (Planificado)
```

| Fase | Ámbito | Estado | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Fase 1** | Motor UI Base | **Implementado** | Jerarquía de widgets, resolución y compilación de CSS modular, formateador de texto y serializador de atributos HTML5. |
| **Fase 2** | Macros JS & Animaciones | *Planificado* | Generación automatizada de código JavaScript para reactividad de estado, transiciones y animaciones declarativas desde Python. |
| **Fase 3** | Runtime Nativo WebView | *Planificado* | Capa de puente bidireccional (IPC) entre el proceso Python y el componente WebView del sistema operativo (WebView2, WebKitGTK, WKWebView). |
| **Fase 4** | Empaquetado Multiplataforma | *Planificado* | Generación automatizada de instaladores y ejecutables independientes para Windows (`.exe` / `.msi`), Linux (`AppImage` / `.deb`) y macOS (`.dmg` / `.app`). |
| **Fase 5** | Aplicaciones Avanzadas | *Planificado* | Soporte especializado para desarrollo de videojuegos (bucle de renderizado, WebGL/Canvas) y herramientas para APIs con interfaz integrada. |

---

## 📋 Detalle de Fases Planificadas

### Fase 2: Macros y Automatización de JavaScript

* **Sistema de Reactividad:** Declaración de variables de estado en Python que sincronizan automáticamente el DOM mediante scripts mínimos generados en la salida.
* **Macros de Animación:** DSL en Python para definir transiciones CSS (`ease-in-out`, interpolaciones de escala, opacidad y movimiento) sin requerir codificación manual en CSS/JS.
* **Gestión de Eventos:** Enlaces declarativos para llamadas asíncronas entre la interfaz y funciones de backend.

### Fase 3: Runtime Integrado Basado en WebView

* **Eliminación de la Sobrecarga de Electron:** Despliegue de la ventana de aplicación utilizando los navegadores ya instalados en el sistema anfitrión.
* **Canal IPC Ligero:** Comunicación bidireccional de baja latencia entre el motor de ejecución en Python y la vista web mediante sockets de dominio Unix o canales de mensajería nativos del WebView.
* **Compatibilidad de Plataformas:**
  * Windows 10/11: Microsoft Edge WebView2.
  * macOS 11+: WebKit (`WKWebView`).
  * Distribuciones Linux: WebKit2GTK.

### Fase 4: Toolchain de Distribución y Empaquetado

* **Ensamblador de Binarios:** Compilación del intérprete de Python, dependencias y assets de la interfaz en un paquete autosuficiente.
* **Firmado de Código:** Herramientas integradas para facilitar la firma digital en los diferentes sistemas operativos.

### Fase 5: Ecosistema para Juegos y APIs con UI

* **Videojuegos Ligeros:** Componentes dedicados para lienzos interactivos (`<canvas>`), soporte de WebGL y controladores de entrada de teclado/ratón de baja latencia.
* **APIs con Panel de Control:** Integración lista para empaquetar servicios REST/RPC junto a dashboards de control administrativo servidos localmente en una única aplicación.
