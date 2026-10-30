from datetime import datetime


class Review:
    def __init__(self, reviewID: int, userID: int,
                 courseID: int, score: int, text: str,
                 date: datetime, editedAt: datetime = None):
        if score < 1 or score > 5:
            raise ValueError("Score must be between 1 and 5")

        self.reviewID = reviewID
        self.userID = userID
        self.courseID = courseID
        self.score = score
        self.text = text
        self.date = date
        self.editedAt = editedAt
        self.votes = []

    def getHelpfulnessScore(self) -> int:
        helpfulness = 0

        for vote in self.votes:
            if vote:
                helpfulness += 1
            else:
                helpfulness -= 1

        return helpfulness