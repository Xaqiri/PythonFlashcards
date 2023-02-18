
def deck_menu():
    ''' Display options and get user input '''
    print('1. Create new card')
    print('2. Display cards')
    print('3. Review deck')
    print('4. Edit deck name')
    print('5. Delete this deck')
    print('6. Update card')
    print('7. Delete card')
    print('0. Back')
    choice = int(input())
    return handle_choice(choice)
    
    
def handle_choice(choice: int) -> str:
    ''' Returns a status based on the user input '''
    try:
        if choice not in range(8):
           return 'invalid_choice'
    except:
        return 'not_number'
    
    match choice:
        case 1: return 'create_card'
        case 2: return 'display_all_card'
        case 3: return 'review_deck'
        case 4: return 'update_deck'
        case 5: return 'delete_deck'
        case 6: return 'update_card'
        case 7: return 'delete_card'
        case 0: return 'exit_deck'
        