class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vector(self.x + outro.x, self.y + outro.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Criando dois vetores
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Somando os vetores usando o operador +
resultado = v1 + v2
print(resultado)  # Saída: Vector(6, 8)
