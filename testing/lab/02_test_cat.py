from unittest import TestCase, main


class CatTests(TestCase):
    NAME = "Name"
    FED = False
    SLEEPY = False
    SIZE = 0

    def setUp(self):
        self.c = Cat(CatTests.NAME)

    def test_init(self):
        self.assertEqual(self.c.name, CatTests.NAME)
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(self.c.size, CatTests.SIZE)

    def test_eat(self):
        self.c.eat()

        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(self.c.size, CatTests.SIZE + 1)

    def test_eat_raises_exception_with_true_fed(self):
        self.c.fed = True

        with self.assertRaises(Exception) as ex:
            self.c.eat()

        self.assertEqual(str(ex.exception), "Already fed.")
        self.assertTrue(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(self.c.size, CatTests.SIZE)

    def test_sleep(self):
        self.c.fed = True
        self.c.sleepy = True
        self.c.sleep()

        self.assertFalse(self.c.sleepy)


    def test_sleep_raises_exceptiom_with_false_fed(self):
        with self.assertRaises(Exception) as ex:
            self.c.sleep()

        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)


if __name__ == "__main__":
    main()
