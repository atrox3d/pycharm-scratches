import datetime

today = datetime.datetime.now()
print(today)                                            # 2022-09-12 07:19:09.150571
print(repr(today))                                      # datetime.datetime(2022, 9, 12, 7, 19, 9, 150571)

today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)                                            # 2022-09-12

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print(yesterday)
print(repr(yesterday))

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
print(yesterday)
