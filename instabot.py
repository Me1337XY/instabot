from instapy import InstaPy 

session = InstaPy(username="anc.yjoseph",password="sirajsiru123") 
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True,percentage=100)

session.like_by_tags(["follow4follow", "messi"], amount = 3)

session.set_dont_like(["sexy","toxic"])

session.end()
