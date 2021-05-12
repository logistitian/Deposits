from django.db import models


class Deposit(models.Model):
    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(decimal_places=2, max_digits=4)

    def interest(self):
        interest = float((self.deposit * ((1 + self.rate)**self.term))-self.deposit)
        return interest