import random, glob, os, sys
from src.vars import editor_list

class Get_Main:

    def __init__(self):

        self.output = {}
        self.read_data()

    def read_data(self):

        all_files = glob.glob(os.path.join('lists', '*.txt'))

        filtered_files = [file for file in all_files if 'stg' not in os.path.basename(file)]

        for file in filtered_files:
            
            self.items = []

            self.name = os.path.split(file)[-1].replace('.txt', '').title()

            self.data = open(file, 'r', encoding="utf-8").read()
            self.parse_data()

    def parse_data(self):

        sections = self.data.split('\n\n')

        for section in sections:

            items = []

            lines = section.split('\n')

            for line in lines:

                line = line.strip("()")
                item, status = line.split(', ') 

                if status == 'Header':
                    header = item
                if status == 'True':
                    items.append(item)

            items = [(item, header) for item in items]

            for item in items:
                self.items.append(item)

        self.get_selection()

    def get_selection(self):

        if not self.items:
            self.output[self.name] =  ('None', 'No Data Found')
        else:
            item, header = random.choice(self.items)
            self.output[self.name] =  (header, item)
    
    def __call__(self):

        if not self.output:
            return "No data available"

        text = ''
        selections = [x for x in editor_list if "STG" not in x]

        for sel in selections:
            header, item = self.output[sel]

            text += f'{sel}: {header}\n{item}\n\n'

        text = text.strip()

        return text