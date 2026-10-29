from abc import ABC, abstractmethod
from typing import Any, List, Optional
from ReviewObserver import ReviewObserver
from Review import Review

class ReviewSubject(ABC):

  def __init__(self):
    self._observers: List[ReviewObserver] = []

  def attach(self, observer: ReviewObserver) -> None:
    if observer not in self._observers:
      self._observers.append(observer)

  def detach(self, observer: ReviewObserver) -> None:
    if observer in self._observers:
      self._observers.remove(observer)

  def notifyObservers(self, review: Review) -> None:
    for observer in self._observers:
      observer.update(review)