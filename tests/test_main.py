from src.main import signup_with_google, signup_with_email, create_first_project, get_project_dashboard
from src.user import User
from src.project import Project

def test_signup_with_google():
    user = signup_with_google('google_id')
    assert user.email == 'example@gmail.com'
    assert user.google_id == 'google_id'

def test_signup_with_email():
    user = signup_with_email('example@gmail.com', 'password')
    assert user.email == 'example@gmail.com'
    assert user.password_hash != 'password'

def test_create_first_project():
    user = User(id=1, email='example@gmail.com', password_hash='password_hash', google_id='google_id')
    project = create_first_project(user)
    assert project.name == 'My First Project'
    assert project.runtime == 'Python'
    assert project.user_id == user.id

def test_get_project_dashboard():
    project = Project(id=1, name='My First Project', runtime='Python', user_id=1)
    dashboard = get_project_dashboard(project)
    assert dashboard['project_name'] == project.name
    assert dashboard['runtime'] == project.runtime
    assert dashboard['generated_components'] == []
    assert dashboard['deployment_status'] == 'Not deployed'
