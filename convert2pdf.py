import os,sys
import subprocess

# traverse directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(os.getcwd()):
    path = root.split(os.sep)
    if ".git" not in path:
        for file in files:
            path_no_ext = os.path.splitext(os.path.join(root,file))[0] 
            print(file)
            if file.endswith(".md") or file.endswith(".rst") or file.endswith(".html"):
                try:
                    #sys.stdout = open(os.devnull, 'w')
                    if file.endswith(".md"):
                        #os.system('grip --user nursenakrbs --pass opheliax0'+ path_no_ext+".md"+" --export "+path_no_ext + ".html ")
                        result = subprocess.Popen("pandoc -s -o "+path_no_ext + ".pdf " + path_no_ext+".md")
                        text = result.communicate()[0]
                        return_code = result.returncode
                        #result = subprocess.run(['grip', path_no_ext+".md","--export",path_no_ext + ".html"], stdout=subprocess.PIPE)
                        #if("Usage:" in result.stdout.decode('utf-8')):
                        #    continue
                        if return_code==0:
                            os.remove(path_no_ext + ".md")
                        else:
                            print("PANDOC ERROR: ",return_code)
                    if file.endswith(".rst"):
                        os.system("rst2html5.py "+ path_no_ext+".rst " + path_no_ext + ".html" )
                        os.remove(path_no_ext + ".rst")
                        os.system("wkhtmltopdf "+ path_no_ext + ".html" + " " + path_no_ext+".pdf")
                        os.remove(path_no_ext + ".html")
                    
                    #sys.stdout = sys.__stdout__
                except WindowsError:
                    continue