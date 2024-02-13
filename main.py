from PyQt5 import QtWidgets
from AIM import Ui_MainWindow
from AtelierHome import Ui_MainWindow2
from GestionPersonnel import Ui_MainWindowGP
from AddAS import Ui_addAS
from MAJ_pers import Ui_MAJ_Personnel

import sys
import os
import sqlite3


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"]="1"
os.environ["QT_SCREEN_SCALE_FACTORS"]="1"
os.environ["QT_SCALE_FACTOR"]="1"

# debut initialisation


class window (QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui2= Ui_MainWindow2()
        self.uiGP = Ui_MainWindowGP()
        self.uiAS =Ui_addAS()
        self.uiMAJPers =Ui_MAJ_Personnel()

        self.ui.setupUi(self)

        self.ui.ConnectButton.clicked.connect(self.seconnecter)


        

        

    def seconnecter(self):
        self.close()
        self.window =QtWidgets.QMainWindow()
       

        self.ui2.setupUi(self.window)
        self.window.show()

        self.ui2.closeUI2.clicked.connect(self.fermerUI2)
        self.ui2.ouvrirGP.clicked.connect(self.ouvrirGP)

# Ouvrir l'interface Gestion du personnel
    def ouvrirGP(self):
        self.window =QtWidgets.QMainWindow()

        # self.ui2.setupUi(self.window)
        # self.window.close()

        self.uiGP.setupUi(self.window)
        self.window.show()


        self.title=self.uiGP.gp_title

        self.uiGP.qpb_1fichierPersonnel
        

        self.btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn2= self.uiGP.qpb_2fichierdePresence
        self.btn3= self.uiGP.qpb_3avance15
        self.btn4= self.uiGP.qpb_4avanceSpeciale
        self.btn5= self.uiGP.qpb_5calculSalaire
        self.btn6= self.uiGP.qpb_6editionBP
        self.btn7= self.uiGP.qpb_7editionJP
        self.btn8= self.uiGP.qpb_8editionIRSA
        self.btn9= self.uiGP.qpb_9editionCNAPS
        self.btn10= self.uiGP.qpb_10gestionConge
        self.btn11= self.uiGP.qpb_11dossierRH


        self.sw = self.uiGP.stackedWidget

        self.p1=self.uiGP.p1_fichierPersonnel
        self.p2=self.uiGP.p2_fichedepresence
        self.p3=self.uiGP.p3_avance15
        self.p4=self.uiGP.p4_avanceSpeciale
        self.p5=self.uiGP.p5_calculSalaire
        self.p6=self.uiGP.p6_editionBP
        self.p7=self.uiGP.p7_editionJP
        self.p8=self.uiGP.p8_editionIRSA
        self.p9=self.uiGP.p9_editionCNAPS
        self.p10=self.uiGP.p10_gestionConges
        self.p11=self.uiGP.page11_dossierRH

        

        self.btn1.clicked.connect(self.ouvrirp1)
        self.uiGP.maj_personnel.clicked.connect(self.ouvrirUiMajPers)
        

        self.btn1_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn2_list=[self.btn1,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn3_list=[self.btn2,self.btn1,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn4_list=[self.btn2,self.btn3,self.btn1,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn5_list=[self.btn2,self.btn3,self.btn4,self.btn1,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn6_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn1,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn7_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn1,self.btn8,self.btn9,self.btn10,self.btn11]
        self.btn8_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn1,self.btn9,self.btn10,self.btn11]
        self.btn9_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn1,self.btn10,self.btn11]
        self.btn10_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn1,self.btn11]
        self.btn11_list=[self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn1]


        self.btn2.clicked.connect(self.ouvrirp2)
        self.btn3.clicked.connect(self.ouvrirp3)
        self.btn4.clicked.connect(self.ouvrirp4)
        self.btn5.clicked.connect(self.ouvrirp5)
        self.btn6.clicked.connect(self.ouvrirp6)
        self.btn7.clicked.connect(self.ouvrirp7)
        self.btn8.clicked.connect(self.ouvrirp8)
        self.btn9.clicked.connect(self.ouvrirp9)
        self.btn10.clicked.connect(self.ouvrirp10)
        self.btn11.clicked.connect(self.ouvrirp11)

        

        self.uiGP.gp_retour_home.clicked.connect(self.retourHome)

        self.ouvrirp1()

# Ouvrir le Widget Gestion Personnel
        
    def ouvrirp1(self):
        self.btn1.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p1)
        for x in self.btn1_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Fichier Personnel")
        self.loadPerson()
    
    def ouvrirUiMajPers(self):
        self.window =QtWidgets.QMainWindow()
        self.uiMAJPers.setupUi(self.window)
        self.window.show()

        self.uiMAJPers.gp_retour_home.clicked.connect(self.retourGP_fp)
    
    def retourGP_fp(self):
        self.ouvrirGP()
        self.ouvrirp1()

    def loadPerson(self):
        self.connecteo = sqlite3.connect("aimData.db")
        self.curs = self.connecteo.cursor()
        sqlquery = "SELECT * FROM Personnels"
        self.rs = self.curs.execute(sqlquery)
        print(self.rs.fetchall())


# Ouvrir le Widget Fiche de Présence
        
    def ouvrirp2(self):
        self.btn2.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p2)
        for x in self.btn2_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Fiche de présence")

# Ouvrir le Widget Avance Quizaine

    def ouvrirp3(self):
        self.btn3.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p3)
        for x in self.btn3_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Fiche quizaine")
        
# Ouvrir le Widget Avance Spéciale

    def ouvrirp4(self):
        self.btn4.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p4)
        for x in self.btn4_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Avance Spéciale")

        self.uiGP.btn_newAS.clicked.connect(self.ouvrirNewAS)

    def ouvrirNewAS(self):
        self.window =QtWidgets.QMainWindow()
        self.uiAS.setupUi(self.window)
        self.window.show()

        self.uiAS.pb_addAS_retour.clicked.connect(self.retourGP_rh)

    def retourGP_rh(self):
        self.ouvrirGP()
        self.ouvrirp4()   


# Ouvrir le Widget Calcul Salaire

    def ouvrirp5(self):
        self.btn5.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p5)
        for x in self.btn5_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Calcul des Salaires")
        

# Ouvrir le Widget Edition Bulletin de Paie

    def ouvrirp6(self):
        self.btn6.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p6)
        for x in self.btn6_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Edition Bulletin de Paie")


# Ouvrir le Widget Journal de Paie

    def ouvrirp7(self):
        # btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn7.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p7)
        for x in self.btn7_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Edition Journal de Paie")
        
# Ouvrir le Widget Edition IRSA
        
    def ouvrirp8(self):
        # btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn8.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p8)
        for x in self.btn8_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Edition IRSA")
        
# Ouvrir le Widget Edition CNAPS
        
    def ouvrirp9(self):
        # btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn9.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p9)
        for x in self.btn9_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Edition CNAPS")
        
# Ouvrir le Widget Congés
        
    def ouvrirp10(self):
        # btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn10.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p10)
        for x in self.btn10_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Gestion des Congés")

# Ouvrir le Widget Dossier RH

    def ouvrirp11(self):
        # btn1= self.uiGP.qpb_1fichierPersonnel
        self.btn11.setStyleSheet("background:rgb(0, 85, 255)")
        self.sw.setCurrentWidget(self.p11)
        for x in self.btn11_list:
            x.setStyleSheet("background:rgb(0, 0, 83)")
        self.title.setText("Dossiers Ressources Humaines")


    

    def retourHome(self):
        self.seconnecter()


    def fermerUI2(self):
        self.window =QtWidgets.QMainWindow()
        self.ui2.setupUi(self.window)
        self.window.close()

 
def create_app():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

create_app()