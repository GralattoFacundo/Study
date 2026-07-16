class IA_Junior:
    def __init__(self, nombre):
        # 1. Variables de varios tipos
        self.nombre = "Martin"
        self.version = 1.0
        self.activa = True
        
        # 2. Tupla (configuración inmutable: comandos que entiende)
        self.comandos_validos = ("saludar", "aprender", "historial", "salir")
        
        # 3. Diccionario (su "cerebro" inicial)
        self.conocimiento = {"saludar": "¡Hola, creador! Sistemas en línea.","aprender": "Estoy listo para aprender cosas nuevas.","historial": "Aquí está tu historial de consultas.","salir": "¡Hasta luego, creador!"}
        
        # 4. Lista (historial dinámico)
        self.historial_usuario = ["Quiero ser saludado.", "Quiero enseñarte algo nuevo.", "Muéstrame mi historial."]

    # 5. Lambda (Función de un renglón para limpiar el input)
    # TODO: Crea una lambda llamada 'limpiar' que tome un texto, le haga .strip() y .lower()
    limpiar = lambda x: x.strip().lower()

    def procesar_comando(self, comando):
        # 6. Match-case (El 'switch' de Python)
        # TODO: Usa 'match comando:' para evaluar las siguientes opciones:
        # - case "saludar": Imprime el valor de "saludar" guardado en el diccionario 'conocimiento'
        # - case "aprender": Pide un nuevo dato al usuario con input() y guárdalo en la lista 'historial_usuario'
        # - case "historial": Usa un ciclo 'for' para imprimir todo lo que hay en 'historial_usuario'
        # - case _: (el caso por defecto) Imprime "Comando no reconocido."
        pass

# --- Bucle Principal ---
# 7. Objetos
mi_ia = IA_Junior("Cerebro_V1")

print(f"Iniciando {mi_ia.nombre} v{mi_ia.version}...")

# 8. Bucle While
# TODO: Crea un bucle 'while mi_ia.activa:'
# Dentro del bucle:
#   - Pide un input al usuario: "Ingresa un comando (o 'salir'): "
#   - Usa tu función lambda para limpiar ese input.
#   - Si el input es "salir", cambia mi_ia.activa a False y despídete.
#   - Si no, pásale el comando a mi_ia.procesar_comando()