# Event Ticketing Management System

A comprehensive Django-based event ticketing management system with role-based access for super admins and vendors.

## Features

- 🎟️ Random ticket number generation
- 👥 Multi-vendor management
- 📊 Real-time dashboard statistics
- 📱 SMS/WhatsApp notifications
- 🔐 Secure authentication
- 📈 Performance tracking
- 💻 Fully responsive design

## Screenshots

[Add screenshots after uploading]

## Installation

### Quick Start

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/event-ticketing-system.git
cd event-ticketing-system
```

2. Create virtual environment:
```bash
python -m venv ticketing_env
```

3. Activate virtual environment:
- Windows: `ticketing_env\Scripts\activate`
- Mac/Linux: `source ticketing_env/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Setup database:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run server:
```bash
python manage.py runserver
```

8. Access the system:
- Open browser: http://127.0.0.1:8000
- Login with your superuser credentials

## Default Credentials

After running the automated setup:
- **Username**: admin
- **Password**: admin123

⚠️ **Change these credentials immediately after first login!**

## Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (development) / PostgreSQL (production)
- **Icons**: Font Awesome 6.4.0

## Project Structure

- `apps/accounts/` - User authentication and authorization
- `apps/core/` - Core ticketing functionality
- `apps/vendors/` - Vendor-specific features
- `templates/` - HTML templates
- `ticketing_system/` - Project settings

## Usage

### Super Admin:
1. Create ticket batches
2. Add vendors
3. Allocate tickets to vendors
4. Monitor vendor performance

### Vendors:
1. Create team members
2. Issue tickets to customers
3. Track ticket sales
4. View dashboard statistics

## Configuration

### SMS/WhatsApp Setup
Edit `ticketing_system/settings.py`:
```python
SMS_API_KEY = 'your-api-key'
WHATSAPP_API_KEY = 'your-api-key'
```

Update `apps/core/utils.py` with your provider's API details.

## Security

For production deployment:
1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use proper database (PostgreSQL/MySQL)
5. Enable HTTPS
6. Set up regular backups

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For support, email your-email@example.com or open an issue on GitHub.

## Author

[Your Name]

## Acknowledgments

- Django Framework
- Bootstrap
- Font Awesome
