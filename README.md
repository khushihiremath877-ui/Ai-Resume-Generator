# AI Resume Generator

## Overview

AI Resume Generator is a web application built using FastAPI, HTML, CSS, and JavaScript. The application collects user information and generates a formatted resume dynamically through a FastAPI backend.

The project demonstrates frontend-backend communication, API development, JSON handling, and dynamic content generation.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Pydantic

### Communication

* REST API
* JSON

---

## Features

* User-friendly interface
* Resume information collection
* Dynamic resume generation
* FastAPI backend integration
* JSON request and response handling

---

## Workflow

1. User enters:

   * Name
   * Email
   * Phone Number
   * Education
   * Skills

2. Frontend sends the data to FastAPI using a POST request.

3. FastAPI processes the request and generates a formatted resume.

4. The generated resume is returned as a JSON response.

5. The frontend displays the generated resume on the webpage.

---

## API Endpoint

### Generate Resume

```http
POST /generate
```

### Sample Request

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "education": "Computer Science",
  "skills": "Python, FastAPI, HTML, CSS"
}
```

### Sample Output

```text
====================================
JOHN DOE
====================================

Email : john@example.com
Phone : 9876543210

------------------------------------
EDUCATION
------------------------------------

Computer Science

------------------------------------
SKILLS
------------------------------------

Python, FastAPI, HTML, CSS

------------------------------------
PROFESSIONAL SUMMARY
------------------------------------

John Doe is a motivated individual with a strong interest in technology, continuous learning and innovation.

====================================
```

---

## Project Structure

```text
AI-Resume-Generator/
│
├── main.py
├── index.html
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Learning Outcomes

* FastAPI basics
* REST API development
* JSON request and response handling
* Frontend-backend integration
* Dynamic content generation
## Architecture Improvements

The project has been refactored into a modular FastAPI structure using separate layers for routes, schemas, and services.

Benefits:

* Improved code organization
* Better maintainability
* Easier scalability for future features
* Clear separation of responsibilities

---

## Author

Khushi Hiremath
