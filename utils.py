import json

def read_htmlFile(html_file):
    with open(html_file,'r',encoding='utf=8') as f:
        return f.read()
    
def load_xpaths(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)