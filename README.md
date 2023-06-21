# URL PDF Remover v. 1.0

## Description
URL PDF Remover v. 1.0 is a straightforward graphical user interface (GUI) application designed to remove the 'where from' metadata from PDF files. It can process both single PDF files and entire folders containing multiple PDF files. By removing 'where from' metadata, the application enhances the privacy and confidentiality of your documents, eliminating potential traces of their original source.

## Features

- User-friendly GUI for ease of use.
- The ability to process single PDF files and entire folders.
- Privacy-focused, removes 'where from' metadata from PDF files.

## Installation & Requirements

This application is written in Python, and thus requires Python 3.7+ to run. Additionally, it uses the following Python libraries: 

- `os`
- `tkinter`
- `tkinter.filedialog`
- `xattr`

You can install the required Python libraries using pip:

```
pip install xattr
```

## Usage

1. Launch the script: `python3 url_pdf.py`
2. The GUI will display two buttons: "Select File" and "Select Folder".
3. Click the relevant button to select a single PDF file or a folder containing PDF files.
4. Once a file or a folder is selected, the application will automatically process the selected PDF files, removing the 'where from' metadata.
5. Upon successful completion, a confirmation message will pop up to inform you that the operation is complete.

## License
This application is free software. Feel free to modify and distribute it under the terms of the license.

## Contributing
Contributions are welcome. Please feel free to fork the project and submit pull requests. 

## Disclaimer
This application is provided as-is. Please make sure you have backups of your documents before using this tool. We are not responsible for any potential loss of data. 

## Contact
If you have any questions, suggestions, or bugs to report, please open an issue on the GitHub page.
