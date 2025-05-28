# Blood-Donation-Management-API
This project is a RESTful API built using Django and Django REST Framework to manage a Blood Donation System. It allows for managing users, patients, and donations with CRUD operations, search, filters, and role-based access.

## 🔧 Features

- User, Patient, and Donation creation with authenticated access
- View lists of users, patients, donations, and completed patients
- Filter and search donations and patients
- Update user and patient records
- Delete user records securely
- RBAC-ready endpoints secured via DRF permissions

## 🛠️ Tech Stack

- Python 3
- Django 4+
- Django REST Framework
- Django Filters
- SQLite / MySQL (configure in `settings.py`)

## 🚀 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/Create-user/` | Create a new user |
| `/Create-patient/` | Register a new patient |
| `/Create-donation/` | Record a new donation |
| `/View-user/` | List all users |
| `/View-patients/` | List all patients |
| `/View-completed-patient/` | List patients with completed donations |
| `/View-donation/` | List donations with filtering & search |
| `/update-user/` | Update existing users |
| `/update-patient/` | Update patients that are not completed |
| `/delete-user/` | Delete a user |

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blood-donation-api.git
   cd blood-donation-api
Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
Test API
Use Postman or any REST client to interact with the endpoints. All create/update/delete operations require authentication.

✍️ Notes
Use Django admin to manually add roles or assign permissions if RBAC is extended.

All POST/PUT/DELETE requests require IsAuthenticated access.
