#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

PDFJS = "%s%s" %("file://",os.path.abspath('./pdfjs/web/viewer.html'))
PDF = "%s%s" %("file://", "%20".join(sys.argv[1:]))
print("loading PDF File:", PDF)

class Window(QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.load(QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec_())
    
