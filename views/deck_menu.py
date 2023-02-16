from globals import *

def deck_menu(choice, controllers):
    print('1. Create new card')
    print('2. Display cards')
    print('3. Review deck')
    print('4. Edit deck name')
    print('5. Delete this deck')
    print('6. Update card')
    print('7. Delete card')
    print('0. Back')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 7:
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
            choice = 0
        case 4:
            if not controllers.get('deck').cur_deck:
                inp = input('Enter deck name: ')
                choice = controllers.get('deck').update_deck_name(inp)
            else:
                choice = controllers.get('deck').update_deck_name()
        case 5:
            controllers.get('card').delete_all_cards(controllers.get('deck').cur_deck.id)
            choice = controllers.get('deck').delete_deck(controllers.get('deck').cur_deck.id)
        case 6:
            card_id = input('Enter id of card to edit: ')
            front = input('Enter front of card: ')
            back = input('Enter back of card: ')
            choice = controllers.get('card').update_card(card_id, front, back)
        case 7:
            card_id = input('Enter id of card to delete: ')
            choice = controllers.get('card').delete_card(card_id)
        case 0:
            controllers.get('deck').exit_deck()
            choice = None
    return choice