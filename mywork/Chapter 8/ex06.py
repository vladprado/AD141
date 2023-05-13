from sys import argv, exit
import os
import time

if len(argv) != 3:
    print("Usar: " + argv[0] + " <diretorio> <tamanho_limite>")
    exit(1)

dir_name = argv[1]
file_size = int(argv[2])

files = os.listdir(dir_name)

for filename in files:
    filedata = os.stat(os.path.join(dir_name, filename))
    if filedata.st_size > file_size:
        print("{} {} {}".format(filename, filedata.st_size, 
                                time.ctime(filedata.st_mtime)))
