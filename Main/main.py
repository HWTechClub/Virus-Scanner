import os
from subprocess import call

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #Project root
CONFIG_PATH = os.path.join(ROOT_DIR,'URL_Scan_IO\URLScanIOMain.py')

class CallPy(object):

  def __init__(self,path=CONFIG_PATH):
     self.path=path

  def call_python_file(self):
     call(["python3","{}".format(self.path)])
	
if __name__=="__main__":
	c=CallPy()
	c.call_python_file()
 