####from .settings import Settings 
 
##class Settings: 
  #  def __init__(self): 
  #      self.database_url = "postgresql://workshop_user:workshop_pass@localhost:5432/workshop_db" 
   #     self.secret_key = "your-secret-key-here" 
    #    self.debug = True 

# config/settings.py

import os

# Base class with default configurations
class Config:
    """Base configuration."""
    # A secret key is used for session management and CSRF protection.
    # In a real app, this should be a long, random string and kept secret.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key-that-you-should-change'

    # Static files and template folders (if using a web framework like Flask)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # API Keys (load from environment variables for security)
    API_KEYS = {
        'GOOGLE_MAPS_API': os.environ.get('GOOGLE_MAPS_API_KEY'),
        'WEATHER_API': os.environ.get('WEATHER_API_KEY')
    }

    # Pagination
    ITEMS_PER_PAGE = 20

    @staticmethod
    def init_app(app):
        """Factory function to be called on app initialization."""
        pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # Use a local SQLite database for easy development
    DATABASE_URI = 'sqlite:///car_system_dev.db'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    # Use an in-memory SQLite database for fast, isolated tests
    DATABASE_URI = 'sqlite:///:memory:'
    # Ensure tests do not use the real API keys
    API_KEYS = {key: None for key in Config.API_KEYS}

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Use a production-grade database like PostgreSQL
    # The URI should be loaded from an environment variable for security
    DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://user:password@localhost/car_system_prod'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # Configure production logging
        import logging
        from logging.handlers import RotatingFileHandler
        if not app.debug:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/car_system.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Car System startup')

# Dictionary to easily access the correct config by name
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
