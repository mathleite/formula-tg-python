class RaceNotStarted(Exception):
    def __init__(self):
        super().__init__('Race not started!')
