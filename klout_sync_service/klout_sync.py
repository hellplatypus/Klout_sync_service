from klout import *
from klout_sync_service import db, USERS, RECENT_ADDED_USERS


class KloutSync:

    def __init__(self, klouut_api_key):
        self.klout_api = Klout(klouut_api_key)
        self.db = db

    def update_old_users(self):
        """
        Update all user in 'users' collection
        """
        result = self.db[USERS].find()
        for doc in result:
            self._update_user(doc['klout_id'], '%s' % USERS)

    def update_recently_added_users(self):

        """
        Update all user in 'recent_added_users' collection, and then move them to 'users' collection.
        """
        result = self.db[RECENT_ADDED_USERS].find()
        for doc in result:
            self._update_user(doc['klout_id'], RECENT_ADDED_USERS)

        result = self.db[RECENT_ADDED_USERS].find()
        recently_added_users_list = [doc for doc in result]
        if recently_added_users_list:
            self.db[USERS].insert_many(recently_added_users_list)
            self.db[RECENT_ADDED_USERS].delete_many({})

    def _update_user(self, klout_id, collection_name):

        score = self.klout_api.user.score(kloutId=klout_id).get('score')

        self.db[collection_name].update_one({"klout_id": klout_id},
                                            {
                                               "$set": {
                                                   "klout_score": score
                                               },
                                            })
