from .constant import UI, UNI, NUI, NUNI


def match_state(request_data):
    """Function to convert values is_urgent and is_important to one state"""
    state_map = {
        '00': NUNI,
        '01': NUI,
        '10': UNI,
        '11': UI
        }

    combination = '{}{}'.format(int(request_data.pop('is_urgent')), int(request_data.pop('is_important')))
    request_data.update(state=state_map.get(combination))
    return request_data


def unmatch_state(state):
    """Function to convert state to is_urgent and is_important values"""
    state_map = {
        NUNI: {"is_urgent": 0, "is_important": 0},
        NUI:  {"is_urgent": 1, "is_important": 0},
        UNI:  {"is_urgent": 0, "is_important": 1},
        UI:   {"is_urgent": 1, "is_important": 1}
    }
    state = state_map.get(state)
    return state
