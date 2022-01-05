def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month = 1
    leftover = 0
    overall = startPriceOld
    while overall < startPriceNew:
        #Loss increase
        if month % 2 == 0:
            percentLossByMonth += 0.5
        #Prices drop
        startPriceOld -= ( startPriceOld * (percentLossByMonth/100) )
        startPriceNew -= ( startPriceNew * (percentLossByMonth/100) )
        #Calculate
        overall = (startPriceOld + (savingperMonth*month) )
        #Month ends
        month += 1
    leftover = round(overall - startPriceNew)
    return [month-1,leftover]

#Test:
print(nbMonths(2000, 8000, 1000, 1.5))