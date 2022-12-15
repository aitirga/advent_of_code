import numpy as np

class File:
    def __init__(self, filename, path, weight):
        self.filename = filename
        self.path = path
        self.weight = weight

class FilesystemReader:
    def __init__(self, path):
        self.path = path
        self.commands = []
        self.read_file()
        self.filesystem = {'/': {}}
        self.cur_pos = '/'

    def read_file(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()
            self.commands = [line.strip() for line in lines]

    def build_filesystem(self):
        for line_idx in range(len(self.commands)):
            cur_line = self.commands[line_idx]
            if '$' in cur_line:
                self.process_command(cur_line)

    def process_command(self, line):
        pass







if __name__ == '__main__':
    filesystem = FilesystemReader('./input_7.dat')
    filesystem.build_filesystem()

