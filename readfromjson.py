from json import *
f=open("blog.json")
# for i in f:
#     print(i)
data=load(f)
# print(data)

with open("blog.json","r",encoding='utf-8') as f:
    data=load(f)
# print(data)
#
# user_posts=[post for post in data if post["userId"]==1]
# print(len(user_posts))
#
# #if number of likes for postid=3
# likes=[len(post["liked_by"]) for post in data if post["postId"]==3]
# print(likes)
#
# #userid=2 liked how many post
# userid2=[post for post in data if 2 in post["liked_by"]]
# print(len(userid2))

#max like
print(max(data,key=lambda post:len(post["liked_by"])))