#Calculates RR peak ratios (N+1)/N, then converts this data to .ly format for lilypond engraving.

import os
import numpy as np

def calculate_ratio(data):                     
    ratio = []
    for i in range(len(data)-1):                
        value = round(data[i+1]/data[i],4)
        ratio.append(value)
        if i>1500:
            print("Limit reached: 1500 bars")
            break
    return ratio

def transcription_regions(ratio,data):                       
    transcription = []
    for i in range(len(ratio)-1):
        if 0.35<=ratio[i]<0.45:
            transcription.append("\\time 7/8")
            transcription.append("4.~ 4 4")
        if 0.45<=ratio[i]<0.55:
            transcription.append("\\time 3/4")
            transcription.append("2 4")
        if 0.55<=ratio[i]<0.675:
            transcription.append("\\time 8/8")
            transcription.append("4.~ 4 4.")
        if 0.675<=ratio[i]<0.775:
            transcription.append("\\time 7/8")
            transcription.append("2 4.")
        if 0.775<=ratio[i]<0.9:
            transcription.append("\\time 9/8")
            transcription.append("4.~ 4 2")        
        if 0.9<=ratio[i]<1.125:
            transcription.append("\\time 2/2")
            transcription.append("2 2")
        if 1.125<=ratio[i]<1.29:
            transcription.append("\\time 9/8")
            transcription.append("2 4.~ 4")   
        if 1.29<=ratio[i]<1.415:
            transcription.append("\\time 7/8")
            transcription.append("4. 2")
        if 1.415<=ratio[i]<1.625:
            transcription.append("\\time 5/8")
            transcription.append("4 4.")
        if 1.625<=ratio[i]<1.875:
            transcription.append("\\time 11/8")
            transcription.append("2 4.~ 2")
        if 1.875<=ratio[i]<2.25:
            transcription.append("\\time 3/4")
            transcription.append("4 2")
        if 2.25<=ratio[i]:
            transcription.append("\\time 7/8")
            transcription.append("4 4~ 4.")
    return transcription

def output_clean():                             
    tmp = [f for f in next(os.walk("Output"))[2] if '.' not in f]
    for i in range(len(tmp)-1):
        os.rename("Output/"+tmp[i],"Output/tmp"+str(i)+".txt")
    for item in os.listdir("Output"):
        os.remove("Output/"+item)

def lilypond_create(transcription,file):             
    f = open (file,"w+")                 
    f.write('\\version "2.22.2"\n')
    f.write("#(define mydrums '((tamtam default #t 0)))")
    f.write('\\new DrumStaff \with { instrumentName = #"RR ratios" }')
    f.write("\\drummode {\n")
    f.write(" \\set DrumStaff.drumStyleTable = #(alist->hash-table mydrums)\n")
    f.write(" \\override Staff.StaffSymbol.line-positions = #'( 0 )\n")
    f.write(" \\override Staff.BarLine.bar-extent = #'(-1.5 . 1.5)\n")
    f.write(" \\numericTimeSignature\n")
    for i in range(len(transcription)):
        f.write(" "+transcription[i]+"\n")
    f.write("}")

def main(patient_file,output_file):
    patient = np.loadtxt(patient_file)
    rr_ratio = calculate_ratio(patient)     #Calculates RR peak ratios: (N+1)/N
    notes = transcription_regions(rr_ratio,patient)    #Converts RR peak ratios to two event lilypond form
    output_clean()                          #Removes old files in output folder
    lilypond_create(notes,output_file)      #Creates the output lilypond file
    os.startfile(output_file)
        
if __name__ == "__main__":
    main()