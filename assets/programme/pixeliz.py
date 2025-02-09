from tkinter import filedialog
from tkinter import *
#déclaration de variables globales utiles dans différentes fonctions
fileImage = ""
Picture=""
#lang = str()

#DMode = False
def pixeliser(scale:int,image:str):#création d'une fonction de pixelisation
    from PIL import Image #importation du module pillow(PIL)

    image1 = Image.open(image)#création d'un objet image1
    L, H = image1.size#récuperation de la taille de l'image
    image2 = Image.new("RGB",(L,H))#création d'une nouvelle image vide à partir des dimensions de la précedente
    #Boucles permettant de parcourir l'ensemble des pixels de l'image1
    for y in range(0,H-1,scale):
        for x in range(0,L-1,scale):


        #récuperation de la couleur du pixel (X,Y)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]

		#création d'un pixel plus grand dans l'image2
            for x2 in range(0,scale+1):
                for y2 in range(0,scale+1):

                    #pour éviter les effets de bord indésirables
                    x1 = x2
                    y1 = y2

                    #pour éviter l'erreur "OutOfRange"
                    if x+x1>=L:
                        x1=(L-x)-1

                    if y+y1>=H:
                        y1=(H-y)-1


                    #dépose du pixel dans l'image2
                    image2.putpixel((x+x1,y+y1),(r,v,b))
        
    #sauvegarde de l'image2
    global Picture
    Picture = image2

    #affichage de l'image2
    image2.show()

def saveFile():#Fonction de sauvegarde de l'image
    try:
        global Picture#appel de la variable globale Picture qui contient les informations de la nouvelle image
        emplacement = filedialog.asksaveasfilename(initialdir = "/", title = "Select folder",filetypes=(("jpeg files", "*.png"), ("all files", "*.*")), defaultextension='.png')#sélection de l'emplacement de sauvegarde de la nouvelle image

        if emplacement:
            Picture.save(emplacement)#sauvegarde de l'image à l'emplacement sélectionné
        else:
            labelImg.configure(text = "Impossible de \nsauvegarder : Nom \ninvalide")
    except:
        labelImg.configure(text = "Impossible de \nsauvegarder : aucune \nimage sélectionée")

def afficherValeur() :

    #Fonction associée au bouton
    valeur = curseurPix.get()
    labelPix.configure(text ="Taille des pixels :"+str(valeur))

    #Pour éviter les erreurs de désignation d'image
    global fileImage
    nameImage = fileImage
    try:
        pixeliser(curseurPix.get(),nameImage)
    except:
        labelImg.configure(text = "Image introuvable, \n veuillez réessayer")
    else:
        labelImg.configure(text = "Image pixelisée \n avec succès")

def selectFile():#sélection de l'image a pixeliser
    Tk.filename = filedialog.askopenfilename (initialdir="/", title="Select file", filetypes=(("jpeg files", "*.png"), ("all files", "*.*")))

    #mise des données de l'image dans la variable globale
    global fileImage
    fileImage = Tk.filename
    txtLabel= str(fileImage)
    if txtLabel == "":
        return
    #affichage du fichier sélectionné
    txtlabel = ""

    txtLabel = "Image sélectionnée : \n"+txtLabel.split("/")[-1]

    #affichage de la variable contenant le nom du fichier
    labelImg.configure(text = txtLabel)
    
#def getInfo():
#    with open("cfg.txt", "r") as cfg:
#       a = cfg.read()
#    return a

#def rstcfg():
#    with open("cfg.txt", "w") as cfg:
#        a = cfg.write("")
#    config()

#fenetre de configuration
#def config():
#    def langEn():
#        with open("cfg.txt", "w") as cfg:
#            a = cfg.write("lang:En")
#        labl_lang.configure(text = 'Selected language : English')
#    def langFr():
#        with open("cfg.txt", "w") as cfg:
#            a = cfg.write("lang:Fr")
#        labl_lang.configure(text = 'Langue sélectionnée : Français')
#    def toggleDarkMode():
#        global DMode
#        if DMode:
#            DMode = False
#        else:
#            DMode = True
#        print("DBG[toggleDarkMode]",DMode)
#    #global DMode
#    #global lang
#    #if DMode and lang = Fr:
#    #msgdmode ='des 
#    cfg = Tk()
#    cfg.title("Pixeliz-Configuration")
#    cfg.geometry("300x200-500+200")
#    cfg.iconbitmap("ressources\\logopixeliz.ico")
#    labl_lang = Label(cfg, text = "langue sélectionnée : Aucune")
#    labl_lang.place(x = 30, y = 0)
#    lang_en = Button(cfg, text = 'English', command = langEn)
#    lang_en.place(x = 30, y = 50)
#    lang_fr = Button(cfg, text = 'Français', command = langFr)
#    lang_fr.place(x = 150, y = 50)
#    dmode = Button(cfg, text = "msgdmode", command = toggleDarkMode)
#    dmode.pack()
#    cfg.mainloop()

#if not getInfo():
#    config()
    
# Création de la fenêtre et des objets associés la fenêtre
fen_princ = Tk()
fen_princ.title("Pixeliz")
fen_princ.geometry("300x300-500+200")
fen_princ.iconbitmap("ressources\\logopixeliz.ico")
#Ajout d'un fichier image
bg = PhotoImage(file = "ressources\\Bg_pixelizz.png")

# afficher l'image en arriere plan
label1 = Label(fen_princ, image = bg)
label1.place(x = 0, y = 0)

#rst = Button(fen_princ,text = "réinitialiser\n les preferences", command = rstcfg)
#rst.place(x=0,y=1)

# Création d'un Label nommé labelPix
labelPix = Label(fen_princ, text = "Taille des pixels", width=50,bg = "#ffffff")
labelPix.pack(padx=90,pady = 20)

# Création d'un Scale nommé curseurPix
curseurPix = Scale(fen_princ, from_ = 30, to = 1, bg = "#ffffff")
curseurPix.pack()

#création d'un label nommé labelImg
labelImg = Label(fen_princ,text="Choisissez un fichier",width = 100,bg = "#ffffff")
labelImg.pack(padx = 80)

#création d'un bouton nommée fileName
fileName = Button(fen_princ, text="Parcourir", command = selectFile)
fileName.pack()


#Création d'un bouton nommé pix
pix = Button(fen_princ, text = "Pixeliser", command = afficherValeur)
pix.pack()


#Création d'un bouton nommé sauvegarder
sauvegarder = Button(fen_princ, text = "Sauvegarder", command = saveFile)
sauvegarder.pack()


#boucle principale permettant à la fenêtre de rester ouverte
fen_princ.mainloop()
