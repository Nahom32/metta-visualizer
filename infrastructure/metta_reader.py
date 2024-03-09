from typing import List
def read_metta_file(url_path: str) -> List[str]:
    raw_data = []
    with open(url_path, 'r') as file:
        for  line in file:
            raw_data.append(line)
    return raw_data
            
            
        
    