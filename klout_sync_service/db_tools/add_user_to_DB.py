from klout_sync_service import recent_added_users, users
from klout_sync_service.db_tools import KLOUT_API_REQUEST_LIMITS


while True:

    cursor = users.find()
    if cursor.count() >= KLOUT_API_REQUEST_LIMITS:
        print 'Sorry DB is full.'
        break

    first_name = raw_input("User's first name: ")
    last_name = raw_input("User's last name: ")

    klout_id = raw_input("User's kloutID: ")
    if not klout_id.isdigit():
        print 'KloutID must consist of digits only. Try again.'
        print
        continue

    klout_score = raw_input("User's klout score: ")
    if not klout_score.isdigit():
        print 'Klout Score must consist of digits only. Try again.'
        print
        continue

    cursor = recent_added_users.find({"klout_id": klout_id})
    if cursor.count() != 0:
        print 'Sorry, user with this klout_id already exists.'
        continue

    recent_added_users.insert_one({'first_name': first_name,
                                   'last_name': last_name,
                                   'klout_id': klout_id,
                                   'klout_score': klout_score})
    print
    print "User added."
    print 'first_name: {0};   last_name: {1};   klout_score: {2};   klout_id: {3};'.format(first_name, last_name,
                                                                                           klout_score, klout_id)
    print
