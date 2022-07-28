import re

def solution(new_id):
    new_id = new_id.lower() # 1
    new_id = re.sub('[^a-z\d\-\_\.]', "", new_id) # 2
    new_id = re.sub('\.\.+', ".", new_id) # 3
    
    if new_id[0] == ".": #4
        if len(new_id) > 1:
            new_id = new_id[1:]
        
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    
    if not new_id: # 5
        new_id += 'a'
        
    if len(new_id) > 15: # 6
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        temp = new_id[-1]
        while len(new_id) != 3: # 7
            new_id += temp
    
    return new_id