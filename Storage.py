from Action import Action


class Storage:
    def __init__(self, action: Action):
        self._action = action
        self._position = action.dest()

    def action(self):
        return self._action

    def position(self):
        return self._position

    def bestAction(self, next_storage):
        return 1

    def balance(self, next_storage):
        return 1
