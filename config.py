from core.base_config import BaseConfig  

class Config(BaseConfig):
    APP_NAME = "DrkCoffee"
    EMAIL: str = "navidved@gmail.com"

    AUTH_USER_METHOD = "get_agent_by_username"
    AUTH_USER_MODULE = "services.blog.repository.agent_repo"

config=Config()