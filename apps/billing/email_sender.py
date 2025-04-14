from django.core.mail import EmailMessage
from .pdf_generator import generate_invoice_pdf

def send_invoice_email(invoice):
    pdf_file = generate_invoice_pdf(invoice)

    email = EmailMessage(
        subject=f"Invoice #{invoice.id}",
        body="Please find your invoice attached.",
        from_email="",
        to=[invoice.patient.email]
    )
    email.attach(f"invoice_{invoice.id}.pdf", pdf_file, "application/pdf")
    email.send()
