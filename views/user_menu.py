from globals import *

STATUS_CODES = {
    'create': 'create_deck',
    'use': 'use_deck',
    'display_all': 'display_all_deck',
    'delete': 'delete_deck',
    'update': 'update_user',
    'delete_user': 'delete_user',
    'exit': 'exit_deck'
}

def user_menu():
    '''
    Create, view, display all, delete, edit username, delete user, sign out
    '''
    print('1. Create new deck')
    print('2. View deck')
    print('3. Display decks')
    print('4. Delete deck')
    print('5. Edit username')
    print('6. Delete user')
    print('0: Exit deck')
    choice = int(input())
    return handle_choice(choice)

def handle_choice(choice):
    try:
        if choice not in CHOICES.keys() or choice < 0 or choice > 7:
            choice = 0
            return choice
    except:
        choice = -1
    match choice: 
        case 0: return STATUS_CODES.get('exit')
        case 1: return STATUS_CODES.get('create')
        case 2: return STATUS_CODES.get('use')
        case 3: return STATUS_CODES.get('display_all')
        case 4: return STATUS_CODES.get('delete')
        case 5: return STATUS_CODES.get('update')
        case 6: return STATUS_CODES.get('delete_user')
        