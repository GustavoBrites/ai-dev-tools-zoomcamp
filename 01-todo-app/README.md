# Django TODO App

A modern, feature-rich TODO application built with Django, featuring a sleek dark-mode UI and full CRUD functionality.

<div align="center">
  <img width="707" height="321" alt="Get to do it app home page" src="https://github.com/user-attachments/assets/ebe60253-32b6-4078-a47e-00b8e273cb6d" />
</div>


## 📋 Description

This TODO application allows users to manage their tasks efficiently with the following features:

- **Create** new tasks with title, description, and due date
- **Edit** existing tasks and update their details
- **Delete** tasks with confirmation
- **Mark tasks as resolved/unresolved** with a single click
- **View all tasks** in an organized, card-based layout
- **Automatic timestamps** for creation and modification tracking

## 🛠️ Tools & Technologies Used

- **Python 3.11+** - Programming language
- **Django 5.2.8** - Web framework
- **uv** - Fast Python package installer and dependency manager
- **SQLite** - Database (default Django database)
- **HTML/CSS** - Frontend with custom styling
- **Google Fonts (Outfit)** - Typography

## ✨ Features

- Modern dark-mode UI with gradient accents
- Responsive card-based layout
- Smooth animations and hover effects
- Clean, intuitive interface
- Comprehensive test coverage (7 automated tests)

## 🚀 How to Run Locally

### Prerequisites

- Python 3.11 or higher installed on your system
- Git (to clone the repository)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-dev-tools-zoomcamp/01-todo-app
   ```

2. **Install uv** (if not already installed)
   ```bash
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```
   This will automatically create a virtual environment and install all required packages.

4. **Run database migrations**
   ```bash
   uv run python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   uv run python manage.py runserver
   ```

6. **Access the application**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## 🧪 Running Tests

To run the automated test suite:

```bash
uv run python manage.py test
```

All 7 tests should pass, covering:
- Model creation and validation
- CRUD operations (Create, Read, Update, Delete)
- Task status toggling
- View rendering and redirects

## 📁 Project Structure

```
01-todo-app/
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo/                # Main TODO application
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates
│   │   └── todo/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── todo_form.html
│   │       └── todo_confirm_delete.html
│   ├── models.py        # TodoItem model
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   └── tests.py         # Test suite
├── manage.py            # Django management script
├── pyproject.toml       # Project dependencies
└── README.md            # This file
```

## 💾 Database Schema

### TodoItem Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key (auto-generated) |
| `title` | CharField | Short description of the task |
| `description` | TextField | Optional detailed description |
| `due_date` | DateTimeField | When the task should be completed |
| `is_resolved` | BooleanField | Whether the task is done (default: False) |
| `created_at` | DateTimeField | Timestamp for creation (auto) |
| `updated_at` | DateTimeField | Timestamp for modification (auto) |

## 🎨 UI Design

The application features a modern, premium design with:
- **Dark theme** with slate background colors
- **Gradient header** (purple to pink)
- **Card-based layout** with hover effects
- **Smooth animations** for better UX
- **Responsive design** that works on all screen sizes

## 📝 License

This project is free to use. Feel free to use, modify, and distribute it as you wish!

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!
