class XYZ:
    def __init__(self, path):
        self.path = path
        
    def write(self, number_of_atoms, comment_line, element, coords):
        with open(self.path, 'w') as f:
            f.write(f'{number_of_atoms}\n')
            f.write(f'{comment_line}\n')
            for x, y, z in coords:
                f.write(f'{element}\t{x:g}\t{y:g}\t{z:g}\n')

    def read(self, path):
        pass
