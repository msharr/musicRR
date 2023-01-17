import musicRR
import openPDF

patient_folder = "Patients\\"
output_folder = "Output\\"

patient_file = "000.txt"
output_file_name = "Peaks"

musicRR.main( patient_folder+patient_file , output_folder+output_file_name+".ly" )
print("Generating...")
openPDF.main()
print("PDF file generated.")