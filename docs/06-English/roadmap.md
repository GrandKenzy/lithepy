# Framework Vision and Roadmap

This document outlines the architectural vision, engineering philosophy, and long-term roadmap for Lithe.

---

## ⚙️ Core Vision: Electron-Free Desktop Apps

The primary mission of Lithe is to provide a modern, ergonomic web-based UI layer for Python desktop applications without the resource footprint of Electron:

1. **Native OS WebViewer:** Instead of packaging an entire Chromium browser and Node.js runtime, Lithe utilizes the operating system's built-in web engine:
   * **Windows:** WebView2 (Edge/Chromium).
   * **macOS:** WKWebView (WebKit).
   * **Linux:** WebKitGTK.
2. **Pure Python Architecture:** The framework core and application business logic remain standard Python with zero external runtime dependencies.
3. **Cross-Platform Bundler:** Lithe will compile applications into standalone executables and native installers for Windows, Linux, and macOS.

---

## ⚙️ Complexity Debt & Design Philosophy

While writing raw HTML and CSS directly can be simpler than learning a framework API, Lithe deliberately introduces an object-oriented Python layer to provide:

* **Robust Structure & Type Safety:** Verified signatures, automated IDs, and modular component reusability.
* **Automation & Macros:** Elimination of manual wiring for CSS links, identifiers, and future reactive JavaScript bindings and animation timelines.
* **Fully Editable Output:** The generated HTML, CSS, and JavaScript are plain text files that developers can inspect, tweak, and refine by hand.

---

## 📋 Phased Roadmap

| Phase | Milestone | Status | Description |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Static UI Engine | **Completed** | Declarative widget tree, modular CSS segregation, HTML5 attribute sanitizer, and static compiler. |
| **Phase 2** | JS Macros & Animations | *Planned* | Python DSL for CSS animations, state management, and automated event handler generation. |
| **Phase 3** | Native WebView Runtime | *Planned* | Bidirectional low-latency IPC bridge connecting the Python runtime directly to OS WebViews. |
| **Phase 4** | Cross-Platform Packager | *Planned* | Single-binary and installer generation for Windows (`.exe`), Linux (`AppImage`), and macOS (`.app`). |
| **Phase 5** | Game & API Ecosystem | *Planned* | Specialized Canvas/WebGL components for lightweight games, and microservice UI dashboard templates. |
