# from globals import *

STATUS_CODES = {
    'not_number': 'not_number',
    'invalid': 'invalid_choice',
    'exit': 'exit_user',
    'create': 'create_user',
    'sign_in': 'use_user',
    'display_all': 'display_all_user'
}
def main_menu():
    print('1. Create new user')
    print('2. Sign in')
    print('3. Display users')
    print('0. Exit')
    try:
        choice = int(input())
    except:
        return STATUS_CODES.get('not_number')
    return handle_choice(choice)
    
def handle_choice(choice):
    try:
        if choice not in range(4):
            return STATUS_CODES.get('invalid')
    except:
        return STATUS_CODES.get('not_number')
    match choice:
        case 0: return STATUS_CODES.get('exit')
        case 1: return STATUS_CODES.get('create')
        case 2: return STATUS_CODES.get('sign_in')
        case 3: return STATUS_CODES.get('display_all')