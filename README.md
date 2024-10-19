# pdf_manipulation_tool

**Disclaimer**: This tool is provided for educational purposes only. Use it responsibly and in accordance with applicable laws and regulations. The developer is not responsible for any misuse of this software.

**pdf_manipulation_tool** is a powerful tool for manipulating PDF files, allowing you to embed executable files, add commands, extract text, and perform other advanced operations. This tool is designed for developers and users looking for enhanced PDF manipulation capabilities.

## Features
- **Embed `.exe` Files**: Insert executable files directly into PDF documents.
- **Add Commands**: Include metadata commands within PDF files for various applications.
- **Extract Text**: Retrieve text content from PDFs and save it to text files.
- **Add URLs**: (Functionality to be implemented) Allow the inclusion of URLs within PDF metadata.
- **Cross-Platform Compatibility**: Works on both Linux and Windows systems.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [On Linux](#on-linux)
  - [On Windows](#on-windows)
  - [On Termux](#on-termux)
  - [Common Arguments](#common-arguments)
  - [Examples](#examples)
- [Error Handling](#error-handling)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
Ensure you have the following software installed on your machine:
- **Python 3.6 or higher**: You can download it from [python.org](https://www.python.org/downloads/). Follow the installation instructions for your operating system.
- **Pip**: The package installer for Python, typically included with Python installations. Verify its installation with:
  ```bash
  pip --version
  ```

### Clone the Repository
1. **Open a terminal** (Linux) or **Command Prompt** (Windows).
2. Execute the following commands to clone the repository:
   ```bash
   git clone https://github.com/yahyasvm/pdf-manipulation-tool.git
   cd pdf-manipulation-tool
   ```

### Install Dependencies
After cloning the repository, install the required Python libraries by running:
```bash
pip install -r requirements.txt
```
This command will ensure all necessary dependencies are installed for **pdf_manipulation_tool** to function properly.

## Usage

### On Linux
1. Open a terminal.
2. Navigate to the project directory:
   ```bash
   cd /path/to/pdf-manipulation-tool
   ```
3. Run the script using the desired options:
   ```bash
   python pdf_manipulation_tool.py <pdf_path> [--url <url>] [--exe <exe_path>] [--command <command>] [--extract]
   ```

### On Windows
1. Open Command Prompt or PowerShell.
2. Change to the project directory:
   ```bash
   cd C:\path\to\pdf-manipulation-tool
   ```
3. Execute the script with appropriate parameters:
   ```bash
   python pdf_manipulation_tool.py <pdf_path> [--url <url>] [--exe <exe_path>] [--command <command>] [--extract]
   ```

### On Termux
1. **Install Termux**: Download and install the Termux app from F-Droid or the Play Store.
2. **Open Termux and update the package list**:
   ```bash
   pkg update && pkg upgrade
   ```
3. **Install Python and Git**:
   ```bash
   pkg install python git
   ```
4. **Clone the repository**:
   ```bash
   git clone https://github.com/yahyasvm/pdf-manipulation-tool.git
   cd pdf-manipulation-tool
   ```
5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the script with the desired options**:
   ```bash
   python pdf_manipulation_tool.py <pdf_path> [--url <url>] [--exe <exe_path>] [--command <command>] [--extract]
   ```

## Common Arguments
- `pdf_path`: Specify the path to the PDF file you want to manipulate. This is a required argument.
- `--url`: (Upcoming feature) URL to be added to the PDF. Currently not implemented.
- `--exe`: Path to the `.exe` file you wish to embed within the PDF. Ensure the path is correct.
- `--command`: Command that will be added to the PDF's metadata. Useful for various applications.
- `--extract`: Flag to indicate that you want to extract text from the specified PDF. Use without additional arguments to save the extracted text.

## Examples
1. **Embed an `.exe` file**:
   ```bash
   python pdf_manipulation_tool.py document.pdf --exe example.exe
   ```
   This command will embed `example.exe` into `document.pdf`, creating a modified PDF with the executable.

2. **Add a command to a PDF**:
   ```bash
   python pdf_manipulation_tool.py document.pdf --command "This is a test command"
   ```
   This command will add the specified command as metadata to the PDF.

3. **Extract text from a PDF**:
   ```bash
   python pdf_manipulation_tool.py document.pdf --extract
   ```
   This command will extract the text content from `document.pdf` and save it to a text file named `extracted_text_from_document.txt`.

## Error Handling
**pdf_manipulation_tool** includes built-in error handling to provide informative messages. Here are some common errors and their messages:
- **File Not Found**: If the specified PDF file does not exist, you will see:
  ```
  Error: File '<pdf_path>' not found.
  ```
- **Invalid Executable Path**: If the provided `.exe` file path is incorrect or not a file, you will see:
  ```
  Error: '<exe_path>' is not a file.
  ```
- **PDF Processing Errors**: For any issues with reading or writing PDF files, appropriate error messages will be logged, such as:
  ```
  Error while processing PDF: <error_message>
  ```
- **Permissions Issues**: Ensure you have the necessary read/write permissions for the files and directories you are accessing.

## Future Improvements
- Implement the functionality to add URLs to PDFs.
- Enhance error reporting and logging for better debugging.
- Create a graphical user interface (GUI) for easier access to features.
- Add support for batch processing of multiple PDF files.

## Contributing
Contributions are welcome! If you have ideas for improvements or new features, please fork the repository and submit a pull request. Make sure to follow the contribution guidelines.

## License
© 2024 YahyaSvm. All rights reserved. This code is provided as-is and may not be reproduced without permission.
