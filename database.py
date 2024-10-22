from pymongo import MongoClient

# 替换以下的连接字符串为你的 MongoDB Atlas 或本地连接字符串
MONGO_URI = "mongodb+srv://luosylois:HDQNHKbMDrxhLJz1@online-course.4tn3g.mongodb.net/"

client = MongoClient(MONGO_URI)  # 创建 MongoDB 客户端连接
db = client["online_course"]  # 创建数据库

# 测试插入数据
course_collection = db["courses"]
course_collection.insert_one({"title": "Python 101", "instructor": "Alice", "duration": 10})

print("数据插入成功：", course_collection.find_one({"title": "Python 101"}))
