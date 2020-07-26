from .rpc.processors import *

import unittest


class TestProcessors(unittest.TestCase):
    def test_valmap1(self):
        mapper = valmap([0, 1, 2, 3], ['off', 'low', 'normal', 'high'])
        self.assertEqual(mapper(1), ['low'])

    def test_valmap2(self):
        mapper = valmap([0, 1, 2, 3], ['off', 'low', 'normal', 'high'], index=1)
        arg0 = 'arg_index_0'
        self.assertEqual(mapper(arg0, 3), [arg0, 'high'])

    def test_choose_int(self):
        chooser = choose(2)
        self.assertEqual(chooser(0, 2, 4, 6), 4)

    def test_choose_iter(self):
        chooser = choose([0, 2, 4])
        results = chooser('one', 'two', 'three', 'four', 'five')
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], 'one')
        self.assertEqual(results[1], 'three')
        self.assertEqual(results[2], 'five')

    def test_int_to_bool(self):
        self.assertEqual(int_to_bool(1), True)
        self.assertEqual(int_to_bool('1'), True)
        self.assertEqual(int_to_bool(0), False)
        self.assertEqual(int_to_bool('0'), False)

    def test_bool_to_int(self):
        self.assertEqual(bool_to_int(True), 1)
        self.assertEqual(bool_to_int(False), 0)

    def test_check_success(self):
        self.assertEqual(check_success(0), True)
        self.assertEqual(check_success(-1), False)

    def test_to_datetime1(self):
        input_ = 1414963929334259
        expected = datetime.datetime(2014, 11, 2, 21, 32, 9, 334259, tzinfo=datetime.timezone.utc)
        self.assertEqual(to_datetime(input_), expected)

    def test_to_datetime2(self):
        self.assertEqual(to_datetime(0), None)
