
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView #, QWebEngineSettings

from os import path
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
 
        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)
 
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)

        self.webView.setUrl(QUrl("file:///D:/python/qtworks/H570.pdf#page=10"))
 
    def url_changed(self):
        self.setWindowTitle(self.webView.title())
 
    def go_back(page:int, self) -> None:
        
        self.webView.page.runJavaScript(f"window.viewer.viewport_.goToPage({page})")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_N:
            self.webView.setUrl(QUrl("file:///D:/python/qtworks/H570.pdf#page=20"))
 
if __name__ == '__main__':
 
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    '''
    if len(sys.argv) > 1:
        win.webView.setUrl(QUrl.fromLocalFile("d:\python\qtworks\H570.pdf"))
    else:
        win.webView.setUrl(QUrl("file:///D:/python/qtworks/H570.pdf#page=10"))
    ''' 
 
    sys.exit(app.exec())