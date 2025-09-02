class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            content = file.readlines()
        return content

    def parse_data(self, lines):
        data = []
        for line in lines:
            name, email = line.strip().split(',')
            data.append({'name': name, 'email': email})
        return data