# Hospital Management System (HMS) API

## Overview

The Hospital Management System (HMS) API allows hospitals and healthcare providers to manage patient records, appointments, prescriptions, billing, and more. This API provides a RESTful interface for all the core functionalities of the system.

## Features
- User authentication and authorization with JWT
- Role-based access control (admin, doctor, patient, staff)
- Appointment scheduling and management
- Patient medical history and lab results management
- Prescription and billing management
- Notifications (email/SMS)

## Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL/MySQL
- **Authentication:** JWT (JSON Web Tokens)
- **Other Libraries:** WeasyPrint (for PDF invoice generation), Redis (for caching)

## Installation

### Prerequisites
- Python 3.x
- Django 5.x
- PostgreSQL

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hospital-management-system-api.git
   cd hospital-management-system-api

Create and activate a virtual environment:

python manage.py migrate
Create a superuser to manage the admin panel (optional):

## API Endpoints

### 1. **User Authentication and Authorization**
- **Register User**  
  `POST /api/users/register/`

- **Login User (JWT)**  
  `POST /api/users/login/`

- **Logout User**  
  `POST /api/users/logout/`

- **List Users (Admin Only)**  
  `GET /api/users/`

- **User Profile**  
  `GET /api/users/profile/`

- **Update User Profile**  
  `PUT /api/users/profile/`

- **Change Password**  
  `POST /api/users/change-password/`

---

### 2. **Appointments**
- **List Appointments**  
  `GET /api/appointments/`

- **Create Appointment**  
  `POST /api/appointments/`

- **Retrieve Appointment (by ID)**  
  `GET /api/appointments/{appointment_id}/`

- **Update Appointment (by ID)**  
  `PUT /api/appointments/{appointment_id}/`

- **Delete Appointment (by ID)**  
  `DELETE /api/appointments/{appointment_id}/`

---

### 3. **Medical History**
- **List Medical History**  
  `GET /api/medical-history/`

- **Create Medical History Entry**  
  `POST /api/medical-history/`

- **Retrieve Medical History Entry (by ID)**  
  `GET /api/medical-history/{history_id}/`

- **Update Medical History (by ID)**  
  `PUT /api/medical-history/{history_id}/`

- **Delete Medical History Entry (by ID)**  
  `DELETE /api/medical-history/{history_id}/`

---

### 4. **Lab Results**
- **List Lab Results**  
  `GET /api/lab-results/`

- **Create Lab Result**  
  `POST /api/lab-results/`

- **Retrieve Lab Result (by ID)**  
  `GET /api/lab-results/{result_id}/`

- **Update Lab Result (by ID)**  
  `PUT /api/lab-results/{result_id}/`

- **Delete Lab Result (by ID)**  
  `DELETE /api/lab-results/{result_id}/`

---

### 5. **Prescriptions**
- **List Prescriptions**  
  `GET /api/prescriptions/`

- **Create Prescription**  
  `POST /api/prescriptions/`

- **Retrieve Prescription (by ID)**  
  `GET /api/prescriptions/{prescription_id}/`

- **Update Prescription (by ID)**  
  `PUT /api/prescriptions/{prescription_id}/`

- **Delete Prescription (by ID)**  
  `DELETE /api/prescriptions/{prescription_id}/`

---

### 6. **Billing**
- **List Invoices**  
  `GET /api/billing/invoices/`

- **Create Invoice**  
  `POST /api/billing/invoices/`

- **Retrieve Invoice (by ID)**  
  `GET /api/billing/invoices/{invoice_id}/`

- **Update Invoice (by ID)**  
  `PUT /api/billing/invoices/{invoice_id}/`

- **Delete Invoice (by ID)**  
  `DELETE /api/billing/invoices/{invoice_id}/`

---

### 7. **Notifications**
- **List Notifications**  
  `GET /api/notifications/`

- **Send Notification**  
  `POST /api/notifications/send/`

---

### 8. **QR Code Generation for Payment**
- **Generate Payment QR Code**  
  `GET /api/payment/qr/{invoice_id}/`


# Authentication Flow

Below is a flowchart describing the user authentication process, including registration, login, accessing protected routes, and logout.

```mermaid
flowchart TD
    A[User Registration] -->|POST /api/users/register/| B[Login]
    B -->|POST /api/users/login/| C{JWT Token}
    C -->|Valid Token| D[Access Protected Routes]
    C -->|Invalid Token| E[Return Unauthorized]
    D --> F[Logout]
    F -->|POST /api/users/logout/| G[Invalidate Token]
    D -->|Access Allowed| H[Perform Actions]
    H --> I[Complete Actions and Logout]