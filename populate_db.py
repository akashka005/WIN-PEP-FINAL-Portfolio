import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Skill, Project, Achievement, Education

def populate():
    # Skills
    Skill.objects.get_or_create(name='Python', level=95, category='Languages')
    Skill.objects.get_or_create(name='JavaScript', level=85, category='Languages')
    Skill.objects.get_or_create(name='C++', level=80, category='Languages')
    
    Skill.objects.get_or_create(name='TensorFlow', category='AI/ML Stack')
    Skill.objects.get_or_create(name='PyTorch', category='AI/ML Stack')
    Skill.objects.get_or_create(name='Scikit-learn', category='AI/ML Stack')
    
    Skill.objects.get_or_create(name='React', category='Web & Tools')
    Skill.objects.get_or_create(name='Flask', category='Web & Tools')
    Skill.objects.get_or_create(name='Django', category='Web & Tools')

    # Projects
    Project.objects.get_or_create(
        title='Fraud Detection System',
        description='ML-based classification of fraudulent vs legitimate transactions.',
        details='Built with Python and TensorFlow, this system analyzes transaction patterns to identify potentially fraudulent activities with high accuracy.',
        date='Sep 2025 – Present',
        tech_stack='Python, TensorFlow, Flask, Streamlit',
        status='active',
        order=1
    )
    
    Project.objects.get_or_create(
        title='AI Resume Analyzer',
        description='NLP-powered web app that extracts skills and provides resume improvement suggestions.',
        details='A Flask-based application that uses NLP to parse resumes and provide actionable feedback for improvement.',
        date='July 2025',
        tech_stack='Flask, NLP, JavaScript, Render',
        status='deployed',
        order=2
    )

    # Achievements
    Achievement.objects.get_or_create(
        title='Top 10 Finalist - Code-A-Haunt Hackathon',
        description='Competed against 100+ teams'
    )
    
    # Education
    Education.objects.get_or_create(
        institution='Lovely Professional University',
        degree='B.Tech CSE (AI/ML)',
        date_range='2023 - 2027',
        grade='CGPA: 6.6'
    )

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()