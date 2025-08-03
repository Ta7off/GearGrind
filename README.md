# GearGrind

Car social media/auction platform built with Django.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Ta7off/GearGrind.git
cd GearGrind
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **⚠️ IMPORTANT**: Fix your settings before running the app. Create a `.env` file or modify `settings.py` directly.

6. Run the server:
```bash
python manage.py runserver
```

## Contributing

Pull requests welcome! Open issues for bugs or ideas.