
def display_message(status):
    
    match status:
        case 'not_number': print('Choice must be a number')
        case 'invalid_choice': print('Invalid choice')
        case 'invalid_username': print('Invalid username')
        case 'invalid_password': print('Invalid password')
        case 'user_found': print('There already exists a user with this username')
        case 'user_not_found': print('User not found')
        case 'user_updated': print('User updated')
        case 'user_deleted': print('User deleted')
        case 'deck_created': print('Deck created')
        case 'deck_found': print('Deck already exists with that name')
        case 'deck_not_found': print('Deck not found')
        case 'deck_name_updated': print('Deck name updated ')
        case 'deck_deleted': print('Deck deleted')
        case 'card_created': print('Card created')
        case 'card_not_found': print('Card not found')
        case 'card_updated': print('Card updated')
        case 'card_not_updated': print('Card failed to update')
        case 'card_deleted': print('Card deleted')
        