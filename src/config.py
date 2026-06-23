import json
from dataclasses import dataclass

@dataclass
class Config:
    google_client_id: str
    google_client_secret: str
    email_password_salt: str

def load_config() -> Config:
    try:
        with open('config.json') as f:
            data = json.load(f)
            return Config(
                google_client_id=data['google_client_id'],
                google_client_secret=data['google_client_secret'],
                email_password_salt=data['email_password_salt']
            )
    except FileNotFoundError:
        # Create a default config if the file does not exist
        default_config = Config(
            google_client_id='default_google_client_id',
            google_client_secret='default_google_client_secret',
            email_password_salt='default_email_password_salt'
        )
        with open('config.json', 'w') as f:
            json.dump({
                'google_client_id': default_config.google_client_id,
                'google_client_secret': default_config.google_client_secret,
                'email_password_salt': default_config.email_password_salt
            }, f)
        return default_config
