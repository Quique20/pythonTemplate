from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(10, 2) == 5
        assert division(30, 15) == 2
        assert division(200, 200) == 1
        assert division(6, 2) == 3
