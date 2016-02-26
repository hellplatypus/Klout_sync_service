from klout_sync_service.db_tools.development_tools import DEFAULT_KLOUT_SCORE
from klout_sync_service import users


valid_klout_ids = ['42502726248593184',
                   '39406501505096204',
                   '32369627086844868',
                   '2055',
                   '851563',
                   '29273402344577515',
                   '34339951923630119',
                   '32088152110028716']

result = users.insert_many([{'first_name': 'first_name' + str(i),
                             'last_name': 'last_name' + str(i),
                             'klout_score': DEFAULT_KLOUT_SCORE,
                             'klout_id': valid_klout_ids[i]} for i in range(len(valid_klout_ids))])

print 'users in database: ', users.count()
