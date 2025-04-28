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

    """
        payload = create_payload(
                         target="ollama",
                         model="mistral", 
                         prompt=PROMPT, 
                         temperature= 0.1, 
                         num_ctx= 2048,  
                         num_predict= 200)
    """
    temp = 1
    context_window = 200
    output_window = 200
    
    # Configure a ModelProvider if there is a URL
    provider = ModelProvider(type=TYPE,  base_url=URL, api_key=API_KEY, model=MODEL, temperature= temp, num_ctx=context_window, num_predict=output_window) if URL else None
    
    # Load Simples Bot Brain loading rules from a CSV
    engine = SimpleEngine(id='bot-1')
    engine.model_provider = provider
    engine.load("bot-rules.csv")

    # Kick start the Bot Runner process
    bot = DiscordBot(token=TOKEN, engine=engine, debug=True, heartbeat = 180)
    bot.run()
