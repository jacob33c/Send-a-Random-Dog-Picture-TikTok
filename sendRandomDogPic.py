import requests
import os


#get a random download link for a dog picture using a dog API
response = requests.get("https://dog.ceo/api/breeds/image/random")
photoURL = response.json()["message"]
print("random dog picture download link = ", photoURL)


#name and destination for the link to be downloaded
picturePath = "/dogPics/dog.jpg"

#download and write picture to a file
Picture_request = requests.get(photoURL)
if Picture_request.status_code == 200:
    with open(picturePath, 'wb') as f:
        f.write(Picture_request.content)

#this will run the shell script to send the downloaded picture
os.system("/dogMsg.sh")

