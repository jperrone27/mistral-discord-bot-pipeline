from dotenv import dotenv_values
from owlmind.pipeline import ModelProvider
from owlmind.simple import SimpleEngine
from owlmind.discord import DiscordBot

if __name__ == '__main__':

    # load token from .env
    config = dotenv_values('.env')
    TOKEN = config['DISCORD_TOKEN']
    URL = config['SERVER_URL']
    MODEL = config['SERVER_MODEL'] if 'SERVER_MODEL' in config else None
    TYPE = config['SERVER_TYPE'] if 'SERVER_TYPE' in config else None
    API_KEY = config['SERVER_API_KEY'] if 'SERVER_API_KEY' in config else None

    #added support for customized temperature and context size
    temp = 0.1
    context_window = 2048
    output_window = 2048
    
    # Configure a ModelProvider if there is a URL
    provider = ModelProvider(type=TYPE,  base_url=URL, api_key=API_KEY, model=MODEL, temperature= temp, num_ctx=context_window, num_predict=output_window) if URL else None
    
    # Load Simples Bot Brain loading rules from a CSV
    engine = SimpleEngine(id='bot-1')
    engine.model_provider = provider
    engine.load("bot-rules.csv")

    # Kick start the Bot Runner process
    bot = DiscordBot(token=TOKEN, engine=engine, debug=True, heartbeat = 180)
    bot.run()
