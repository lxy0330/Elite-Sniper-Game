import time
import tkinter as tk
import tkinter.font as tkFont
import PIL
from PIL import ImageTk
import random
import pygame

pygame.mixer.init()
reload_sound = pygame.mixer.Sound("music/reload.wav")
thunder_sound = pygame.mixer.Sound("music/thunderstorm.wav")
gamer_sound = pygame.mixer.Sound("music/gamer.wav")
shoot_sound = pygame.mixer.Sound("music/shoot_sound.wav")
mission_sound = pygame.mixer.Sound("music/mission_complete.wav")

mission_fail = pygame.mixer.Sound("music/endgame.wav")
yell_sound = pygame.mixer.Sound("music/yell.wav")
glass_sound = pygame.mixer.Sound("music/glass_break.wav")

easyname = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
hardname = []
citizen_filename = ["citizens01.png","citizens02.png","citizens03.png","citizens04.png","citizens05.png","citizens06.png","citizens07.png","citizens08.png","citizens09.png","citizens10.png","citizens11.png"]
citizen_name = []

president_name = ""
terrorist_name = ""

t1man_pic = "t1"
t2man_pic = "t2"

file1 = open("txt/EnglishName.txt", "r")
for i in file1:
    word = i.strip()
    hardname.append(word)
file1.close()

storerecord = []  # 存開始的瞬間最高紀錄
top = 0  # 存遊戲開始時的最高紀錄
originmax = 0

typecode = []
location = [[68,180],[281,180],[492,180],[705,180],[917,180], [70,430], [281,430], [492,430], [705,430], [917,430]] #y-25
random.shuffle(location)
random.shuffle(easyname)
random.shuffle(hardname)
random.shuffle(citizen_filename)

gamemode_hard = False
gamemode_crazy = False
citizen_name
number = 0
t = 10
virus = False
stopvirus = False
presidentdie = False

# 雙人遊戲設定
t1_code = ["t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o"]
t2_code = ["q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v"]
in_t1 = []
in_t2 = []
empty = ""
t1_people = 4
t2_people = 4
random.shuffle(t1_code)
random.shuffle(t2_code)

pygame.mixer.init()
shoot_sound2 = pygame.mixer.Sound("music/shoot_sound2.wav")
yell_sound2 = pygame.mixer.Sound("music/yell2.wav")
mission_sound2 = pygame.mixer.Sound("music/mission_complete2.wav")


class menu(tk.Frame):# 遊戲開始頁面

    def __init__(self):
        global gamemode_hard, gamemode_crazy, presidentdie
        gamemode_hard = False
        gamemode_crazy = False
        self.has_played_menu_music = False
        presidentdie = False
        tk.Frame.__init__(self)
        typecode = []
        self.grid()
        self.place()
        self.menu_pic = ImageTk.PhotoImage(file = "background_pic/menu1.png")
        self.gamerule_pic = ImageTk.PhotoImage(file = "background_pic/gamerule.png")
        self.gamerule2p_pic = ImageTk.PhotoImage(file = "background_pic/gamerulefor2.png")
        self.producer_pic = ImageTk.PhotoImage(file = "background_pic/producer.png")

        self.createMenuWidget()

        self.stop = mission_sound.stop()
        self.stop2 = thunder_sound.stop()
        self.play = thunder_sound.play()

        self.stop3 = gamer_sound.stop()
        self.stop4 = mission_sound.stop()
        self.stop5 = mission_fail.stop()

        self.stop6 = mission_sound2.stop()

    def createMenuWidget(self): # 初始選單

        global virus, storerecord

        if self.has_played_menu_music == False:
            self.play = thunder_sound.play()

        file2 = open("txt/max.txt", "r")
        storerecord = []
        for i in file2:
            record = i.strip()
            record = int(record)
            storerecord.append(record)
        file2.close()
        f2 = tkFont.Font(size = 20, family = "Courier New")

        self.menu_image = tk.Label(self,image = self.menu_pic, compound = tk.CENTER)
        self.menu_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.StartBtn = tk.Button(self, text = "Start", font = f2, height = 1, width = 14 ,fg = "White", bg = "#614a3e", activeforeground = "White",activebackground = "Gray",command = self.createGamemodeWidget)
        self.StartBtn.place(x = 1150, y = 300)
        self.Gamerule = tk.Button(self, text = "GameRule", height = 1, width = 14, font = f2,fg = "White", bg = "#614a3e" ,activeforeground = "White",activebackground = "Gray",command = self.createGameruleWidget)
        self.Gamerule.place(x = 1150, y = 400)
        self.Gamerule2p = tk.Button(self, text = "2p GameRule", height = 1, width = 14, font = f2,fg = "White", bg = "#614a3e" ,activeforeground = "White",activebackground = "Gray",command = self.createGamerule2pWidget)
        self.Gamerule2p.place(x = 1150, y = 500)
        self.Producer = tk.Button(self, text = "Producer", height = 1, width = 14, font = f2,fg = "White", bg = "#614a3e" ,activeforeground = "White",activebackground = "Gray",command = self.createProducerWidget)
        self.Producer.place(x = 1150, y = 600)
        virus = False

    def createGameruleWidget(self):
        self.has_played_menu_music = True
        f2 = tkFont.Font(size = 20, family = "Courier New")
        self.gamerule_image = tk.Label(self,image = self.gamerule_pic, compound = tk.CENTER)
        self.gamerule_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.Back2 = tk.Button(self, text = "Back" , height = 1, width = 8, font = f2, activeforeground = "White", activebackground = "Gray", command = self.createMenuWidget)
        self.Back2.place(x = 1120 , y = 680)
        self.play = reload_sound.play()

    def createGamerule2pWidget(self):
        self.has_played_menu_music = True
        f2 = tkFont.Font(size = 13, family = "Courier New")
        self.gamerule2p_image = tk.Label(self,image = self.gamerule2p_pic, compound = tk.CENTER)
        self.gamerule2p_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.Back2 = tk.Button(self, text = "Back" , height = 1, width = 8, font = f2, activeforeground = "White", activebackground = "Gray", command = self.createMenuWidget)
        self.Back2.place(x = 360 , y = 455)
        self.play = reload_sound.play()

    def createProducerWidget(self):
        self.has_played_menu_music = True
        f2 = tkFont.Font(size = 20, family = "Courier New")
        self.producer_image = tk.Label(self,image = self.producer_pic, compound = tk.CENTER)
        self.producer_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.Back3 = tk.Button(self, text = "Back" , height = 1, width = 8, font = f2, activeforeground = "White", activebackground = "Gray", command = self.createMenuWidget)
        self.Back3.place(x = 320 , y = 680)
        self.play = reload_sound.play()

    def createGamemodeWidget(self): # 遊戲模式選單
        f2 = tkFont.Font(size = 20, family = "Courier New")
        self.play = reload_sound.play()
        self.menu_image = tk.Label(self,image = self.menu_pic, compound = tk.CENTER)
        self.menu_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.EasyBtn = tk.Button(self, text = "Easy", height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.easygame)
        self.EasyBtn.place(x = 1150, y = 100)
        self.HardBtn = tk.Button(self, text = "Hard" , height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.hardgame)
        self.HardBtn.place(x = 1150, y = 200)
        self.CrazyBtn = tk.Button(self, text = "Crazy" , height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.crazygame)
        self.CrazyBtn.place(x = 1150, y = 300)
        self.VirusBtn = tk.Button(self, text = "Turmoil" , height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.virusmode)
        self.VirusBtn.place(x = 1150, y = 400)
        self.CrazyBtn = tk.Button(self, text = "2-Player" , height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.twoplayer)
        self.CrazyBtn.place(x = 1150, y = 500)
        self.Back = tk.Button(self, text = "Back" , height = 1, width = 14, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.back)
        self.Back.place(x = 1150 , y = 600)

    def back(self):
        self.has_played_menu_music = True
        self.createMenuWidget()

    def easygame(self): # 簡單模式初始設定
        global easyname, typecode, t, storerecord, top, originmax
        typecode = []
        t = 10
        top = storerecord[0]
        originmax = storerecord[0]
        for i in range(len(easyname)):
            typecode.append(easyname[i])
        self.play = reload_sound.play()
        self.stop = thunder_sound.stop()
        self.after(1400,menu.destroy(self))
        gamer()


    def hardgame(self):# 困難模式初始設定
        global hardname, typecode, t, gamemode_hard, storerecord, top, originmax
        typecode = []
        for i in range(len(hardname)):
            typecode.append(hardname[i])
        t = 20
        top = storerecord[1]
        originmax = storerecord[1]
        gamemode_hard = True

        self.play = reload_sound.play()
        self.stop = thunder_sound.stop()
        self.after(1400,menu.destroy(self))
        gamer()

    def crazygame(self):
        global easyname, typecode, gamemode_crazy, gamemode_hard, t, storerecord, top, originmax
        top = storerecord[2]
        originmax = storerecord[2]
        typecode = []
        for i in range(100):
            word = ""
            rnd = random.randint(7,9)
            for j in range(rnd):
                k = random.randint(0,25)
                word += easyname[k]
            typecode.append(word)
        t = 30

        gamemode_crazy = True
        gamemode_hard = True
        self.play = reload_sound.play()
        self.stop = thunder_sound.stop()
        self.after(1400,menu.destroy(self))
        gamer()

    def twoplayer(self):

        self.play = reload_sound.play()
        self.stop = thunder_sound.stop()
        self.after(1400,menu.destroy(self))
        two_player()


    def virusmode(self):  # 增加病毒模式
        global virus

        if virus == False:
            self.VirusBtn.configure(bg = "Red")
            virus = True
        else:
            self.VirusBtn.configure(bg = '#614a3e')
            virus = False

        self.play = reload_sound.play()



class mission_complete(tk.Frame):# 遊戲結算頁面

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.end_pic = ImageTk.PhotoImage(file = "background_pic/end.png")
        self.fail_pic = ImageTk.PhotoImage(file = "background_pic/jail_resized.png")
        self.createEndWidget()

        self.stop = gamer_sound.stop()

    def createEndWidget(self):
        global presidentdie

        file2 = open("txt/max.txt", "w")  # 把新的歷史紀錄寫入檔案
        file2.truncate()
        if gamemode_crazy is True:
            file2.write(str(storerecord[0])+"\n")
            file2.write(str(storerecord[1])+"\n")
            file2.write(str(top)+"\n")
        elif gamemode_hard is True:
            file2.write(str(storerecord[0])+"\n")
            file2.write(str(top)+"\n")
            file2.write(str(storerecord[2])+"\n")
        else:
            file2.write(str(top)+"\n")
            file2.write(str(storerecord[1])+"\n")
            file2.write(str(storerecord[2])+"\n")
        file2.close()

        if presidentdie == True:
            self.play = mission_fail.play()
            f1 = tkFont.Font(size = 30, family = "Courier New", weight = "bold")
            self.end_image = tk.Label(self,image = self.fail_pic, compound = tk.CENTER)
            self.end_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
            self.EndBtn_pic = ImageTk.PhotoImage(file='endbtn.png')
            self.Back = tk.Button(self, text = "Escape" , height = 1, width = 16, font = f1, activeforeground = "White", activebackground = "Gray", command = self.back_to_menu)
            self.Back.place(x = 550 , y = 700)


            if number > originmax:  #破紀錄顯示
                self.show = tk.Label(self, text = "New Record! But does it mean anything?", fg = "red", bg = "DarkGoldenrod2",height = 1, width = 40, font = f1)
                self.show.place(x = 315, y = 100)

            if number <= 1:  # 標示你成功次數
                self.show = tk.Label(self, text = "You succeeded %d time, but tou killed the mayor. \n Therefore, you suck! You such a loser.\n And you are in the jail"%number, fg = "white", bg = "slate gray",  height = 3, width = 50, font = f1)
                self.show.place(x = 150, y = 160)
            else:
                self.show = tk.Label(self, text = "You succeeded %d time, but tou killed the mayor. \n Therefore, you suck! You such a loser. \n And you are in the jail"%number, fg = "white", bg = "slate gray", height = 3, width = 50, font = f1)
                self.show.place(x = 150, y = 160)
        else:
            self.play2 = mission_sound.play()
            f1 = tkFont.Font(size = 30, family = "Courier New")
            self.end_image = tk.Label(self,image = self.end_pic, compound = tk.CENTER)
            self.end_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
            self.EndBtn_pic = ImageTk.PhotoImage(file='endbtn.png')
            self.EndBtn = tk.Button(self, image =self.EndBtn_pic , padx = 0, pady = 0, highlightthickness = 0, compound = tk.CENTER, borderwidth = 0,  relief = "flat",command = self.back_to_menu)
            self.EndBtn.place(x = 1200, y = 720)
            self.play = mission_sound.play()

            if number > originmax:  #破紀錄顯示
                self.show = tk.Label(self, text = "New Record!", fg = "red", bg = "yellow", height = 1, width = 30, font = f1)
                self.show.place(x = 315, y = 300)

            if number <= 1:  # 標示你成功次數
                self.show = tk.Label(self, text = "You succeeded %d time"%number, bg = "#6f645d" , fg = "White", height = 1, width = 30, font = f1)
                self.show.place(x = 300, y = 500)
            else:
                self.show = tk.Label(self, text = "You succeeded %d times"%number, bg = "#6f645d" , fg = "White", height = 1, width = 30, font = f1)
                self.show.place(x = 300, y = 500)

    def back_to_menu(self):
        global t, number

        number = 0
        gamemode_hard = False
        gamemode_crazy = False
        t = 10
        virus = False
        stopvirus = False
        presidentdie = False
        self.after(1500,mission_complete.destroy(self))
        menu()

class gamer(tk.Frame):# 遊戲主程式/主畫面

    def __init__(self):

        tk.Frame.__init__(self)
        self.grid()
        self.settimer()
        self.bg_pic = ImageTk.PhotoImage(file = "background_pic/background.png")
        self.tomb_pic = ImageTk.PhotoImage(file = "window_pic/tomb_window.png")
        self.crack_pic = ImageTk.PhotoImage(file = "window_pic/shattered_window.png") # 窗戶破掉的照片
        self.closedwindow_pic = Image.PhotoImage(file = "window_pic/dark_window.png")
        self.has_shooted = False
        self.createWidgets()


    holdup = True

    def settimer(self):
        global t

        f3 = tkFont.Font(size = 48, family = "Courier New")
        self.lblNum = tk.Label(self, text = t , height = 1, width = 5, font = f3, bg = "#6f645d" , fg = "White", relief = "raised")
        self.lblNum.place(x = 50, y = 50)
        if t > 0.00:
            self.lblNum.configure(text ="%0.2f" % t)
            if number < 2:  # 根據射擊次數調整時間快慢(可能每台電腦要調的t的參數會不太一樣)
                t -= 0.01
                if t < 0.00:
                    t = 0.00
            elif number < 4:
                t -= 0.015
                if t < 0:
                    t = 0.00
            else:
                t -= 0.03
                if t < 0.00:
                    t = 0.00
            t = round(t,2)
            if self.holdup == True:
                self.after(7, self.settimer)
            else:
                self.after(3200, self.settimer)
                self.holdup = True

        else:
            self.after(500, self.finishgame)


    def virus(self):
        global stopvirus, virus, typecode, location

        random.shuffle(location)
        random.shuffle(typecode)
        self.citizen_name.clear()

        if stopvirus == True:
            stopvirus = False
            return

        for i in range(10):
            self.unit[i].place(x = location[i][0], y = location[i][1])

        self.unit[0].place(x = location[0][0], y = location[0][1]) #原為12/26
        self.president_type.configure(text = typecode[0])
        self.president_type.place(x = location[0][0]+2, y = location[0][1]+157)
        self.president_name = typecode[0]

        self.unit[1].place(x = location[1][0], y = location[1][1])
        self.terrorist_type.configure(text = typecode[1])
        self.terrorist_type.place(x = location[1][0]+2, y = location[1][1]+157)
        self.terrorist_name = typecode[1]

        self.unit[2].place(x = location[2][0], y = location[2][1])
        self.unit[2].configure(image = self.citizen2_pic)
        self.citizen2_type.configure(text = typecode[2])
        self.citizen2_type.place(x = location[2][0]+2, y = location[2][1]+157)


        self.unit[3].place(x = location[3][0], y = location[3][1])
        self.unit[3].configure(image = self.citizen3_pic)
        self.citizen3_type.configure(text = typecode[3])
        self.citizen3_type.place(x = location[3][0]+2, y = location[3][1]+157)

        self.citizen_name.append(typecode[2])
        self.citizen_name.append(typecode[3])

        if gamemode_hard == True:

            self.unit[4].place(x = location[4][0], y = location[4][1])
            self.unit[4].configure(image = self.citizen4_pic)
            self.citizen4_type.configure(text = typecode[4])
            self.citizen4_type.place(x = location[4][0]+2, y = location[4][1]+157)

            self.unit[5].place(x = location[5][0], y = location[5][1])
            self.unit[5].configure(image = self.citizen5_pic)
            self.citizen5_type.configure(text = typecode[5])
            self.citizen5_type.place(x = location[5][0]+2, y = location[5][1]+157)

            self.citizen_name.append(typecode[4])
            self.citizen_name.append(typecode[5])


        if virus == True and stopvirus == False:
            self.after(2000, self.virus)
        elif stopvirus == True:
            stopvirus = False

    def createWidgets(self):

        global virus, t  # 前面有settimer那裡有time = t, 注意error
        f2 = tkFont.Font(size = 28, family = "Courier New")
        f4 = tkFont.Font(size = 20, family = "Courier New", weight = "bold")
        type_font = tkFont.Font(size = 12 , family = "Courier New",weight = "bold")

        if self.has_shooted == False:
            self.play = gamer_sound.play(5)


        random.shuffle(location)
        random.shuffle(typecode)
        random.shuffle(citizen_filename)

        self.terrorist_pic = ImageTk.PhotoImage(file = citizen_filename[9])
        self.wanted_pic = ImageTk.PhotoImage(file = "1-"+str(citizen_filename[9]))

        self.president_pic = ImageTk.PhotoImage(file = "mayor.png")
        self.citizen2_pic = ImageTk.PhotoImage(file = citizen_filename[0])
        self.citizen3_pic = ImageTk.PhotoImage(file = citizen_filename[1])
        self.closedwindow_pic = ImageTk.PhotoImage(file = "window_pic/dark_window.png")
        self.bg_image = tk.Label(self,image = self.bg_pic, compound = tk.CENTER)
        self.bg_image.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)

        self.unit=[0,0,0,0,0,0,0,0,0,0]# 窗戶編號和對應的代碼

        for i in range(10):
            self.unit[i] = tk.Label(self,image = self.closedwindow_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0, bg = "White")
            self.unit[i].place(x = location[i][0], y = location[i][1])

        self.unit[0].configure(image = self.president_pic)
        self.unit[1].configure(image = self.terrorist_pic)
        self.unit[2].configure(image = self.citizen2_pic)
        self.unit[3].configure(image = self.citizen3_pic)

        self.president_type = tk.Label(self, text = typecode[0], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
        self.president_type.place(x = location[0][0]+2, y = location[0][1]+157)
        self.president_name = typecode[0]

        self.terrorist_type = tk.Label(self, text = typecode[1], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
        self.terrorist_type.place(x = location[1][0]+2, y = location[1][1]+157)
        self.terrorist_name = typecode[1]

        self.citizen_name = []

        self.citizen2_type = tk.Label(self, text = typecode[2], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
        self.citizen2_type.place(x = location[2][0]+2, y = location[2][1]+157)

        self.citizen3_type = tk.Label(self, text = typecode[3], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
        self.citizen3_type.place(x = location[3][0]+2, y = location[3][1]+157)

        self.citizen_name.append(typecode[2])
        self.citizen_name.append(typecode[3])
        self.people = 4

        if gamemode_hard == True:

            self.citizen4_pic = ImageTk.PhotoImage(file = citizen_filename[2])
            self.citizen5_pic = ImageTk.PhotoImage(file = citizen_filename[3])

            self.unit[4].configure(image = self.citizen4_pic)
            self.unit[5].configure(image = self.citizen5_pic)

            self.citizen4_type = tk.Label(self, text = typecode[4], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
            self.citizen4_type.place(x = location[4][0]+2, y = location[4][1]+157)

            self.citizen5_type = tk.Label(self, text = typecode[5], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
            self.citizen5_type.place(x = location[5][0]+2, y = location[5][1]+157)

            self.citizen_name.append(typecode[4])
            self.citizen_name.append(typecode[5])
            self.people = 6

        if gamemode_crazy == True:

            if virus == False:


                self.citizen6_pic = ImageTk.PhotoImage(file = citizen_filename[4])
                self.citizen7_pic = ImageTk.PhotoImage(file = citizen_filename[5])
                self.unit[6].configure(image = self.citizen6_pic)
                self.unit[7].configure(image = self.citizen7_pic)

                self.citizen6_type = tk.Label(self, text = typecode[6], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
                self.citizen6_type.place(x = location[6][0]+2, y = location[6][1]+157)

                self.citizen7_type = tk.Label(self, text = typecode[7], height = 1, width = 12, font = type_font, bg = "#ecd3c4")
                self.citizen7_type.place(x = location[7][0]+2, y = location[7][1]+157)

                self.citizen_name.append(typecode[6])
                self.citizen_name.append(typecode[7])

                self.people = 8
            else:
                self.people = 6

        # 懸賞單
        self.wanted = tk.Label(self, image = self.wanted_pic,height = 120, width = 120)
        self.wanted.place(x = 1212, y = 425)

        self.txt_ans = tk.Text(self, height = 1, width = 16, font = f2, bg = "#827575")
        self.txt_ans.place(x = 360, y = 700)
        self.txt_ans.focus()  #讓游標直接放在textbox裡 不用按一下就可以直接輸入
        self.txt_ans.bind("<Return>", self.clickBtnShoot)

        self.Success = tk.Label(self, height = 1, width = 9, text = "Success",font = f4, bg = "#482d29", fg = "White", relief = "raised")
        self.Success.place(x = 1180, y = 80)

        self.count = tk.Label(self, height = 1, width = 3, text = number ,font = f4,bg = "#482d29", fg = "White", relief = "raised")
        self.count.place(x = 1324, y = 80)

        self.result = tk.Label(self,height = 1, width = 12, text = "",font = f4,bg = "#482d29", fg = "White", relief = "raised")
        self.result.place(x = 1180, y = 120)

        self.highsocre = tk.Label(self, height = 1, width = 9, text = "Record",font = f4,bg = "#614a3e", fg = "White", relief = "raised")
        self.highsocre.place(x = 1180, y = 160)

        self.top = tk.Label(self, height = 1, width = 3, text = top,font = f4, bg = "#614a3e", fg = "White", relief = "raised")
        self.top.place(x = 1324, y = 160)

        self.EndBtn_pic = ImageTk.PhotoImage(file='endbtn.png')
        self.EndBtn = tk.Button(self, image = self.EndBtn_pic , padx = 0, pady = 0,highlightthickness = 0, compound = tk.CENTER, borderwidth = 0, relief = "flat",command = self.endgame)
        self.EndBtn.place(x = 1200, y = 720)


        if virus == True:
            self.after(2000, self.virus)

    def clickBtnShoot(self,event=None):# 射擊答案判定

        global number, stopvirus, citizen_name, president_name, terrorist_name, t, top

        self.has_shooted = True
        stopvirus = True
        ans = str(self.txt_ans.get("1.0", tk.END)).strip()

        if ans == self.president_name:
            self.play = yell_sound.play()
            self.play2 = glass_sound.play()
            self.shoot_result = "Fail"
            self.result.configure(text = "Fail!")

        elif ans == self.terrorist_name:
            self.play3 = yell_sound.play()
            self.shoot_result = "Success"
            self.result.configure(text = "Success!")

        elif ans in self.citizen_name:
            self.play4 = yell_sound.play()
            self.shoot_result = "Wrong"
            self.wrong_index = self.citizen_name.index(ans)
            self.result.configure(text = "Wrong!")

        else:
            self.play2 = glass_sound.play()
            self.shoot_result="Empty"
            self.result.configure(text = "Miss Fire!")

        self.txt_ans.delete("1.0", tk.END)
        #self.shouldReset = True
        self.holdup = False
        #self.txt_ans.configure(text = "")
        #self.after(1500,self.ChangeStage)
        self.play = shoot_sound.play()
        #self.play = winsound.PlaySound('shoot_sound.wav', winsound.SND_ASYNC)

        if self.shoot_result == "Success":
            number += 1
            self.count.configure(text = str(number))
            if number > top:
                top = number
                self.top.configure(text = top)
            self.unit[1].configure(image = self.tomb_pic)
            self.after(1000,self.closewindow)

        elif self.shoot_result == "Empty":
            if t < 2:
                t = 0
            else:
                t -= 2
            for i in range(self.people,10):
                self.unit[i].configure(image = self.crack_pic)

            f3 = tkFont.Font(size = 48, family = "Courier New")
            self.minustwo = tk.Label(self, text = "-2" , height = 1, width = 2, font = f3, bg = "#6f645d" , fg = "White", relief = "raised")
            self.minustwo.place(x = 250, y = 50)

            self.after(1000,self.closewindow)

        elif self.shoot_result == "Wrong":  # ans wrong_index要注意因為citizen是從2-10
            if t < 2:
                t = 0
            else:
                t -= 2
            if str(self.wrong_index+2) == "2":
                self.unit[2].configure(image = self.tomb_pic)

            elif str(self.wrong_index+2) == "3":
                self.unit[3].configure(image = self.tomb_pic)

            elif str(self.wrong_index+2) == "4":
                self.unit[4].configure(image = self.tomb_pic)

            elif str(self.wrong_index+2) == "5":
                self.unit[5].configure(image = self.tomb_pic)

            elif str(self.wrong_index+2) == "6":
                self.unit[6].configure(image = self.tomb_pic)

            elif str(self.wrong_index+2) == "7":
                self.unit[7].configure(image = self.tomb_pic)

            f3 = tkFont.Font(size = 48, family = "Courier New")
            self.minustwo = tk.Label(self, text = "-2" , height = 1, width = 2, font = f3, bg = "#6f645d" , fg = "White", relief = "raised")
            self.minustwo.place(x = 250, y = 50)

            self.after(1000,self.closewindow)

        elif self.shoot_result == "Fail":
            global presidentdie
            t = 0
            if self.people == 4:
                self.unit[0].configure(image = self.tomb_pic)
                self.unit[2].configure(image = self.tomb_pic)
                self.unit[3].configure(image = self.tomb_pic)


            elif self.people==6:
                self.unit[0].configure(image = self.tomb_pic)
                self.unit[2].configure(image = self.tomb_pic)
                self.unit[3].configure(image = self.tomb_pic)
                self.unit[4].configure(image = self.tomb_pic)
                self.unit[5].configure(image = self.tomb_pic)
            elif self.people==8:
                self.unit[0].configure(image = self.tomb_pic)
                self.unit[2].configure(image = self.tomb_pic)
                self.unit[3].configure(image = self.tomb_pic)
                self.unit[4].configure(image = self.tomb_pic)
                self.unit[5].configure(image = self.tomb_pic)
                self.unit[6].configure(image = self.tomb_pic)
                self.unit[7].configure(image = self.tomb_pic)
            for i in range(self.people,10):
                self.unit[i].configure(image = self.crack_pic)
            presidentdie = True
            self.after(2000, self.finishgame)


    def closewindow(self):
        self.next_pic = ImageTk.PhotoImage(file = "wanted_pic/wanted_back.png")
        self.after(1000)
        for i in range(10):
            self.unit[i].configure(image = self.closedwindow_pic)
        self.wanted.configure(image = self.next_pic)
        self.after(1000,self.createWidgets)

    def finishgame(self):
        gamer.destroy(self)
        mission_complete()

    def endgame(self):
        global t, number
        number = 0
        gamemode_hard = False
        gamemode_crazy = False
        t = 10
        virus = False
        stopvirus = False
        presidentdie = False
        gamer.destroy(self)
        menu()

class two_player(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)
        self.grid()
        self.place()
        self.pack()
        self.menu_pic = ImageTk.PhotoImage(file = "background_pic/2p-back.png")
        self.team1_pic = ImageTk.PhotoImage(file = "window_pic/soldier.png")
        self.team2_pic = ImageTk.PhotoImage(file = "window_pic/soldier_brown.png")
        self.empty_pic = ImageTk.PhotoImage(file = "window_pic/empty.png")
        self.tomb_pic = ImageTk.PhotoImage(file = "window_pic/tomb.png")

        self.createWidget()

    def createWidget(self):

        global t1_people, t2_people, t1_code, t2_code, in_t1, in_t2, t1man_pic, t2man_pic, virus

        in_t1.clear()
        in_t2.clear()

        t1_people = 4
        t2_people = 4
        self.t1 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.t2 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

        self.menu = tk.Label(self, image = self.menu_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0, bg = "White")
        self.menu.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        f1 = tkFont.Font(size = 12, family = "Courier New")
        f2 = tkFont.Font(size = 25, family = "Courier New", weight = "bold")
        self.Back = tk.Button(self, text = "Back" , height = 1, width = 6, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.back)
        self.Back.place(x = 665 , y = 700)

        for i in range(4):

            self.t1[i][0] = tk.Label(self, image = self.empty_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0)
            self.t1[i][1] = tk.Label(self, text = empty, font = f1, width = 10,bg = "#ecd3c4")
            self.t1[i][0].place(x = 71 , y = i*207+15)
            self.t1[i][1].place(x = 70 , y = i*207+141)

            self.t1[i+4][0] = tk.Label(self, image = self.team1_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0)
            self.t1[i+4][1] = tk.Label(self, text = empty, font = f1, width = 10 ,bg = "#ecd3c4")
            self.t1[i+4][0].place(x = 275 , y = i*207+15)
            self.t1[i+4][1].place(x = 270 , y = i*207+142)

        for j in range(4):

            self.t2[j][0] = tk.Label(self, image = self.team2_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0)
            self.t2[j][1] = tk.Label(self, text = empty, font = f1, width = 10, bg = "#ecd3c4")
            self.t2[j][0].place(x = 1072 , y = j*207+15)
            self.t2[j][1].place(x = 1071 , y = j*207+140)

            self.t2[j+4][0] = tk.Label(self, image = self.empty_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0)
            self.t2[j+4][1] = tk.Label(self, text = empty, font = f1, width = 10, bg = "#ecd3c4")
            self.t2[j+4][0].place(x = 1271 , y = j*208+14)
            self.t2[j+4][1].place(x = 1271 , y = j*207+140)

        t1man_pic = self.t1[4][0].cget("image")
        t2man_pic = self.t2[0][0].cget("image")
        self.t1[0][0].focus_set()
        self.t1[0][0].bind("<Key>", self.keys)

        print(self.t2[6][0].cget("image"))

        #set team1 code
        j = 0
        random.shuffle(t1_code)
        for i in range(8):
            if self.t1[i][0].cget("image") == t1man_pic:
                self.t1[i][1].configure(text = t1_code[j])
                in_t1.append(t1_code[j])
                j += 1

            else:
                self.t1[i][1].configure(text = empty)

        #set team2 code
        j = 0
        random.shuffle(t2_code)
        for i in range(8):
            if self.t2[i][0].cget("image") == t2man_pic:
                self.t2[i][1].configure(text = t2_code[j])
                in_t2.append(t2_code[j])
                j += 1

            else:
                self.t2[i][1].configure(text = empty)

        print(in_t1)
        print(in_t2)

        if virus == True:
            self.after(2000, self.virus)

    def virus(self):
        global stopvirus, virus

        random.shuffle(self.t1)
        random.shuffle(self.t2)

        for i in range(4):
            self.t1[i][0].place(x = 75 , y = i*208+15)
            self.t1[i][1].place(x = 90 , y = i*206+145)
            self.t1[i+4][0].place(x = 275 , y = i*208+15)
            self.t1[i+4][1].place(x = 290 , y = i*206+145)

        for j in range(4):
            self.t2[j][0].place(x = 1075 , y = j*208+15)
            self.t2[j][1].place(x = 1090 , y = j*206+145)
            self.t2[j+4][0].place(x = 1275 , y = j*208+15)
            self.t2[j+4][1].place(x = 1290 , y = j*206+145)

        #reset team1 code
        j = 0
        random.shuffle(t1_code)
        in_t1.clear()
        for i in range(8):
            if self.t1[i][0].cget("image") == t1man_pic:
                self.t1[i][1].configure(text = t1_code[j])
                in_t1.append(t1_code[j])
                j += 1

            else:
                self.t1[i][1].configure(text = empty)

        #reset team2 code
        j = 0
        random.shuffle(t2_code)
        in_t2.clear()
        for i in range(8):
            if self.t2[i][0].cget("image") == t2man_pic:
                self.t2[i][1].configure(text = t2_code[j])
                in_t2.append(t2_code[j])
                j += 1

            else:
                self.t2[i][1].configure(text = empty)

        #print(in_t1)
        #print(in_t2)

        if stopvirus == True:
            stopvirus = False
            return


        if virus == True and stopvirus == False:
            self.after(2000, self.virus)
        elif stopvirus == True:
            stopvirus = False

    def keys(self,event):
        global t1_people, t2_people, t1_code, t2_code, in_t1, in_t2
        self.play = shoot_sound2.play()
        print(event.char)

        # t1 get shot
        find_empty_space = 0
        j = 0

        if event.char in t1_code:
            if event.char in in_t1:
                for i in range(8):
                    if self.t1[i][1].cget("text") == event.char:
                        self.play1 = yell_sound2.play()
                        self.t1[i][0].configure(image = self.tomb_pic) # team1 dead
                        t1_people -= 1
                        in_t1.remove(event.char) # clear dead player code
                        self.t1[i][1].configure(text = empty)

                        while find_empty_space == 0:

                            if self.t2[j][0].cget("image") != t2man_pic:
                                self.t2[j][0].configure(image = self.team2_pic) # add extra player to t2
                                t2_people += 1
                                find_empty_space = 1

                                random.shuffle(t2_code)
                                for code in t2_code:
                                    if code not in in_t2:
                                        self.t2[j][1].configure(text = code) #add
                                        in_t2.append(code)
                                        break
                            j += 1


            elif event.char not in in_t1:
                check = 0
                #print("hi")
                for i in range(8):
                    #print("yo")
                    #print(self.t2[i][0].cget("image"))
                    if self.t2[i][0].cget("image") == t2man_pic and check == 0:
                        self.play1 = yell_sound2.play()
                        self.t2[i][0].configure(image = self.tomb_pic) # team2 dead
                        t2_people -= 1
                        in_t2.remove(self.t2[i][1].cget("text")) # clear dead player code
                        self.t2[i][1].configure(text = empty)
                        check = 1
                        while find_empty_space == 0:
                            if self.t1[j][0].cget("image") != t1man_pic:
                                self.t1[j][0].configure(image = self.team1_pic) # add extra player to t1
                                t1_people += 1
                                find_empty_space = 1
                                random.shuffle(t1_code)

                                for code in t1_code:
                                    if code not in in_t1:
                                        self.t1[j][1].configure(text = code) #add
                                        in_t1.append(code)
                                        break
                            j += 1



        # t2 get shot
        find_empty_space = 0
        j = 0

        if event.char in t2_code:
            if event.char in in_t2:
                for i in range(8):
                    if self.t2[i][1].cget("text") == event.char:
                        self.play1 = yell_sound2.play()
                        self.t2[i][0].configure(image = self.tomb_pic) # team2 dead
                        t2_people -= 1
                        in_t2.remove(event.char) # clear dead player code
                        self.t2[i][1].configure(text = empty)

                        while find_empty_space == 0:
                            if self.t1[j][0].cget("image") != t1man_pic:
                                self.t1[j][0].configure(image = self.team1_pic) # add extra player to t1
                                t1_people += 1
                                find_empty_space = 1
                                random.shuffle(t1_code)

                                for code in t1_code:
                                    if code not in in_t1:
                                        self.t1[j][1].configure(text = code) #add
                                        in_t1.append(code)
                                        break
                            j += 1


            elif event.char not in in_t2:
                #print("hi")
                check = 0
                for i in range(8):
                    #print("yo")
                    if self.t1[i][0].cget("image") == t1man_pic and check == 0:
                        self.play1 = yell_sound2.play()
                        self.t1[i][0].configure(image = self.tomb_pic) # team1 dead
                        t1_people -= 1
                        in_t1.remove(self.t1[i][1].cget("text")) # clear dead player code
                        self.t1[i][1].configure(text = empty)
                        check = 1
                        while find_empty_space == 0:
                            if self.t2[j][0].cget("image") != t2man_pic:
                                self.t2[j][0].configure(image = self.team2_pic) # add extra player to t2
                                t2_people += 1
                                find_empty_space = 1
                                random.shuffle(t2_code)

                                for code in t2_code:
                                    if code not in in_t2:
                                        self.t2[j][1].configure(text = code) #add
                                        in_t2.append(code)
                                        break
                            j += 1


        if t1_people == 8 or t2_people == 8:
            two_player.destroy(self)
            two_player_end()


    def back(self):
        self.after(1500,two_player_end.destroy(self))
        menu()


class two_player_end(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)
        self.grid()
        self.place()
        self.pack()
        self.menu_pic = ImageTk.PhotoImage(file = "background_pic/menu1.png")
        self.createWidget()


    def createWidget(self):
        f2 = tkFont.Font(size = 30, family = "Courier New", weight = "bold")
        self.menu = tk.Label(self, image = self.menu_pic, compound = tk.CENTER, highlightthickness = 0, borderwidth = 0, bg = "White")
        self.menu.grid(row = 0, column = 0, columnspan = 10 , rowspan = 10)
        self.Back = tk.Button(self, text = "Back" , height = 1, width = 16, font = f2, activeforeground = "White", activebackground = "Gray", fg = "White", bg = "#614a3e", command = self.back)
        self.Back.place(x = 515 , y = 600)

        #f2 = tkFont.Font(size = 30, family = "Courier New", weight = "bold")
        self.play3 = mission_sound2.play()

        if t1_people == 8:
            self.show = tk.Label(self, text = "Team1 win", fg = "red", bg = "DarkGoldenrod2",height = 1, width = 40, font = f2)
            self.show.place(x = 235, y = 100)

        if t2_people == 8:
            self.show = tk.Label(self, text = "Team2 win", fg = "red", bg = "DarkGoldenrod2",height = 1, width = 40, font = f2)
            self.show.place(x = 235, y = 100)

    def back(self):
        self.after(1500,two_player_end.destroy(self))
        menu()

sniper = menu()
sniper.master.title("The Real Frealing Sniper")
sniper.mainloop()
