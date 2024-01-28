class GameStateManager:
    def __init__(self):
        self.state = "menu_principal"

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state