import unittest

from pymongo import MongoClient

from klout_sync_service import KLOUT_API_KEY, RECENT_ADDED_USERS, USERS
from klout_sync_service.klout_sync import KloutSync

INVALID_KLOUT_SCORE = 0


class TestKloutSync(unittest.TestCase):

    def test_update_old_user(self):

        self.users.insert_many([{'first_name': 'first_name' + str(i),
                                 'last_name': 'last_name' + str(i),
                                 'klout_score': INVALID_KLOUT_SCORE,
                                 'klout_id': self.valid_klout_ids[i]} for i in range(len(self.valid_klout_ids))])
        self.klout_sync.update_old_users()

        result = self.users.find()
        for doc in result:
            self.assertNotEqual(doc['klout_score'], INVALID_KLOUT_SCORE)

    def test_update_recent_user(self):
        self.recent_users.insert_many([{'first_name': 'first_name' + str(i),
                                        'last_name': 'last_name' + str(i),
                                        'klout_score': INVALID_KLOUT_SCORE,
                                        'klout_id': self.valid_klout_ids[i]} for i in range(len(self.valid_klout_ids))])

        self.klout_sync.update_recently_added_users()

        self.assertEqual(self.recent_users.count(), 0)

        result = self.recent_users.find()
        for doc in result:
            self.assertNotEqual(doc['klout_score'], INVALID_KLOUT_SCORE)

    @classmethod
    def setUpClass(cls):

        cls.client = MongoClient()
        cls.db = cls.client['test_klout_sync_service_database']
        cls.users = cls.db[USERS]
        cls.recent_users = cls.db[RECENT_ADDED_USERS]
        cls.klout_sync = KloutSync(KLOUT_API_KEY)
        cls.klout_sync.db = cls.db
        cls.valid_klout_ids = ['42502726248593184',
                               '39406501505096204']

    def tearDown(self):
        self.users.delete_many({})
        self.recent_users.delete_many({})
