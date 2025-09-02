# filepath: greeting-server/greeting-server/src/main.py

from file_reader import FileReader
from emailer import Emailer
from config import DATA_FILE_PATH

def main():
    # Initialize FileReader and Emailer
    file_reader = FileReader()
    emailer = Emailer()

    # Fetch data from the file
    data = file_reader.read_file(DATA_FILE_PATH)
    parsed_data = file_reader.parse_data(data)

    # Send greeting emails
    for recipient in parsed_data:
        emailer.send_email(recipient)

if __name__ == "__main__":
    main()