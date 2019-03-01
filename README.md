# Instagram-Follow-and-Like-Bot
This bot allows us to like and follow profiles
# steps to follow:
# Update username and password in config.json
# create a InstagramBot object            
bot = InstagramBot()

# initialize the driver
bot.setDriver()

# login as the bot
bot.login()

# either follow any profile giving only the user id which is part of: 
# profile url: https://www.instagram.com/rahulshaw274/
# userid: rahulshaw274
profileToFollow = 'rahulshaw274'
bot.follow(profileToFollow)

# or like every photo of a pofile
profileToLike = 'rahulshaw274'
bot.likePhoto(profileToLike)
