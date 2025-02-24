from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    NAME = "Name"
    TYPE = "Type"
    SOUND = "Sound"
    KINGDOM = "animals"

    def setUp(self):
        self.m = Mammal(TestMammal.NAME, TestMammal.TYPE, TestMammal.SOUND)

    def test_init(self):
        self.assertEqual(self.m.name, TestMammal.NAME)
        self.assertEqual(self.m.type, TestMammal.TYPE)
        self.assertEqual(self.m.sound, TestMammal.SOUND)

    def test_make_sound(self):
        self.assertEqual(self.m.make_sound(), f"{TestMammal.NAME} makes {TestMammal.SOUND}")

    def test_get_kingdom(self):
        self.assertEqual(self.m.get_kingdom(), TestMammal.KINGDOM)

    def test_info(self):
        self.assertEqual(self.m.info(), f"{TestMammal.NAME} is of type {TestMammal.TYPE}")

if __name__ == "__main__":
    main()
