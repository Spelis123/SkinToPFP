import tkinter
from tkinter import filedialog, messagebox
from ctypes import windll
import requests, urllib, PIL, webbrowser, os, time, base64
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
checkifcachefolderexist = os.path.exists("./Cache")
if checkifcachefolderexist == False:
    os.mkdir("Cache")
    os.mkdir("Cache/Skins")
    os.mkdir("Cache/PFPs")

GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080
WS_BORDER = 0x00800000


def set_appwindow(window):
    hwnd = windll.user32.GetParent(window.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    # re-assert the new window style
    window.wm_withdraw()
    window.after(10, lambda: window.wm_deiconify())

global window, z#, minimized, window_left_custom
window = ""
skinimage = ""
outputskin = ""
window = tkinter.Tk()
window.after(10, lambda: set_appwindow(window))
window_left_custom = False
z = 0
#minimized = 0
def boolLeftWindow(setBool):
    window_left_custom = setBool
    if window_left_custom == True:
        print("true")
        stopignoringme()
    elif window_left_custom == False:
        print("false")
        ignoreme()
def stopignoringme():
    while window.attributes("-alpha") >= 0.5:
        if window_left_custom == True:
            window.attributes("-alpha", window.attributes("-alpha")-0.1)
            time.sleep(0.1)
            print(window.attributes("-alpha"))
def ignoreme():
    while window.attributes("-alpha") <= 0.5:
        if not window_left_custom == True:
            window.attributes("-alpha", window.attributes("-alpha")+0.1)
            time.sleep(0.1)
            print(window.attributes("-alpha"))
def quitlol():
    #settingsfile = open("Settings.txt","w")
    #settingsfile.write(str(int(showuploadcheckvar.get())) + "\n" + str(int(showXcheckvar.get())))
    #settingsfile.close()
    window.destroy()
    quit()
def minimizelol():
    global z#,minimized
    #if not minimized:
    window.state("withdrawn")
    window.overrideredirect(0)
    window.state("iconic")
#    minimized = 1
    z = 1
#    else:
#        unminimizelol()
#    time.sleep(0.1)
#def unminimizelol():
#    global z,minimized
#    window.state("withdrawn")
#    window.overrideredirect(1)
#    window.state("iconic")
#    minimized = 0
#    z = 0
def frameMapped(event=None):
    global z
    window.overrideredirect(True)
    if z == 1:
        set_appwindow(window)
        z = 0
def StartMove(event):
    window.x = event.x
    window.y = event.y
def StopMove(event):
    window.x = None
    window.y = None
def OnMotion(event):
    deltax = event.x - window.x
    deltay = event.y - window.y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))
def openlist():
    if not online.get() == "":
        webbrowser.open("https://namemc.com/profile/" + online.get())
def uploadfrompc():
    pass
    #localskinimage = askopenfilename(title="Select Skin:",filetypes=[('Image Files', '*.png')])
    #file = open(localskinimage, "rb")
    #contentlol = file.read()
    #cachelol = open("skinout.png", "wb")
    #cachelol.write(contentlol)
    #file.close()
    #print(cachelol)
    #messagebox.showinfo("Saved!","PFP Saved!")
def downloadfromweb():
    global skinimage,outputskin
    skinimage = requests.get("https://minecraft.tools/download-skin/" + online.get())
    file = open("skinout.png", "wb")
    file.write(skinimage.content)
    if previewcheck.get() == 1:
        os.startfile("skinout.png")
    file.close()
    file2 = open("Cache/Skins/" + online.get() + ".png", "wb")
    file2.write(skinimage.content)
    file2.close()
    #    croptheimage()
    messagebox.showinfo("Saved!","Skin Saved!")
#def croptheimage():
    #    head1 = outputskin.crop(5,8,15,15)
window.title("Skin Stealer")
window.geometry("342x232+100+100")
window.attributes("-transparentcolor","purple")
window.state("iconic")
window.overrideredirect(1)
window.state("normal")
z = 1
bglol = tkinter.PhotoImage(file="assets/bg.png")
pc = tkinter.PhotoImage(file="assets/pc.png")
dl = tkinter.PhotoImage(file="assets/dl.png")
nm = tkinter.PhotoImage(file="assets/nmsl.png")
settingsimg = tkinter.PhotoImage(file="assets/settings.png")
backimg = tkinter.PhotoImage(file="assets/back.png")
def switchToSettings():
    titlebartext.config(text="Settings")
    mainframe.config(width=0)
    settingsframe.config(width=330)
def switchToMain():
    titlebartext.config(text=window.wm_title())
    mainframe.config(width=330)
    settingsframe.config(width=0)
    window.update()
backgroundcanvas = tkinter.Label(
    image=bglol,
    width=342,
    height=232,
).place(x=-2,y=-2)
titlebar = tkinter.Frame(
    bg="#c6c6c6",
    width=326,
    height=40
)
titlebar.place(x=8,y=6)
mainframe = tkinter.Frame(bg="#c6c6c6",width=330,height=185)
mainframe.place(x=6,y=39)
settingsframe = tkinter.Frame(bg="#c6c6c6",width=0,height=185) # TODO: set width to 330 when showing
settingsframe.place(x=6,y=39)
text1 = tkinter.Label(
    text="Local:",
    font=("Minecraft",15),
    fg="#3F3F3F",
    bg="#c6c6c6",
    master=mainframe
)
text2 = tkinter.Label(
    text="Web Download:",
    font=("Minecraft",15),
    fg="#3F3F3F",
    bg="#c6c6c6",
    master=mainframe,
)
titlebartext = tkinter.Label(
    bg="#c6c6c6",
    text=window.wm_title(),
    font=("Minecraft",15),
    master=titlebar,
    fg="#3F3F3F",
)
titlebartext.place(x=2,y=0)
infoButton = tkinter.Button(
    text="?",
    font=("Minecraft",16),
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=0,
    width=2,
    height=1,
    master=titlebar,
    command= lambda: messagebox.showinfo("Instructions",'Press the "Ctrl" and "E" key to minimize the application, to unminimize click the taskbar icon.\nTo close the application, simply press the "ESC" key \n\nPlease note that the "upload from pc" button doesnt work.\nTo download a skin or show their skin list type a minecraft username in the textbox above and then press the button to download or show list\n\nThe gear icon leads to the settings menu as you might have guessed, there you can change settings such as: \nenabling or disabling the Cache folder completely, \nhiding the Upload button, \nshowing the Exit and Minimize buttons (disabled and enabled separately) along with the instructions/help/info button where you are now.\n\nClick OK to continue\n\nProgram made by spelis, please do not copy as your own.')
)
infoButton.place(x=300,y=-10)
settingsButton = tkinter.Button(
    image=settingsimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=0,
    command=switchToSettings,
    master=mainframe,
    width=27,
    height=27
).place(x=300,y=155)
backtomainButton = tkinter.Button(
    image=backimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=0,
    command=switchToMain,
    master=settingsframe,
    width=27,
    height=27
).place(x=300,y=155)
upload = tkinter.Button(
    image=pc,
    bd=0,
    command=uploadfrompc,
    master=mainframe,
)
online = tkinter.Entry(
    width=21,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
download = tkinter.Button(
    image=dl,
    bd=0,
    command=downloadfromweb,
    master=mainframe,
)
showlist = tkinter.Button(
    image=nm,
    bd=0,
    command=openlist,
    master=mainframe,
)
previewcheck = tkinter.IntVar()
openfilecheckbox = tkinter.Checkbutton(
    bg="#717171",
    activebackground="#717171",
    font=("Minecraft",11),
    variable=previewcheck,
    foreground="black",
    height=1,
    master=mainframe,
)
showuploadcheckvar = tkinter.BooleanVar()
#settings_get = open("Settings.txt","r")
#settings_gotten = bool(settings_get.readline(0))
#print(str(settings_gotten))
#settings_get.close()
showuploadcheckvar.set(True)
showuploadbutton = tkinter.Checkbutton(
    text="Show Upload Button",
    variable=showuploadcheckvar,
    font="Minecraft",
    master=settingsframe,
    bg="#c6c6c6",
    activebackground="#c6c6c6",
    command= lambda: ((text1.place(x=4, y=-1), upload.place(x=4, y=25),openfilecheckbox.place(x=99,y=110),text2.place(x=4, y=56),online.place(x=4,y=83),showlist.place(x=4,y=142),download.place(x=4,y=108)) if showuploadcheckvar.get() else (text1.place_forget(), upload.place_forget(),openfilecheckbox.place(x=99,y=52),text2.place(x=4, y=-1),online.place(x=4,y=25),download.place(x=4,y=50),showlist.place(x=4,y=85)))
)
showuploadbutton.place(x=4,y=0)
showXcheckvar = tkinter.BooleanVar()
#settings1_get = open("Settings.txt","r")
#settings1_gotten = bool(settings1_get.readline(1))
#print(str(settings1_gotten))
#settings1_get.close()
showXcheckvar.set(False)
showXbutton = tkinter.Checkbutton(
    text='Show Quit and Minimize Buttons',
    variable=showXcheckvar,
    font="Minecraft",
    master=settingsframe,
    bg="#c6c6c6",
    activebackground="#c6c6c6",
    command= lambda: ((infoButton.place(x=300,y=-10)) if showXcheckvar.get() else (infoButton.place(x=300,y=-10)))
)
showXbutton.place(x=4,y=30)

(text1.place(x=4, y=-1), upload.place(x=4, y=25),openfilecheckbox.place(x=99,y=110),text2.place(x=4, y=56),online.place(x=4,y=83),showlist.place(x=4,y=142),download.place(x=4,y=108)) if showuploadcheckvar.get() else (text1.place_forget(), upload.place_forget(),openfilecheckbox.place(x=99,y=52),text2.place(x=4, y=-1),online.place(x=4,y=25),download.place(x=4,y=50),showlist.place(x=4,y=85))

window.bind("<Control-e>", lambda i : minimizelol())
window.bind("<Escape>", lambda i : quitlol())
titlebar.bind("<ButtonPress-1>", StartMove)
titlebar.bind("<ButtonRelease-1>", StopMove)
titlebar.bind("<B1-Motion>", OnMotion)
window.bind("<Map>", frameMapped)
#window.bind("<Leave>", lambda i : stopignoringme())
#window.bind("<Enter>", lambda i : ignoreme())

window.mainloop()