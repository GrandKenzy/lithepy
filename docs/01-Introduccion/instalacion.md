# Instalación

Lithe está escrito en Python puro y no tiene dependencias externas: solo utiliza la biblioteca estándar (`pathlib`, `html`, `typing`).

---

## ⚙️ Requisitos

| Requisito | Valor |
| :--- | :--- |
| Python | 3.10 o superior. El código usa uniones de tipos `X \| Y` evaluadas en tiempo de ejecución (por ejemplo, `AttrValue` en `core/attrs.py`), disponibles desde 3.10. Verificado con Python 3.14. |
| Dependencias | Ninguna |
| Sistema operativo | Cualquiera con Python. La salida es HTML y CSS estándar. |

---

## 📦 Preparación

Lithe todavía no se publica como paquete (`pip install`). Los paquetes `ui` y `core` y el módulo `main` se importan como módulos de primer nivel, por lo que los scripts deben ejecutarse **desde la raíz del repositorio** o con esa carpeta en `sys.path`.

```bash
cd lithe
python test.py
```

Comprobación: tras ejecutar `test.py` deben existir `source/index.html` y la carpeta `source/css/`.

---

## ⚠️ Consideraciones

1. **Directorio de trabajo:** `compile_and_make('source')` interpreta la ruta de salida de forma relativa al directorio de trabajo actual, no a la ubicación del script.
2. **Sobrescritura:** los archivos de salida se sobrescriben en cada compilación. Las ediciones manuales hechas sobre `source/` se pierden si se vuelve a compilar.
3. **Archivos obsoletos:** los archivos CSS de contenedores se nombran según su identificador (por ejemplo, `Container_0___Widget_9.css`). Si el árbol cambia, los archivos de compilaciones anteriores no se eliminan; conviene borrar la carpeta de salida antes de recompilar.

---

## 💡 Uso desde otra carpeta

Si el script vive fuera del repositorio, añadir la raíz de Lithe a `sys.path` antes de importar:

```python
import sys
sys.path.insert(0, r'C:\ruta\a\lithe')

import ui
import main
```
