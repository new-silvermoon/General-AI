from utils import Action
from utils import Simulation
import json

pacman_action_list = []

def achieve_all_objectives(states_list, actions_list, objectives_list, objectives_stack):
    """

    """
    for objective in objectives_list:
        states_list = achieve_objective(states_list,actions_list,objective,objectives_stack)
        if states_list is None:
            return None

    for objective in objectives_list:
        if objective not in states_list:
            return None

    #print(states_list)
    return states_list

def achieve_objective (states_list,actions_list,objective,objectives_stack):
    """

    """
    result = []
    """
    Checking if the objective is already present in the state_list
    """
    if objective in states_list:
        return states_list
    
    if objective in objectives_stack:
        return None
    
    for action in actions_list:
        """
        Checks if the action is correct by verifying the presence of objective in add-list
        """
        
        if objective not in action['states_to_be_added']:
            continue
        
        """
        Try initiating the action
        """
        result = apply_action(action,states_list,actions_list, objective, objectives_stack)

        if result is not None:
            return result

def apply_action(action,states_list, actions_list,objectives_list, objectives_stack):
    """

    """
    result = []
    new_states = []
    for objective in objectives_list:
        objectives_stack.append(objective)

    result = achieve_all_objectives(states_list,actions_list,action['conditions'],objectives_stack)

    if result is None:
        return None

    states_to_be_added = action['states_to_be_added']
    states_to_be_deleted = action['states_to_be_deleted']

    """Removing states"""
    for state in result:
        if state not in states_to_be_deleted:
            new_states.append(state)

    """Adding states"""
    for state in states_to_be_added:
        new_states.append(state)


    return new_states

def solve_problem(start_states_list, objectives_list, actions_list):
    global pacman_action_list
    prefix = "Executing"
    final_states_list = []
    prefixed_final_states_list = []

    for action in actions_list:
        action['states_to_be_added'].append(prefix +" "+ action['action_name'])

        """Adding moves list for pacman"""
        pacman_action_list.append(action['action_name'])

    final_states_list = achieve_all_objectives(start_states_list,actions_list,objectives_list,[])

    if final_states_list is None:
        return None
    else:
        for state in final_states_list:
            if state.startswith(prefix):
                prefixed_final_states_list.append(state)

        return prefixed_final_states_list

def main():
    global pacman_action_list
    filename = '/Users/stephanie/PycharmProjects/General-AI/General-Problem-Solver/data/pacman_scenario.json'
    with open(filename,'r') as json_file:
        json_data = json.load(json_file)
        start_state_list = json_data.get('start')
        end_state = json_data.get('end')
        actions_list = json_data.get('actions')

        # result = solve_problem(start_state_list,end_state,actions_list)
        # print(result)
        for state in solve_problem(start_state_list,end_state,actions_list):
            print(state)

        """Initiating Pacman action"""
        sim = Simulation.Simulation(pacman_action_list)
        sim.draw_init_objects()


if __name__ == '__main__':
    main()

