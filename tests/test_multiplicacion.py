from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(4, 2) == 8
        assert multiplicacion(2, 2) == 4
        assert multiplicacion(5, 10) == 50
        assert multiplicacion(6, 30) == 180
