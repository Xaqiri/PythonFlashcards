from globals import *

def main_menu(controllers):
    print('1. Create new user')
    print('2. Sign in')
    print('3. Display users')
    print('0. Exit')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 4:
            choice = 0
            return choice
    except:
        choice = -1
    match choice:
        case 0:
            choice = 3
        case 1:
            choice = controllers.get('user').create_new_user()
        case 2:
            choice = controllers.get('user').sign_in()
            controllers.get('deck').cur_user = controllers.get('user').cur_user
        case 3:
            choice = controllers.get('user').display_users()
    return choice