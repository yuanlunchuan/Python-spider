from pymongo import MongoClient

class MongoTest:
  ip = ''
  port = 0

  def __init__(self, ip, port):
    self.ip = ip
    self.port = port

  def collect(self):
    return MongoClient(self.ip, self.port)

  def getCollection(self):
    return MongoClient(self.ip, self.port).huaxiHospital.Doctor

# mongo_test = MongoTest('localhost', 27017)
for doctor in MongoClient('localhost', 27017).huaxiHospital.Doctor:
  print("----: ", doctor)

