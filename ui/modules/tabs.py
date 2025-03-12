import customtkinter

class Tabs(customtkinter.CTkTabview):

    def __init__(self, master, tabs):
        
        super().__init__(master)

        CTkTabview_Theme = {
            "segmented_button_selected_color": '#DAC703',
            "segmented_button_selected_hover_color": '#B5A203',
            "segmented_button_unselected_hover_color": '#B5A203',
            "text_color": 'black'
        }

        self.configure(**CTkTabview_Theme)

        for tab in tabs:
            self.add(tab)

        self.pack(fill='both', expand=True)