from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
import random
import datetime
import os

### ΚλΑΣΗ ΠΟΥ ΔΗΜ/ΓΕΙ ΠΑΡΑΘΥΡΑ. δΕΝ ΤΗΝ ΠΕΙΡΑΖΟΥΜΕ (ΕΚΤΟΣ ΑΝ ΧΡΕΙΑΣΤΕΙ ΝΑ ΕΙΣΑΓΟΥΜΕ FRAME)

class Window():
    def __init__(self, title, bgcolor, fgcolor, imagefile, size, *msgargs):
        self.win = tk.Tk()
        self.win.configure(bg = bgcolor)
        self.win.title(title)
        self.win.geometry(size)
        self.win.resizable(0,0)
        
        if imagefile != None:
            img = ImageTk.PhotoImage(Image.open(imagefile).resize((int(size.split("x")[0]), int(size.split("x")[1])), Image.ANTIALIAS))
            lbl = tk.Label(self.win, image=img)
            lbl.img = img  # Keep a reference in case this code put is in a function.
            lbl.place(relx=0.5, rely=0.5, anchor='center')
        if len(msgargs) > 0:
            label = tk.Label(self.win, text = msgargs[0], bg=bgcolor, fg=fgcolor, font = ('Arial', '12'), padx='10', pady='10', wraplength=int(size.split("x")[0])-30, justify="center")
            label.grid(row=0, column=0)
            i=1
            for arg in msgargs[1:]:
                button = tk.Button(self.win, text=arg[0], command=arg[1])
                button.grid(row=i, column=0)
                i=i+1


def NumPick():
    if players == 1:
        Listofcolors = [random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)]
        while True:
            if len(Listofcolors) == len(set(Listofcolors)):
                return Listofcolors
            else: Listofcolors = [random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)]
    if players == 2:
        return [color0u.get(), color1u.get(), color2u.get(), color3u.get()]


def maingame():
    intro.win.destroy()
    global root
    root = Window('Mastermind (C)', bgcolor, fgcolor, None, '700x800', 'Παίζει ο παίκτης: {0} :: Ημ/νία: {1}. Επιλέξτε τα χρώματα απο τα combo box'.format(playername[rounds%2], datetime.datetime.now().strftime('%d-%m-%y')))


    global color0, color1, color2, color3, randomcolors, gamecanvas

    gamecanvas = tk.Canvas(root.win, height=660, width=480)
    gamecanvas.place(relx=0.1, rely=0.045)
    canvimg = ImageTk.PhotoImage(Image.open('MastermindTemplate1.1.jpg'))
    gamecanvas.create_image(243, 330, image=canvimg)

    if counter==0 : randomcolors=NumPick()
    
    color0 = ttk.Combobox(root.win, values = colors, width = 7)
    color0.place(relx=0.1, rely=0.9)
    color1 = ttk.Combobox(root.win, values = colors, width = 7)
    color1.place(relx=0.196, rely=0.9)
    color2 = ttk.Combobox(root.win, values = colors, width = 7)
    color2.place(relx=0.292, rely=0.9)
    color3 = ttk.Combobox(root.win, values = colors, width = 7)
    color3.place(relx=0.388, rely=0.9)
    okbut = tk.Button(root.win, text= 'Παίξε!', width=10, height=1, bg='blue', fg = 'white', command = checkinp).place(relx=0.5, rely=0.9)
    
    root.win.mainloop()
    
    startscreen() #Εμφανιζεται η αρχικη οθονη οταν πατω Χ


def check2player():
    if '' in [color0u.get(), color1u.get(), color2u.get(), color3u.get()]:
        msg=Window('Error', bgcolor, fgcolor, None, '200x140', 'Πρεπει να επιλέξεις καποιο χρώμα! Δεν μπορεί να ναι κενο', ('Help', about), ('Send Feedback', about))
    elif len([color0u.get(), color1u.get(), color2u.get(), color3u.get()]) != len(set([color0u.get(), color1u.get(), color2u.get(), color3u.get()])):
        msg=Window('Error', bgcolor, fgcolor, None, '300x140', 'Στο mastermind ο κωδικος αποτελείται απο διαφορετικα χρωματα', ('Help', about), ('Send Feedback', about))
    else:
        maingame()
def twoplayers():
    global colorinit, players
    colorinit = Window('Color selector', bgcolor, fgcolor, None, '500x200', 'Είσαι ο παίκτης 2. Παρακαλώ επέλεξε τον μυστικο κωδικό με χρώματα που πρέπει να μαντέψει ο άλλος παίκτης. Στη συνέχεια πάτησε "Επιλογή κωδικού" και κλείσε το παραθυρο.')
    global color0u, color1u, color2u, color3u
    color0u = ttk.Combobox(colorinit.win, values = colors, width = 8)
    color0u.place(relx=0.1, rely=0.5)
    color1u = ttk.Combobox(colorinit.win, values = colors, width = 8)
    color1u.place(relx=0.3, rely=0.5)
    color2u = ttk.Combobox(colorinit.win, values = colors, width = 8)
    color2u.place(relx=0.5, rely=0.5)
    color3u = ttk.Combobox(colorinit.win, values = colors, width = 8)
    color3u.place(relx=0.7, rely=0.5)
    okbut = tk.Button(colorinit.win, text= 'Επιλογή κωδικού!', width=20, height=1, bg='green', fg = 'white', command = check2player).place(relx=0.1, rely=0.8)
    players=2
    colorinit.win.mainloop()
  
def alternatingplayers():
    global rounds
    rounds=rounds+1
    maingame()

def checkinp():
    global counter, players
    
    Li = [color0.get(), color1.get(), color2.get(), color3.get()]
    outputcolors = []
    if '' in Li:
        msg=Window('Error', bgcolor, fgcolor, None, '200x140', 'Πρεπει να επιλέξεις καποιο χρώμα! Δεν μπορεί να ναι κενο', ('Help', about), ('Send Feedback', about))
        if music=='YES': playsound.playsound('sound6.wav', False)
    elif len(Li) != len(set(Li)):
        msg=Window('Error', bgcolor, fgcolor, None, '300x140', 'Στο mastermind ο κωδικος αποτελείται απο διαφορετικα χρωματα', ('Help', about), ('Send Feedback', about))
        if music=='YES': playsound.playsound('sound6.wav', False)

    elif '' not in Li:
        l=0
        for color in Li:
            ball = gamecanvas.create_oval((l+1)*19+l*46, (counter+1)*17+counter*47.5, (l+1)*19+l*46+46, (counter+1)*17+counter*47.5+46, fill=colorhexvals[color])
            l=l+1
        print(randomcolors, players, counter)
        for i in range(4):
            if Li[i] == randomcolors[i]:
                outputcolors.append('RED')
            if Li[i] in randomcolors and Li[i] != randomcolors[i]:
                outputcolors.append('WHITE')
        j=0
        for output in outputcolors:
            if output == 'RED':
                ball2 = gamecanvas.create_oval(323+j*32.3, 26.3+counter*65, 346.5+j*32.3, 49.8+counter*65, fill='red')
            if output == 'WHITE':
                ball2 = gamecanvas.create_oval(323+j*32.3, 26.3+counter*65, 346.5+j*32.3, 49.8+counter*65, fill='white')
            if output == '' or output == None:
                pass
            j=j+1
            
        print(outputcolors)
        if outputcolors == ['RED', 'RED', 'RED', 'RED']:
            filesc=open('SETTINGS.txt', 'a', encoding='UTF-8')
            filesc.write(datetime.datetime.now().strftime('%d - %m - %y  --> Παίκτης ') + playername[rounds%2] +' - '+ str(counter) + ' Προσπάθειες \n' )                                                                                      #να βαλουμε και ημερομηνια -ωρα
            filesc.close()
            root.win.destroy()
            go = Window('Game Over', bgcolor, fgcolor, None, '400x100', 'Συγχαρητήρια! Κέρδισες. \nΜπορείς να δείς το αναλυτικό σκορ σου στην καρτέλλα "Προβολή-Διαγραφή σκορ"')
        counter=counter+1
        if music=='YES': playsound.playsound('sound1.wav', False)
        
    if counter>10:
        root.win.destroy()
        filesc=open('SETTINGS.txt', 'a', encoding='UTF-8')   #NA balv to encoding!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        filesc.write('{}  {}  - Αποτυχία\n '.format(str(datetime.datetime.now().strftime('%d - %m - %y  --> Παίκτης ')), playername[rounds%2]))        #να βαλουμε και ημερομηνια -ωρα
        filesc.close()
        counter=0
        players=1
        go = Window('Game Over', bgcolor, fgcolor, None, '400x100', f'Game Over!! Ο συνδυασμός ήτανε: \n {randomcolors}')
        go.win.mainloop()
        
##  ΑΥΤΟ ΤΟ ΚΟΜΜΑΤΙ ΚΩΔΙΚΑ ΕΙΝΑΙ ΟΚ ##

def writetofile(bgcolor, fgcolor, player, deletescore):
    newfile = open('SETTINGS.txt', 'w', encoding='UTF-8')
    if bgcolor != '' or fgcolor != '' or player != ['','']:
        newfile.write('CONFIGURED\n')
        newfile.write(f'{fgcolor}\n')
        newfile.write(f'{bgcolor}\n')
        newfile.write(f'{player[0]}\n')
        newfile.write(f'{player[1]}\n')
        newfile.write(f'{lines[5]}\n')
    if deletescore == True:
        newfile.write(''.join(lines[:6]))
        newfile.close()
    elif deletescore == False:
        newfile.write(''.join(lines[6:]))
        newfile.close()
def applysettings():
    theme = themecombo.get()
    if theme == 'Λευκό': bgcolor, fgcolor = '#FFFFFF', '#000000'
    if theme == 'Μαύρο': bgcolor, fgcolor = '#000000', '#FFFFFF'
    if theme == 'Πράσινο': bgcolor, fgcolor = '#003301', '#FFFF66'
    else: pass
    writetofile(bgcolor, fgcolor, [textbox.get(), textbox2.get()], False)
def delscore(): writetofile('', '', ['', ''], True)
def settings():
    global themecombo, textbox, textbox2, colqcheck, var
    setdialog = Window('Ρυθμίσεις', bgcolor, fgcolor, None, '400x300', 'Για να καταχωρηθούν οι αλλαγές, πατήστε Εφαρμογή και επανεκκινήστε το παιχνίδι', ('Εφαρμογή', applysettings))
    themecombo = ttk.Combobox(setdialog.win, values=('Λευκό', 'Μαύρο', 'Πράσινο'), width=12)
    themecombo.place(relx = 0.1, rely = 0.4)
    themecombo.set("Λευκό")
    textbox = tk.Entry(setdialog.win, width=15)
    textbox.place(relx = 0.1, rely = 0.5)
    textbox2 = tk.Entry(setdialog.win, width=15)
    textbox2.place(relx = 0.1, rely = 0.6)
    checkbox = tk.Checkbutton(setdialog.win, variable=music, onvalue='YES', offvalue='NO')
    checkbox.place(relx=0.1, rely=0.7)
    label = tk.Label(setdialog.win, text="Επιλογή Θέματος", bg=bgcolor, fg=fgcolor)
    label.place(relx=0.4, rely=0.4)
    label = tk.Label(setdialog.win, text="Oνομα πρωτεύοντος παίκτη", bg=bgcolor, fg=fgcolor)
    label.place(relx=0.4, rely=0.5)
    label = tk.Label(setdialog.win, text="Oνομα δευτερεύοντος παίκτη", bg=bgcolor, fg=fgcolor)
    label.place(relx=0.4, rely=0.6)
    label = tk.Label(setdialog.win, text="Μουσική - Ήχος ON/OFF", bg=bgcolor, fg=fgcolor)
    label.place(relx=0.4, rely=0.7)

    
def about():                                                      ### ΕΔΩ ΘΑ ΒΑΛΟΥΜΕ ΤΑ ΟΝΟΜΑΤΑ ΜΑΣ
    aboutdialog = Window('Πανεπιστήμιο Πατρών 2021',bgcolor, fgcolor, None, '400x400', 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
    
def showscore():
    file = open('SETTINGS.txt', 'r', encoding='UTF-8')
    text = ''.join(file.readlines()[6:]).rstrip()
    scoredialog = Window('Διαχείριση Σκόρ', bgcolor, fgcolor, None, '400x600', text, ('Εκκαθάριση όλων', delscore))
    file.close()
    

#######################################
###  ΤΟ ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ              ###
###  ΑΚΟΛΟΥΘΕΙ Η ΣΥΝΑΡΤΗΣΗ ΜΑΙΝGAME ###
#######################################

def startscreen():
    global intro, counter, players
    counter=0
    players=1
    counter=0
    intro = Window('Καλώς ορίσατε στό Mastermind', None, 'white', 'background.png', '400x300')

    lab0 = tk.Label(intro.win, text = "Mastermind", bg='#000000', fg='#ffffff', font=('Times New Roman','23'), padx='20', pady='0')
    lab0.grid(row=0, column=1)
    lab1 = tk.Label(intro.win, text = 'Ας παίξουμε ένα παιχνίδι Mastermind!\nΤο πρόγραμμα θα επιλέξει έναν συνδυασμό\n4 χρωμάτων και εσύ έχεις 10 ευκαιρίες να τον μαντέψεις!', bg='#000000', fg='#999999', font = ('Helvetica', '12'), padx='10', pady='10')
    lab1.grid(row=1, column=1)

    butintro1 = tk.Button(intro.win, text='1 παίκτης - Αυτόματη επιλογή κωδικού', bg='brown', fg='white', height='1', width='50', command= maingame )
    butintro1.grid(row=2, column=1)
    butintro2 = tk.Button(intro.win, text='2 παίκτες - Χειρ/τη επιλογή κωδικού', bg='brown', fg='white', height='1', width='50', command= twoplayers )
    butintro2.grid(row=3, column=1)
    butintro6 = tk.Button(intro.win, text='2 παίκτες εναλλάξ', bg='brown', fg='white', height='1', width='50', command= alternatingplayers )
    butintro6.grid(row=4, column=1)
    butintro3 = tk.Button(intro.win, text='Ρυθμίσεις', bg='brown', fg='white', height='1', width='25', command= settings )
    butintro3.grid(row=5, column=1)
    butintro4 = tk.Button(intro.win, text='Περί', bg='brown', fg='white', height='1', width='25', command= about)
    butintro4.grid(row=6, column=1)
    butintro5 = tk.Button(intro.win, text='Προβολή -Διαγραφh σκορ', bg='brown', fg='white', height='1', width='25', command= showscore)
    butintro5.grid(row=7, column=1)
    if music=='YES': playsound.playsound('sound11.mp3', False)
    intro.win.mainloop()



#####################################################
#####        Το πρόγραμμα αρχίζει εδώ          ######
#####################################################
    
colors = ('Μαύρο', 'Άσπρο', 'Μπλε', 'Κόκκινο', 'Κίτρινο', 'Πράσινο', 'Πορτοκαλί', 'Μωβ')
colorhexvals = {'Μαύρο':'#000000', 'Άσπρο':'#FFFFFF', 'Μπλε':'#0000FF', 'Κόκκινο':'#FF0000', 'Κίτρινο':'#FFFF00', 'Πράσινο':'#00FF00', 'Πορτοκαλί':'#FFA500', 'Μωβ':'#7F00FF'}
rounds=0
playername=['', '']
try:
    file = open('SETTINGS.TXT', 'r', encoding='UTF-8')
    lines=file.readlines()
    if lines[0] != 'CONFIGURED\n':
        os.system("MODE 1000")
        os.system("pip install pillow")                                         ### ΑΥΤΟΜΑΤΟΠΟΙΗΜΕΝΗ ΕΓΚΑΤΑΣΤΑΣΗ ΒΙΒΛΙΟΘΗΚΩΝ. ΘΑ ΒΑΛΟΥΜΕ ΚΑΙ ΗΧΗΤΙΚΑ ΕΦΦΕ
        os.system("pip install playsound==1.2.2")
        file.close()
        with open('SETTINGS.TXT', 'w', encoding='UTF-8') as file:
            file.write('CONFIGURED\n#000000\n#FFFFFF\nPlayer1\nPlayer2\nYES\n')
        a=Window('Αυτόματη εγκατάσταση απαραίτητων αρθρωμάτων','white', 'black', None, '500x150', 'Παρακαλώ επανεκκινείστε το προγραμμα. Εαν αντιμετωπίζετε καποιο προβλημα, εγκαταστήστε τα modules: pillow & playsound. \nΚαλή διασκέδαση!!')
        a.win.mainloop()
    else:
        fgcolor = lines[1].rstrip()
        bgcolor = lines[2].rstrip()
        playername[0] = lines[3].rstrip()
        playername[1] = lines[4].rstrip()
        music = lines[5].rstrip()
        file.close()
        import playsound
        startscreen()
except FileNotFoundError:
    file=open('SETTINGS.TXT', 'w', encoding='UTF-8')
    file.write('Empty')
    file.close()
    a=Window('Αυτόματη εγκατάσταση απαραίτητων αρθρωμάτων','white', 'black', None, '500x150', 'Δημιουργήθηκε αρχείο στο οποίο αποθηκεύονται οι ρυθμίσεις και το σκορ. Παρακαλώ επανεκκινείστε το προγραμμα')
    a.win.mainloop()
