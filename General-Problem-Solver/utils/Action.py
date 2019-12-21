class Action:
    action_name = None
    conditions = None
    states_to_be_added = []
    states_to_be_deleted = []

    def __init__(self, action_name, conditions, states_to_be_added, states_to_be_deleted):
        self.action_name = action_name
        self.conditions = conditions
        self.states_to_be_added = states_to_be_added
        self.states_to_be_deleted = states_to_be_deleted

    def get_conditions(self):
        return self.conditions

    def get_states_to_be_added(self):
        return self.states_to_be_added

    def get_states_to_be_deleted(self):
        return self.states_to_be_deleted

    def add_state(self,state):
        return self.states_to_be_added.append(state)

    def remove_state(self,state):
        return self.states_to_be_added.remove(state)

