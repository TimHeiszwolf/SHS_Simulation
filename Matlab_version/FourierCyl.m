function Power = FourierCyl(temperature_to, temperature_from, thermal_conductivity, length, radius_1, radius_2)
    %https://en.wikipedia.org/wiki/Thermal_conduction#Fourier's_law and lecture slides.
    %'temperature_to' is the temperature of the thing the power is flowing to if it is colder than the other thing and logicly 'temperature_from' is the temperature of the other thing.
    Power = 2*pi*length*thermal_conductivity*(temperature_from-temperature_to)/log(max(radius_1,radius_2)/min(radius_1,radius_2));
