from datetime import datetime


class Reply:
    def __init__(self, replyID: int, reviewID: int,
                 userID: int, text: str, date: datetime):
        self.replyID = replyID
        self.reviewID = reviewID
        self.userID = userID
        self.text = text
        self.date = date