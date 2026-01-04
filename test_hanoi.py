import unittest
from hanoi import hanoi_solver

class TestHanoiSolver(unittest.TestCase):
    def test_hanoi_1(self):
        expected = "[1] [] []\n[] [] [1]"
        self.assertEqual(hanoi_solver(1), expected)

    def test_hanoi_2(self):
        expected = "[2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1]"
        self.assertEqual(hanoi_solver(2), expected)

    def test_hanoi_3(self):
        expected = (
            "[3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n"
            "[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1]"
        )
        self.assertEqual(hanoi_solver(3), expected)
