from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from PyQt6.QtGui import QAction
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.action = []
        self.pdf_file = ''
        self.isFirst = True 
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("PDF Viewer")
        self.resize(1000,750)
 
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.webView.urlChanged.connect(self.onLoadFinished)

        self.setCentralWidget(self.webView)

        self.menubar = self.menuBar()

        self.file_menu = self.menubar.addMenu('ファイル')
        self.new_file =QAction('新規ファイル')
        self.file_menu.addAction(self.new_file)
        self.new_file.triggered.connect(self.showDialog1)        

        self.mokuji_menu = self.menubar.addMenu('目次')

        self.showDialog1()
        
    def showDialog1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open PDF file', '', 'PDF files (*.pdf | *.PDF)')
        if fname[0]:

            self.pdf_file = fname[0]
            self.webView.load(QUrl("file:///" + self.pdf_file))

            self.mokuji_menu.clear()
            self.mokuji_dict = {}
            self.action = []
            text_file = fname[0].replace('.PDF', '.txt').replace('.pdf', '.txt')
            with open(text_file, 'r', encoding='UTF-8') as f:
                for data in f:
                    data = data.rstrip()
                    each_line = data.split(',')
                    self.action.append(QAction(each_line[1].strip()))
                    self.mokuji_menu.addAction(self.action[-1])
                    self.action[-1].triggered.connect(lambda state, x = each_line[0].strip(): self.gotoPage(x))
    
    def gotoPage(self, x):

        self.isFirst = True
        self.webView.load(QUrl("file:///" + self.pdf_file + "#page=" + x))

    def onLoadFinished(self):
        if self.isFirst:
            self.sender().reload()
            self.isFirst = False

if __name__ == '__main__':
    app = QApplication([])
    ex = Window()
    ex.show()
    app.exec()
