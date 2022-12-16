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

    def process_cd(self, line: str):
        line = line.split(' ')
        if line[-1] == '..':
            self.cur_pos = '/'.join(self.cur_pos.split('/')[:-1])
        elif line[-1] == '/':
            self.cur_pos = '/'
        else:
            if len(self.cur_pos) == 1:
                self.cur_pos += line[-1]
            else:
                self.cur_pos += '/' + line[-1]
        self.add_to_filesystem(self.cur_pos)


    def process_command(self, line):
        if 'cd' in line:
            self.process_cd(line)
        if 'ls' in line:
            pass

    def add_to_filesystem(self, cur_pos: str):
        parents = self.get_current_list(cur_pos)
        # Access to the n-th depth in the filesystem
        last_filesystem_point = self.filesystem
        for parent in parents[:-1]:
            last_filesystem_point = last_filesystem_point.get(parent)
        if last_filesystem_point.get(parents[-1]) is None:
            last_filesystem_point[parents[-1]] = {}






    def get_depth(self, pos: str):
        return pos.count('/')

    def get_current_depth(self):
        return self.get_depth(self.cur_pos)

    def get_parent(self, pos: str):
        return '/'.join(pos.split('/')[:-1])

    def get_current_parent(self):
        return self.get_parent(self.cur_pos)

    def get_current_list(self, pos: str):
        cur_list = pos.split('/')
        cur_list[0] = '/'
        if cur_list[-1] == '':
            cur_list = cur_list[:-1]
        return cur_list








if __name__ == '__main__':
    filesystem = FilesystemReader('./input_7.dat')
    filesystem.build_filesystem()

