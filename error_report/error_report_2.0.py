
year_2020 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2021 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2022 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

with open("SAP_CubeDataload.txt", "r") as f:
    for line in f:
        if "2020|" in line:
            for key in year_2020:
                if key in line:
                    year_2020[key] += 1

        elif "2021|" in line:
            for key in year_2021:
                if key in line:
                    year_2021[key] += 1

        elif "2022|" in line:
            for key in year_2022:
                if key in line:
                    year_2022[key] += 1


print()
print("2020:")
print(year_2020)
print()
print("2021:")
print(year_2021)
print()
print("2022:")
print(year_2022)
print()
print(input("press enter to close"))
