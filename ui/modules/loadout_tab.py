import customtkinter
from src import *
from src.vars import win_size, editor_list

class Loadout_Tab(customtkinter.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self._add_button()
        self._add_text()

        self.pack(fill='both', expand=True)
        
    def _add_button(self):

        gen_btn = customtkinter.CTkButton(self, text='Generate Loadout', command=self.get_loadout)
        gen_btn.pack(fill='x')

    def _add_text(self):

        width = int(win_size.split('x')[0])
        width = width * 0.9

        self.text_area = customtkinter.CTkLabel(
            self,
            text='Loadout will appear here after the button is pressed.',
            anchor='center',
            wraplength=width
        )
        self.text_area.pack(fill='both', expand=True)

    def get_loadout(self):
         
        self.loadout = ''

        self.loadout += Get_Main()()
        self.loadout = '\n\n'.join([self.loadout, Get_Stratagems()()])

        self.text_area.configure(text=self.loadout)