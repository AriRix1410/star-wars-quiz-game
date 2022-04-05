class Question:
    """
    This is a class for storing information about the questions.
    Attributes:
        prompt: The question being asked.
        answer: The answer of the question.
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer