#    test.py
#
#    Written by Benson Yeh, 3/10/2021, 
#    Require chrome , Internet connect , 192.168.xx.x Authority  
#
#-------------------------------------------------------------------

import sys
# import threading
import os
import webbrowser    
# from pathlib import Path

import time


from file_ui import Ui_MainWindow
from Tool.Search import search

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel 
from PyQt5.QtGui import QPixmap, QStandardItemModel, QFont, QStandardItem, QIcon
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QToolBar, QStatusBar, \
    QHBoxLayout, QGroupBox, QComboBox, QCheckBox, QListView, QTabWidget, QPlainTextEdit, QProgressBar, QFileDialog, \
    QMessageBox, \
    QAction ,QListWidget
# from PyQt5.QtCore import QDate , QDateTime   



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setWindowTitle('ACES SI File check')
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'D:/00_ACES/00_Jane_Work/20211004_Pyqt_test/logo/favicon.ico')))
        self.setupUi(self)
        self._create_header()
        # self._get_currenttime()
        
        
        self.single_search_btn.clicked.connect(self._sigle_file_search)
        self.Browse_btn.clicked.connect(self._Browse)
        self.Open_pdf_btn.clicked.connect(self._open_pdf)
        # listWidget = QListWidget()

        self.Browse_btn.setEnabled(True) 
        self.single_search_btn.setEnabled(False) 
        

        # self.range_search_btn.clicked.connect(self._range_search)
        self.statusBar().showMessage('ready')
        

 

        self.show()
     
    def _create_header(self):
        '''Creating the header display including the company logo'''
        
        self.im = QPixmap("D:/00_ACES/00_Jane_Work/20211004_Pyqt_test/logo/SI_file_check.png")
        self.label_6.setPixmap(self.im)
        self.label_6.setGeometry(50,10,900,80)
        

    # def _get_currenttime(self):
    #     self.check_test_date_1.setDate(QDate.currentDate())
    #     self.check_test_date_2.setDate(QDate.currentDate())

    def _Browse(self,si_file_path):
        '''
        set path to network location
        ''' 
        self.single_search_btn.setEnabled(True) 

        try:
            self.statusBar().showMessage('Waiting....')  
            self.SI_file_folder_Browser.clear()
            si_file_path = QFileDialog.getExistingDirectory(self,"choose folder","//192.168.26.2/Project/SI_Test(電子工程二部)/")
            # print(si_file_path)
            self.SI_file_folder_Browser.append(si_file_path)
            self.statusBar().showMessage('Selected Folder') 
            
        except:
            self.SI_file_folder_Browser.clear()
            self.SI_file_folder_Browser.append("Try Again")

    

    def _sigle_file_search(self):
        
        self.single_search_btn.setEnabled(False) 

        self.data = []
        
        
        self.listWidget.clear()
        self.statusBar().showMessage('Searching....')  
        location = os.path.join('{}'.format(self.SI_file_folder_Browser.toPlainText()))
        num = self.single_sn.text()
        try:
            
             
            self.data = search(self,location,num)
            QApplication.processEvents() #refresh GUI   
            # print(self.data)   
            self.listWidget.addItems(self.data)
            self.statusBar().showMessage('Finish')
            self.single_search_btn.setEnabled(True) 
        
    
        except IOError:
            print("error path")
            self.SI_file_folder_Browser.append("Error path")
            
        # self.listWidget.clicked.connect(self._open_pdf) 
    
    def _open_pdf(self, item):
        '''
        use chrome to open pdf
        '''
        try:
            path = self.listWidget.currentItem().text()
            new_path = path.replace(' ','%20') #%20 can replace space in path
            chrome_path = r"C://Program Files//Google//Chrome//Application//chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open('file://{}'.format(new_path) ,new=1)

        except:
            self.statusBar().showMessage('please select pdf') 


            

    # def _split_word(self,word):
    #     aa = list(word) 
    #     for i in aa:
    #         print(i)       

    # def _range_search(self):
    #     num = []
    #     start = self.range_start.text()
    #     end = self.range_end.text()


    #     path = 'path_output.txt'
    #     with open(path, 'r') as f_txt:
    #         f_txt
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controller()
    sys.exit(app.exec_())
    
