from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admins: list[int]

@dataclass
class Config:
    bot: TgBot


def load_config_data(path: str|None=None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot=TgBot(token=env('BOT_TOKEN'),
                            admins=list(map(int, env.list('ADMINS')))))
