#Checks if any PDF exists and then opens it. There should only be one - as we delete all others in musicRR.py.

import os
import time

def main():
    while not any(fname.endswith('.pdf') for fname in os.listdir('Output')): 
        time.sleep(1)
    time.sleep(1)
    pdf_files = [f for f in os.listdir('Output') if f.endswith('.pdf')]
    os.startfile("Output\\"+pdf_files[0])

if __name__ == "__main__":
    main()

