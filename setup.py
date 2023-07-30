#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path = os.path.dirname(os.path.realpath(__file__))
os.system("sudo apt install python3-pip -y")
os.system("sudo apt install qt6-base-dev -y")
os.system("python3 -m pip install numpy")
os.system("python3 -m pip install pyqt6")
os.system("chmod u+x main.py")
print(50*'=')
print("bibliotecas instaladas")
print("Criando desktop icone")
print(path)
texto = f"""[Desktop Entry]
Name=Termoquimica
Exec=bash -c "{path}/main.py -url %U"
Icon={path}/temps/ico2.png
Type=Application
Terminal=false
Categories=Science;Chemistry;Physics;Education;
MimeType=outhers
X-GNOME-SingleWindow=true
Name[pt_BR]=termoquimica
Comment=Program para calcular funções termodinâmicas
"""
with open (path+"/termoquimica.desktop", 'w') as saida:
    saida.write(texto)
print(" rm  ~/.local/share/applications/termoquimica.desktop")
os.system(" rm  ~/.local/share/applications/termoquimica.desktop")
print(f"ln -s {path}/termoquimica.desktop  ~/.local/share/applications/termoquimica.desktop")
os.system(f"ln -s {path}/termoquimica.desktop  ~/.local/share/applications/termoquimica.desktop")
print("done")
