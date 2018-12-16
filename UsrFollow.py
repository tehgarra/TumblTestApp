import pytumblr
 # Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)
 #Variable Declaration
count = 0
osNum = 0
 #Print list of blogs using loop
while (count <= 19) :
  print(client.following(offset=osNum)['blogs'][count]['url'])
  count = count + 1
   if (count > 19) :
    count = 0
    osNum = osNum + 21
 # TODO
# ask for authentication
# check for total_blogs from usr
#...
