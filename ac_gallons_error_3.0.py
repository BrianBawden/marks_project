from datetime import datetime

start_time = datetime.now()
year_2020 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2021 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2022 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

year_list = ["2020|", "2021|", "2022|"]

with open("SAP_CubeDataload.txt", "r") as f:
    for line in f:
        for x in year_list:
            if x in line:
                for i in month_list:
                    if i in line:
                        if x == "2020|":
                            year_2020[i] += 1
                        elif x == "2021|":
                            year_2021[i] += 1
                        elif x == "2022|":
                            year_2022[i] += 1
end_time = datetime.now()
print("time: ", end_time - start_time)
print(2020)
print(year_2020)
print()
print(2021)
print(year_2021)
print()
print(2022)
print(year_2022)
print()
    

    

    

    
