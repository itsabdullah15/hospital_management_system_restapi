from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Invoice
def generate_invoice_pdf(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)

    # Create an in-memory buffer
    buffer = BytesIO()

    # Create a PDF canvas
    p = canvas.Canvas(buffer, pagesize=letter)

    # Set up the PDF content (you can customize it as per your needs)
    p.drawString(100, 750, f"Invoice ID: {invoice.id}")
    p.drawString(100, 730, f"Date: {invoice.date}")
    p.drawString(100, 710, f"Customer Name: {invoice.customer.name}")
    
    # You can add more details or customize this section as per your template

    # Finalize the PDF
    p.showPage()
    p.save()

    # Move buffer position to beginning of file
    buffer.seek(0)
