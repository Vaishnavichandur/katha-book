from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def paid_amount(self):
        return sum(payment.amount for payment in self.payments.all())

    def due_amount(self):
        return self.total_amount - self.paid_amount()

    def __str__(self):
        return self.name


class Payment(models.Model):
    customer = models.ForeignKey(Customer, related_name="payments", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default="2025-10-06")

    def __str__(self):
        return f"{self.amount} on {self.date}"
