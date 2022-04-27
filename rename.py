import os

#counter=0
# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    path = root.split(os.sep)
    if not ".git" == root.lower():
        for file in files:
            #rename sub-files
            if len(path) > 3:
                i = 3
                new_name = ""
                while i < len(path):
                    new_name += "(" + path[i] + ")"
                    i += 1
                    #to prevent hitting the filename + path character limit of the os
                    if len(new_name)+len(file.lower()) > 180:
                        new_name += "---"
                        break
                new_name += file
                #print (len(path),"  ", new_name)
                #counter += 1
                try:
                    os.rename(os.path.join(root,file), os.path.join(root,new_name))
                except WindowsError:
                    continue
#print(counter)
