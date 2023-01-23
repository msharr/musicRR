#Writes and executes .ly file to generate PDF file
import os

def transcription_regions(ratio):                       
    transcription = []
    for i in range(len(ratio)-1):
        transcription.append("\\tempo 4 = "+str(ratio[i].tempo))
        if ratio[i].notes == 0.4:
            transcription.append("\\time 7/8")
            transcription.append("4.~ 4 4")
        elif ratio[i].notes == 0.5:
            transcription.append("\\time 3/4")
            transcription.append("2 4")
        elif ratio[i].notes == 0.66:
            transcription.append("\\time 8/8")
            transcription.append("4.~ 4 4.")
        elif ratio[i].notes == 0.75:
            transcription.append("\\time 7/8")
            transcription.append("2 4.")
        elif ratio[i].notes == 0.8:
            transcription.append("\\time 9/8")
            transcription.append("4.~ 4 2")        
        elif ratio[i].notes == 1:
            transcription.append("\\time 2/2")
            transcription.append("2 2")
        elif ratio[i].notes == 1.25:
            transcription.append("\\time 9/8")
            transcription.append("2 4.~ 4")   
        elif ratio[i].notes == 1.33:
            transcription.append("\\time 7/8")
            transcription.append("4. 2")
        elif ratio[i].notes == 1.5:
            transcription.append("\\time 5/8")
            transcription.append("4 4.")
        elif ratio[i].notes == 1.75:
            transcription.append("\\time 11/8")
            transcription.append("2 4.~ 2")
        elif ratio[i].notes == 2:
            transcription.append("\\time 3/4")
            transcription.append("4 2")
        elif ratio[i].notes == 2.5:
            transcription.append("\\time 7/8")
            transcription.append("4 4~ 4.")
    return transcription

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

def main(ratio_data, output_file):
    notes = transcription_regions(ratio_data)    
    lilypond_create(notes,output_file)      
    os.startfile(output_file)

if __name__ == "__main__":
    main()