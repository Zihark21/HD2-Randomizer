import customtkinter, os, sys
from .modules import *
from src.vars import win_size, tab_list
from src.__version__ import version

class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme(os.path.join('assets', 'HD2_Theme.json'))

        ico_path = os.path.join('assets', 'HD2.ico')
            
        self.iconbitmap(ico_path)
        self.title(f'HD2 Randomizer - v{version}')
        self.center_window()

        self.tabs = Tabs(self, tab_list)
        Loadout_Tab(self.tabs.tab('Loadout'))
        # Options tab to be added here
        Editor_Tab(self.tabs.tab('Editor'))

    def center_window(self):

        self.update()
        self.update_idletasks()
        self.resizable(False, False)

        scale = customtkinter.ScalingTracker.get_window_dpi_scaling(self)

        sw = int(self.winfo_screenwidth() * scale // 2)
        sh = int(self.winfo_screenheight() * scale // 2)

        geo = self._parse_geometry_string(win_size)

        pos_x = int(sw - (geo[0] // 2))
        pos_y = int(sh - (geo[1] // 2))

        self.geometry(f'{win_size}+{pos_x}+{pos_y}')