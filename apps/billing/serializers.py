from rest_framework import serializers
from .models import Invoice, InvoiceService


class InvoiceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceService
        fields = ['id', 'name', 'description', 'amount']


class InvoiceSerializer(serializers.ModelSerializer):
    services = InvoiceServiceSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'patient', 'created_at', 'due_date', 'total_amount', 'is_paid', 'services']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        invoice = Invoice.objects.create(**validated_data)
        for service_data in services_data:
            InvoiceService.objects.create(invoice=invoice, **service_data)
        return invoice

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if services_data:
            instance.services.all().delete()
            for service_data in services_data:
                InvoiceService.objects.create(invoice=instance, **service_data)

        return instance
