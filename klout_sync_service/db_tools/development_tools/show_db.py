from klout_sync_service import users, recent_added_users

cursor = users.find()
print "Users: "
if cursor.count():
    for doc in cursor:
        print doc
else:
    print 'Collection is empty.'

print

cursor = recent_added_users.find()
print "Recent added users: "
if cursor.count():
    for doc in cursor:
        print doc
else:
    print 'Collection is empty.'
