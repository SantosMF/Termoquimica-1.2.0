#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
import sys
import Interface  # arquivo *.py gerado pelo pyuic5
import os
import modulo1 
path = os.path.dirname(os.path.realpath(__file__))

class App(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        qr=self.frameGeometry()
        self.position = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(self.position)
        self.move(qr.topLeft())
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('background:gray')
        self.icon1 = QtGui.QIcon()
        self.icon2 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap(path+"/temps/ico2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.icon2.addPixmap(QtGui.QPixmap(path+"/temps/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.setWindowIcon(self.icon1)
#----------------- campo para conectar os módulos às funções ------------------
        self.framex = QtWidgets.QLabel(self) ## oculta seletor
        self.framex.setGeometry(2,410,300,20)
        #self.framex.setStyleSheet("background:#000000")
        self.ajuda.triggered.connect(self.AjudaDef)
        self.sobre.triggered.connect(self.SobreDef)
        self.fechar.triggered.connect(self.FecharDef)
        self.tempU.triggered.connect(self.SetarU)
        self.tempH.triggered.connect(self.SetarH)
        self.tempS.triggered.connect(self.SetarS)
        self.tempG.triggered.connect(self.SetarG)
        self.tempA.triggered.connect(self.SetarA)
        self.simetria.triggered.connect(self.SimetriaDef)
        self.convert.triggered.connect(self.ConvertDef) 
        self.Complete.triggered.connect(self.SetarTudo)
        
        self.Molecule.toggled.connect(self.G1)
        self.Solid.toggled.connect(self.G2)
        self.Atoms.toggled.connect(self.G3)
        
        self.btn1.clicked.connect(self.open_scf)
        self.btn1.setIcon(self.icon2)
        self.btn1.setToolTip("Pesquisar")
        self.btn2.clicked.connect(self.open_dynmat) 
        self.btn2.setIcon(self.icon2)
        self.btn2.setToolTip("Pesquisar")       
        self.btn3.clicked.connect(self.Print)         
        self.btn4.clicked.connect(self.Salvar)         
        self.btn5.clicked.connect(self.Clean) 


#------------------------ campo para as funções -------------------------------
    def G1(self):
        self.groupBox.setCheckable(True)
        self.NoLinear.setEnabled(True)
        self.Linear.setEnabled(True)
        self.sym.setEnabled(True)
        self.line_sym.setEnabled(True)
        self.Atoms.setChecked(False)
    def G2(self):
        self.groupBox.setChecked(False)
        self.Atoms.setChecked(False)
        self.NoLinear.setChecked(True)
        self.line_sym.setEnabled(False)
        self.sym.setEnabled(False)
    def G3(self):
        if self.Atoms.isChecked():
            self.line_sym.setEnabled(False)
            self.sym.setEnabled(False)
        else:
            self.line_sym.setEnabled(True)
            self.sym.setEnabled(True)

#-----------------------------------------------------------------------------
    def open_scf(self): # pesquisar arquivos
        self.file_scf, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir", "","*.out")
        if self.file_scf:
            self.line_scf.setText(self.file_scf)
    def open_dynmat(self): # pesquisar arquivos
        self.fileDynmat, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir", "","*.out")
        if self.fileDynmat:
            self.line_dynmat.setText(self.fileDynmat)
    def Salvar(self):
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar como", ".dat",("*.dat"),)
        try:
            with open (self.fileName, 'w') as saida:
                saida.write(self.texto1.toPlainText())
        except: pass
    def Clean(self):
        self.texto1.clear()
        self.line_scf.clear()
        self.line_dynmat.clear()
        self.statusBar.showMessage('')
        self.statusBar.setStyleSheet('background:gray')
    def Calcular(self): ## função que retorna resultados termodinâmicos
        if self.line_scf.text() != '' and self.line_dynmat.text() != '': #
            self.statusBar.showMessage('')
            self.statusBar.setStyleSheet('background:gray')
            try:
#----------------------------Sólidos------------------------------------------
                self.texto1.setReadOnly(True)
                if self.Solid.isChecked(): # computar solidos
                    tipo = 'solido'
                    dados = [tipo, # formato da resposta
                             self.line_scf.text(), # path scf.out
                             self.line_dynmat.text(), # path mat.out
                             self.T_min.text(), # temperatura mínima
                             self.T_max.text(), # temperatura máxima
                             0, # pressão
                             0, # número de simetria
                             None, #
                             self.deltaT.text()] # Delta
                    return modulo1.Termo(dados)
#----------------------------Moléculas----------------------------------------
                elif self.Molecule.isChecked():# computar sistemas moleculares
#----------------------------poliatômico--------------------------------------
                    if self.NoLinear.isChecked(): # poliatomico
                        tipo = 'molecula'
                        lin = 'nolinear'
                        dados = [tipo, # formato da resposta
                                 self.line_scf.text(), # path scf.out
                                 self.line_dynmat.text(), # path mat.out
                                 self.T_min.text(), # temperatura mínima
                                 self.T_max.text(), # temperatura máxima
                                 self.line_Press.text(), # pressão
                                 self.line_sym.text(), # número de simetria
                                 lin, # poliatomico
                                 self.deltaT.text()] # Delta T
                        return modulo1.Termo(dados)
#-----------------------------------------------------------------------------
#----------------------------linear-------------------------------------------
                    elif self.Linear.isChecked(): # linear
                        tipo = 'molecula'
                        lin = 'linear'
                        dados = [tipo, # formato da resposta
                                 self.line_scf.text(), # path scf.out
                                 self.line_dynmat.text(), # path mat.out
                                 self.T_min.text(), # temperatura mínima
                                 self.T_max.text(), # temperatura máxima
                                 self.line_Press.text(), # pressão
                                 self.line_sym.text(), # número de simetria
                                 lin, # poliatomico
                                 self.deltaT.text()] # Delta T
                        return modulo1.Termo(dados)
#-----------------------------------------------------------------------------
#----------------------------monoatômico--------------------------------------
                    elif self.Atoms.isChecked(): # computar atomos no vácuo
                        tipo = 'molecula'
                        lin = 'atomo'
                        dados = [tipo, # formato da resposta
                                 self.line_scf.text(), # path scf.out
                                 self.line_dynmat.text(), # path mat.out
                                 self.T_min.text(), # temperatura mínima
                                 self.T_max.text(), # temperatura máxima
                                 self.line_Press.text(), # pressão
                                 1, # número de simetria self.line_sym.text()
                                 lin, # monoatomico
                                 self.deltaT.text()] # Delta T
                        return modulo1.Termo(dados)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText("Verifique os arquivos inseridos")
                msg.setWindowTitle("Atenção")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
                returnValue = msg.exec()
               # if returnValue == 4194304: # Cancel
                    #pass
                if returnValue == 1024: # Ok
                    pass
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Verifique se todos os arquivos foram inseridos")
            msg.setWindowTitle("Atenção")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
            returnValue = msg.exec()
           # if returnValue == 4194304: # Cancel
                #pass
            if returnValue == 1024: # Ok
                pass
#-----------------------------------------------------------------------------
#---------------função para plotar os resultados na tela----------------------
    def Print(self):
        if self.Calcular() != None:
            self.texto1.setText(str(self.Calcular()))
        else:
            pass
###############################################################################
#-----------------------------------------------------------------------------
    def Leitura(self):
        T = [] # lista para armazenar as temperaturas
        U = [] # lista para armazenar energias internas
        S = [] # lista para armazenar entropia
        H = [] # lista para armazenar entalpia
        G = [] # lista para armazenar energias Gibbs
        A = [] # lista para armazenar energias de Helmholtz
        tempo = 'Dados do último cálculo '
        self.texto1.setReadOnly(True)
        with open(path+'/temps/temp.nyp', 'r') as data:
            for lines in data:
                if 'Criado' in lines:
                    tempo += lines[0:36]
                elif 'Funções termodinâmicas' in lines: #variável de controle
                    data.readline()#, data.readline()
                    break
            try:
                for lines in data:
                    d = lines.split()
                    T.append(d[0]), U.append(d[1]),S.append(d[2]),
                    H.append(d[3]), G.append(d[4]), A.append(d[5])
            except:
                pass
        return T, U, S, H, G, A, tempo
#----------------------Temperatura x Energia interna--------------------------
    def SetarU(self):
        Dados = self.Leitura()
        res = []
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage(Dados[6])
            self.statusBar.setStyleSheet("background:red")
        for  x, y in zip (Dados[0], Dados[1]):
            res.append(str(f'{x:^5}\t{y:^15}\n'))
        resultado ="".join(map(str,res))
        self.texto1.clear()
        self.texto1.setText(resultado)
#--------------------Temperatura x entropia-----------------------------------
    def SetarS(self):
        Dados = self.Leitura()
        res = []
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage(Dados[6])
            self.statusBar.setStyleSheet("background:red")
        for  x, y in zip (Dados[0], Dados[2]):
            res.append(str(f'{x:^5}\t{y:^15}\n'))
        resultado ="".join(map(str,res))
        self.texto1.clear()
        self.texto1.setText(resultado)
#-------------------Temperatura x entalpia------------------------------------
    def SetarH(self):
        Dados = self.Leitura()
        res = []
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage(Dados[6])
            self.statusBar.setStyleSheet("background:red")
        for  x, y in zip (Dados[0], Dados[3]):
            res.append(str(f'{x:^5}\t{y:^15}\n'))
        resultado ="".join(map(str,res))
        self.texto1.clear()
        self.texto1.setText(resultado)
#------------------Temperatura x enegia de Gibbs------------------------------
    def SetarG(self):
        Dados = self.Leitura()
        res = []
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage(Dados[6])
            self.statusBar.setStyleSheet("background:red")
        for  x, y in zip (Dados[0], Dados[4]):
            res.append(str(f'{x:^5}\t{y:^15}\n'))
        resultado ="".join(map(str,res))
        self.texto1.clear()
        self.texto1.setText(resultado)
#-----------------Temperatura x energia de Helmholtz --------------------------
    def SetarA(self):
        Dados = self.Leitura()
        res = []
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage(Dados[6])
            self.statusBar.setStyleSheet("background:red")
        for  x, y in zip (Dados[0], Dados[1]):
            res.append(str(f'{x:^5}\t{y:^15}\n'))
        resultado ="".join(map(str,res))
        self.texto1.clear()
        self.texto1.setText(resultado)
#----------------------------- Tudo -------------------------------------------
    def SetarTudo(self):
        if self.texto1.toPlainText() == '':
            self.statusBar.showMessage('Dados do último cálculo ')
            self.statusBar.setStyleSheet("background:red")
        with open(path+'/temps/temp.nyp', 'r') as data:
            resultado = data.read()
        self.texto1.clear()
        self.texto1.setText(resultado)   
#-----------------------------------------------------------------------------
    def FecharDef(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Deseja mesmo fechar?")
        msg.setWindowTitle("Atenção")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
        returnValue = msg.exec()
        if returnValue == 4194304: # Cancel
            pass
        if returnValue == 1024: # Ok
            self.close()
    def SimetriaDef(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('''Números de simetria para algumas moléculas
            H2O  \t 2
            CO2  \t 1
            C6H6 \t 12
            H2   \t 2
            O2   \t 2
            N2   \t 2
            HCl  \t 1
            HBr  \t 1
            HI   \t 1
            ''')
            msg.setWindowTitle("Números de simetria")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
            returnValue = msg.exec()
            if returnValue == 1024: # Ok ##4194304: # Cancel
                pass
    def ConvertDef(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('''
            1.0 Ry:
                    = 0.5 hartree
                    = 13.605691930242388 eV
                    = 1312.7496997450642 kJ/mol
                    = 313.75470835207074 kcal/mol
                    = 2.17987197e-21 kJ
                    = 5.21001904875717e-22 kcal''')
            msg.setWindowTitle("Fatores de conversão")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
            returnValue = msg.exec()
            if returnValue == 1024: # Ok
                pass
    def SobreDef(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('''
            Software para calcular funções termodinâmicas
                    autor: Márcio F. Santos
                    email: marciofs600@gmail.com
            Ícones usados:
            "https://www.flaticon.com/br/icones-gratis/seo-e-web''')
            msg.setWindowTitle("Sobre")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
            returnValue = msg.exec()
            if returnValue == 1024: # Ok
                pass
    def AjudaDef(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("""
            # NOTAS DE USO:
            Software desenvolvido para ler arquivos de saída do pacote computacional Quantum Espresso v>=6.4.1
            A temperatura mínima deve ser diferente da máxima.  
            
            Após inserir todos os dados, basta clicar em "Calcular" que o resultado será plotado na tela.

            Teclas de atalho para exibir funções separadas.

                        F7 = 'Temperatura x E_interna
                        F8 = 'Temperatura x Entropia
                        F9 = 'Temperatura x Entalpia
                        F10 = 'Temperatura x E_Gibbs
                        F11 = 'Temperatura x E_Helmholtz

            Para salvar os dados, basta clicar em "Salvar"
            
            Mais informações: leia o arquivo README.md""")
            msg.setWindowTitle("Ajuda")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok )#| QMessageBox.Cancel)
            returnValue = msg.exec()
           # if returnValue == 4194304: # Cancel
                #pass
            if returnValue == 1024: # Ok
                pass
#------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec()

if __name__ == '__main__':
    main()
