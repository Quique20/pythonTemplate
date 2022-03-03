from app.operaciones import resto


class TestClass:
    def test_division(self):
        assert resto(10, 3) == 1
        assert resto(10, 4) == 2
        assert resto(10, 5) == 0
        assert resto(7, 2) == 1
