
def main_menu():
    ''' Display options and get user input '''
    print('1. Create new user')
    print('2. Sign in')
    print('3. Display users')
    print('0. Exit')
    try:
        choice = int(input())
    except:
        return 'not_number'
    return handle_choice(choice)
    
def handle_choice(choice: int) -> str:
    ''' Returns a status based on the user input '''
    try:
        if choice not in range(4):
            return 'invalid_choice'
    except:
        return 'not_number'
    match choice:
        case 0: return 'exit'
        case 1: return 'create_user'
        case 2: return 'sign_in'
        case 3: return 'display_all_user'