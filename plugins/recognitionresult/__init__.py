from yapsy.IPlugin import IPlugin
import os
import config
from subprocess import Popen

enabled = True

class RecognitionResultPlugin(IPlugin):
    def __init__(self):
        self.fd = open( config.results_file, mode="at")
        current_folder = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_folder,"recognitionbar_tk.py")
        try:
            Popen([ui_path])
        
        except Exception as e:
            print "Error writing recognition result: "+str(e)
        
        
    def register_rpcs(self, server):
        server.register_function(self.on_recognition)
        server.register_function(self.on_failure)
        server.register_function(self.on_begin)
    
    def on_begin(self,):
        self.write_message(config.begin_literal)
    def on_failure(self,):
        self.write_message(config.failure_literal)    
    def on_recognition(self,phrase="nothing"):
        self.write_message(phrase)
        
    def write_message(self,message):
        try:
            self.fd.write(message+"\n")
            self.fd.flush()
            
        except Exception as e:
            print "Error writing recognition result: "+str(e)
