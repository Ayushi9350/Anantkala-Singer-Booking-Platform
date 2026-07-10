# 🎵 Anantkala — Singer Management System

## VS Code ma Run Karva na Steps (Step by Step)

### Step 1: Terminal Open Karo
VS Code ma `Ctrl + ` ` (backtick) press karo terminal open thase

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 3: Migrations Chalaavo
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Admin User Banavo
```bash
python manage.py createsuperuser
```
- Username, email, password nakhso

### Step 5: Server Start Karo
```bash
python manage.py runserver
```

### Website Open Karo:
- **Home Page:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Singers Page:** http://127.0.0.1:8000/singers/
- **Login Page:** http://127.0.0.1:8000/accounts/login/

---

## Google OAuth Setup (Google Login Mate)

1. https://console.cloud.google.com/ par jao
2. New Project banavo — "Anantkala"
3. APIs & Services → Credentials → Create OAuth 2.0 Client ID
4. Authorized redirect URI: `http://127.0.0.1:8000/accounts/google/callback/`
5. Client ID and Secret copy karo
6. `settings.py` ma update karo:
   ```python
   'client_id': 'YOUR_GOOGLE_CLIENT_ID',  # paste karo
   'secret': 'YOUR_GOOGLE_CLIENT_SECRET',  # paste karo
   ```
7. Admin panel → Sites → localhost:8000 → example.com ne badlo

---

## Admin Panel ma Singer Add Karvani Rite
1. `/admin/` par jao
2. Login karo (superuser credentials)
3. **Genres** → Genre add karo (e.g. "Classical", "Bollywood")
4. **Singers** → Singer add karo:
   - Name, Photo, Bio, Genre
   - Price, Experience
   - Contact details
   - Featured checkbox tick karo home page par avva mate
5. Gallery images pan add thay singer detail ma

---

## Project Structure
```
anantkala/
├── manage.py
├── settings.py
├── urls.py
├── requirements.txt
├── singers/          ← Singer app
│   ├── models.py     ← Singer, Genre, Gallery models
│   ├── views.py      ← Home, List, Detail, About, Contact
│   ├── admin.py      ← Admin panel config
│   └── urls.py
├── booking/          ← Booking app  
│   ├── models.py     ← Booking model
│   ├── views.py      ← Book singer, My bookings
│   ├── forms.py      ← Booking form
│   └── urls.py
├── templates/
│   ├── base.html     ← Navbar + Footer
│   ├── account/
│   │   └── login.html ← Google login page
│   ├── singers/
│   │   ├── home.html
│   │   ├── singer_list.html
│   │   ├── singer_detail.html
│   │   ├── about.html
│   │   └── contact.html
│   └── booking/
│       ├── book_singer.html
│       └── my_bookings.html
├── static/
│   └── css/
│       └── style.css  ← Dark Golden Theme
└── media/            ← Uploaded singer photos
```

---

## Features
✅ Dark Golden Luxury Theme (Cinzel Decorative Font)
✅ Google OAuth Login (No Registration needed)
✅ Singer Listing with Genre Filter
✅ Singer Detail with Gallery
✅ Online Booking System
✅ My Bookings Page
✅ Full Admin Panel
✅ Responsive Design
✅ Featured Singers on Homepage
✅ Animated scroll reveals
