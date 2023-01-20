import musicRR
import openPDF
import transcriber
import os

patient_folder = "Patients\\"
patient_file = "000.txt"
output_folder = "Output\\"
output_file_name = "Peaks"

start_time = 1674148538

def output_clean():                             
    tmp = [f for f in next(os.walk("Output"))[2] if '.' not in f]
    for i in range(len(tmp)-1):
        os.rename("Output/"+tmp[i],"Output/tmp"+str(i)+".txt")
    for item in os.listdir("Output"):
        os.remove("Output/"+item)
        
output_clean()                          #Removes old files in output folder
ratio_data = musicRR.main(patient_folder+patient_file, start_time )
transcriber.main(ratio_data, output_folder+output_file_name+".ly")
print("Generating...")
openPDF.main()
print("PDF file generated.")