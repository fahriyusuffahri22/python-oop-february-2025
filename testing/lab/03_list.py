from unittest import TestCase, main


class IntegerListTests(TestCase):
    ARGS = [x for x in range(10)]
    I = len(ARGS) // 2

    def setUp(self):
        self.il = IntegerList(*IntegerListTests.ARGS)

    def test_init_with_integers_args(self):
        self.assertEqual(self.il.get_data(), IntegerListTests.ARGS)

    def test_init_with_string_args(self):
        il = IntegerList(*(str(x) for x in IntegerListTests.ARGS))
        self.assertEqual(il.get_data(), [])

    def test_init_with_mixed_args(self):
        il = IntegerList(*(x if x % 2 == 0 else str(x) for x in IntegerListTests.ARGS))
        self.assertEqual(il.get_data(), [x for x in IntegerListTests.ARGS if x % 2 == 0])

    def test_add(self):
        element = IntegerListTests.ARGS[IntegerListTests.I]
        expected_data = IntegerListTests.ARGS.copy()
        expected_data.append(element)

        self.assertEqual(self.il.add(element), expected_data)

    def test_add_raises_value_error_with_not_int_value(self):
        element = str(IntegerListTests.ARGS[IntegerListTests.I])

        with self.assertRaises(ValueError) as ex:
            self.il.add(element)

        self.assertEqual(str(ex.exception), "Element is not Integer")
        self.assertEqual(self.il.get_data(), IntegerListTests.ARGS)

    def test_remove_index(self):
        expected_element = IntegerListTests.ARGS[IntegerListTests.I]
        expected_data = IntegerListTests.ARGS.copy()
        expected_data.pop(IntegerListTests.I)

        self.assertEqual(self.il.remove_index(IntegerListTests.I), expected_element)
        self.assertEqual(self.il.get_data(), expected_data)

    def test_remove_index_raises_index_error_with_length_value(self):
        i = len(IntegerListTests.ARGS)

        with self.assertRaises(IndexError) as ex:
            self.il.remove_index(i)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(self.il.get_data(), IntegerListTests.ARGS)

    def test_remove_index_raises_index_error_with_bigger_length_value(self):
        i = len(IntegerListTests.ARGS) + 1

        with self.assertRaises(IndexError) as ex:
            self.il.remove_index(i)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(self.il.get_data(), IntegerListTests.ARGS)


    def test_get(self):
        self.assertEqual(self.il.get(IntegerListTests.I), IntegerListTests.ARGS[IntegerListTests.I])

    def test_get_raises_index_error_with_length_value(self):
        i = len(IntegerListTests.ARGS)

        with self.assertRaises(IndexError) as ex:
            self.il.get(i)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_raises_index_error_with_bigger_length_value(self):
        idx = len(IntegerListTests.ARGS) + 1

        with self.assertRaises(IndexError) as ex:
            self.il.get(idx)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert(self):
        element = IntegerListTests.ARGS[IntegerListTests.I]
        self.il.insert(IntegerListTests.I, element)

        expected_data = IntegerListTests.ARGS.copy()
        expected_data.insert(IntegerListTests.I, element)

        self.assertEqual(self.il.get_data(), expected_data)

    def test_insert_raises_index_error_with_length_value(self):
        i = len(IntegerListTests.ARGS)
        element = IntegerListTests.ARGS[IntegerListTests.I]

        with self.assertRaises(IndexError) as ex:
            self.il.insert(i, element)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_raises_index_error_with_bigger_length_value(self):
        i = len(IntegerListTests.ARGS) + 1
        element = IntegerListTests.ARGS[IntegerListTests.I]

        with self.assertRaises(IndexError) as ex:
            self.il.insert(i, element)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_raises_value_error_with_not_int_value(self):
        idx = IntegerListTests.I
        element = str(IntegerListTests.ARGS[IntegerListTests.I])

        with self.assertRaises(ValueError) as ex:
            self.il.insert(idx, element)

        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.il.get_biggest(), max(IntegerListTests.ARGS))

    def test_get_index(self):
        self.assertEqual(self.il.get_index(IntegerListTests.I), IntegerListTests.ARGS[IntegerListTests.I])


if __name__ == "__main__":
    main()
