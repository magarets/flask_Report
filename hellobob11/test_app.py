import unittest
import app

class TestHello(unittest.TestCase):
    def test_add(self):
        h = app.Hello()
        a = 2
        b = 3
        add = h.add(a, b)
        self.assertEqual(int(add), a + b)

    def test_sub(self):
        h = app.Hello()
        a = 3
        b = 5
        sub = h.sub(a, b)
        self.assertEqual(int(sub), a - b)

if __name__ == "__main__":
    print(unittest.main())