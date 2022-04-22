
year_2020 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2021 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

year_2022 = {"JAN": 0, "FEB": 0, "MAR": 0, "APR": 0, "MAY": 0, "JUN": 0, "JUL": 0, "AUG": 0, "SEP": 0, "OCT": 0, "NOV": 0, "DEC": 0}

with open("SAP_CubeDataload.txt", "r") as f:
    for line in f:
        if "2020|" in line:
            if "JAN" in line:
                year_2020["JAN"] += 1
            elif "FEB" in line:
                year_2020["FEB"] += 1
            elif "MAR" in line:
                year_2020["MAR"] += 1
            elif "APR" in line:
                year_2020["APR"] += 1
            elif "MAY" in line:
                year_2020["MAY"] += 1
            elif "JUN" in line:
                year_2020["JUN"] += 1
            elif "JUL" in line:
                year_2020["JUL"] += 1
            elif "AUG" in line:
                year_2020["AUG"] += 1
            elif "SEP" in line:
                year_2020["SEP"] += 1
            elif "OCT" in line:
                year_2020["OCT"] += 1
            elif "NOV" in line:
                year_2020["NOV"] += 1
            elif "DEC" in line:
                year_2020["DEC"] += 1

        elif "2021|" in line:
            if "JAN" in line:
                year_2021["JAN"] += 1
            elif "FEB" in line:
                year_2021["FEB"] += 1
            elif "MAR" in line:
                year_2021["MAR"] += 1
            elif "APR" in line:
                year_2021["APR"] += 1
            elif "MAY" in line:
                year_2021["MAY"] += 1
            elif "JUN" in line:
                year_2021["JUN"] += 1
            elif "JUL" in line:
                year_2021["JUL"] += 1
            elif "AUG" in line:
                year_2021["AUG"] += 1
            elif "SEP" in line:
                year_2021["SEP"] += 1
            elif "OCT" in line:
                year_2021["OCT"] += 1
            elif "NOV" in line:
                year_2021["NOV"] += 1
            elif "DEC" in line:
                year_2021["DEC"] += 1

        elif "2022|" in line:
            if "JAN" in line:
                year_2022["JAN"] += 1
            elif "FEB" in line:
                year_2022["FEB"] += 1
            elif "MAR" in line:
                year_2022["MAR"] += 1
            elif "APR" in line:
                year_2022["APR"] += 1
            elif "MAY" in line:
                year_2022["MAY"] += 1
            elif "JUN" in line:
                year_2022["JUN"] += 1
            elif "JUL" in line:
                year_2022["JUL"] += 1
            elif "AUG" in line:
                year_2022["AUG"] += 1
            elif "SEP" in line:
                year_2022["SEP"] += 1
            elif "OCT" in line:
                year_2022["OCT"] += 1
            elif "NOV" in line:
                year_2022["NOV"] += 1
            elif "DEC" in line:
                year_2022["DEC"] += 1

print()
print("2020")
print(year_2020)
print()
print("2021")
print(year_2021)
print()
print("2022")
print(year_2022)
print()
print(input("press enter to close"))