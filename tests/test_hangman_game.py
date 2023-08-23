import unittest
from unittest.mock import Mock
from hangman.game_logic.hangman_game import HangmanGame
from hangman.hangman_db.models.theme import Theme

class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        self.game = HangmanGame()
        self.mock_db_session = Mock()


    def test_get_game_data(self):
        game_data = self.game.get_game_data()
        self.assertEqual(game_data, {
            "theme_id": None,
            "theme_name": None,
            "secret_word": "",
            "guess_word": [],
            "guessed_letters": [],
            "guesses_left": 10,
            "win": None,
        })

    def test_select_theme_valid(self):
        theme_id = 1
        mock_theme = Theme(id=theme_id, name="Test Theme")
        self.game.THEMES = [mock_theme]
        
        self.game.select_theme(theme_id)
        self.assertEqual(self.game.theme_id, theme_id)
        self.assertEqual(self.game.theme_name, "Test Theme")

    def test_select_theme_invalid(self):
        theme_id = 1
        self.game.THEMES = []
        
        with self.assertRaises(ValueError):
            self.game.select_theme(theme_id)



    def test_guess_letter_correct(self):
        self.game.secret_word = "apple"
        self.game.guess_word = ["_", "_", "_", "_", "_"]
        
        response, status_code = self.game.guess_letter("a")
        self.assertEqual(response, "Good guess!")
        self.assertEqual(status_code, 201)
        self.assertEqual(self.game.guess_word, ["a", "_", "_", "_", "_"])

    def test_guess_letter_incorrect(self):
        self.game.secret_word = "apple"
        self.game.guess_word = ["_", "_", "_", "_", "_"]
        self.game.guesses_left = 10

        response, status_code = self.game.guess_letter("z")
        self.assertEqual(response, "Wrong guess. 9 guesses left.")
        self.assertEqual(status_code, 203)
        self.assertEqual(self.game.guesses_left, 9)





if __name__ == '__main__':
    unittest.main()
