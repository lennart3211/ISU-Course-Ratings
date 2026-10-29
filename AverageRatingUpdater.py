from Review import Review
from ReviewObserver import ReviewObserver

class AverageRatingUpdater(ReviewObserver):

  def update(self, review: Review) -> None:
    # Logic to update course average rating upon a new review
    pass