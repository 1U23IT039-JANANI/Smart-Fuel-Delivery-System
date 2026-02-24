Smart Fuel Delivery System - README

Project Description
Smart Fuel Delivery System is a Django-based web application that allows users to:

- Register and login.
- Book fuel orders (Petrol/Diesel) with details like liters, address, and phone number.
- Track order status.
- Dashboard for users showing their orders.
- Admin panel to manage all orders.

This project is suitable as a college project or demo for learning Django, authentication, and CRUD operations.

Features

1. User Registration & Login  
   Users can create accounts and log in to the system.

2. Book Fuel  
   Users can book fuel by entering:
   - Name (auto from user)
   - Fuel type (Petrol/Diesel)
   - Liters
   - Address
   - Phone number

3. Dashboard  
   Users can view all their orders and track status.

4. Admin Panel  
   Admin can see all users’ orders and update order status (Pending, Approved, On the Way, Delivered).

5. Order Confirmation  
   After booking, a success message appears.

6. Responsive & Modern UI  
   Navbar, forms, and dashboard are styled using CSS.

Technologies Used

- Python 3.x
- Django 4.x
- HTML / CSS / Bootstrap (optional)
- SQLite (default Django database)

Project Structure

fuel_delivery/
├── fuel_delivery/          # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── main/                   # Django app
│   ├── models.py           # Order model
│   ├── views.py            # Views: register, dashboard, book_order, track_order
│   ├── forms.py            # User registration form
│   ├── templates/          # HTML templates
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── book_order.html
│   │   ├── register.html
│   │   └── login.html
│   └── static/             # CSS files
│       └── styles.css
└── manage.py

Setup Instructions (Run on Another System)

1. Clone or copy the project  
   Copy the entire `fuel_delivery` folder to the new system.

2. Install Python  
   Make sure Python 3.x is installed. Check with:

   python --version

3. Install virtual environment (optional but recommended)

   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

4. Install dependencies  
   Install Django if not installed:

   pip install django

   If you have a `requirements.txt` file, you can do:

   pip install -r requirements.txt

5. Apply migrations  
   Navigate to the project root where `manage.py` exists and run:

   python manage.py makemigrations
   python manage.py migrate

6. Create superuser (for admin access)

   python manage.py createsuperuser

   Follow the prompts to create a username, email, and password.

7. Run the development server

   python manage.py runserver

8. Access the app  

   Open your browser and go to:

   - User dashboard: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

Default URLs

Page                  | URL
----------------------|----------------------------
Admin Panel          | /admin/
Login                | /login/
Logout               | /logout/
Register             | /register/
User Dashboard       | /dashboard/
Book Fuel Order      | /book/
Track Order          | /track/<order_id>/

Notes

- Make sure DEBUG = True in settings.py while testing locally.
- For deployment, change DEBUG = False and configure allowed hosts.
- The project uses SQLite database by default — no extra database setup needed.
- You can customize the CSS in static/styles.css for colors, fonts, and layout.

Optional Improvements

- Add Bootstrap or other CSS framework for better UI.
- Add email or SMS notifications for order confirmation.
- Implement Google Maps API for picking address and latitude/longitude.
- Add pagination for dashboard orders if users have many orders.

This README provides everything to run, test, and modify the project on another system.
username ;admin \ password ; admin112233
