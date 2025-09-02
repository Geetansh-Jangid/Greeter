# Greeting Server

This project is a simple server application that fetches data from a file and sends greeting emails to the specified recipients. It is structured to separate concerns, with dedicated modules for reading files and sending emails.

## Project Structure

```
greeting-server
├── src
│   ├── main.py          # Entry point of the application
│   ├── emailer.py       # Handles email sending functionality
│   ├── file_reader.py    # Reads and processes data from files
│   └── config.py        # Configuration settings
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd greeting-server
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure SMTP settings**:
   Update the `src/config.py` file with your SMTP server details and the path to the data file.

4. **Run the application**:
   Execute the main script:
   ```
   python src/main.py
   ```

## Usage

- The application reads recipient data from a specified file and sends greeting emails based on that data.
- Ensure that the data file is formatted correctly as per the requirements defined in `src/file_reader.py`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.