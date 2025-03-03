import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Juan", 10, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Juan. Total: $40"

def test_asientos_insuficientes():
    pelicula = Pelicula("Juan", 3, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."

def test_cero_entradas():
    pelicula = Pelicula("Juan", 10, 8)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Juan. Total: $0"
