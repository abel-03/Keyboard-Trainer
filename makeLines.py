import random

def makeLines(self):
    with open('txt/texts') as f:
        self.lines = [line for line in f.read().split('\n') if line.strip() != '']
    random.shuffle(self.lines)
    self.line_number = -1