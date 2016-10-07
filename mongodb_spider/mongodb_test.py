from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.huaxiHospital
collection = db.Doctor
for doctor in collection.find():
  print('------', doctor)
