import customtkinter, glob, os, sys

class Editor_Tab(customtkinter.CTkFrame):

    def __init__(self, master):

        super().__init__(master)
        self.pack(fill='both', expand=True)

        self.set_statics()

        menu = customtkinter.CTkOptionMenu(self, values=self.edit_list, command=lambda opt: self.get_list(opt))
        menu.set('')
        menu.pack(fill='x')

        self.edit_frame = customtkinter.CTkScrollableFrame(self)
        self.edit_frame.pack(fill='both', expand=True)

        tog_btn = customtkinter.CTkButton(self, text='Invert Selection', command=self.toggle_data)
        tog_btn.pack(fill='x', pady=5)

        save_btn = customtkinter.CTkButton(self, text='Save Current Selection', command=self.save_list)
        save_btn.pack(fill='x')

    def set_statics(self):

        self.edit_paths = glob.glob(os.path.join('lists', '*.txt'))
        self.edit_list = []

        for path in self.edit_paths:
            temp = os.path.split(path)[-1].replace('.txt', '')
            self.edit_list.append(temp)

    def update_frame(self, opts):

        try:
            for widget in self.widgets:
                widget.destroy()
        except:
            pass

        self.widgets = []
        self.edit_frame._parent_canvas.yview_moveto(0)

        for opt, unlock in opts:
            if unlock == 'Header':
                label = customtkinter.CTkLabel(self.edit_frame, text=opt)
                label.pack(fill='x')
                self.widgets.append(label)
            else:
                checkbox = customtkinter.CTkCheckBox(self.edit_frame, text=opt)
                checkbox.pack(anchor='w')
                if unlock == 'True':
                    checkbox.select()
                self.widgets.append(checkbox)

    def toggle_data(self):
        for widget in self.widgets:
            if isinstance(widget, customtkinter.CTkCheckBox):
                widget.toggle()

    def set_index(self, opt):

        opt_list = self.edit_list.index(opt)
        self.opt_path = self.edit_paths[opt_list]

    def get_list(self, opt):

        self.set_index(opt)

        content = open(self.opt_path, 'r').read()

        if content:

            items = []

            sections = content.split('\n\n')

            for section in sections:

                lines = section.split('\n')

                for line in lines:

                    temp = []

                    line = line.strip("()")
                    item, status = line.split(', ') 

                    temp.append(item)
                    temp.append(status)

                    items.append(temp)

            self.update_frame(items)

        else:

            return 'No data found'

    def save_list(self):

        text_list = []
        text = ''

        for widget in self.widgets:
            if isinstance(widget, customtkinter.CTkCheckBox):
                text_list.extend([(widget.cget('text'), widget.get())])
            elif isinstance(widget, customtkinter.CTkLabel):
                text_list.extend([(widget.cget('text'), 'Header')])

        for i in text_list:
            item, status = i
            if status == 'Header':
                text += f'\n({item}, Header)\n'
            elif status == 1:
                text += f'({item}, {True})\n'
            else:
                text += f'({item}, {False})\n'

        text = text.strip()

        open(self.opt_path, 'w').write(text)