#/usr/bin/env python

def main():
    with open('URL.INP','r') as inp, open('URL.OUT','w') as ou:
        for line in inp:                  
            cleanedLine = line.strip()  
            if cleanedLine:
                print >>ou, (cleanedLine)
            if line.startswith("[http://[") or line.startswith("[https://[") or line.startswith("[www.[") or line.startswith("[http://www.[") or line.startswith("[https://www.["):
                line = line.replace("[http://[", "Username: ") 
                line = line.replace("[https://[", "Username ") 
                line = line.replace("[www.[", "Username ") 
                line = line.replace("[http://www.[", "Username: ") 
                line = line.replace("[https://www.[", "Username: ")
            if "[:" in line:
                line = line.replace("[:", "\n" "Password: ")
            if "]@]" in line or "[@]" in line:
                line = line.replace("]@]", "\n" "Hostname: ") 
                line = line.replace("[@]", "\n" "Hostname: ")
            if "]/" in line:
                line = line.replace("]/", "\n" "Path: ")
            if "/" in line:
                line = line.replace("/", "\n" "Substance: ", 1)
            if "[?" in line:
                line = line.replace("[?", "\n" "Parameters: ")
            if not line.startswith("[http://[") or line.startswith("[https://[") or line.startswith("[www.[") or line.startswith("[http://www.[") or line.startswith("[https://www.["):
                line = line.replace("[", "Username: ")   
            if "]" in line:
                line = line.replace("]", "")
            print >> ou, line        
   
    inp.close()
    ou.close()
    
if __name__ == "__main__": main()