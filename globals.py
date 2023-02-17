'''
TODO: Figure out a better way to do choices.  Having the key be the string would probably be the better idea
'''
from status_codes import StatusCodes
from database import Database


STATUS_CODES = StatusCodes()
DB = Database()


CHOICES = {
    -12: 'card_does_not_exist',
    -11: 'card_deleted',
    -10: 'card_not_updated',
    -9: 'deck_not_found',
    -8: 'deck_deleted',
    -7: 'user_deleted',
    -6: 'user_does_not_exist',
    -5: 'deck_exists',
    -4: 'user_exists',
    -3: 'invalid_password',
    -2: 'invalid_username',
    -1: 'nonnumber',
    0: 'invalid',
    1: 'user_created',
    2: 'signed_in',
    3: 'exit',
    4: 'display_all_user',
    5: 'deck_created',
    6: 'display_all_deck',
    7: 'delete_user',
    8: 'deck_name_updated',
    9: 'user_name_updated',
    10: 'deck_found',
    11: 'card_created',
    12: 'display_all_card',
    13: 'card_updated'
}

# status_codes = {
#     'general': [
#         'nonnumber', 
#         'invalid', 
#         'exit'
#     ],
#     'main': [

#     ],
#     'user': [
#         'user_created', 
#         'user_exists', 
#         'show_all_users', 
#         'user_updated', 
#         'user_deleted', 
#         'invalid_username', 
#         'invalid_password', 
#         'user_does_not_exist',
#         'signed_in'
#     ],
#     'deck': [
#         'deck_created',
#         'display_decks',
#         'deck_name_updated',
#         'deck_found',
#         'deck_exists',
#         'deck_not_found',
#         'deck_deleted'
#     ],
#     'card': [
#         'card_not_found',
#         'card_deleted',
#         'card_not_updated',
#         'card_created',
#         'display_cards',
#         'card_updated'
#     ],
# }

