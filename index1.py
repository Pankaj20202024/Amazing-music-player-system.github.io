import tkinter
from tkinter import *
from tkinter.ttk import Progressbar
import datetime
from pygame import mixer
from tkinter import filedialog
import os
import pickle
from mutagen.mp3 import MP3
import pafy
import requests
from tkinter import messagebox

def volumeup():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(volume + 0.02)
    progressbarvolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarvolume['value'] = mixer.music.get_volume() * 100


def volumedown():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(volume - 0.02)
    progressbarvolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarvolume['value'] = mixer.music.get_volume() * 100


def stopmusic():
    mixer.music.stop()
    audiostatus.configure(text='Stopped.......')


def mutemusic():
    global current_volume
    current_volume = mixer.music.get_volume()
    mutebuttonorignal.grid_remove()
    unmutebuttonorignal.grid()
    mixer.music.set_volume(0)
    audiostatus.configure(text='muted......')


def unmutemusic():
    unmutebuttonorignal.grid_remove()
    mutebuttonorignal.grid()
    mixer.music.set_volume(current_volume)
    audiostatus.configure(text='Playing......')


def pausemusic():
    playbuttonorignal.grid()
    pausebuttonorignal.grid_remove()
    mixer.music.pause()
    audiostatus.configure(text='paused.......')


def play_online_bar_visible():
    global btnstate
    if btnstate is True:
        for x in range(305):
            navroot.place(x=-x, y=0)
            topframe.update()
        online_song_label.place(x=10, y=483)
        topframe.config(bg='gray17')
        root.config(bg="aquamarine")
        btnstate = False

def is_module_active(timeout):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def play_online():
    check=is_module_active(timeout=1)
    if check==False:
        messagebox.showinfo("Warning ", "Please Check Your Internet Connection")

    audio = entry.get()
    print(audio)
    import pywhatkit as kit

    kit.playonyt(audio)


Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        ytdlocationError.config(text=Folder_Name, fg='dark green')
    else:
        ytdlocationError.config(text='Please Choose Folder !! ', fg="red")


def Downloadmp3():
    check=is_module_active(timeout=1)
    if check==False:
        messagebox.showinfo("Warning ", "Please Check Your Internet Connection")
    url = url_text.get()
    video = pafy.new(url)
    audios = video.getbestaudio()
    audios.download(Folder_Name)
    ytdError.configure(text='Download complete ', fg='dark green')

def download_song():
        global btnstate
        if btnstate is True:
            for x in range(305):
                navroot.place(x=-x, y=0)
                topframe.update()
            mp3_download_frame.place(x=12, y=62)
            topframe.config(bg='gray17')
            root.config(bg="aquamarine")

            btnstate = False


def send_songs():

    check=is_module_active(timeout=1)
    if check==False:
        messagebox.showinfo("Warning ", "Please Check Your Internet Connection")

    import pywhatkit as pwt
    num1=contact_number.get()
    hour=hours.get()
    minutes=minute.get()
    info=your_mess.get()
    pwt.sendwhatmsg(num1,info,hour,minutes)
    status_send_label.configure(text="Message Sendeed",fg="green")

def share_songs():
    global btnstate
    if btnstate is True:

        for x in range(305):
            navroot.place(x=-x, y=0)
            topframe.update()
        whatup_frame_label.place(x=10,y=60)
        topframe.config(bg='gray17')
        root.config(bg="aquamarine")

        btnstate = False

################## setting switch function ####################
def switch():
    global btnstate
    if btnstate is True:
        for x in range(305):
            navroot.place(x=-x, y=0)
            topframe.update()

        topframe.config(bg='gray17')
        root.config(bg="aquamarine")

        btnstate = False

    else:
        mp3_download_frame.place_forget()
        online_song_label.place_forget()
        whatup_frame_label.place_forget()
        topframe.config(bg='gray25')
        root.config(bg='aquamarine')

        for x in range(-305, 0):
            navroot.place(x=x, y=0)
            topframe.update()

        btnstate = True

def create():
    mixer.init()

    global audiotrackimage, audiocontrol, playbutton_image, pausebutton_image, resumebutton_image, stopbutton_image
    global navwithplaylist, count, text, progressbarvolumelabel, progressbarvolume, audiostatus, unmutemusic, current
    global mutebuttonorignal, unmutebuttonorignal, pausebuttonorignal, playbuttonorignal, current, playmusic_from_button
    global online_song_label,download_song,mp3_download_frame,topframe,navroot,slider_music_name
    ############# images of global variable ##################
    global mutebutton_image, unmutebutton_image, previousbutton_image, next_image, volume_up_image, volume_down_image
    global menu_image, cancel_image, btnstate, imlist, download_image, play_online_image, load_song_image, entry

    ######### global variable for downloading the audio from youtube ############
    global ytdlocationError, choices, ytdchoice, url_text, ytdError,download_image_for_music,select_folder,online_playing

    ################## whatup audio  share  global images ######################
    global song_name, status_audio_label, chose_audios, send_audios, contact_number,share_songs,whatup_frame_label
    global hours,minute,your_mess,status_send_label

    btnstate = False

    ############# fixing images  in  some variable ###########

    playbutton_image = PhotoImage(file='play.png')
    pausebutton_image = PhotoImage(file='pause.png')
    resumebutton_image = PhotoImage(file='resume.png')
    stopbutton_image = PhotoImage(file='stop.png')
    mutebutton_image = PhotoImage(file='mute.png')
    unmutebutton_image = PhotoImage(file='speaker.png')
    previousbutton_image = PhotoImage(file='previous.png')
    next_image = PhotoImage(file='next-button.png')
    volume_down_image = PhotoImage(file='volume-down1.png')
    volume_up_image = PhotoImage(file='volume-up1.png')
    menu_image = PhotoImage(file='menu.png')
    cancel_image = PhotoImage(file='cancel.png')
    download_image_for_music=PhotoImage(file='download1.png')
    select_folder=PhotoImage(file='choose.png')
    online_playing=PhotoImage(file="video.png")
    chose_audios=PhotoImage(file="tap.png")
    send_audios=PhotoImage(file="share.png")



    ############# resizing for the images  #############
    playbutton_image = playbutton_image.subsample(9, 9)
    pausebutton_image = pausebutton_image.subsample(9, 9)
    resumebutton_image = resumebutton_image.subsample(9, 9)
    stopbutton_image = stopbutton_image.subsample(9, 9)
    mutebutton_image = mutebutton_image.subsample(9, 9)
    unmutebutton_image = unmutebutton_image.subsample(9, 9)
    previousbutton_image = previousbutton_image.subsample(9, 9)
    next_image = next_image.subsample(9, 9)
    volume_up_image = volume_up_image.subsample(8, 8)
    volume_down_image = volume_down_image.subsample(9, 9)
    menu_image = menu_image.subsample(11, 11)
    cancel_image = cancel_image.subsample(12, 12)
    download_image_for_music=download_image_for_music.subsample(7,7)
    select_folder=select_folder.subsample(7,7)
    online_playing=online_playing.subsample(7,7)
    chose_audios=chose_audios.subsample(8,8)
    send_audios=send_audios.subsample(8,8)

    ######### fixing image of audio track  frame ################
    audiotrackimage = PhotoImage(file='319256.png')
    ######## change size of image #####
    audiotrackimage = audiotrackimage.subsample(6, 6)

    ####### frame1 #########

    navwithplaylist = LabelFrame(root, bg='gray17', bd=5, relief=tkinter.GROOVE, fg='aquamarine',font=('arial',10,'italic bold'))
    navwithplaylist.configure(width=730, height=730)
    navwithplaylist.grid(row=0, column=0, padx=2, pady=2, rowspan=4)


    ############ frame2 ###########
    audiotrakframe = LabelFrame(root, bg='gray17', bd=7, fg='aquamarine', text='AUDIO TRACK ',
                                font=('arial', 12, 'italic bold'),
                                relief=tkinter.GROOVE)
    audiotrakframe.configure(width=400, height=350)
    audiotrakframe.grid(row=0, column=1, padx=3, pady=10)

    widget = Label(audiotrakframe, image=audiotrackimage)
    widget.grid(row=0, column=1, padx=0, pady=0)

    ######################## slider and progresss bar frame ###########
    ############## frame 3 #########################
    sliderandprogressbar = LabelFrame(root, bg='gray17', bd=7, relief=tkinter.GROOVE, fg='pink')
    sliderandprogressbar.configure(width=600, height=70)
    sliderandprogressbar.grid(row=2, column=1, padx=5, pady=1, columnspan=2)

    progressbarmusicstartlabel = Label(sliderandprogressbar, text='0:00:0', bg='navy', bd=3, width=8, fg='aquamarine')
    progressbarmusicstartlabel.grid(row=0, column=0)

    progressbarmusic = Progressbar(sliderandprogressbar, orient=HORIZONTAL, mode='determinate', value=0)
    progressbarmusic.grid(row=0, column=1, ipadx=180, ipady=5)

    progressbarmusicendlabel = Label(sliderandprogressbar, text='0:00:0', bg='navy', bd=3, width=8, fg='aquamarine')
    progressbarmusicendlabel.grid(row=0, column=2)

    ######################## audio control frame ###################

    audiocontrol = LabelFrame(root, bg='gray17', fg='aquamarine', bd=7, text='CONTROLS ',
                              font=('arial', 12, 'italic bold')
                              , relief=tkinter.GROOVE)
    audiocontrol.configure(width=650, height=370)
    audiocontrol.grid(row=3, column=1, padx=5, pady=4, columnspan=3)

    ########################  volume control frame #####################

    volumecontrol = LabelFrame(root, bg='gray17', bd=6, relief=tkinter.GROOVE)
    volumecontrol.configure(width=100, height=300)
    volumecontrol.grid(row=0, column=2, padx=4, pady=10)

    #################### audio status label in audiocontrol frame ####################
    audiostatus = Label(audiocontrol, text=' ', font=('arial', 12, 'italic bold '), bg='skyblue', relief=tkinter.GROOVE,
                        bd=4, width=10)
    audiostatus.grid(row=1, column=1, padx=1, pady=10)
    audiostatus.grid_remove()

    #################### creating nav bar ###############################

    topframe = LabelFrame(navwithplaylist, bg='gray17', width=730, height=730)
    topframe.pack(side='top', fill=tkinter.X)

    ############## nav bar button ##########################

    menu_button = Button(topframe, bd=0, image=menu_image, bg='gray17',
                         activebackground='gray17', command=switch, padx=20)
    menu_button.place(x=10, y=5)

    ############# setting nav root frame ########################
    navroot = LabelFrame(navwithplaylist, bg='gray17', height=730, width=300, padx=0)
    navroot.place(x=-305, y=0)

    topframe_of_navbar = Label(navroot, font='Bhanschrift 15', bg='aquamarine', fg='violet', height=2, width=300,
                               padx=20)
    topframe_of_navbar.place(x=0, y=0)

    ############## playlist ########################

    playlistlabel = LabelFrame(navwithplaylist, bg='aquamarine', bd=6, width=40, height=10, text='PLAYLIST',
                               font=('arial', 13, 'italic bold'),
                               fg='navy')
    playlistlabel.place(x=417, y=5)
    scrollbar = Scrollbar(playlistlabel, orient=VERTICAL)
    scrollbar.grid(row=0, column=1, rowspan=5, sticky='ns', padx=0)

    if os.path.exists('songs.pickle'):
        f = open('songs.pickle', 'rb')
        song_list = pickle.load(f)
    else:
        song_list = []

    current = 0


    def playmusic(event=None):
        global current,music_names
        if event is not None:
            current = listbox.curselection()[0]
            music_names = song_list[current]
            for i in range(len(song_list)):
                listbox.itemconfigure(i, bg='gray')
                break

        mixer.music.load(song_list[current])
        listbox.activate(current)
        mixer.music.set_volume(0.4)
        progressbarvolumelabel['text'] = '40%'
        progressbarvolume['value'] = 40
        audiostatus.configure(text='Playing......')
        playbuttonorignal.grid_remove()
        pausebuttonorignal.grid()
        mixer.music.play()
        audiostatus.grid(row=1, column=1, padx=1, pady=10)
        song = MP3(song_list[current])
        totalsonglength = int(song.info.length)
        progressbarmusic['maximum'] = totalsonglength
        progressbarmusicendlabel['text'] = str(datetime.timedelta(seconds=totalsonglength))
        music_names = song_list[current]

        def progressbarmusictic():
            currentsonglength = mixer.music.get_pos() // 1000
            progressbarmusic['value'] = currentsonglength
            progressbarmusicstartlabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentsonglength))))
            progressbarmusic.after(2, progressbarmusictic)


        progressbarmusictic()

    def previous_song():
        global current,previous
        previous=current

        if current > 0:
            current = current - 1
        else:
            current = 0
            playmusic()
        listbox.itemconfigure(current, bg='navy',fg='white')
        playmusic()


    def next_song():
        global current
        if current < len(song_list) - 1:
            current = current + 1
        else:
            current = 0
            playmusic()
        listbox.itemconfigure(current, bg='navy',fg='white')
        playmusic()


    def resumemusic_from_button():
        playbuttonorignal.grid_remove()
        pausebuttonorignal.grid()
        mixer.music.unpause()
        audiostatus.configure(text='Playing......')

    def enumerat_song(song_list):
        for index, song in enumerate(song_list):
            listbox.insert(index, os.path.basename(song))



    listbox = Listbox(playlistlabel, selectmode=SINGLE, yscrollcommand=scrollbar.set, selectbackground='navy')
    enumerat_song(song_list)
    listbox.bind('<Double-1>', playmusic)
    listbox.config(height=27, width=25, bg='gray60', font=('arial', 15, 'italic bold'), fg='gray1')
    listbox.grid(row=0, column=0, rowspan=5, padx=1, pady=0)
    scrollbar.config(command=listbox.yview, bg='gray17')

    def loadsongs():
        songlist = []
        directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    path = (root_ + '/' + file).replace('\\', '/')
                    songlist.append(path)
        f = open('songs.pickle', 'wb')
        pickle.dump(songlist, f)

        song_list = songlist


        listbox.delete(0, END)
        enumerat_song(song_list)

    ############ setting y axis ############
    y = 80
    ############ setting nav bar option #############
    option = ["WhatsApp Messages ", "Load Songs ", "Download Songs", "PLay Online"]

    ########### setting nav bar option button ############
    for i in range(4):
        # icon=icons[i]
        if option[i] == 'WhatsApp Messages ':
            icons_image = Button(navroot, text=option[i], font='Bhanschrift 15', bg='gray17', fg='aquamarine',
                                 activebackground='gray17', activeforeground='green', bd=0, compound=RIGHT,command=share_songs
                                 )
            icons_image.place(x=10, y=y)
            y = y + 60


        elif option[i] == 'Load Songs ':
            icons_image = Button(navroot, text=option[i], font='Bhanschrift 15', bg='gray17', fg='aquamarine',
                                 command=loadsongs,
                                 activebackground='gray17', activeforeground='green', bd=0, compound=RIGHT)
            icons_image.place(x=10, y=y)
            y = y + 60

        elif option[i] == 'Download Songs':
            icons_image = Button(navroot, text=option[i], font='Bhanschrift 15', bg='gray17', fg='aquamarine',
                                 activebackground='gray17', activeforeground='green', bd=0, compound=RIGHT,command=download_song)
            icons_image.place(x=10, y=y)
            y = y + 60

        elif option[i] == 'PLay Online':
            icons_image = Button(navroot, text=option[i], font='Bhanschrift 15', bg='gray17', fg='aquamarine',
                                 activebackground='gray17', activeforeground='green', bd=0, compound=RIGHT,
                                 command=play_online_bar_visible)
            icons_image.place(x=10, y=y)
            y = y + 60

        ####### nav bar close button ################
        cancel_button = Button(navroot , bg='aquamarine', bd=0, image=cancel_image,
                               activebackground='aquamarine', command=switch)
        cancel_button.place(x=250, y=3)

        ############# VOLUME PROGRESS BAR ##################
    volume_progress_label = Label(volumecontrol, bg='navy', bd=4, width=5, height=23)
    volume_progress_label.grid(row=0, column=0, padx=4)

    progressbarvolume = Progressbar(volume_progress_label, orient=VERTICAL, mode='determinate', value=0, length=330)
    progressbarvolume.grid(row=0, column=0, ipadx=10)

    progressbarvolumelabel = Label(volume_progress_label, text='0%', bg='gray', width=3)
    progressbarvolumelabel.grid(row=0, column=0)

    ################## Button for audiocontrol frame  ######################

    previousbuttonorignal = Button(audiocontrol, image=previousbutton_image, relief=tkinter.GROOVE, width=200,
                                   bg='gray17', bd=8, borderwidth=0, activebackgroun='gray17', command=previous_song)

    previousbuttonorignal.grid(row=0, column=0, padx=1, pady=10)

    playbuttonorignal = Button(audiocontrol, image=playbutton_image, relief=tkinter.GROOVE, width=200, bg='gray17',
                               bd=8, borderwidth=0, activebackgroun='gray17', command=resumemusic_from_button)

    playbuttonorignal.grid(row=0, column=1, padx=1, pady=10)

    pausebuttonorignal = Button(audiocontrol, image=pausebutton_image, relief=tkinter.GROOVE, width=200, bg='gray17',
                                bd=8, activebackground='gray17', borderwidth=0, command=pausemusic)
    pausebuttonorignal.grid(row=0, column=1, padx=1, pady=10)
    pausebuttonorignal.grid_remove()

    nexbuttonorignal = Button(audiocontrol, image=next_image, relief=tkinter.GROOVE, width=180, bg='gray17',
                              bd=8, borderwidth=0, activebackgroun='gray17', command=next_song)

    nexbuttonorignal.grid(row=0, column=2, padx=1, pady=10)

    stopbuttonorignal = Button(audiocontrol, image=stopbutton_image, relief=tkinter.GROOVE, width=180, bg='gray17',
                               bd=8,
                               activebackground='gray17', borderwidth=0, command=stopmusic)
    stopbuttonorignal.grid(row=1, column=0, padx=1, pady=10)

    mutebuttonorignal = Button(audiocontrol, image=mutebutton_image, relief=tkinter.GROOVE, width=180, bg='gray17',
                               bd=8,
                               activebackground='gray17', borderwidth=0, command=mutemusic)
    mutebuttonorignal.grid(row=1, column=2, padx=1, pady=10)

    unmutebuttonorignal = Button(audiocontrol, image=unmutebutton_image, relief=tkinter.GROOVE, width=100, bg='gray17',
                                 bd=8,
                                 activebackground='gray17', borderwidth=0, command=unmutemusic)
    unmutebuttonorignal.grid(row=1, column=2, padx=1, pady=10)
    unmutebuttonorignal.grid_remove()

    volume_up_buttonorignal = Button(audiocontrol, image=volume_up_image, relief=tkinter.GROOVE, width=180, bg='gray17',
                                     bd=8,
                                     activebackground='gray17', borderwidth=0, command=volumeup)
    volume_up_buttonorignal.grid(row=2, column=0, padx=1, pady=10)

    volume_down_buttonorignal = Button(audiocontrol, image=volume_down_image, relief=tkinter.GROOVE, width=180,
                                       bg='gray17', bd=8,
                                       activebackground='gray17', borderwidth=0, command=volumedown)
    volume_down_buttonorignal.grid(row=2, column=2, padx=1, pady=10)

    ############### for playing online song ##############

    online_song_label = Label(navwithplaylist, bg='aquamarine', width=55, height=15, bd=5)
    online_song_label.place(x=10, y=483)

    onlineplaying_frame = LabelFrame(online_song_label, bg='gray17', text='ONLINE VIDEO PLAYER', bd=5,
                                     fg='aquamarine', font=('arial', 14, 'italic bold'), width=380, height=210)
    onlineplaying_frame.grid(row=0, column=0, padx=4, pady=4)

    text_label = Label(onlineplaying_frame, text='Enter Song Name :- ', bg='gray17', bd=6, width=15, height=1,
                       font=('arial', 15, 'italic bold'), fg='aquamarine')
    text_label.grid(row=0, column=0, pady=2)

    entry = Entry(onlineplaying_frame, bg='sky blue', bd=6,fg='navy', width=33, font=('arial', 12, 'italic bold'))
    entry.grid(row=1, column=0, padx=32)

    name_of_song = Button(onlineplaying_frame, bg='gray17', width=80, height=80, activebackground='gray17',
                          command=play_online,image=online_playing,borderwidth=0)
    name_of_song.grid(row=2, column=0, padx=20, pady=12)
    online_song_label.place_forget()

    ######################### for downloading the audio file from youtube ##############

    mp3_download_frame = Label(navwithplaylist, bg="aquamarine", bd=1, font=('arial ', 14, 'italic bold'), width=33,
                               height=28)
    mp3_download_frame.place(x=5, y=62)

    mp3_download_frame_label = LabelFrame(mp3_download_frame, bg="gray17", bd=6, text="MP3 DOWNLOAD ",
                                          font=('arial ', 14, 'italic bold'),
                                          width=385, height=640, fg='aquamarine')
    mp3_download_frame_label.grid(row=0, column=0, padx=6, pady=10)

    main_label = Label(mp3_download_frame_label, text='Enter The Url Of The Video', bg='gray17', bd=4,
                       font=('arial', 14, 'italic bold '), fg='aquamarine')
    main_label.grid(row=0, column=0, padx=55, pady=20)

    ytdEntryvar = StringVar()
    url_text = Entry(mp3_download_frame_label,bg='skyblue', bd=4, text=ytdEntryvar, font=('arial ', 14, 'italic bold')
                     , width=20,fg='navy')
    url_text.grid(row=1, column=0, padx=3, pady=15)

    ytdError = Label(mp3_download_frame_label, text=" ",bg='gray', fg='red', font=('arial', 13, 'italic bold '), width=20)
    ytdError.grid(row=2, column=0, padx=55, pady=20)

    location_label = Label(mp3_download_frame_label, text='Select The Location ', bg='gray17', bd=4,
                           font=('arial', 14, 'italic bold ')
                           , fg='aquamarine')
    location_label.grid(row=3, column=0, padx=20, pady=20)

    location_button = Button(mp3_download_frame_label, bg='gray17',font=('arial', 14, 'italic bold'), bd=7
                             , activebackground='gray17', command=openLocation,image=select_folder,borderwidth=0)
    location_button.grid(row=4, column=0, padx=55, pady=10)


    ytdlocationError = Label(mp3_download_frame_label, text="", fg='red', font=('arial', 13, 'italic bold '),
                             width=20,bg='gray')
    ytdlocationError.grid(row=5, column=0, padx=55, pady=20)


    ############### for downloading the audio dowloading button maken ##################################
    download_label = Label(mp3_download_frame_label, text='Download The Video File', bg='gray17', bd=4,
                           font=('arial', 14, 'italic bold '), fg='aquamarine')
    download_label.grid(row=6, column=0, padx=55, pady=20)

    download_button = Button(mp3_download_frame_label, bg='gray17',font=('arial', 14, 'italic bold'), bd=7,
                             activebackground='gray17',borderwidth=0,command=Downloadmp3,image=download_image_for_music)
    download_button.grid(row=7, column=0, padx=55, pady=10)
    mp3_download_frame.place_forget()

    ################### whatup audio sharing #############################

    whatup_frame_label=Label(navwithplaylist,bg='aquamarine',width=56,height=43)
    whatup_frame_label.place(x=10,y=60)

    whatup_audio_frame=LabelFrame(whatup_frame_label,text='SHARE MESSAGES',font=('arail',14,'bold'),bd=5,bg="gray17",fg='aquamarine',width=385,height=640)
    whatup_audio_frame.grid(row=0,column=0,padx=5,pady=5)


    whatup_number_label=Label(whatup_audio_frame,bg='gray17',width=30,height=3,
                              text="Enter Contact Number To Whom \n  You Want To Send  Message\nWith Country Code(+91) ", font=('arail',14,'italic bold')
                              ,fg='aquamarine')
    whatup_number_label.grid(row=0,column=0,padx=5,pady=5)


    contact_number=StringVar()

    whatup_number_entry=Entry(whatup_audio_frame,bg='sky blue',width=30,fg="navy",text=contact_number,font=('arial',15,' bold'))
    whatup_number_entry.grid(row=1,column=0,padx=5,pady=5)

    information_label=Label(whatup_audio_frame,bg='gray17',width=25,height=1,text="Enter Your Message  ",
                      font=('arail',15,'italic bold'),fg='aquamarine')
    information_label.grid(row=2,column=0,padx=5,pady=5)

    your_mess=StringVar()

    your_message=Entry(whatup_audio_frame,bg='sky blue',width=30,fg="navy",text=your_mess,font=('arial',15,' bold'))
    your_message.grid(row=3,column=0,padx=5,pady=5)

    hours_label=Label(whatup_audio_frame,bg='gray17',width=25,height=2,text="Enter Hours At Which\nYou Want To Send The Message",
                      font=('arail',15,'italic bold'),fg='aquamarine')
    hours_label.grid(row=4,column=0,padx=5,pady=10)

    hours=IntVar()

    gave_minute=Entry(whatup_audio_frame,bg='sky blue',width=30,fg="navy",text=hours,font=('arial',15,' bold'))
    gave_minute.grid(row=5,column=0,padx=5,pady=5)

    minute_label = Label(whatup_audio_frame, bg='gray17', width=25, height=2,
                         text="Enter Minute At Which\nYou Want To Send The Message",
                         font=('arail', 15, 'italic bold'), fg='aquamarine')
    minute_label.grid(row=6, column=0, padx=5, pady=10)

    minute=IntVar()

    gave_second=Entry(whatup_audio_frame,bg='sky blue',width=30,fg="navy",text=minute,font=('arial',15,' bold'))
    gave_second.grid(row=7,column=0,padx=5,pady=5)


    send_audio_label=Label(whatup_audio_frame,bg='gray17',width=30,height=3,text="Send Message",
                      font=('arail',14,'italic bold'),fg='aquamarine')
    send_audio_label.grid(row=8,column=0,padx=5,pady=5)

    send_song=Button(whatup_audio_frame,bg='gray17',text='Send Song',bd=6,font=('arial',14,'italic bold')
                     ,activebackground='gray17',image=send_audios,borderwidth=0,command=send_songs)
    send_song.grid(row=9,column=0,padx=5,pady=5)

    status_send_label=Label(whatup_audio_frame,bg='gray',width=25,height=1,text='',
                      font=('arail',14,'italic bold'),fg='aquamarine')
    status_send_label.grid(row=10,column=0,padx=5,pady=5)

    whatup_frame_label.place_forget()

root = Tk()

root.state('zoomed')
root.title("Simple Music PLayer ")
root.iconbitmap("music.ico")
root.resizable(False, False)
root.configure(bg='aquamarine')

create()
root.mainloop()