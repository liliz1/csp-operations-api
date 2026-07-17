def demo():
    print("1. Creo el recurso")
    yield "Hola" 
    print("2. Libero el recurso")
    yield "ADIOAS" 


g=demo()

print(next(g))
next(g)


try:
    next(g)
except StopIteration:
    print("Fin del generador")