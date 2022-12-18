#---IMPORTS---#
import tkinter
from tkinter import filedialog, messagebox
from ctypes import windll
import requests, urllib, PIL, webbrowser, os, time, base64, subprocess, tkinter.ttk, io, datetime, winreg as wr, threading
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from tktooltip import ToolTip as tp
#!--Parameters---#

SkinToPFP_update: bool = False #* Default: True
SkinToPFP_update_githubrepo: str = "https://github.com/Spelis123/SkinToPFP" #* Default: "https://github.com/Spelis123/SkinToPFP"

window_minimize_and_exit_buttons: bool = False #* Default: False
tbcolorunfocus = "#aaaaaa" #*can be set to tbcolor or a hex code (Default: "#aaaaaa")
tbcolormoving = "#0080ff" #* insert your fav color can be i.e "green" or "#0080ff" etc.

#!--CODE (dont mess with unless you know what ur doin. not that much will happen im just warning you)---#

updater = tkinter.Tk()
updater.title("Skin To PFP Updater")

class WebDL:
    def __init__(self, url,size=1,type="PhotoImage"):
        global filetype, rdata
        filetype = type
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        if not type == "executable":
            image = Image.open(io.BytesIO(raw_data))
            sizex, sizey = image.size
            sizex = round(sizex / size)
            sizey = round(sizey / size)
            image2 = image.resize((sizex,sizey))
        if type == "PhotoImage":
            self.image = ImageTk.PhotoImage(image2)
        if type == "Icon":
            imagef = open("TempFiles\TempWebImg.ico", "wb")
            imagef.write(raw_data)
        if type == "binary":
            rdata = io.BytesIO(raw_data)
            print(rdata)
    def get(self):
        if filetype == "PhotoImage":
            return self.image
        if filetype == "Icon":
            return "TempFiles\TempWebImg.ico"
            imagef.close()
        if filetype == "binary":
            return 

def centerScreen(root, x, y):
    sw = int(root.winfo_screenwidth())
    sh = int(root.winfo_screenheight())
    ww = int(x)
    wh = int(y)
    posw = str(round(sw/2-ww/2))
    posh = str(round(sh/2-wh/2))
    root.geometry(str(x) + "x" + str(y) + "+" + posw + "+" + posh)

def updatefunction():
    updatestate['value']=25
    newexe = WebDL(SkinToPFP_update_githubrepo + "/blob/main/dist/SkinStealer.exe?raw=true",type="executable").get()
    time.sleep(0.5)
    updatestate['value']=50
    oldexe = open("dist/SkinStealer.exe", "rb")
    print(oldexe.read())
    time.sleep(0.5)
    updatestate['value']=75
    if not oldexe == newexe:
        time.sleep(0.5)
        updatestate['value']=80
        updateque = tkinter.messagebox.askyesno("Update","Update Found! Wanna Update?")
        if updateque == 1:
            print("YUES")
            oldexe = open("dist/SkinStealer.exe", "wb")
            oldexe.write(newexe.read())
        else:
            print("NOEEE")
            updater.destroy()


centerScreen(updater, 250, 50)

style = tkinter.ttk.Style()
style.configure("TProgressBar", foreground="black", background="black")
style.map('TProgressBar',
    foreground=[('pressed', 'blue'),
    ('active', 'red')])


updAnimCan = tkinter.Canvas(updater,bg="#303030",bd=-1,height=10000,width=10000).place(x=-2,y=-2)
updatestate=tkinter.ttk.Progressbar(updater,orient=tkinter.HORIZONTAL,length=1920,mode='determinate')
updatestate.pack()
updatetext = tkinter.Label(text="Updating Your Instance Of SkinToPFP",bg="#303030",fg="#ffffff").pack()
if SkinToPFP_update == True:
    updatefunction()
elif SkinToPFP_update == False:
    updater.destroy()
updater.mainloop()

if os.path.exists("./TempFiles") == False:
    os.mkdir("TempFiles")    

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

global window, z, focus#, minimized, window_left_custom

focus = 1
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
        window.focus_force()
def StartMove(event):
    window.x = event.x
    window.y = event.y
    titlebartext.config(bg=tbcolormoving)
def StopMove(event):
    window.x = None
    window.y = None
    titlebartext.config(bg=tbcolor)
def focusnomore(event):
    focus = 0
    titlebartext.config(bg=tbcolorunfocus)
    window.attributes("-alpha",0.5)
def focusyes(event):
    focus = 1
    titlebartext.config(bg=tbcolor)
    window.attributes("-alpha",1)
def OnMotion(event):
    deltax = event.x - window.x
    deltay = event.y - window.y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))
def openlist():
    if not online.get() == "":
        webbrowser.open("https://namemc.com/profile/" + online.get())
def dllinklol():
    if online2.get() in "https://":
        skinimage = requests.get(online2.get())
        file = open("Cache/Skins/TempSkin.png", "wb")
        file.write(skinimage)
        file.close()
        file2 = open("Cache/Skins/SkinFromLink.png", "wb")
        file2.write(skinimage)
        file2.close()
        messagebox.showinfo("Saved!","Skin Saved!")
    else:
        messagebox.showerror("Invalid Link :/","Image Didn't Download.\nBad Link Error. Please Use HTTPS Protocol")
def uploadfrompc():
    localskinimage = askopenfilename(title="Select Skin:",filetypes=[('Image Files', '*.png')])
    file = open(localskinimage, "rb")
    contentlol = file.read()
    cachelol = open("Cache/Skins/" + offline.get() + ".png", "wb")
    cachelol2 = open("Cache/Skins/TempSkin.png", "wb")
    cachelol.write(contentlol)
    cachelol2.write(contentlol)
    file.close()
    messagebox.showinfo("Saved!","PFP Saved!")
def downloadfromweb():
    global skinimage,outputskin
    skinimage = requests.get("https://minecraft.tools/download-skin/" + online.get())
    file = open("Cache/Skins/TempSkin.png", "wb")
    file.write(skinimage.content)
    if previewcheck.get() == 1:
        os.startfile("Cache/Skins/TempSkin.png")
    file.close()
    file2 = open("Cache/Skins/" + online.get() + ".png", "wb")
    file2.write(skinimage.content)
    file2.close()
    #    croptheimage()
    messagebox.showinfo("Saved!","Skin Saved!")
#def croptheimage():
    #    head1 = outputskin.crop(5,8,15,15)

class changeChars:
    def __init__(self, text, char, setTo):
        changechar = []
        newtext = ""
        for i in range(len(text)):
            if text[i] == char:
                changechar.append(i)
        for i in range(len(text)):
            if text[i] == char:
                newtext = newtext + setTo
            else:
                newtext = newtext + text[i]
        print(newtext)

bglol = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/bg.png").get()
bgframe = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/bgmain.png").get()
pc = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/pc.png").get()
dl = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/dl.png").get()
dllink = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/dllink.png").get()
opdir = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/openfolder.png").get()
nm = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/nmsl.png").get()
settingsimg = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/settings.png").get()
helpimg = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/help.png").get()
backimg = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/back.png").get()
pmc = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/downloadpmcskin.png",2.65).get()
logoicon = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/icon.png",6).get()
logoico = WebDL("https://raw.githubusercontent.com/Spelis123/SkinToPFP/main/assets/icon.ico",1,type="Icon").get()

window.title("Skin Stealer")
window.geometry("470x296+100+100")
window.attributes("-transparentcolor","purple")
window.state("iconic")
window.overrideredirect(1)
window.state("normal")
window.iconbitmap(logoico)
z = 1

def switchToSettings():
    titlebartext.config(text=window.wm_title() + " - Settings")
    mainframe.config(width=0)
    settingsframe.config(width=330)
def switchToHow():
    titlebartext.config(text=window.wm_title() + " - How To Use?")
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
    width=470,
    height=296,
).place(x=-2,y=-2)
mainframe = tkinter.Frame(bg="#c6c6c6",width=454,height=188)
mainframe.place(x=6,y=39)

mainframebg = tkinter.Label(mainframe,image=bgframe,bd=-1).place(x=0,y=0)

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
tbcolor = "#c6c6c6"
titlebar = tkinter.Frame(
    bg="#c6c6c6",
    width=450,
    height=30
);titlebar.place(x=10,y=6)
titlebartext = tkinter.Label(
    bg=tbcolor,
    image=logoicon,
#    text=window.wm_title(),
#    font=("Minecraft",15),
    master=titlebar,
    fg="#3F3F3F",
    width=450,
);titlebartext.place(x=0,y=0)
titlebaricon = tkinter.Label(
    image=logoicon,
    master=titlebar,
    bg=tbcolor,
)#.place(x=0,y=0)
infoButton = tkinter.Button(
    image=helpimg,
    bg="#555555",
    activebackground="#454545",
    bd=-1,
    command=switchToHow,  #messagebox.showinfo("Instructions",'Press the "Ctrl" and "E" key to minimize the application, to unminimize click the taskbar icon.\nTo close the application, simply press the "ESC" key \n\nPlease note that the "upload from pc" button doesnt work.\nTo download a skin or show their skin list type a minecraft username in the textbox above and then press the button to download or show list\n\nThe gear icon leads to the settings menu as you might have guessed, there you can change settings such as: \nenabling or disabling the Cache folder completely, \nhiding the Upload button, \nshowing the Exit and Minimize buttons (disabled and enabled separately) along with the instructions/help/info button where you are now.\n\nClick OK to continue\n\nProgram made by spelis, please do not copy as your own.')
    width=27,
    height=27
)
infoButton.place(x=401,y=197)
settingsButton = tkinter.Button(
    image=settingsimg,
    bg="#555555",
    activebackground="#454545",
    bd=-1,
    command=switchToSettings,
    width=27,
    height=27
).place(x=431,y=197)
backtomainButton = tkinter.Button(
    image=backimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=-1,
    command=switchToMain,
    master=settingsframe,
    width=27,
    height=27
).place(x=300,y=155)
upload = tkinter.Button(
    image=pc,
    bd=-1,
    command=uploadfrompc,
    master=mainframe,
    bg="#c6c6c6"
)
online = tkinter.Entry(
    width=30,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
online2 = tkinter.Entry(
    width=30,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)
offline = tkinter.Entry(
    width=25,
    bg="Black",
    highlightthickness=1,
    highlightbackground="White",
    font="Minecraft",
    fg="white",
    master=mainframe,
)

howtotabs = tkinter.ttk.Notebook(howframe, height=185,width=330)
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
dlpmcs3 = tkinter.Label(PlanetMC,
    text="This should also work with any other image.\n(If there is a download button that leads to a link)",
    font=("Minecraft",8),
    bg="#c6c6c6",
    justify=tkinter.LEFT
).place(x=0,y=115),

backtomainButton2 = tkinter.Button(
    image=backimg,
    bg="#c6c6c6",
    activebackground="#e7e7e7",
    bd=-1,
    command=switchToMain,
    master=howframe,
    width=27,
    height=27,
)
backtomainButton2.place(x=300,y=155)

download = tkinter.Button(
    image=dl,
    bd=-1,
    command=downloadfromweb,
    master=mainframe,
    bg="#c6c6c6"
)
download2 = tkinter.Button(
    image=dllink,
    bd=-1,
    command=dllinklol,
    master=mainframe,
    bg="#c6c6c6"
)
current_dir = os.getcwd()
print(current_dir)
openfolder = tkinter.Button(
    image=opdir,
    bd=-1,
    command=lambda: subprocess.Popen(f'explorer /open,"{current_dir}\\Cache"'),
    master=mainframe,
    bg="#c6c6c6"
)
showlist = tkinter.Button(
    image=nm,
    bd=-1,
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
NameTip = tp(offline,"Filename\n\nEnter Your Desired Filename For The Skin File",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
MinecraftUserTip = tp(online,"Minecraft Username\n\nEnter Minecraft Username (Any Valid One) To Download It \nOtherwise It'll Just Give You A Normal Steve Skin.",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
SkinlinkTip = tp(online2,"Image Link\n\nEnter The Link To Any Image And I'll Try To Make A Profile Picture For You.\nPlease Also Make Sure It Is A Direct Download (No Need To Click Buttons To Get There)",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
PreviewTip = tp(openfilecheckbox,"Open In Image Editor On Download?\n\nWhen Clicking The Download Button I Will\nOpen The Image In Your Default Image Viewer/Editor",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
DlLinkTip = tp(download2,"Download (Web)\n\nDownloads Skin From A Link",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)
openfolderTip = tp(openfolder,"Open Folder\n\nOpens The Folder/Directory Where The Skins Are Located.",delay=-1,parent_kwargs={"bg": "#000000", "padx": 2, "pady": 2},
        fg="#ffffff", bg="#1c1c1c", padx=5, pady=5)


text1.place(x=4, y=-1)
upload.place(x=4, y=25)
openfilecheckbox.place(x=47,y=150)
text2.place(x=4, y=56)
online.place(x=4,y=83)
online2.place(x=4,y=110)
offline.place(x=54,y=32)
showlist.place(x=77,y=145)
download.place(x=5,y=145)
openfolder.place(x=150,y=145)
download2.place(x=114,y=145)

window.bind("<Control-e>", lambda i : minimizelol())
window.bind("<Escape>", lambda i : quitlol())
titlebartext.bind("<ButtonPress-1>", StartMove)
titlebartext.bind("<ButtonRelease-1>", StopMove)
titlebartext.bind("<B1-Motion>", OnMotion)
window.bind("<Map>", frameMapped)
window.bind('<FocusOut>', focusnomore)
window.bind('<FocusIn>', focusyes)
window.bind('<Enter>', lambda i : window.attributes('-alpha',0.75) if focus == 0 else None)

window.mainloop()