#Writes and executes .ly file to generate PDF file
import os

def transcription_regions(ratio):                       
    transcription = []
    for i in range(len(ratio)-1):
        # transcription.append("\\tempo 4 = "+str(round(60000/data[i])))
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
    notes = transcription_regions(ratio_data)    #Converts RR peak ratios to two event lilypond form
    lilypond_create(notes,output_file)      #Creates the output lilypond file
    os.startfile(output_file)

if __name__ == "__main__":
    main()