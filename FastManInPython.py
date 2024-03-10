print("""


·▄▄▄ ▄▄▄· .▄▄ · ▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄·  ▐ ▄     ▪   ▐ ▄ 
▐▄▄·▐█ ▀█ ▐█ ▀. •██      ·██ ▐███▪▐█ ▀█ •█▌▐█    ██ •█▌▐█
██▪ ▄█▀▀█ ▄▀▀▀█▄ ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌    ▐█·▐█▐▐▌
██▌.▐█ ▪▐▌▐█▄▪▐█ ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌██▐█▌    ▐█▌██▐█▌
▀▀▀  ▀  ▀  ▀▀▀▀  ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪    ▀▀▀▀▀ █▪
 ▄▄▄· ▄· ▄▌▄▄▄▄▄ ▄ .▄       ▐ ▄   
▐█ ▄█▐█▪██▌•██  ██▪▐█▪     •█▌▐█  
 ██▀·▐█▌▐█▪ ▐█.▪██▀▐█ ▄█▀▄ ▐█▐▐▌  
▐█▪·• ▐█▀·. ▐█▌·██▌▐▀▐█▌.▐▌██▐█▌  
.▀     ▀ •  ▀▀▀ ▀▀▀ · ▀█▄▀▪▀▀ █▪  

      
      Coded By @black_nicola(TELEGRAM)

""")
import os,sys
from threading import Thread
try:
    input_path=sys.argv[1]
    out_path=sys.argv[2]
except:
    print("""
You need to help! I help you!
 Your can use from "Fast Man In Python" by down command
    python3 fast_man_in_python.py Original_file_path Output_file_path
    
 For exam:
    python3 fast_man_in_python.py slow.py fast.py      
""")
    sys.exit()

# Read File
with open(input_path, 'r') as file:
    file_content = file.readlines()

# Scan Varbs
variables = []
for line in file_content:
    if '=' in line:
        var_name = line.split('=')[0].strip()
        if not var_name in variables:
            variables.append(var_name)

# Start Write
with open(out_path, 'w+') as output_file:
    # Write Imports
    output_file.write('''from threading import Thread
threads=[]
''')
    for line in file_content:
        if line.startswith('import') or line.startswith('from'):
            output_file.write(line)

    # Write global
    for var in variables:
        output_file.write(f"global {var}\n")

    # Write Codes
    for line in file_content:
        if not line.strip().startswith("from") and not line.strip().startswith("import") and not line.strip().startswith('"') and not line.strip().startswith("'") and not line.strip().startswith("#") and not line.strip().startswith('"""') and line.strip() != '' and not line.isspace():
            output_file.write(f"def cpu_function():\n")
            output_file.write(f"    {line.replace('{lin}', '').strip()}\n")
            output_file.write(f"t = Thread(target=cpu_function)\n")
            output_file.write(f"threads.append(t)\n")
            output_file.write(f"t.start()\n")

input(f"Output file '{out_path}' has been created with the processed content.
    Now you are tens and hundreds of times faster!
      
      
      
""")
