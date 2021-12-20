global ratel, rate5, rate15
rate1 = 5.57
rate5 = 11.75
rate15 = 28.49 
function parcelCost(weight)
    overWeight = "Too Heavy, parcel rates do not apply"
    underWeight = "Send as package, not parcel"
    if weight >= 20 then
        theCost = overWeight
    elseif weight >=15 then
        theCost = str(rate5)
    elseif weight >= 1 then 
        theCost = str(rate1)
    else 
        theCost = underWeight 
    endif
    return theCost
end function
//main program
    parecelWeight = float(input("Enter parecl weight: ")
    while parcelWeight != 0:
        print("Postage cost: ", parcelCost(parcelWeight))
    parcelWeight = float(input("Enter parcel weight: "))
endwhile. 

