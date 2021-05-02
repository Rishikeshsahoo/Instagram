import instaloader
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

username='rishikeshsahoo_2828'
password='32416282rishi'

L=instaloader.Instaloader()
L.login(username,password)


root=Tk()
root.title=('NOT FOLLOWING BAD PEOPLE')
root.geometry('500x400')


profile=instaloader.Profile.from_username(L.context,username)


me_follow_list=[]
i_follow_list=[]


for me_folloing in profile.get_followees():
    me_follow_list.append(me_folloing.username)

for i_following in profile.get_followers():
    i_follow_list.append(i_following.username)



main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)

my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

second_frame=Frame(my_canvas)

my_canvas.create_window((0,0),window=second_frame, anchor='nw')

for i in me_follow_list:
    if i not in i_follow_list:

        Label(second_frame,text=i,font=("Arial bold", 18),justify='center').pack(padx=150)


root.mainloop()