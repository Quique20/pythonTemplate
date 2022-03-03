from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(3, 2) == 1
        assert resta(2, 2) == 0
        assert resta(10, 15) == -5
        assert resta(20, 10) == 10
