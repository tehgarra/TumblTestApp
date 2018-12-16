import pytumblr
 # Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)
 #Variable Declaration
count = 0 #general counter
osNum = 0 # offset value
 #Print list of blogs using loop
while (count <= 19) :
  print(client.following(offset=osNum)['blogs'][count]['url']) #note1
  count = count + 1
   if (count > 19) :
    count = 0
    osNum = osNum + 21
 # TODO
# ask for authentication
# check for total_blogs from usr
#...

#note1: possible bug, or inential decrease of displayed blogs starting after offset 57
