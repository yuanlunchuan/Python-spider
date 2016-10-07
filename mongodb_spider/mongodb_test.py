from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.huaxiHospital
collection = db.Doctor

item = {
  'name': 'zhangsan',
  'age': 29
}
collection.insert(item)
for doctor in collection.find():
  print('------', doctor)
