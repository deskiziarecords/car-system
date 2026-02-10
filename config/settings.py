from .settings import Settings 
 
class Settings: 
    def __init__(self): 
        self.database_url = "postgresql://workshop_user:workshop_pass@localhost:5432/workshop_db" 
        self.secret_key = "your-secret-key-here" 
        self.debug = True 
