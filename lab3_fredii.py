#  Fredi miranda| Lab 3 | Intro to Pythin

# Ticket 1


username = "fredi"
print(len(username))
# predict: 5 
#  yes the lenght counted every variable in it





# Ticket 2
name = "fredi"
print("First character of username: ", username[0]) #F

print("last character of username: ", username[-1]) # i
print("Last index of username: ", len(username) -1) # 4

# i predict the first letter of the username will be f and the last will be i

# the last index len(username) p1 is minus 1 because it starts counting @ 0 






# Ticket 3

print("Welcome to loop, " + username)

print(f"Welcome to loop, {username}")

# both lines are identical

# i liked the f-string more





# Ticket 4

#username[0] = "x"print(username.upper())
print(username.upper())
# i predicted that this would make me confused and then make it work again

# it at first it makes an error then when you add a string with a dot method it makes eveything to be under controll 







# Ticket 5

feed = ["God is love", "Im a nice person", "The day is nice"]

print(len(feed))
print(feed[0])

# the number 3 will show u because there is three captions that are int the list.

# i used the index method to get the first post because the lists starts counting at the number 0 in python







# Ticket 6

feed.append("I am very nice")
print(feed)

# the prediction came true that there would only be three index

# the 4th post sits at index 3 because the list positions always start at 0 








# Ticket 7

feed.pop(0)
feed.sort()
print(feed)

# my predictoin was correct becuase i predicted that "God is love" got removed and it was set to revoe the things by order

# i used pop(0) to remove the first post from the list and then i use .sort() to arange it alphabetical order









# Ticket 8

profile ={
    "username": "fredi",
    "followers": 20, 
    "verified": True
}
print(profile["followers"])
#profile[0]

#  KeyError: 0

# the follower number was 20 which was printed, but i think that profile[0] will look for the first thing on the comand.

#the dictionaries look up values by the key names insted of the number in the indexes.  





# Ticket 9

profile["followers"] = profile["followers"] + 50
profile["bio"] = "i love God"
print(profile)

print(profile.get("age"))

# .get("age") will print no age because the key is missing "age"

# .get() is safer because it does not crash when the key is missing and if the key does not exist it will reture none.




# Ticket 10

print(f"{profile['username']} has {profile['followers']} followers and {len(feed)} post. Top post: {feed[0]}")