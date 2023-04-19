import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup

class WebBrowserApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Web Browser App")
        self.url_entry = ttk.Entry(self.parent, width=50)
        self.url_entry.pack(side=tk.TOP, fill=tk.X)
        self.word_count_label = ttk.Label(self.parent, text="")
        self.word_count_label.pack(side=tk.TOP)
        self.fetch_button = ttk.Button(self.parent, text="Fetch", command=self.fetch_website)
        self.fetch_button.pack(side=tk.TOP)

    def fetch_website(self):
        url = self.url_entry.get()
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        word_count = len(text.split())
        self.word_count_label.config(text="Word count: {}".format(word_count))

if __name__ == "__main__":
    root = tk.Tk()
    app = WebBrowserApp(root)
    root.mainloop()
