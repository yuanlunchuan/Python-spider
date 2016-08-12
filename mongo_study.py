import pymongo

connection = pymongo.MongoClient()
tdb = connection.mongoStudy
post_info = tdb.test

jike = { 'name': '极客', 'age': 5, 'skill': 'Python' }
post_info.insert(jike)
print('运行完成')
