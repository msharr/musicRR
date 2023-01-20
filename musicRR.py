#Calculates RR peak ratios (N+1)/N

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

def main(patient_file, start_time):
    patient = np.loadtxt(patient_file)
    rr_ratio = calculate_ratio(patient)     #Calculates RR peak ratios: (N+1)/N
    return rr_ratio

if __name__ == "__main__":
    main()