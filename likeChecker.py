from TikTokApi import TikTokApi
import time
import os




api = TikTokApi()

def getLikeCount():
    tiktoks = api.byUsername('username', count=1)
    
    for tiktok in tiktoks:
        likeCount = tiktok["stats"]["diggCount"]
        return likeCount

def sendRandomDogPic():
    os.system("python3 sendRandomDogPic.py")



def update():
    initialCount = 0
    while True:
        mostRecentAmountofLikes = getLikeCount()
        if mostRecentAmountofLikes > initialCount:
            newLikes = mostRecentAmountofLikes - initialCount
            initialCount = mostRecentAmountofLikes
            print("Amount of new likes = ",newLikes)
            for x in range(newLikes):
                sendRandomDogPic()
        else:
            print("no new shares")
        print("sleepy time")
        time.sleep(5)

print("current like count = ",getLikeCount())

update()

