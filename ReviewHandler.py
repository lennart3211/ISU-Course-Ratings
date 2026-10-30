
from ReviewStorage import ReviewStorage
from User import User
from Admin import Admin
from Course import Course
from Review import Review
from Reply import Reply

class ReviewHandler:

  def __init__(self, review_storage: ReviewStorage):
    self.review_storage = review_storage

  def createReview(
      self, user: User, course: Course, score: int, text: str
  ) -> Review:
    review = Review(
        reviewID=0, courseID=course.courseID, userID=user.userID, score=score, text=text
    )
    self.review_storage.saveReview(review)
    return review

  def editReview(
      self, user: User, review: Review, score: int, text: str
  ) -> None:
    review.score = score
    review.text = text
    self.review_storage.saveReview(review)

  def deleteReview(self, user: User, review: Review) -> None:
    self.review_storage.deleteReview(review.reviewID)

  def replyToReview(self, user: User, review: Review, text: str) -> Reply:
    reply = Reply(replyID=0, reviewID=review.reviewID, userID=user.userID, text=text)
    self.review_storage.saveReply(reply)
    return reply

  def voteOnReview(self, user: User, review: Review, isHelpful: bool) -> None:
    self.review_storage.saveVote(user.userID, review.reviewID, isHelpful)

  def getReviews(self, course: Course, sortByScore: bool) -> List[Review]:
    reviews = self.review_storage.retreiveReviewsForCourse(course.courseID)
    if sortByScore:
      reviews.sort(key=lambda r: r.score, reverse=True)
    return reviews

  def adminDeleteReview(self, admin: Admin, review: Review) -> None:
    self.review_storage.deleteReview(review.reviewID)

  def adminDeleteReply(self, admin: Admin, reply: Reply) -> None:
    self.review_storage.deleteReply(reply.replyID)