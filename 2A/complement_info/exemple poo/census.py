from source import Source

class Census(Source):
    def __init__(self, name, start_collect, end_collect,input_file):
        super().__init__(name, start_collect, end_collect,input_file)
        
    def custom_process(self):
        print("Traitement d'un fichier de rencensement")