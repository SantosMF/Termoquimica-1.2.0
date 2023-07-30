# Arquivo: Makefile
Interface.py: Interface.ui
	pyuic6 Interface.ui -o Interface.py
