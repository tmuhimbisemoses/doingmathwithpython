from pylab import plot, show, legend, title, xlabel, ylabel
nyc_temp_2000=[31.3,37.3,47.2,51.0,63.5,71.3,72.7]
nyc_temp_2006=[40.9,35.7,43.1,55.7,63.1,71.0,77.9]
nyc_temp_2012=[37.3,40.9,50.9,54.8,65.1,71.0,78.8]
months = range(1,8)
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012, marker='o')
title('Average monthly temprature in NYC')
xlabel('Month')
ylabel('Temprature')
legend([2000,2006,2012])
show()

