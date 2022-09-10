#import requests
import requests


#ask for user id
user_id = input("Enter your user id: ")

#ask for token
token = input("Enter your token: ")



#make a request to the discord api using the GetUser endpoint
r = requests.get("https://canary.discord.com/api/v9/users/" + user_id, headers={"Authorization": token})




#check if the request was successful
if r.status_code == 200:
    print("Success!")



    #print the user's username and discriminator
    print("Username: " + r.json()["username"] + "#" + r.json()["discriminator"])

    #print the user's id
    print("User ID: " + r.json()["id"])

   
    


    #print the user's avatar url if they have one
    if r.json()["avatar"] != None:
        print("Avatar url: https://cdn.discordapp.com/avatars/" + user_id + "/" + r.json()["avatar"] + ".png")
    
    #print the user's banner url if they have one
    if r.json()["banner"] != None:
        print("Banner url: https://cdn.discordapp.com/banners/" + user_id + "/" + r.json()["banner"] + ".png")

    #print the user's banner color if they have one
    if r.json()["accent_color"] != None:
        print("Banner color: " + str(r.json()["accent_color"]))

    #print the user's flags
    print("Flags: " + str(r.json()["public_flags"]))
    





else:
    print("Error!")
    print(r.status_code)
