from datetime import datetime

start_time = datetime.now()

y_2020 = 2020
jan_20 = 0
feb_20 = 0
mar_20 = 0
apr_20 = 0
may_20 = 0
jun_20 = 0
jul_20 = 0
aug_20 = 0
sep_20 = 0
oct_20 = 0
nov_20 = 0
dec_20 = 0

y_2021 = 2021
jan_21 = 0
feb_21 = 0
mar_21 = 0
apr_21 = 0
may_21 = 0
jun_21 = 0
jul_21 = 0
aug_21 = 0
sep_21 = 0
oct_21 = 0
nov_21 = 0
dec_21 = 0

y_2022 = 2022
jan_22 = 0
feb_22 = 0
mar_22 = 0
apr_22 = 0
may_22 = 0
jun_22 = 0
jul_22 = 0
aug_22 = 0
sep_22 = 0
oct_22 = 0
nov_22 = 0
dec_22 = 0


with open("SAP_CubeDataload.txt", "r") as f:
    for line in f:
        if "2020|" in line:
            if "JAN" in line:
                jan_20 += 1
            elif "FEB" in line:
                feb_20 += 1
            elif "MAR" in line:
                mar_20 += 1
            elif "APR" in line:
                apr_20 += 1
            elif "MAY" in line:
                may_20 += 1
            elif "JUN" in line:
                jun_20 += 1
            elif "JUL" in line:
                jul_20 += 1
            elif "AUG" in line:
                aug_20 += 1
            elif "SEP" in line:
                sep_20 += 1
            elif "OCT" in line:
                oct_20 += 1
            elif "NOV" in line:
                nov_20 += 1
            elif "DEC" in line:
                dec_20 += 1

        elif "2021|" in line:
            if "JAN" in line:
                jan_21 += 1
            elif "FEB" in line:
                feb_21 += 1
            elif "MAR" in line:
                mar_21 += 1
            elif "APR" in line:
                apr_21 += 1
            elif "MAY" in line:
                may_21 += 1
            elif "JUN" in line:
                jun_21 += 1
            elif "JUL" in line:
                jul_21 += 1
            elif "AUG" in line:
                aug_21 += 1
            elif "SEP" in line:
                sep_21 += 1
            elif "OCT" in line:
                oct_21 += 1
            elif "NOV" in line:
                nov_21 += 1
            elif "DEC" in line:
                dec_21 += 1

        elif "2022|" in line:
            if "JAN" in line:
                jan_22 += 1
            elif "FEB" in line:
                feb_22 += 1
            elif "MAR" in line:
                mar_22 += 1
            elif "APR" in line:
                apr_22 += 1
            elif "MAY" in line:
                may_22 += 1
            elif "JUN" in line:
                jun_22 += 1
            elif "JUL" in line:
                jul_22 += 1
            elif "AUG" in line:
                aug_22 += 1
            elif "SEP" in line:
                sep_22 += 1
            elif "OCT" in line:
                oct_22 += 1
            elif "NOV" in line:
                nov_22 += 1
            elif "DEC" in line:
                dec_22 += 1

end_time = datetime.now()

print("time: ", end_time - start_time)
print()
print(y_2020)
print(f"Errors Found In January: {jan_20}")
print(f"Errors Found In February: {feb_20}")
print(f"Errors Found In March: {mar_20}")
print(f"Errors Found In April: {apr_20}")
print(f"Errors Found In May: {may_20}")
print(f"Errors Found In June: {jun_20}")
print(f"Errors Found In July: {jul_20}")
print(f"Errors Found In August: {aug_20}")
print(f"Errors Found In September: {sep_20}")
print(f"Errors Found In October: {oct_20}")
print(f"Errors Found In November: {nov_20}")
print(f"Errors Found In December: {dec_20}")
print()
print(y_2021)
print(f"Errors Found In January: {jan_21}")
print(f"Errors Found In February: {feb_21}")
print(f"Errors Found In March: {mar_21}")
print(f"Errors Found In April: {apr_21}")
print(f"Errors Found In May: {may_21}")
print(f"Errors Found In June: {jun_21}")
print(f"Errors Found In July: {jul_21}")
print(f"Errors Found In August: {aug_21}")
print(f"Errors Found In September: {sep_21}")
print(f"Errors Found In October: {oct_21}")
print(f"Errors Found In November: {nov_21}")
print(f"Errors Found In December: {dec_21}")
print()
print(y_2022)
print(f"Errors Found In January: {jan_22}")
print(f"Errors Found In February: {feb_22}")
print(f"Errors Found In March: {mar_22}")
print(f"Errors Found In April: {apr_22}")
print(f"Errors Found In May: {may_22}")
print(f"Errors Found In June: {jun_22}")
print(f"Errors Found In July: {jul_22}")
print(f"Errors Found In August: {aug_22}")
print(f"Errors Found In September: {sep_22}")
print(f"Errors Found In October: {oct_22}")
print(f"Errors Found In November: {nov_22}")
print(f"Errors Found In December: {dec_22}")
print()
