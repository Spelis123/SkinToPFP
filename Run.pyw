import tkinter
from tkinter import filedialog, messagebox
from ctypes import windll
import requests, urllib, PIL, webbrowser, os, time, base64, subprocess, tkinter.ttk, io
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from tktooltip import ToolTip as tp

import subprocess

keyPath = "\\Dator\\HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion"
output = subprocess.run(["reg", 
                 "query",
                 keyPath,
                 "/v",
                 "BuildLabEx"], 
               capture_output=True,
               text=True)
print(output.stdout)

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
    window.destroy()
    quit()
def minimizelol():
    global z
    window.state("withdrawn")
    window.overrideredirect(0)
    window.state("iconic")
    z = 1
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
def skindexid():
    if tOD.get() == "The Skindex":
        if not online2.get() == "":
            webbrowser.open("https://www.minecraftskins.com/skin/" + online2.get() + "/e/") 
def dllinklol():
    pass
def uploadfrompc():
    localskinimage = askopenfilename(title="Select Skin:",filetypes=[('Image Files', '*.png')])
    file = open(localskinimage, "rb")
    contentlol = file.read()
    cachelol = open("skinout.png", "wb")
    cachelol.write(contentlol)
    file.close()
    messagebox.showinfo("Saved!","PFP Saved!")
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
class WebImage:
    def __init__(self, url, resize=False, sizex=0, sizey=0):
        print(url)
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        if resize == True:
            image2 = image.resize((sizex,sizey))
            self.image = ImageTk.PhotoImage(image2)
        else:
            self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
window.title("Skin Stealer")
window.geometry("342x232+100+100")
window.attributes("-transparentcolor","purple")
window.state("iconic")
window.overrideredirect(1)
window.state("normal")
z = 1

style = tkinter.ttk.Style()
style.theme_create("Spelis")
style.configure("Custom.TNotebook",
    foreground="#3f3f3f",
    background="#c6c6c6",
    font="Minecraft 15",
    bordercolor="#c6c6c6")
style.configure("Custom.TNotebook.Tab",
    foreground="#c6c6c6",
    background=["#555555","#555555","#444444"],
    font="Minecraft 8")

style.theme_use("Spelis")

bglol = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/bg.png", False, 0, 0)
pc = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/pc.png", False, 0, 0)
dl = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/dl.png", False, 0, 0)
#dllink = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/dllink.png", False, 0, 0)
nm = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/nmsl.png", False, 0, 0)
settingsimg = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/settings.png", False, 0, 0)
helpimg = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/help.png", False, 0, 0)
backimg = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/back.png", False, 0, 0)
pmc = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/downloadpmcskin.png",True,172,111).get()
logoicon = WebImage("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/icon.png",True,28,30).get()
def switchToSettings():
    titlebartext.config(text="Settings")
    mainframe.config(width=0)
    settingsframe.config(width=330)
def switchToHow():
    titlebartext.config(text="How To Use?")
    mainframe.config(width=0)
    howframe.config(width=330)
def switchToMain():
    titlebartext.config(text=window.wm_title())
    mainframe.config(width=330)
    settingsframe.config(width=0)
    howframe.config(width=0)
    window.update()
backgroundcanvas = tkinter.Label(
    image=bglol,
    width=342,
    height=232,
).place(x=-2,y=-2)
titlebar = tkinter.Frame(
    bg="#c6c6c6",
    width=324,
    height=40
)
titlebar.place(x=10,y=6)
mainframe = tkinter.Frame(bg="#c6c6c6",width=330,height=185)
mainframe.place(x=6,y=39)
settingsframe = tkinter.Frame(bg="#c6c6c6",width=0,height=185) # TODO: set width to 330 when showing
settingsframe.place(x=6,y=39)
howframe = tkinter.Frame(bg="#c6c6c6",width=0,height=185) # TODO: set width to 330 when showing
howframe.place(x=6,y=39)
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
titlebartext.place(x=32,y=0)
titlebaricon = tkinter.Label(
    image=logoicon,
    master=titlebar,
    bg="#c6c6c6",
).place(x=0,y=0)
infoButton = tkinter.Button(
    image=helpimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=0,
    master=mainframe,
    command=switchToHow,  #messagebox.showinfo("Instructions",'Press the "Ctrl" and "E" key to minimize the application, to unminimize click the taskbar icon.\nTo close the application, simply press the "ESC" key \n\nPlease note that the "upload from pc" button doesnt work.\nTo download a skin or show their skin list type a minecraft username in the textbox above and then press the button to download or show list\n\nThe gear icon leads to the settings menu as you might have guessed, there you can change settings such as: \nenabling or disabling the Cache folder completely, \nhiding the Upload button, \nshowing the Exit and Minimize buttons (disabled and enabled separately) along with the instructions/help/info button where you are now.\n\nClick OK to continue\n\nProgram made by spelis, please do not copy as your own.')
    width=27,
    height=27
)
infoButton.place(x=270,y=155)
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
    bg="#c6c6c6"
)
online = tkinter.Entry(
    width=16,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
online2 = tkinter.Entry(
    width=16,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
offline = tkinter.Entry(
    width=21,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
tOD = tkinter.StringVar()
tOD.set("Link")

tODlol = tkinter.OptionMenu(mainframe, tOD, "The Skindex", "NovaSkin", "Link")
tODlol.place(x=5,y=150)

howtotabs = tkinter.ttk.Notebook(howframe, height=185,width=330,style="Custom.TNotebook")
howtotabs.place(x=0,y=0)#185 330


PlanetMC = tkinter.Frame(howtotabs,bg="#c6c6c6")
VK = tkinter.Frame(howtotabs,bg="#c6c6c6")

howtotabs.add(PlanetMC,text="PMC Skin Downloading")
howtotabs.add(VK,text="Visibility Controls")

dlpmcs = tkinter.Label(PlanetMC,
    image=pmc,
    bg="#c6c6c6"
).place(x=0,y=0)
dlpmcs2 = tkinter.Label(PlanetMC,
    text="Go to any PlanetMinecraft\nskin and RIGHT CLICK the\ndownload skin button, then\n'Copy Link'. Now you can\npaste it in the link input\nand it will download the\nskin succesfully.",
    font=("Minecraft",8),
    bg="#c6c6c6",
).place(x=176,y=0)

backtomainButton2 = tkinter.Button(
    image=backimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=0,
    command=switchToMain,
    master=howframe,
    width=27,
    height=27,
)
backtomainButton2.place(x=300,y=155)

download = tkinter.Button(
    image=dl,
    bd=0,
    command=downloadfromweb,
    master=mainframe,
    bg="#c6c6c6"
)
download2 = tkinter.Button(
    image=dllink,
    bd=0,
    command=dllinklol,
    master=mainframe,
    bg="#c6c6c6"
)
showlist = tkinter.Button(
    image=nm,
    bd=0,
    command=openlist,
    master=mainframe,
    bg="#c6c6c6"
)
howtouse = tkinter.Label(
    text='Press the "Ctrl" and "E" key to\nminimize the application,to\nunminimize click the taskbar\nicon. To close the application,\nsimply press the "ESC" key',
    master=VK,
    justify="center",
    font=("Minecraft",15),
    bg="#c6c6c6"
).place(x=5,y=0)
previewcheck = tkinter.IntVar()
openfilecheckbox = tkinter.Checkbutton(
    text="",
    bg="#c6c6c6",
    activebackground="#c6c6c6",
    font=("Minecraft",11),
    variable=previewcheck,
    foreground="black",
    height=1,
    master=mainframe,
)
DownloadTip = tp(download,"Download\n\nDownloads Skin From Minecraft",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
NMCTip = tp(showlist,"NameMC\n\nShow NameMC Profile For This User",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
UploadTip = tp(upload,"Upload\n\nUpload From PC Using File Explorer",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
UploadPathTip = tp(offline,"Skin Texture File Path\n\nEnter Path To Skin Texture",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
MinecraftUserTip = tp(online,"Minecraft Username\n\nEnter Minecraft Username (Any Valid One) To Download It \nOtherwise It'll Just Give You A Normal Steve Skin.",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
SkinlinkTip = tp(online2,"Image Link\n\nEnter The Link To Any Image And I'll Try To Make A Profile Picture For You.\nPlease Also Make Sure It Is A Direct Download (No Need To Click Buttons To Get There)",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
PreviewTip = tp(openfilecheckbox,"Open In Image Editor On Download?\n\nWhen Clicking The Download Button I Will\nOpen The Image In Your Default Image Viewer/Editor",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
LinkTypeTip = tp(tODlol,"Link Type\n\nWhat Type Of Link Is This? Is It Just A Normal Link Or Is It\nSomething Else?\n\nClick The Popup Below And Select A Link Type e.x: Planet Minecraft Skin Link",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
DlLinkTip = tp(download2,"Download (Web)\n\nDownloads Skin From A Link",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)


text1.place(x=4, y=-1)
upload.place(x=4, y=25)
openfilecheckbox.place(x=150,y=150)
text2.place(x=4, y=56)
online.place(x=4,y=83)
online2.place(x=4,y=110)
offline.place(x=54,y=32)
showlist.place(x=254,y=83)
download.place(x=180,y=83)
download2.place(x=217,y=83)

window.bind("<Control-e>", lambda i : minimizelol())
window.bind("<Escape>", lambda i : quitlol())
titlebar.bind("<ButtonPress-1>", StartMove)
titlebar.bind("<ButtonRelease-1>", StopMove)
titlebar.bind("<B1-Motion>", OnMotion)
window.bind("<Map>", frameMapped)

window.mainloop()