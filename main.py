#    test.py
#
#    Written by Benson Yeh, 3/10/2021, Aces Electronics Co., Ltd.
#    Require chrome , Internet connect , 192.168.26.2 Authority  
#
#-------------------------------------------------------------------

import sys
# import threading
import os
import webbrowser    
# from pathlib import Path
from os import walk
import time


from file_ui import Ui_MainWindow


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel 
from PyQt5.QtGui import QPixmap, QStandardItemModel, QFont, QStandardItem, QIcon
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QToolBar, QStatusBar, \
    QHBoxLayout, QGroupBox, QComboBox, QCheckBox, QListView, QTabWidget, QPlainTextEdit, QProgressBar, QFileDialog, \
    QMessageBox, \
    QAction
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
        # self.open_pdf.clicked.connect(self._open_pdf)


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

    def _open_pdf(self,qModelindex):
        try:
            # self.listView.clearSelection()  
            path = os.path.join('{}'.format(self.items[qModelindex.row()]))
            new_path = path.replace(' ','%20') # %20 can replace blank space in the windows path
            print(new_path)
            chrome_path = r"C://Program Files//Google//Chrome//Application//chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open('file://{}'.format(new_path) ,new=1)
            # os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" file:{}'.format(new_path)) 
        
        except:
            print("Error Open Browser")    
        
    def _sigle_file_search(self):

        self.single_search_btn.setEnabled(False) 

        self.R75_Browser.clear()
        self.xls_Browser.clear()
        self.items=[]
        listModel=QStringListModel()
        
    
        self.statusBar().showMessage('Searching....')  
        location = os.path.join('{}'.format(self.SI_file_folder_Browser.toPlainText()))
        pdf_Counter = 0
        R75_Counter = 0
        xls_Counter = 0
        try:
            num = self.single_sn.text()
            file_name_Extension = [num + ".pdf", num + ".R75", num + ".xls"]

            for root, dirs, files in walk(location+"/"):
                for f in files:
                    if f == file_name_Extension[0]:  #pdf
                        pdf_Counter = pdf_Counter +1
                        
                        fullpath = os.path.join(root, f)
                        print(fullpath)
                        self.items.append(str(fullpath))
                        listModel.setStringList(self.items)
                        self.listView.setModel(listModel)

                        
                    if f == file_name_Extension[1]:  #R75
                        R75_Counter = R75_Counter +1
                   
                        fullpath = os.path.join(root, f)
                        print(fullpath)
                        self.R75_Browser.append(fullpath)
                        
                    if f == file_name_Extension[2]:  #xls
                        xls_Counter = xls_Counter +1
                        
                        fullpath = os.path.join(root, f)
                        print(fullpath)
                        self.xls_Browser.append(fullpath)
    
                    QApplication.processEvents() #refresh GUI   
            self.statusBar().showMessage('Finish')
            self.single_search_btn.setEnabled(True) 
            
            print(self.listView)
            self.listView.clicked.connect(self._open_pdf)  
            
            # if pdf_Counter == 0:
            #     self.pdf_Browser.append("Not Found !!")
            if R75_Counter == 0:
                self.R75_Browser.append("Not Found !!") 
            if xls_Counter == 0:
                self.xls_Browser.append("Not Found !!") 
                     
    
        except IOError:
            print("error path")
            self.SI_file_folder_Browser.append("Error path")

        



            

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
    