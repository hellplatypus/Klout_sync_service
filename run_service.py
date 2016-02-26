import time

from klout_sync_service import KLOUT_API_KEY, OLD_USERS_UPDATE_PERIOD, RECENT_USERS_UPDATE_PERIOD
from klout_sync_service.klout_sync import KloutSync
from threading import Timer


klout_sync = KloutSync(KLOUT_API_KEY)

xtime = 0

while True:
    if xtime == OLD_USERS_UPDATE_PERIOD:
        Timer(0, klout_sync.update_old_users, ()).start()
        Timer(0, klout_sync.update_recently_added_users, ()).start()
        xtime = 0
        time.sleep(RECENT_USERS_UPDATE_PERIOD)
    else:
        Timer(0, klout_sync.update_recently_added_users, ()).start()
        time.sleep(RECENT_USERS_UPDATE_PERIOD)
        xtime += RECENT_USERS_UPDATE_PERIOD
