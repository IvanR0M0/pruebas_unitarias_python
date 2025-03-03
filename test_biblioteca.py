import pytest
from biblioteca import Libro, Biblioteca

# Pruebas para la clase Libro
def test_libro_atributos():
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    assert libro.titulo == "Rebelión en la granja"
    assert libro.autor == "George Orwell"
    assert libro.anio == 1945
    assert libro.prestado is False

def test_libro_estado():
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    assert str(libro) == "Rebelión en la granja de George Orwell (1945) - disponible"
    libro.prestado = True
    assert str(libro) == "Rebelión en la granja de George Orwell (1945) - prestado"

# Pruebas para la clase Biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    assert biblioteca.buscar_libro("Rebelión en la granja") is not None

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Rebelión en la granja")
    assert biblioteca.buscar_libro("Rebelión en la granja") is None

def test_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("1984")
    assert len(biblioteca.libros) == 1

def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    assert biblioteca.buscar_libro("Rebelión en la granja") == libro

def test_buscar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.buscar_libro("1984") is None

def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("Rebelión en la granja", "George Orwell", 1945)
    libro2 = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    lista = biblioteca.listar_libros()
    assert "Rebelión en la granja de George Orwell (1945) - disponible" in lista
    assert "1984 de George Orwell (1949) - disponible" in lista
   

def test_prestar_libro_exitoso():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.prestar_libro("Rebelión en la granja")
    assert resultado == "Has pedido prestado el libro 'Rebelión en la granja'."
    assert libro.prestado is True

def test_prestar_libro_ya_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Rebelión en la granja")
    resultado = biblioteca.prestar_libro("Rebelión en la granja")
    assert resultado == "El libro 'Rebelión en la granja' ya está prestado."

def test_prestar_libro_no_existente():
    biblioteca = Biblioteca()
    resultado = biblioteca.prestar_libro("1984")
    assert resultado == "El libro '1984' no se encuentra en la biblioteca."

def test_devolver_libro_exitoso():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Rebelión en la granja")
    resultado = biblioteca.devolver_libro("Rebelión en la granja")
    assert resultado == "Has devuelto el libro 'Rebelión en la granja'."
    assert libro.prestado is False

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.devolver_libro("Rebelión en la granja")
    assert resultado == "El libro 'Rebelión en la granja' no estaba prestado."

def test_devolver_libro_no_existente():
    biblioteca = Biblioteca()
    resultado = biblioteca.devolver_libro("1984")
    assert resultado == "El libro '1984' no se encuentra en la biblioteca."

if __name__ == "__main__":
    pytest.main()