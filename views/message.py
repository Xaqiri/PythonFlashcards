from globals import *

def display_message(choice, db):
    if type(choice) != int:
        print(choice)
        return
    match choices[choice]:
        case 'nonnumber':
            print('Choice must be a number')
        case 'invalid':
            print('Invalid choice')
        case 'invalid_username':
            print('Invalid username')
        case 'invalid_password':
            print('Invalid password')
        case 'user_created':
            print('User created')
        case 'user_exists':
            print('User already exists')
        case 'user_does_not_exist':
            print('User does not exist')
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
        case 'user_name_updated':
            print('User name updated')
        case 'display_users':
            [print(i) for i in db.user_cache]
        case 'display_decks':
            [print(i) for i in db.deck_cache]
        case 'display_cards':
            [print(i) for i in db.card_cache]
        