from mastermind import Codemaker


class TestMastermind:
    def test_codebreaker_guesses_all_blue_combination(self):
        codemaker = Codemaker(["blue", "blue", "blue", "blue"])
        guess = ["blue", "blue", "blue", "blue"]

        evaluation = codemaker.evaluate(guess)

        assert [4, 0] == evaluation