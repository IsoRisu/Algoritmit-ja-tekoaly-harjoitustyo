import unittest
from main import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_play_middle(self):
        # Play a piece to middle
        self.board.play(3,0)
        result = self.board.print_board()
        print(result)

        self.assertEqual(result, """| | | | | | | |\n| | | | | | | |\n| | | | | | | |\n| | | | | | | |\n| | | | | | | |\n| | | |0| | | |\n 0 1 2 3 4 5 6""")
