# Code taken from [Mike Dane](https://www.youtube.com/watch?v=SgQhwtIoQ7o)
class Question:
    """
    This is a class for storing information about the questions.
    """
    def __init__(self, prompt, answer):
        """
        Parameters:
        prompt: The question being asked.
        answer: The answer of the question.
        """
        self.prompt = prompt
        self.answer = answer
