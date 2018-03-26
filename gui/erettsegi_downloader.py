import tkinter as tk
from tkinter import messagebox
import pygubu


#globalis_valtozok:
path = None
kozep = None
emelt = None
tavasz = None
osz = None

class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('erettsegi_downloader_gui.ui')

        self.mainwindow = builder.get_object('Frame_1', self.master) 
        self.filepath = builder.get_object('filepath')
        
        builder.connect_callbacks(self)
        
    def path_changed(self, event=None):
        global path
        path = self.filepath.cget('path')
    
    def letoltes_clicked(self):
        messagebox.showinfo('Érettségi Downloader', 'A letöltés elkészült')

    def kozep_selected(self):
        global kozep
        kozep = 1

    def emelt_selected(self):
        global emelt
        emelt = 1

    def tavasz_selected(self):
        global tavasz
        tavasz = 1
    
    def osz_selected(self):
        global osz
        osz = 1

    
if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()
