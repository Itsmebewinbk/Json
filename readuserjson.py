from json import *
with open("users.json") as f:
    data=load(f)
print((data))

#followers of id 2:
folllower_user=[user["followers"] for user in data if user["id"]==2]
print(folllower_user)
#user wiyh max follower

user= max(data,key = lambda post:len(post["followers"]))
print(user)