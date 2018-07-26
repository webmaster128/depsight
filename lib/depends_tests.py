import unittest

from . import depends

class TestDependsOn(unittest.TestCase):
    def test_depends_on_one_level(self):
        deps = { 'B': ['A'] }
        self.assertEqual(depends.depends_on('B', 'A', deps), True)
        self.assertEqual(depends.depends_on('A', 'B', deps), False)
        self.assertEqual(depends.depends_on('C', 'A', deps), False)
        self.assertEqual(depends.depends_on('C', 'B', deps), False)
        self.assertEqual(depends.depends_on('B', 'C', deps), False)
        self.assertEqual(depends.depends_on('A', 'C', deps), False)

    def test_depends_on_two_level(self):
        deps = { 'C': ['B'], 'B': ['A'] }
        self.assertEqual(depends.depends_on('C', 'A', deps), True)

    def test_depends_on_multi_level(self):
        deps = {
            'F': ['E'],
            'E': ['D'],
            'D': ['C'],
            'C': ['B'],
            'B': ['A'],
        }
        self.assertEqual(depends.depends_on('F', 'E', deps), True)
        self.assertEqual(depends.depends_on('F', 'D', deps), True)
        self.assertEqual(depends.depends_on('F', 'C', deps), True)
        self.assertEqual(depends.depends_on('F', 'B', deps), True)
        self.assertEqual(depends.depends_on('F', 'A', deps), True)
        self.assertEqual(depends.depends_on('E', 'D', deps), True)
        self.assertEqual(depends.depends_on('E', 'C', deps), True)
        self.assertEqual(depends.depends_on('E', 'B', deps), True)
        self.assertEqual(depends.depends_on('E', 'A', deps), True)
        self.assertEqual(depends.depends_on('D', 'C', deps), True)
        self.assertEqual(depends.depends_on('D', 'B', deps), True)
        self.assertEqual(depends.depends_on('D', 'A', deps), True)
        self.assertEqual(depends.depends_on('C', 'B', deps), True)
        self.assertEqual(depends.depends_on('C', 'A', deps), True)
        self.assertEqual(depends.depends_on('B', 'A', deps), True)

        self.assertEqual(depends.depends_on('A', 'A', deps), False)
        self.assertEqual(depends.depends_on('A', 'B', deps), False)
        self.assertEqual(depends.depends_on('A', 'C', deps), False)
        self.assertEqual(depends.depends_on('A', 'D', deps), False)
        self.assertEqual(depends.depends_on('A', 'E', deps), False)
        self.assertEqual(depends.depends_on('A', 'F', deps), False)
        self.assertEqual(depends.depends_on('B', 'B', deps), False)
        self.assertEqual(depends.depends_on('B', 'C', deps), False)
        self.assertEqual(depends.depends_on('B', 'D', deps), False)
        self.assertEqual(depends.depends_on('B', 'E', deps), False)
        self.assertEqual(depends.depends_on('B', 'F', deps), False)
        self.assertEqual(depends.depends_on('C', 'C', deps), False)
        self.assertEqual(depends.depends_on('C', 'D', deps), False)
        self.assertEqual(depends.depends_on('C', 'E', deps), False)
        self.assertEqual(depends.depends_on('C', 'F', deps), False)
        self.assertEqual(depends.depends_on('D', 'D', deps), False)
        self.assertEqual(depends.depends_on('D', 'E', deps), False)
        self.assertEqual(depends.depends_on('D', 'F', deps), False)
        self.assertEqual(depends.depends_on('E', 'E', deps), False)
        self.assertEqual(depends.depends_on('E', 'F', deps), False)
        self.assertEqual(depends.depends_on('F', 'F', deps), False)
