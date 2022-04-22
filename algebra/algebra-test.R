AP <- AirPassengers
print(AP)
plot(AP)
class(AP)
#It is of the type ts which means “time series” 7
start(AP)
end(AP)
frequency(AP) #frequency per year
#Time series is very useful in R,8 but sometimes requires advanced functions
(colnames() etc. do not work).
#You can always extract the raw data from it:
raw.data <- AP[1:length(AP)]
class(raw.data)
plot(AP)
