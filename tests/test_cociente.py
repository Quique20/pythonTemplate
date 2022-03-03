from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(10, 3) == 3
        assert cociente(10, 4) == 2
        assert cociente(20, 7) == 2
        assert cociente(20, 6) == 3
