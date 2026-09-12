class InterviewSession:
    """
    Store the state of an interview session.
    """

    def __init__(self, questions: list[str]):
        self.questions = questions
        self.current_question_index = 0
        self.evaluations = []

    def get_current_question(self) -> str | None:
        """
        Return the current interview question.
        """

        if self.current_question_index >= len(self.questions):
            return None

        return self.questions[self.current_question_index]

    def add_evaluation(self, evaluation: dict):
        """
        Store an evaluation for the current question
        and move to the next question.
        """

        self.evaluations.append(evaluation)
        self.current_question_index += 1

    def is_complete(self) -> bool:
        """
        Check whether all questions have been answered.
        """

        return self.current_question_index >= len(self.questions)

    def get_progress(self) -> dict:
        """
        Return interview progress.
        """

        return {
            "current_question": self.current_question_index + 1,
            "total_questions": len(self.questions),
            "completed": self.current_question_index,
            "is_complete": self.is_complete()
        }