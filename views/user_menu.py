
def user_menu() -> str:
    ''' Display options and get user input '''
    print('1. Create new deck')
    print('2. View deck')
    print('3. Display decks')
    print('4. Delete deck')
    print('5. Edit username')
    print('6. Delete user')
    print('0: Sign out')
    try:
        choice: int = int(input())
    except:
        return 'not_number'
    return handle_choice(choice)

def handle_choice(choice: int) -> str:
    ''' Returns a status based on the user input '''
    try:
        if choice not in range(8):
            return 'invalid_choice'
    except:
        return 'not_number'
    match choice: 
        case 0: return 'exit_user'
        case 1: return 'create_deck'
        case 2: return 'use_deck'
        case 3: return 'display_all_deck'
        case 4: return 'delete_deck'
        case 5: return 'update_user'
        case 6: return 'delete_user'
        