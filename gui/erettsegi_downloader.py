import tkinter as tk
from tkinter import messagebox
import pygubu
import os
from letolt import letolt

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

#globalis_valtozok:
path = None
targy = None
ev = None
mo = None
szint= None

class MyApplication:

    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file(os.path.join(CURRENT_DIR, 'erettsegi_mainframe.ui'))

        self.mainwindow = builder.get_object('mainwindow')
        
        self.filepath = builder.get_object('filepath')
        self.evek = builder.get_object('evek')
        self.targyak = builder.get_object('targyak')
        builder.connect_callbacks(self)
        
    def path_changed(self, event=None):
        global path
        path = self.filepath.cget('path')
    
    def letoltes_clicked(self):
        letolt(ev, mo, szint, targy, path)
        messagebox.showinfo('Érettségi Downloader', 'A letöltés elkészült')

    def kozep_selected(self):
        global szint
        szint = 'kozep'

    def emelt_selected(self):
        global szint
        szint = 'emelt'

    def tavasz_selected(self):
        global mo
        mo = 'maj'
        
    def osz_selected(self):
        global mo
        mo = 'okt'

    def ev_selected(self, event=None):
        global ev
        ev = self.evek.get()[2:4]

    def targy_selected(self, event=None):
        global targy
        if self.targyak.get() == 'magyar_irodalom':
            targy = 'magyir'
        elif self.targyak.get() == 'történelem':
            targy = 'tort'
        elif self.targyak.get() == 'matematika':
            targy = 'mat'
        elif self.targyak.get() == 'német':
            targy = 'nemet'
        elif self.targyak.get() == 'informatika':
            targy = 'inf'
    
    def quit(self, event=None):
        self.mainwindow.quit()

    def run(self):
        self.mainwindow.mainloop()
        
if __name__ == '__main__':
    #root = tk.Tk()
    app = MyApplication()
    app.run()
