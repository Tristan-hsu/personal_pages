from flask import render_template, request, redirect, url_for, flash, jsonify, send_file, session
from app import app, db
from github_api import GitHubAPI
from translations import (
    TRANSLATIONS, PERSONAL_INFO_TRANSLATIONS, WORK_EXPERIENCE_TRANSLATIONS,
    EDUCATION_TRANSLATIONS, SKILLS_TRANSLATIONS, PROJECTS_TRANSLATIONS,
    CERTIFICATIONS_TRANSLATIONS
)
import os

# Helper functions for language switching
def get_current_language():
    """Get current language from session or default to English"""
    return session.get('language', 'en')

def get_translation(key, subkey=None):
    """Get translation for current language"""
    lang = get_current_language()
    if subkey:
        return TRANSLATIONS.get(lang, {}).get(key, {}).get(subkey, key)
    return TRANSLATIONS.get(lang, {}).get(key, key)

def get_personal_info():
    """Get personal info in current language"""
    lang = get_current_language()
    return PERSONAL_INFO_TRANSLATIONS.get(lang, PERSONAL_INFO_TRANSLATIONS['en'])

def get_work_experience():
    """Get work experience in current language"""
    lang = get_current_language()
    return WORK_EXPERIENCE_TRANSLATIONS.get(lang, WORK_EXPERIENCE_TRANSLATIONS['en'])

def get_education():
    """Get education in current language"""
    lang = get_current_language()
    return EDUCATION_TRANSLATIONS.get(lang, EDUCATION_TRANSLATIONS['en'])

def get_skills():
    """Get skills in current language"""
    lang = get_current_language()
    return SKILLS_TRANSLATIONS.get(lang, SKILLS_TRANSLATIONS['en'])

def get_projects():
    """Get projects in current language"""
    lang = get_current_language()
    return PROJECTS_TRANSLATIONS.get(lang, PROJECTS_TRANSLATIONS['en'])

def get_certifications():
    """Get certifications in current language"""
    lang = get_current_language()
    return CERTIFICATIONS_TRANSLATIONS.get(lang, CERTIFICATIONS_TRANSLATIONS['en'])

# Language switching route
@app.route('/set-language/<language>')
def set_language(language):
    """Set language preference in session"""
    if language in ['en', 'zh']:
        session['language'] = language
    return redirect(request.referrer or url_for('index'))

# Template context processor to inject translations
@app.context_processor
def inject_translations():
    """Inject translations into all templates"""
    return {
        'get_translation': get_translation,
        'current_language': get_current_language(),
        'translations': TRANSLATIONS.get(get_current_language(), TRANSLATIONS['en'])
    }

@app.route('/')
def index():
    github_api = GitHubAPI()
    github_user = github_api.get_user_info()
    github_repos = github_api.get_repositories()
    
    return render_template('index.html',
                         personal_info=get_personal_info(),
                         education=get_education(),
                         work_experience=get_work_experience(),
                         skills=get_skills(),
                         certifications=get_certifications(),
                         projects=get_projects(),
                         github_user=github_user,
                         github_repos=github_repos)



@app.route('/download-resume')
def download_resume():
    try:
        return send_file('static/resume.pdf', as_attachment=True, download_name='Ming-Hsuan_Hsu_Resume.pdf')
    except FileNotFoundError:
        flash('Resume file not found. Please contact me directly.', 'error')
        return redirect(url_for('index'))

@app.route('/api/github-stats')
def github_stats():
    github_api = GitHubAPI()
    user_info = github_api.get_user_info()
    repos = github_api.get_repositories()
    
    if user_info and repos:
        stats = {
            'total_repos': len(repos),
            'total_stars': sum(repo.get('stargazers_count', 0) for repo in repos),
            'total_forks': sum(repo.get('forks_count', 0) for repo in repos),
            'languages': {}
        }
        
        # Aggregate languages
        for repo in repos:
            if 'languages' in repo:
                for lang, bytes_count in repo['languages'].items():
                    stats['languages'][lang] = stats['languages'].get(lang, 0) + bytes_count
        
        return jsonify(stats)
    
    return jsonify({'error': 'Unable to fetch GitHub stats'}), 500
