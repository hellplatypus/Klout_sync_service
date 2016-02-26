from klout_sync_service import users, recent_added_users


result = users.delete_many({})
print 'users deleted from "users" collection: ', result.deleted_count

result = recent_added_users.delete_many({})
print 'users deleted from "recent_added_users" collection: ', result.deleted_count
