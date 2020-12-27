from subprocess import call

class CallPy(object):

  def __init__(self,path='../../Virus-Scanner/URL_Scan_IO/URLScanIOMain.py'):
     self.path=path

  def call_python_file(self):
     call(["python3","{}".format(self.path)])
	
if __name__=="__main__":
	c=CallPy()
	c.call_python_file()
 