import generator



class PGCLI:
    def __init__(self):
        self.history = generator.load_history()
        self.config = generator.load_config()

    def 