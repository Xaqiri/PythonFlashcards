from globals import *

def user_menu(controllers):
    print('1. Create new deck')
    print('2. View deck')
    print('3. Display decks')
    print('4. Delete deck')
    print('5. Edit username')
    print('6. Delete user')
    print('0: Sign out')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 7:
            choice = 0
            return choice
    except:
        choice = -1
    match choice: 
        case 0:
            controllers.get('user').sign_out(controllers.get('deck'))
            choice = None
        case 1:
            choice = controllers.get('deck').create_deck()
        case 2:
            inp = input('Enter deck name: ')
            choice = controllers.get('deck').view_deck(inp)
            controllers.get('card').cur_deck = controllers.get('deck').cur_deck
        case 3:
            choice = controllers.get('deck').display_decks()
        case 4:
            deckId = input('Enter deck id to delete: ').casefold()
            controllers.get('card').delete_all_cards(deckId)
            choice = controllers.get('deck').delete_deck(deckId)
        case 5:
            choice = controllers.get('user').update_user_name()
        case 6:
            inp = input('Are you sure? This action is irreversible  y/n ').casefold()
            if inp == 'y':
                controllers.get('deck').delete_all_decks(controllers.get('user').cur_user.id, controllers.get('card').delete_all_cards)
                choice = controllers.get('user').delete_user()
            else:
                choice = None
    return choice