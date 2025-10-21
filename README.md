# 🧠 Keylogger Educativo en Python

## 📘 Descripción del proyecto
Este proyecto implementa un **keylogger educativo** desarrollado en **Python**, cuyo propósito es **comprender cómo funcionan los registros de pulsaciones en entornos inseguros**, dentro de un **entorno controlado y ético**.  
> ⚠️ **Advertencia:** Este software se utiliza **únicamente con fines educativos**. Su uso fuera de entornos autorizados o con fines no éticos es **estrictamente prohibido**.

---

## 🎯 Objetivo
Implementar en un entorno controlado un keylogger para comprender su uso en entornos inseguros.  
La práctica es **educacional** y **no debe ser usada con intenciones no éticas o ilegales**.  
La aplicación registra las teclas presionadas en un archivo de texto (`key_events.log`).

---

## 🧩 Archivos principales
| Archivo | Descripción |
|----------|--------------|
| `main.py` | Código principal del keylogger |
| `requirements.txt` | Dependencias necesarias para ejecutar el script |
| `key_events.log` | Archivo de registro generado automáticamente con las pulsaciones capturadas |

---

## ⚙️ Requisitos
- Python **3.10+**
- Librería [`keyboard`](https://github.com/boppreh/keyboard)

Instálala ejecutando:
```bash
pip install -r requirements.txt
```
## 🚀 Ejecución

1. **Clona el repositorio y entra a la carpeta**
```bash
git clone https://github.com/usuario/tu-repo.git
cd tu-repo
```

2. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecuta el programa**
```bash
python main.py
```

6. **Uso básico**
- Presiona cualquier tecla para comenzar a registrar.
- Para **detener** el keylogger, pulsa **ESC**.

7. **Verifica el registro generado — Windows**
```bash
type key_events.log
```

8. **Verifica el registro generado — Linux / macOS**
```bash
cat key_events.log
```

9. **Notas de permisos**
- En **Windows**, ejecuta la terminal/VS Code **como Administrador** si no captura teclas.
- En **Linux**, si no registra teclas, ejecuta con privilegios elevados:
```bash
sudo python main.py
```

## 🧮 Ejemplo de ejecución

```bash
--- Keylogger Iniciado ---
[INFO] El registro se guardará en: key_events.log
[INFO] Pulsa cualquier tecla para empezar.
[INFO] Presiona la tecla 'ESC' para detener.
[ESPACIO]
a
b
[ENTER]
[FIN] Keylogger detenido por el usuario. Registro completo guardado.
```

<img width="355" height="445" alt="image" src="https://github.com/user-attachments/assets/6a32a6c6-49d1-4472-a072-6061962befff" />


El archivo generado `key_events.log` contendrá un registro línea por línea de todas las teclas presionadas, por ejemplo:

```css
a
b
c
[ESPACIO]
[ENTER]
[BORRAR]
```






