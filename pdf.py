
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView

from os import path
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("PDF Viewer")
        self.resize(1000,750)
 
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)
        self.showDialog1()

    def showDialog1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open PDF file')
        if fname[0]:
            print(fname[0])
            self.webView.setUrl(QUrl("file:///" + fname[0]))

if __name__ == '__main__':
 
    import sys
    app = QApplication([])
    ex = Window()
    ex.show()
    app.exec()
