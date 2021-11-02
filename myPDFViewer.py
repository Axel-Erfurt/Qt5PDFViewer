#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

root = os.path.dirname(sys.argv[0])
PDFJS = f"file://{os.path.abspath('./web/viewer.html')}"
print(PDFJS)
PDF = f'file://{"%20".join(sys.argv[1:])}'
print("loading PDF:", PDF)

class Window(QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        if len(sys.argv) > 1:
            self.load(QUrl.fromUserInput(f'{PDFJS}?file={PDF}'))
        else:
            self.load(QUrl.fromUserInput(f"{PDFJS}?file=file://{root}/test.pdf"))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec_())
    
