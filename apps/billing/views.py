from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from .email_sender import send_invoice_email

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def perform_create(self, serializer):
        invoice = serializer.save()
        send_invoice_email(invoice)
