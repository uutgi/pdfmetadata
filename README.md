# PDF Metadata Remover v2.0

## Description
PDF Metadata Remover v2.0 is a user-friendly graphical user interface (GUI) application designed to remove the 'where from' metadata from PDF files. This tool is capable of processing both individual PDF files and entire folders containing multiple PDFs. By removing the 'where from' metadata, the application enhances the privacy and confidentiality of your documents, eliminating potential traces of their original source.

## Features

- Intuitive GUI for easy navigation.
- Support for processing single PDF files and entire directories.
- Privacy-focused: Removes 'where from' metadata from PDF files.

## Installation & Requirements

This application is written in Python and requires Python 3.7 or higher to run. It also depends on the following Python libraries:

- `os`
- `tkinter`
- `tkinter.filedialog`
- `xattr`

You can install the necessary Python libraries using pip:

- `pip install xattr`

## Usage

To run the application, execute the following command: python3 pdf_metadata_remover.py
The GUI will display two buttons: "Select File" and "Select Folder."
Click the relevant button to choose either a single PDF file or a folder containing multiple PDF files.
Once you've made your selection, the application will automatically process the chosen PDF files, removing the 'where from' metadata.
Upon successful completion, a confirmation message will pop up, informing you that the operation has been completed.
License

This application is free software. Feel free to modify and distribute it under the terms of the license.

## Contributing

Contributions are welcome. Please feel free to fork the project and submit pull requests.

## Disclaimer

This application is provided as-is. Please ensure you have backups of your documents before using this tool. We are not responsible for any potential loss of data.

## Contact

If you have any questions, suggestions, or wish to report bugs, please open an issue on the GitHub repository page.

Please make sure to adapt the file name (`pdf_metadata_remover.py`) and other details as needed to match the actual file and project structure.
