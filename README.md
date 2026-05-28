# Inventory Management System (React + Flask)

## Project Overview
This is a full-stack Inventory Management System built using:

- Frontend: React (Vite)
- Backend: Flask (Python)
- Database: SQLite
- Authentication: JWT

---

## Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes

### Inventory Management
- Create Products
- Read Products
- Update Products
- Delete Products

### Relationships
- One-to-Many: Category → Products
- Many-to-Many: Users ↔ Products

---

## Tech Stack

### Frontend
- React
- React Router
- Axios

### Backend
- Flask
- Flask SQLAlchemy
- Flask-JWT-Extended
- Flask-Migrate

### Database
- SQLite

---

## Project Structure

inventory_project/
│
├── backend/
│ ├── app.py
│ ├── models/
│ ├── routes/
│ ├── extensions.py
│
├── frontend/
│ ├── src/
│ ├── pages/
│ ├── components/


---

## How to Run Project

### Backend
```bash
cd backend
python app.py

#Frontend

cd frontend
npm install
npm run dev

Authentication Flow
User registers
User logs in
JWT token is generated
Token stored in localStorage
Protected routes accessed using token
API Endpoints
Auth
POST /api/auth/register
POST /api/auth/login
Products
GET /api/products
POST /api/products
PUT /api/products/<id>
DELETE /api/products/<id>
Current Status
React frontend: Debugging routing issue
Backend: Running
Database: Working

#Author
Robert Maina