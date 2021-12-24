from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
import random


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
                button = tk.Button(self.win, text=arg[0], command=arg[1] )
                button.grid(row=i, column=0)
                i=i+1       
    def terminate(self):
        self.win.destroy()



def NumPick():
    mcol = ['white', 'black', 'blue', 'red', 'green', 'yellow', 'orange', 'purple']
    m0 = random.choice(mcol)
    m1 = random.choice(mcol)
    m2 = random.choice(mcol)
    m3 = random.choice(mcol)
    value = [m0, m1, m2, m3]
    return value


def maingame():
    intro.terminate()

    global root
    root = Window('Mastermind (C)2021 upatras All rights ', 'black', '#FFFFFF', None, '900x600')


    global color0, color1, color2, color3

    canvas = ImageTk.PhotoImage(Image.open('canvas.png'))
    lblcan = tk.Label(root.win, image=canvas)
    lblcan.place(relx=0.01, rely=0.085)
    
    colors = ('black', 'white', 'blue', 'red', 'yellow', 'green', 'orange', 'purple')
    color0 = ttk.Combobox(root.win, values = colors, width = 8)
    color0.place(relx=0.1, rely=0.9)
    color1 = ttk.Combobox(root.win, values = colors, width = 8)
    color1.place(relx=0.2, rely=0.9)
    color2 = ttk.Combobox(root.win, values = colors, width = 8)
    color2.place(relx=0.3, rely=0.9)
    color3 = ttk.Combobox(root.win, values = colors, width = 8)
    color3.place(relx=0.4, rely=0.9)
    okbut = tk.Button(root.win, text= 'Παίξε!', width=10, height=1, bg='blue', fg = 'white', command = checkinp).place(relx=0.5, rely=0.9)
    
    root.win.mainloop()
    
    startscreen() #Εμφ η αρχ οθονη οταν πατω Χ

counter=0
if counter==0 : randomcolors=NumPick()

def checkinp():
    global counter
    
    Li = [color0.get(), color1.get(), color2.get(), color3.get()]

    
    b1 = ImageTk.PhotoImage(Image.open('b1.png'))
    lb1 = tk.Label(root.win, image=b1)
    lb1.place(relx=0.1  , rely= (47*(9.4-counter))/600)

    b2 = ImageTk.PhotoImage(Image.open('b2.png'))
    lb2 = tk.Label(root.win, image=b2)
    lb2.place(relx=0.2  , rely= (47*(9.4-counter))/600)

    b3 = ImageTk.PhotoImage(Image.open('b3.png'))
    lb3 = tk.Label(root.win, image=b3)
    lb3.place(relx=0.3  , rely= (47*(9.4-counter))/600)

    b4 = ImageTk.PhotoImage(Image.open('b4.png'))
    lb4 = tk.Label(root.win, image=b4)
    lb4.place(relx=0.4  , rely= (47*(9.4-counter))/600)
    
    print(randomcolors)
    for i in range(4):
        if Li[i] == randomcolors[i]:
            print("RED")
        if Li[i] in randomcolors and Li[i] != randomcolors[i]:
            print("WHITE")
    
    counter=counter+1
    if counter>10:
        root.terminate()
        counter=0
        go = Window('Game Over', "black", 'white', None, '400x100', 'Game Over!!')
        go.win.mainloop()
        

def startscreen():
    global intro
    intro = Window('Καλώς ορίσατε στό Mastermind', None, 'white', 'background.png', '400x300')

    lab0 = tk.Label(intro.win, text = "Mastermind", bg="black", fg='white', font=('Times New Roman','23'), padx='20', pady='0')
    lab0.grid(row=0, column=1)
    lab1 = tk.Label(intro.win, text = 'Ας παίξουμε ένα παιχνίδι Mastermind!\nΤο πρόγραμμα θα επιλέξει έναν συνδυασμό\n4 χρωμάτων και εσύ έχεις 10 ευκαιρίες να τον μαντέψεις!', bg='#000000', fg='#999999', font = ('Helvetica', '12'), padx='10', pady='10')
    lab1.grid(row=1, column=1)

    butintro1 = tk.Button(intro.win, text='1 παίκτης - Αυτόματη επιλογή κωδικού', bg='brown', fg='white', height='1', width='50', command= maingame )
    butintro1.grid(row=2, column=1)
    butintro2 = tk.Button(intro.win, text='2 παίκτες - Παιχνίδι μέσω LAN', bg='brown', fg='white', height='1', width='50', command= NumPick )
    butintro2.grid(row=3, column=1)
    butintro3 = tk.Button(intro.win, text='Ρυθμίσεις', bg='brown', fg='white', height='1', width='25', command= NumPick )
    butintro3.grid(row=5, column=1)
    butintro4 = tk.Button(intro.win, text='Περί', bg='brown', fg='white', height='1', width='25', command= NumPick )
    butintro4.grid(row=6, column=1)
    butintro5 = tk.Button(intro.win, text='Προβολή -Διαγραφh σκορ', bg='brown', fg='white', height='1', width='25', command= intro.terminate )
    butintro5.grid(row=7, column=1)



    intro.win.mainloop()

#####          Το πρόγραμμα αρχίζει εδώ

if __name__ == "__main__":
    startscreen()

