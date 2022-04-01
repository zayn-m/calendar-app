from abc import ABC, abstractmethod

class ICalculateView:
    @abstractmethod
    def display_age(self, date_of_birth): pass

    @abstractmethod
    def display_date_from_days(self, days): pass
