# 🐕 Self-Service Kiosk for Pet Adoption

Intelligent self-service kiosk system that connects pets available for adoption with compatible people through an interactive decision flow.

## 🎯 Main Features

### ✅ Decision Flow System
- **Intuitive interface** with multiple sequential choices
- **Intelligent algorithm** that calculates compatibility based on preferences
- **2 distinct decision paths**: Family with children and Small apartment
- **5 interactive questions** about type, size, age, personality, and available time

### ✅ Pet Registration
- **Complete form** with data validation
- **Fields**: name, type (dog/cat), breed, age, size, personality
- **Image upload** with real-time preview
- **Secure storage** in a relational database

### ✅ Information Retrieval
- **Intelligent search system** with filters based on user choices
- **Sort by compatibility** (0-100%)
- **Clear and organized display** with interactive cards
- **Personalized recommendations** based on the pet's profile User

### ✅ Responsive Interface
- **Modern design** with Bootstrap 5.3
- **Optimized for touch screen** kiosks
- **100% responsive** for different screen sizes
- **Smooth animations** and visual feedback

## 🚀 Technologies Used

- **Backend**: Django 5.2.8 (Python)
- **Frontend**: Django Templates, Bootstrap 5.3, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production)
- **Styles**: CSS3 with gradients and animations
- **Icons**: Font Awesome 6.4

## 📋 Documentation

- [📄 Product Requirements](.trae/documents/prd-requisitos-totem-pet.md)
- [🏗️ Architecture] [Technical](.trae/documents/arquitetura-tecnica-totem-pet.md)
- [📊 Decision Flow Report](.trae/documents/relatorio-fluxo-decisao.md)
- [📖 Installation and Usage Guide](.trae/documents/guia-instalacao-uso.md)

## ⚡ Quick Installation

### Option 1: Automatic Script
```bash
# Run automatic configuration script
python execute_system.py
```

### Option 2: Manual
```bash
# Install dependencies
pip install django==5.2.8 pillow

# Configure database
python manage.py makemigrations
python manage.py migrate

# Create test data (optional)
python create_test_data.py

# Start server
python manage.py runserver 0.0.0.0:8000
```

## 🌐 System Access

After starting the server, access:
- **Main System**: http://localhost:8000/
- **Django Admin**: http://localhost:8000/admin/

## 📱 Usage Flow

### For Users
1. **Home**: Initial screen with "Start Now" button
2. **Questions**: Answer 5 questions about preferences
3. **Results**: View compatible pets sorted by compatibility
4. **Details**: View complete information about the chosen pet
5. **Interest**: Express interest in adoption

### For Administrators
1. **Registration**: Use the form to add new pets
2. **Management**: Manage pets through the administrative panel
3. **Monitoring**: Track usage statistics

## 🎨 Design

### Color Palette
- **Primary**: Teal (#667eea)
- **Secondary**: Purple (#764ba2)
- **Follow**: Green (#28a745)
- **Background**: Soft Gradient (#f8f9fa → #e9ecef)

### Typography
- **Main**: Helvetica Neue
- **Titles**: Bold (700)
- **Body**: Regular (400)

## 🔧 Compatibility Algorithm

The system calculates compatibility based on:
- **Pet Type** (0-40 points)
- **Size** (0-25 points)
- **Age** (0-20 points)
- **Personality** (0-15 points)

**Result**: Score from 0-100% with Minimum of 50% for display

## 📊 Examples of Paths

### Path 1: Family with Children
- Type: Dog → Large → Puppy/Adult → Playful → Long time
- Results: Golden Retriever (95%), Labrador (92%), Beagle (88%)

### Path 2: Small Apartment
- Type: Cat → Small → Adult → Calm → Short time
- Results: Persian (90%), Shih Tzu (87%), Maine Coon (85%)

## 🗂️ Project Structure

```
totem_auto/
├── app/ # Main application
│ ├── models.py # Data models
│ ├── views.py # Business logic
│ ├── urls.py # Application routes
│ └── templates/ # HTML templates
├── static/ # Static files
│ ├── css/ # CSS styles
│ ├── images/ # System images
│ └── fonts/ # Custom fonts
├── totem/ # Django configuration
├── media/ # Image uploads (created on run)
├── .trae/documents/ # Project documentation
├── create_test_data.py # Test data script
├── execute_system.py # Automatic execution script
└── manage.py # Django Manager
```

## 🧪 Tests

### Included Test Data
- 8 pets with different characteristics
- Mix of dogs and cats
- Various breeds and personalities

### Test Cases
- ✅ Complete decision flow
- ✅ Registration of new pets
- ✅ System
