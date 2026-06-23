from src.config import load_config
from src.user import create_user, User
from src.project import create_project, Project

def signup_with_google(google_id: str) -> User:
    config = load_config()
    # Simulate Google OAuth flow
    return create_user(email='example@gmail.com', password='password', google_id=google_id)

def signup_with_email(email: str, password: str) -> User:
    config = load_config()
    # Simulate email/password flow
    return create_user(email=email, password=password)

def create_first_project(user: User) -> Project:
    return create_project(name='My First Project', runtime='Python', user_id=user.id)

def get_project_dashboard(project: Project) -> dict:
    return {
        'project_name': project.name,
        'runtime': project.runtime,
        'generated_components': [],
        'deployment_status': 'Not deployed'
    }
