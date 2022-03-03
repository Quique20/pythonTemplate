from app.rot13_cipher import rot13


class TestClass:
    def test_rot13(self):
        assert rot13("hello world") == "uryyb jbeyq"

