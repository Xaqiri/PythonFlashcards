from globals import *

def deck_menu(choice, controllers):
    print('1. Create new card')
    print('2. Display cards')
    print('3. Review deck')
    print('4. Edit deck name')
    print('5. Delete this deck')
    print('0. Back')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 5:
            choice = 0
            return choice
    except:
        choice = -1
    
    match choice:
        case 1:
            front = input('Enter card front: ')
            back = input('Enter card back: ')
            choice = controllers.get('card').create_card(front, back, controllers.get('deck').cur_deck.id)
        case 2:
            choice = controllers.get('card').display_cards()
        case 3:
            pass
        case 4:
            if not controllers.get('deck').cur_deck:
                inp = input('Enter deck name: ')
                choice = controllers.get('deck').update_deck_name(inp)
            else:
                choice = controllers.get('deck').update_deck_name()
        case 5:
            choice = controllers.get('deck').delete_deck(controllers.get('deck').cur_deck.id)
        case 0:
            controllers.get('deck').cur_deck = None
            choice = None
    return choice