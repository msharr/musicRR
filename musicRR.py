#Calculates RR peak ratios (N+1)/N

import numpy as np

class patientBar:
    def __init__(self, notes, tempo, start, end): 
        self.notes = notes
        self.tempo = tempo
        self.start = start
        self.end = end

def calculate_ratio(data, start_time):                     
    ratio = []
    ratio.append(patientBar(round(data[1]/data[0],4), round(60000/data[0]), start_time, start_time+(data[0]+data[1])/1000))
    for i in range(1,len(data)-1):                
        value = round(data[i+1]/data[i],4)
        ratio.append(patientBar(value, round(60000/data[i]), ratio[i-1].end, ratio[i-1].end+(data[i]+data[i+1])/1000))
        if i>1500:
            print("Limit reached: 1500 bars")
            break
    return ratio

def main(patient_file, start_time):
    patient = np.loadtxt(patient_file)
    rr_ratio = calculate_ratio(patient,start_time)   
    return rr_ratio

if __name__ == "__main__":
    main()