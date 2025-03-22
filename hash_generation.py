import sys
sys.path.append(r"D:\SHA 512")
from converting_to_binary import  convert_text_to_binary
from final_hash_calculation import HashCalculation
from converting_to_binary import convert_text_to_binary 


class HashGeneration:
    def __init__(self,text):
        self.text = text
       
    def gen_hash(self):
        binary_encoded_list = convert_text_to_binary(self.text)
        hash_calculation = HashCalculation(self.text,binary_encoded_list)
        hash_list = hash_calculation.hash_calulation()
        hash_code = []
        for i  in range(len(hash_list)):
            hash_code.append(hash_list[i][2:len(hash_list[i])])
    
        hash_code = "".join(hash_code)
        
        return int(hash_code,16)
    
    
    
    


