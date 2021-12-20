# Search
import os
from os import walk
from PyQt5.QtWidgets import QApplication
def search(self,location,num):
        '''
        to search network location
        '''
        data = []
        file_name_Extension = [num + ".pdf", num + ".R75", num + ".xls"]

        for root, dirs, files in walk(location+"/"):
            for f in files:
                if f == file_name_Extension[0]:  #pdf
                        
                    fullpath = os.path.join(root, f)
                    print(fullpath)
                    data.append(fullpath)
                QApplication.processEvents() #refresh GUI     
                        
                        # self.listWidget.setModel(listModel)

                    # if f == file_name_Extension[1]:  #R75
                    #     R75_Counter = R75_Counter +1
                   
                    #     fullpath = os.path.join(root, f)
                    #     print(fullpath)
                    #     self.R75_Browser.append(fullpath)
                        
                    # if f == file_name_Extension[2]:  #xls
                    #     xls_Counter = xls_Counter +1
                        
                    #     fullpath = os.path.join(root, f)
                    #     print(fullpath)
                    #     self.xls_Browser.append(fullpath)
                
        return data
