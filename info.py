import instaloader
from tkinter import *
from secreats import username,password

L=instaloader.Instaloader()
L.login(username,password)

profile=instaloader.Profile.from_username(L.context,username)

print(profile.username)
print(profile.followers)
print(profile.followees)
print(profile.full_name)
print(profile.biography)
print(profile.profile_pic_url)

root=Tk()
root.title=('NOT FOLLOWING BAD PEOPLE')
root.geometry('600x500')

msg="Full Name: {}\nUsername: {}\nUser-ID: {}\nFollowers: {}\nFollowees: {}\n\nBiography: {}".format(profile.full_name,profile.username,profile.userid,profile.followers,profile.followees,profile.biography)

Label(root,text=msg,font=("Arial bold", 18),relief='ridge').pack()
root.mainloop()


# posts.url, posts.caption, posts.likes, posts.comments

# post_mgs="Url: {}\n\nCaption: {}\nLikes: {}\nComments: {}"

for post in profile.get_posts():
    L.download_post(post, target=profile.username)
