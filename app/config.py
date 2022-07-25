from app.core.setting_defs import SettingDefs


class Settings(SettingDefs):
    # customize defult app settings
    app_name = "DarkCoffee Blog"
    sqlite_database_name = "blog.db"
    
    # define app settings
    email: str = "navidved@gmail.com"
    company: str = "AlphaNeuron"
    

settings = Settings()