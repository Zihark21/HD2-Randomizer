import customtkinter, os, sys
from .modules import *
from src.vars import win_size, tab_list
from src.__version__ import version

class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        customtkinter.set_appearance_mode('dark')

        ico_path = os.path.join('assets', 'HD2.ico')
            
        self.iconbitmap(ico_path)
        self.title(f'HD2 Randomizer - v{version}')
        self.geometry(win_size)
        self.resizable(False, False)

        self.tabs = Tabs(self, tab_list)
        Loadout_Tab(self.tabs.tab('Loadout'))
        Editor_Tab(self.tabs.tab('Editor'))