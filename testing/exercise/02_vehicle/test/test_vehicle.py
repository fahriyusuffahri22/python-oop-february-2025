from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    FUEL = 100
    HORSE_POWER = 100

    def setUp(self):
        self.v = Vehicle(VehicleTests.FUEL, VehicleTests.HORSE_POWER)

    def test_init(self):
        self.assertEqual(self.v.fuel, VehicleTests.FUEL)
        self.assertEqual(self.v.capacity, VehicleTests.FUEL)
        self.assertEqual(self.v.horse_power, VehicleTests.HORSE_POWER)
        self.assertEqual(self.v.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive(self):
        half_capacity = VehicleTests.FUEL / 2
        self.v.drive(half_capacity / Vehicle.DEFAULT_FUEL_CONSUMPTION)

        self.assertEqual(self.v.fuel, half_capacity)

    def test_drive_raises_exception_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.v.drive(VehicleTests.FUEL / self.v.fuel_consumption + 1)

        self.assertEqual(str(ex.exception), "Not enough fuel")
        self.assertEqual(self.v.fuel, VehicleTests.FUEL)

    def test_refuel(self):
        half_capacity = VehicleTests.FUEL / 2
        self.v.fuel = 0
        self.v.refuel(half_capacity)

        self.assertEqual(self.v.fuel, half_capacity)

    def test_refuel_raises_exception_without_enough_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.v.refuel(1)

        self.assertEqual(str(ex.exception), "Too much fuel")
        self.assertEqual(self.v.fuel, VehicleTests.FUEL)

    def test__str__(self):
        self.assertEqual(
            str(self.v),
            f"The vehicle has {VehicleTests.HORSE_POWER} horse power with {VehicleTests.FUEL} fuel left and "
            f"{Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        )


if __name__ == "__main__":
    main()
