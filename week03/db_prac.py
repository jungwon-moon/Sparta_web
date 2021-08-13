from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})

# all_users = list(db.users.find({'name': '덤블도어'}, {'_id': False}))
#
# for user in all_users:
#     print(user)

# user = db.users.find_one({'name': '덤블도어'}, {'_id': False})
#
# print(user)

# db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
# db.users.update_many({'name': '덤블도어'}, {'$set': {'age': 19}})

# db.users.delete_one({'name': '덤블도어'})