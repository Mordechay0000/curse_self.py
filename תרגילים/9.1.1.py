def are_files_equal(file1, file2):
    def read_file(file):
        with open(file, 'r') as f:
            return f.read()
    return read_file(file1) == read_file(file2)