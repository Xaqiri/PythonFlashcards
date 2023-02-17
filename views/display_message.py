from globals import *

def display_message(status, controllers):
    
    # if type(choice) != int:
    #     print(choice)
    #     return 'bad choice'
    # match choices[choice]:
    # case 1:
    #         choice = 
    #     case 2:
    #         choice = controllers.get('user').sign_in()
    #         controllers.get('deck').cur_user = controllers.get('user').cur_user
    #     case 3:
    #         choice = controllers.get('user').display_users()
    # if status == STATUS_CODES.not_number:
    #     print('ye')
    #     print(status)
    # if status in [STATUS_CODES.not_found('user'), STATUS_CODES.deleted('user')]:
    #     print(status)
    status = CHOICES[status] if type(status) == int else status
    match status:
        case STATUS_CODES.not_number:
            print('Choice must be a number')
        case STATUS_CODES.not_found:
            print(status)
        case 'invalid':
            print('Invalid choice')
        case 'invalid_username':
            print('Invalid username')
        case 'invalid_password':
            print('Invalid password')
        case 'create_user':
            controllers.get('user').create_new_user()
            print('User created')
        case 'user_found':
            print('There already exists a user with this username')
        case 'deck_created':
            print('Deck created')
        case 'deck_exists':
            print('Deck already exists with that name')
        case 'user_deleted':
            print('User deleted')
        case 'deck_deleted':
            print('Deck deleted')
        case 'deck_not_found':
            print('Deck not found')
        case 'deck_name_updated':
            print('Deck name updated ')
        case 'user_updated':
            print('User updated')
        case 'card_created':
            print('Card created')
        case 'card_updated':
            print('Card updated')
        case 'card_not_updated':
            print('Card failed to update')
        case 'card_deleted':
            print('Card deleted')
        case 'card_does_not_exist':
            print('Card does not exist')
        case 'display_users':
            [print(i) for i in DB.user_cache]
        case 'display_decks':
            [print(i) for i in DB.deck_cache]
        case 'display_cards':
            [print(i) for i in DB.card_cache]
        
