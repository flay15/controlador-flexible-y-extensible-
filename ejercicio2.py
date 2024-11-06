class Componente:
    def ejecutar(self):
        raise NotImplementedError("Este método debe ser implementado por cada componente")

class ComponenteA(Componente):
    def ejecutar(self):
        print("Ejecutando Componente A")
        return "Resultado de Componente A"

class ComponenteB(Componente):
    def ejecutar(self):
        print("Ejecutando Componente B")
        return "Resultado de Componente B"

class Controlador:
    def __init__(self):
        self.componentes = {}

    def registrar_componente(self, nombre, componente):
        if not isinstance(componente, Componente):
            raise ValueError("El componente debe ser una instancia de la clase Componente")
        self.componentes[nombre] = componente

    def ejecutar_componente(self, nombre):
        if nombre not in self.componentes:
            print(f"El componente {nombre} no está registrado.")
            return
        resultado = self.componentes[nombre].ejecutar()
        print(f"Resultado de {nombre}: {resultado}")

    def ejecutar_todos(self):
        for nombre, componente in self.componentes.items():
            print(f"Ejecutando {nombre}:")
            componente.ejecutar()

if __name__ == "__main__":
    controlador = Controlador()
    controlador.registrar_componente("A", ComponenteA())
    controlador.registrar_componente("B", ComponenteB())

    controlador.ejecutar_componente("A")
    controlador.ejecutar_componente("B")
    controlador.ejecutar_todos()
