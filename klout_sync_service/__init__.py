from pymongo import MongoClient

KLOUT_API_KEY = 'txn5u9gp7twkrwft3k5bmrmy'

RECENT_USERS_UPDATE_PERIOD = 3600
OLD_USERS_UPDATE_PERIOD = 86400

USERS = 'users'
RECENT_ADDED_USERS = 'recent_added_users'

client = MongoClient()
db = client['klout_sync_service_database']
users = db[USERS]
recent_added_users = db[RECENT_ADDED_USERS]
