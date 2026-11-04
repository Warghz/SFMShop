from abc import abstractmethod, ABC

class Payment(ABC):

    def __init__(self, total):
        self.total = total


    @abstractmethod
    def process_payment():
        pass


class CardPayment(Payment):

    def __init__(self, total, card_number):
        super().__init__(total)
        self.__card_number = card_number


    @property
    def card_number(self):
        return self.__card_number


    def process_payment(self):
        return f"Оплата картой **** {self.card_number[-4:]}: {self.total} руб."


class PayPalPayment(Payment):

    def __init__(self, total, mail):
        super().__init__(total)
        self.mail = mail


    def process_payment(self):
        return f"Оплата PayPal ({self.mail}): {self.total} руб."
        
