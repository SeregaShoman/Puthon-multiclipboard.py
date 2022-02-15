###################################
#####To use, enter python double_сlipboard.py in terminal with the necessary command
###################################
import sys 
import clipboard
import json

SAVA_DATA = "cl_board.json"
print('Commands: Save, Load, List, Delete')
def save_items(filepath, data):
	with open(filepath, 'w') as w:
         json.dump(data, w)

def load_js (filepath):
	try:
	    with open(filepath, 'r') as w:
	        data = json.load(w)
	        return data
	except:
	    return{}        

if len(sys.argv) == 2:
    com = sys.argv[1]
    data = load_js(SAVA_DATA)
    if com == 'Save':
        key = input("Enter the key: ")
        data[key] = clipboard.paste()
        save_items(SAVA_DATA, data)
    elif com == 'Load':
        key = input("Enter the key: ")
        if key in data:
        	clipboard.copy(data[key])
        	print('Copied to clipboard')
        else:
        	print('Key does not exist')
    elif com == 'List':
        print(data)
    elif com == 'Delete':
        print(data)
        key = input("Enter key for dell: ")
        if key in data:
            del data[key]
            print(data)
    else:
        print('Unknown command')
else:
	print('Please pass exactly one command')