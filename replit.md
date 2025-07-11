# Portfolio Website

## Overview

This is a personal portfolio website for Ming-Hsuan Hsu, an AI Engineer and Data Scientist. The application is built with Flask and showcases professional experience, education, projects, and provides a contact form for potential clients or employers.

## User Preferences

Preferred communication style: Simple, everyday language.
Language support: Chinese and English bilingual support required.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with SQLite default (configurable to PostgreSQL via DATABASE_URL)
- **Forms**: Flask-WTF for form handling and validation
- **Session Management**: Flask sessions with configurable secret key

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5 with dark theme
- **JavaScript**: Vanilla JavaScript for interactive features
- **Icons**: Font Awesome for UI icons

### Database Schema
- **Contact Model**: Removed - Contact form functionality has been disabled per user request

## Key Components

### Core Application (`app.py`)
- Flask application factory pattern
- Database initialization and configuration
- Environment-based configuration (DATABASE_URL, SESSION_SECRET)
- ProxyFix middleware for deployment compatibility

### Data Models (`models.py`)
- Contact model removed - contact form functionality disabled
- Uses SQLAlchemy ORM with declarative base

### Forms (`forms.py`)
- Contact form functionality removed per user request

### GitHub Integration (`github_api.py`)
- GitHubAPI class for fetching user profile and repository data
- Supports GitHub token authentication for higher rate limits
- Filters out forked repositories and includes language information

### Internationalization (`translations.py`)
- Comprehensive translation system for Chinese and English
- Supports navigation, content sections, and form labels
- Personal information, work experience, education, and projects in both languages
- Session-based language preference storage

### Routes (`routes.py`)
- Language switching functionality with session storage
- Template context processor for translation injection
- Dynamic data loading based on current language
- Main portfolio page rendering with localized content
- Contact form handling with translated messages
- Resume download functionality
- GitHub data integration

### Frontend Assets
- **CSS**: Custom styling with dark theme, timeline components, and responsive design
- **JavaScript**: Navigation handling, scroll effects, animations, and GitHub stats loading

## Data Flow

1. **User visits website** → Flask serves index.html with personal data
2. **GitHub data loading** → JavaScript makes AJAX calls to fetch repository information
3. **Contact form submission** → Form data validated and stored in database
4. **Resume download** → Static file served through Flask route

## External Dependencies

### Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Flask-WTF: Form handling
- WTForms: Form validation
- Requests: HTTP client for GitHub API
- Werkzeug: WSGI utilities

### Frontend Dependencies
- Bootstrap 5: CSS framework
- Font Awesome: Icon library
- Custom CSS and JavaScript

### Third-party Services
- GitHub API: For fetching repository and profile data
- Optional GitHub token for authenticated requests

## Deployment Strategy

### Environment Configuration
- `DATABASE_URL`: Database connection string (defaults to SQLite)
- `SESSION_SECRET`: Flask session secret key
- `GITHUB_TOKEN`: Optional GitHub API authentication token

### Database Management
- Automatic table creation on application startup
- SQLAlchemy handles database migrations and schema management
- Configurable database engines (SQLite for development, PostgreSQL for production)

### Static Files
- CSS and JavaScript files served through Flask's static file handling
- Resume file downloadable through dedicated route

### Production Considerations
- ProxyFix middleware configured for reverse proxy deployment
- Database connection pooling configured
- Logging configured for debugging and monitoring

The application follows a traditional MVC pattern with Flask, making it easy to extend and maintain. The modular structure allows for easy addition of new features like blog posts, project galleries, or additional contact methods.