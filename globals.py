'''
# TODO: Figure out a better way to do choices.  Having the key be the string would probably be the better idea
'''

choices = {
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
    4: 'display_users',
    5: 'deck_created',
    6: 'display_decks',
    7: 'delete_user',
    8: 'deck_name_updated',
    9: 'user_name_updated',
    10: 'deck_found',
    11: 'card_created',
    12: 'display_cards',
    13: 'card_updated'
}

# choices2 = {
#     'general': [
#         'nonnumber', 'invalid', 'exit'
#     ],
#     'main': [
#
#     ],
#     'user': [
#         'user_exists', 'user_created', 'show_all_users', 'user_updated', 'user_deleted', 'invalid_username', 'invalid_password', 'signed_in'
#     ]
# }
