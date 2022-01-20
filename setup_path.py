# Import this module to automatically setup path to local win32py module
# This module first tries to see if win32py module is installed via pip
# If it does then we don't do anything else
# Else we look up grand-parent folder to see if it has win32py folder
#    and if it does then we add that in sys.path

import os,sys,logging

#this class simply tries to see if airsim 
class SetupPath:
    @staticmethod
    def getDirLevels(path):
        path_norm = os.path.normpath(path)
        return len(path_norm.split(os.sep))

    @staticmethod
    def getCurrentPath():
        cur_filepath = __file__
        return os.path.dirname(cur_filepath)

    @staticmethod
    def getGrandParentDir():
        cur_path = SetupPath.getCurrentPath()
        if SetupPath.getDirLevels(cur_path) >= 2:
            return os.path.dirname(os.path.dirname(cur_path))
        return ''

    @staticmethod
    def getParentDir():
        cur_path = SetupPath.getCurrentPath()
        if SetupPath.getDirLevels(cur_path) >= 1:
            return os.path.dirname(cur_path)
        return ''

    @staticmethod
    def addPyWin32Module():
        # if pywin32 module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            pywin32_path = os.path.join(parent, 'pywin32')
            client_path = os.path.join(pywin32_path, 'pythoncom.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("pywin32 module not found in parent folder. Using installed package (pip install pywin32).") 

    @staticmethod
    def addtwillModule():
        # if twill module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            twill_path = os.path.join(parent, 'twill-3.0.1')
            client_path = os.path.join(twill_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("twill module not found in parent folder. Using installed package (pip install twill).")       
     
    @staticmethod
    def addpandasModule():
        # if pandas module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            pandas_path = os.path.join(parent, 'pandas-1.3.5')
            client_path = os.path.join(pandas_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("pandas module not found in parent folder. Using installed package (pip install pandas).")  

    @staticmethod
    def addRequestsModule():
        # if requests module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            r_path = os.path.join(parent, 'requests-2.26.0')
            client_path = os.path.join(r_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("requests module not found in parent folder. Using installed package (pip install requests).")  

    @staticmethod
    def addZipModule():
        # if zip module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            z_path = os.path.join(parent, 'zip-0.0.2')
            client_path = os.path.join(z_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("zip module not found in parent folder. Using installed package (pip install zip).")  

    @staticmethod
    def addNumpyModule():
        # if numpy module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            numpy_path = os.path.join(parent, 'numpy-1.21.4')
            client_path = os.path.join(numpy_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("numpy module not found in parent folder. Using installed package (pip install numpy).")  

    @staticmethod
    def addMatplotlibModule():
        # if matplotlib module is installed then don't do anything else
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            mat_path = os.path.join(parent, 'matplotlib-3.5.1')
            client_path = os.path.join(mat_path, 'setup.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("matplotlib module not found in parent folder. Using installed package (pip install matplotlib).")   

SetupPath.addpandasModule()
SetupPath.addNumpyModule()
SetupPath.addMatplotlibModule()
SetupPath.addRequestsModule()
SetupPath.addZipModule()   
SetupPath.addtwillModule() 
SetupPath.addPyWin32Module()       