# Bakery Order Management System

## Problem
A local bakery was struggling to manage orders received via walk-ins, phone calls, and WhatsApp.

## Assumptions
- Staff will use the system on desktop/laptop
- Three order statuses: Pending, Completed, Cancelled
- No customer login required for MVP

## Features Implemented
- Dashboard with total, pending, completed order counts
- Add new orders
- View all orders with color-coded status
- Update existing orders
- Delete orders

## Database Design
- **Order**: customer_name, phone, product, quantity, status

## Setup Instructions
1. Clone the repo
2. Install dependencies: `pip install django`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`
5. Open: `http://127.0.0.1:8000`

## Future Improvements
- Customer login portal to check order status
- WhatsApp notification integration
- Sales reports and charts
- Mobile app