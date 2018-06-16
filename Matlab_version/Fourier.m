function Power = Fourier(temperature_to, temperature_from, thermal_conductivity, distance, area)
    %https://en.wikipedia.org/wiki/Thermal_conduction#Fourier's_law
    %'temperature_to' is the temperature of the thing the power is flowing to if it is colder than the other thing and logicly 'temperature_from' is the temperature of the other thing.
    Power = area*thermal_conductivity*(temperature_from-temperature_to)/distance;
