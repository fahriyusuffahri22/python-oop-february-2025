from unittest import TestCase, main


class CarTests(TestCase):
    MAKE = "MAKE"
    MODEL = "MODEL"
    FUEL_CONSUMPTION = 10
    FUEL_CAPACITY = 100
    FUEL_AMOUNT = 0

    def setUp(self):
        self.c = Car(CarTests.MAKE, CarTests.MODEL, CarTests.FUEL_CONSUMPTION, CarTests.FUEL_CAPACITY)

    def test_init(self):
        self.assertEqual(self.c.make, CarTests.MAKE)
        self.assertEqual(self.c.model, CarTests.MODEL)
        self.assertEqual(self.c.fuel_consumption, CarTests.FUEL_CONSUMPTION)
        self.assertEqual(self.c.fuel_capacity, CarTests.FUEL_CAPACITY)
        self.assertEqual(self.c.fuel_amount, CarTests.FUEL_AMOUNT)

    def test_make_raise_exception_with_empty_str_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.make = ""

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_make_raise_exception_with_none_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.make = None

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_raise_exception_with_empty_str_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = ""

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_raise_exception_with_none_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = None

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_raise_exception_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = 0

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_raise_exception_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = -1

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_raise_exception_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = 0

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_raise_exception_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = -1

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_raise_exception_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_amount = -1

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        half_fuel_capacity = self.c.fuel_capacity / 2
        self.c.refuel(half_fuel_capacity)
        self.assertEqual(self.c.fuel_amount, half_fuel_capacity)

        self.c.refuel(self.c.fuel_capacity)
        self.assertEqual(self.c.fuel_amount, self.c.fuel_capacity)

    def test_refuel_raise_exception_with_zero_fuel_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_raise_exception_with_negative_fuel_value(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(-1)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_drive(self):
        half_fuel_capacity = self.c.fuel_capacity / 2
        self.c.refuel(self.c.fuel_capacity)
        self.c.drive(half_fuel_capacity / self.c.fuel_consumption * 100)

        self.assertEqual(self.c.fuel_amount, half_fuel_capacity)

    def test_drive_raises_exception_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.c.drive(100)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")



if __name__ == "__main__":
    main()
