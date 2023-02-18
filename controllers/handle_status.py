
def handle_status(status, controllers):
    match status:
        case 'create_user': return controllers.get('user').create_user()
        case 'create_deck': return controllers.get('deck').create_deck()
        case 'create_card': return controllers.get('card').create_card()
        case 'display_all_user': return controllers.get('user').display_users()
        case 'display_all_deck': return controllers.get('deck').display_decks()
        case 'display_all_card': return controllers.get('card').display_cards()
        case 'update_user': return controllers.get('user').update_user_name()
        case 'update_deck': return controllers.get('deck').update_deck_name()
        case 'update_card': return controllers.get('card').update_card()
        case 'delete_user': return controllers.get('user').delete_user(controllers.get('deck'), controllers.get('card'))
        case 'delete_deck': return controllers.get('deck').delete_deck()
        case 'delete_card': return controllers.get('card').delete_card()
        case 'exit_deck': return controllers.get('deck').exit_deck()
        case 'exit_user': controllers.get('user').sign_out(controllers.get('deck'))
        case 'use_deck': return controllers.get('deck').view_deck(controllers.get('card'))
        case 'sign_in': return controllers.get('user').sign_in(controllers.get('deck'))
        case 'review_deck': return 'exit'