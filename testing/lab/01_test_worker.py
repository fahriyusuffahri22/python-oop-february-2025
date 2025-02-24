from unittest import TestCase, main


class WorkerTests(TestCase):
    NAME = "Name"
    SALARY = 1000
    ENERGY = 10
    MONEY = 0

    def setUp(self):
        self.w = Worker(WorkerTests.NAME, WorkerTests.SALARY, WorkerTests.ENERGY)

    def test_init(self):
        self.assertEqual(self.w.name, WorkerTests.NAME)
        self.assertEqual(self.w.salary, WorkerTests.SALARY)
        self.assertEqual(self.w.energy, WorkerTests.ENERGY)
        self.assertEqual(self.w.money, WorkerTests.MONEY)

    def test_work(self):
        self.w.work()

        self.assertEqual(self.w.money, self.w.salary)
        self.assertEqual(self.w.energy, WorkerTests.ENERGY - 1)

    def test_work_raises_exception_with_zero_energy(self):
        self.w.energy = 0

        with self.assertRaises(Exception) as ex:
            self.w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")
        self.assertEqual(self.w.money, WorkerTests.MONEY)
        self.assertEqual(self.w.energy, 0)

    def test_work_raises_exception_with_negative_energy(self):
        self.w.energy = -1

        with self.assertRaises(Exception) as ex:
            self.w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")
        self.assertEqual(self.w.money, WorkerTests.MONEY)
        self.assertEqual(self.w.energy, -1)

    def test_worker_rest(self):
        self.w.rest()
        self.assertEqual(self.w.energy, WorkerTests.ENERGY + 1)

    def test_worker_get_info(self):
        self.assertEqual(self.w.get_info(), "Name has saved 0 money.")



if __name__ == "__main__":
    main()
