import importlib, os

class MAXBot:
    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def load_cogs(self):
        cogs_dir = 'src/cogs'
        for file in os.listdir(cogs_dir):
            if file.endswith('.py'):
                module_name = f"src.cogs.{file[:-3]}"
                module = importlib.import_module(module_name)
                module.setup(self.bot, self.dp)


