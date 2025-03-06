import random, os, glob, sys

class Get_Stratagems:

    def __init__(self):

        self.items = []
        self.stgs = []
        self.output = 'Strategems:'
        self.read_data()

    def read_data(self):

        files = glob.glob(os.path.join('lists', '*stg*.txt'))

        for file in files:

            data = open(file, 'r', encoding="utf-8").read()
            data = self.parse_data(data)

            if 'backpacks' in file:
                self.bps = data
            if 'support_weapons' in file:
                self.sw = data
                self.sw_bp = [x for x in self.sw if "*" in x]

            self.items.extend(item for item in data)

        self.get_selection()

    def parse_data(self, data):

        temp = []

        lines = data.split('\n')

        for line in lines:

            line = line.strip("()")
            item, status = line.split(', ') 

            if status == 'True':
                temp.append(item)

        return temp
    
    def get_selection(self):

        if not self.items:
            return "No data available"

        for _ in range(4):

            opt = random.choice(self.items)

            self.items = [x for x in self.items if x != opt]

            if opt in self.sw:
                self.items = [x for x in self.items if x not in self.sw]
                if opt in self.sw_bp:
                    self.items = [x for x in self.items if x not in self.bps]
            if opt in self.bps:
                self.items = [x for x in self.items if x not in self.sw_bp]
                self.items = [x for x in self.items if x not in self.bps]

            self.stgs.append(opt)

    def __call__(self):

        for stg in self.stgs:
            self.output = '\n'.join([self.output, stg])

        self.output.strip()

        return self.output