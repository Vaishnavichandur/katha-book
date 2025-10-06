from rest_framework import serializers
from .models import Customer, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'date']


class CustomerSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    paid = serializers.SerializerMethodField()
    due = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'name', 'village', 'phone', 'total_amount', 'payments', 'paid', 'due']

    def get_paid(self, obj):
        return obj.paid_amount()

    def get_due(self, obj):
        return obj.due_amount()
