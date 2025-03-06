import customtkinter

class Tabs(customtkinter.CTkTabview):

    def __init__(self, master, tabs):
        
        super().__init__(master)

        for tab in tabs:
            self.add(tab)

        self.pack(fill='both', expand=True)