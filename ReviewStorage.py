from DBConnection import DBConnection
from Review import Review
from Reply import Reply
from typing import List, Optional

class ReviewStorage:

  def __init__(self, db: DBConnection):
    self.db = db

  def saveReview(self, review: Review) -> None:
    pass

  def retreiveReview(self, reviewID: int) -> Optional[Review]:
    return None

  def retreiveReviewsForCourse(self, courseID: int) -> List[Review]:
    return []

  def deleteReview(self, reviewID: int) -> None:
    pass

  def saveReply(self, reply: Reply) -> None:
    pass

  def deleteReply(self, replyID: int) -> None:
    pass

  def saveVote(self, userID: int, reviewID: int, isHelpful: bool) -> None:
    pass