# Django Core Backend Project

This is a **complete Django Core backend project** built step-by-step to understand Django fundamentals, ORM, admin panel, authentication, and best practices.  

---

## Project Goal

Build a working Django backend with:

- Virtual environment  
- `requirements.txt`  
- Homepage  
- Database models (`Profile`, `Post`)  
- Admin panel  
- Authentication system (signup/login/dashboard)  

---

## Folder Structure

django project/
├─ venv/
└─ core/
├─ manage.py
├─ core/
│ ├─ settings.py
│ ├─ urls.py
│ └─ ...
└─ users/
├─ views.py
├─ models.py
├─ admin.py
├─ forms.py
├─ urls.py
└─ templates/
└─ users/
├─ signup.html
├─ login.html
├─ dashboard.html
└─ home.html


---

## Setup Instructions

### Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies

```bash
pip install django
pip install -r requirements.txt
```