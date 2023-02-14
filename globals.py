'''
# TODO: Figure out a better way to do choices.  Having the key be the string would probably be the better idea
'''

choices = {
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
    4: 'show_all_users',
    5: 'deck_created',
    6: 'show_all_decks',
    99: 'http://localhost:8080/user/all'
}

# choices2 = {
#     'general': [
#         'nonnumber', 'invalid', 'exit'
#     ],
#     'main': [
#         'user_exists', 'invalid_username', 'invalid_password', 'user_created', 'signed_in', 'show_all_users'
#     ],
#     'user': [
#         'deck_exists', 'deck_created', 'show_all_decks'
#     ]
# }
