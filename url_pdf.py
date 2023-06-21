import os
import xattr
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFMetadataRemover:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF Metadata Remover")
        self.root.geometry('300x200')

        # Create a label to display the title
        self.title_label = tk.Label(self.root, text="URL PDF REMOVER v. 1.0", fg='orange', font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.file_or_folder = tk.BooleanVar()
        self.file_or_folder.set(False) # default is file selection
        
        self.select_file_button = tk.Checkbutton(self.root, text="Select Folder", variable=self.file_or_folder,
                                                onvalue=True, offvalue=False, command=self.change_select_mode, fg='white')
        self.select_file_button.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file_or_folder)
        self.select_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="QUIT", fg="red", command=self.root.quit)
        self.quit_button.pack(pady=10)

        tk.mainloop()

    def change_select_mode(self):
        if self.file_or_folder.get() == True: # folder selection mode
            self.select_button.config(text="Select Folder")
        else:
            self.select_button.config(text="Select File")

    def select_file_or_folder(self):
        if self.file_or_folder.get() == True: # folder selection
            path = filedialog.askdirectory()
            self.remove_where_from_attribute(path)
        else: # file selection
            path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
            self.remove_single_file_metadata(path)
            
        messagebox.showinfo("Info", "Metadata removal completed!")

    def remove_where_from_attribute(self, input_folder):
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".pdf"):
                    self.remove_single_file_metadata(os.path.join(root, file))

    def remove_single_file_metadata(self, input_path):
        try:
            attr = xattr.getxattr(input_path, 'com.apple.metadata:kMDItemWhereFroms')
            xattr.removexattr(input_path, 'com.apple.metadata:kMDItemWhereFroms')
            print(f"Removed where from metadata from {input_path}")
        except (KeyError, OSError, IOError):
            print(f"No 'where from' metadata found for {input_path}")

if __name__ == "__main__":
    app = PDFMetadataRemover()
