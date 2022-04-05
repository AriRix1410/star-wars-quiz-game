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
