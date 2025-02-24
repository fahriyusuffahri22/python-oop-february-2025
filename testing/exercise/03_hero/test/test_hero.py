from unittest import TestCase, main
from project.hero import Hero



class HeroTests(TestCase):
    def test_init(self):
        hero = Hero("Username", 10, 1000, 100)
        self.assertEqual(hero.username, "Username")
        self.assertEqual(hero.level, 10)
        self.assertEqual(hero.health, 1000)
        self.assertEqual(hero.damage, 100)

    def test_battle_draw(self):
        hero1 = Hero("Username", 10, 1000, 100)
        hero2 = Hero("Username2", 10, 1000, 100)

        self.assertEqual(hero1.battle(hero2), "Draw")
        self.assertEqual(hero1.health, 0)
        self.assertEqual(hero2.health, 0)

    def test_battle_win(self):
        hero1 = Hero("Username", 10, 2000, 100)
        hero2 = Hero("Username2", 10, 1000, 100)

        self.assertEqual(hero1.battle(hero2), "You win")
        self.assertEqual(hero1.level, 11)
        self.assertEqual(hero1.health, 1005)
        self.assertEqual(hero1.damage, 105)
        self.assertEqual(hero2.health, 0)

    def test_battle_lose(self):
        hero1 = Hero("Username", 10, 1000, 100)
        hero2 = Hero("Username2", 10, 2000, 100)

        self.assertEqual(hero1.battle(hero2), "You lose")
        self.assertEqual(hero2.level, 11)
        self.assertEqual(hero2.health, 1005)
        self.assertEqual(hero2.damage, 105)
        self.assertEqual(hero1.health, 0)

    def test_battle_raises_exception_when_fight_yourself(self):
        hero = Hero("Username", 10, 1000, 100)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")
        self.assertEqual(hero.level, 10)
        self.assertEqual(hero.health, 1000)
        self.assertEqual(hero.damage, 100)

    def test_battle_raises_value_error_when_you_need_rest(self):
        hero1 = Hero("Username", 10, 0, 100)
        hero2 = Hero("Username2", 10, 1000, 100)

        with self.assertRaises(Exception) as ex:
            hero1.battle(hero2)

        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

        self.assertEqual(hero1.level, 10)
        self.assertEqual(hero1.health, 0)
        self.assertEqual(hero1.damage, 100)

        self.assertEqual(hero2.level, 10)
        self.assertEqual(hero2.health, 1000)
        self.assertEqual(hero2.damage, 100)

    def test_battle_raises_value_error_when_your_enemy_need_rest(self):
        hero1 = Hero("Username", 10, 1000, 100)
        hero2 = Hero("Username2", 10, 0, 100)

        with self.assertRaises(Exception) as ex:
            hero1.battle(hero2)

        self.assertEqual(str(ex.exception), f"You cannot fight Username2. He needs to rest")

        self.assertEqual(hero1.level, 10)
        self.assertEqual(hero1.health, 1000)
        self.assertEqual(hero1.damage, 100)

        self.assertEqual(hero2.level, 10)
        self.assertEqual(hero2.health, 0)
        self.assertEqual(hero2.damage, 100)

    def test__str__(self):
        hero = Hero("Username", 10, 1000, 100)

        self.assertEqual(
            str(hero),
            f"Hero Username: 10 lvl\n"
            f"Health: 1000\n"
            f"Damage: 100\n"
        )


if __name__ == "__main__":
    main()
