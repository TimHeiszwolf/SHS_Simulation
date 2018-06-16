function Power = Radiation(temperature_to, temperature_from, emisivity_to, emisivity_from, area_to, area_from)
    %https://en.wikipedia.org/wiki/Thermal_radiation#Radiative_power
    %http://www.infrared-thermography.com/material-1.htm
    %'temperature_to' is the temperature of the thing the power is flowing to if it is colder than the other thing and logicly 'temperature_from' is the temperature of the other thing.
    Boltzman_const=5.670367*10^-8;
    Power=Boltzman_const*((emisivity_from*area_from*temperature_from^4)-(emisivity_to*area_to*temperature_to^4));