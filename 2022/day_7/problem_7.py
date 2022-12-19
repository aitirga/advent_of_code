import numpy as np

class File:
    def __init__(self, filename, path, weight):
        self.filename = filename
        self.path = path
        self.weight = weight

    def __repr__(self):
        return f"File({self.filename}, {self.weight})"

class FilesystemReader:
    def __init__(self, path, total_space=70000000):
        self.path = path
        self.commands = []
        self.read_file()
        self.filesystem = {'/': {}}
        self.cur_pos = '/'
        self.total_space = total_space
        self.build_filesystem()

    def read_file(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()
            self.commands = [line.strip() for line in lines]

    def build_filesystem(self):
        for line_idx in range(len(self.commands)):
            cur_line = self.commands[line_idx]
            if '$' in cur_line:
                split_line = cur_line.split(' ')
                if split_line[1] == 'cd':
                    self.process_cd(cur_line)
                if split_line[1] == 'ls':
                    ls_flag = True
                    while ls_flag:
                        if line_idx + 1 >= len(self.commands):
                            break
                        line_idx += 1
                        cur_line = self.commands[line_idx]
                        if '$' in cur_line:
                            ls_flag = False
                        else:
                            current_filesystem_dict = self.get_folder_in_filesystem(self.cur_pos)
                            if 'dir' in cur_line:
                                # Add to filesystem
                                current_filesystem_dict[cur_line.split(' ')[-1]] = {}
                            else:
                                current_filesystem_dict[cur_line.split(' ')[-1]] = File(cur_line.split(' ')[-1], self.cur_pos, int(cur_line.split(' ')[-2]))

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

    def get_folder_in_filesystem(self, pos: str):
        cur_list = self.get_current_list(pos)
        last_filesystem_point = self.filesystem
        for parent in cur_list:
            last_filesystem_point = last_filesystem_point.get(parent)
        return last_filesystem_point

    def process_command(self, line):
        if 'cd' in line:
            self.process_cd(line)

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

    def get_pathdict_weight(self, pathdict: dict):
        weight = 0
        def get_weigth(pathdict: dict):
            nonlocal weight
            for key, value in pathdict.items():
                if isinstance(value, dict):
                    get_weigth(value)
                elif isinstance(value, File):
                    weight += value.weight

        get_weigth(pathdict)
        return weight

    def __str__(self):
        return str(filesystem.filesystem)

    def __repr__(self):
        return filesystem.filesystem


    def filter_by_weigth(self, min_weight):
        folders = []
        def recurrent_filter(filesystem_dict):
            nonlocal folders
            for key, value in filesystem_dict.items():
                if isinstance(value, dict):
                    weight = self.get_pathdict_weight(value)
                    if weight < min_weight:
                        folders.append(weight)
                        pass
                    recurrent_filter(value)
        recurrent_filter(self.filesystem_nonroot)
        return folders

    def find_smallest_directory(self, target_filesystem_weigth=4E6):
        folder_weight = 0
        target_weigth = abs(self.free_space - target_filesystem_weigth)
        folders = []
        def recurrent_filter(filesystem_dict):
            nonlocal folder_weight
            for key, value in filesystem_dict.items():
                if isinstance(value, dict):
                    weight = self.get_pathdict_weight(value)
                    if weight > target_weigth:
                        folders.append(weight)
                    recurrent_filter(value)
        recurrent_filter(self.filesystem_nonroot)

        return np.array(folders).min()

    @property
    def filesystem_nonroot(self):
        return filesystem.filesystem['/']

    @property
    def filesystem_weight(self):
        return self.get_pathdict_weight(self.filesystem)

    @property
    def free_space(self):
        return self.total_space - self.filesystem_weight


if __name__ == '__main__':
    filesystem = FilesystemReader('./input_7.dat')
    folders = filesystem.filter_by_weigth(100000)
    min_folder_weight = filesystem.find_smallest_directory(30000000)



