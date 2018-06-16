%%%%%%HARD CODE YOUR INPUT DATA HERE!
amount_water=(1*10^-3+8*pi*0.006^2+8*pi*(0.007^2-0.006^2))*10^3;%kilogram
heat_capacity_water=4185.0;%http://www.wolframalpha.com/input/?i=heat+capacity+of+water
amount_air=0.04845;%kilogram http://www.wolframalpha.com/input/?i=mass+1.620*0.67*0.035+m%5E3+of+air
heat_capacity_air=1007.0;%http://www.wolframalpha.com/input/?i=heat+capacity+air
amount_plate=5.861;%http://www.wolframalpha.com/input/?i=weight+0.67*1.62*0.002+m%5E3+aluminium
heat_capacity_plate=904.0;%http://www.wolframalpha.com/input/?i=specific+heat+capacity+aluminium

temperature_water=20.0+273;
temperature_air=20.0+273;
temperature_amb=20.0+273;
temperature_plate=20.0+273;

conductivity_glass=0.19;%https://en.wikipedia.org/wiki/List_of_thermal_conductivities
thickniss_glass=0.1*2;
area_glass=1.62*0.67;

conductivity_styrofoam=0.4;
thickniss_styrofoam=0.05;
area_styrofoam=2*0.035*(1.62+0.67);

conductivity_rock_wool=0.39;
thickniss_rock_wool=0.1*2;
area_rock_wool=0.2*pi*(0.055+2*0.1);

conductivity_copper=401.0;
thickniss_copper=0.001;
area_copper=2*pi*0.006*8;
length_copper=8;
radius_1_copper=0.005;
radius_2_copper=0.006;

conductivity_plate=235.0;
tickniss_plate=0.002;
area_plate=1.62*0.67-(8*3*2*0.006);

delta_time=1;
end_time=60*30;


%%% THE ACTUAL SIMULATION STARTS HERE!
data=zeros(end_time/delta_time, 4);
loop=1;

input_wattage_water=0.6*(8*3*2*0.006)*1000*0.63;
input_wattage_plate=0.6*((1.670*0.67-8*3*2*0.006)*1000*0.63);

for time = 0:delta_time:end_time
    %%%%%%Resetting the varables
    water_dQ=0;
    air_dQ=0;
    plate_dQ=0;
    
    water_dQ=water_dQ+delta_time*input_wattage_water;
    plate_dQ=plate_dQ+delta_time*input_wattage_plate;
    
    
    %%%%%%Starting the physics of this tick
    %%%Heat flow ambiant to air
    %air_dQ=air_dQ+delta_time*Fourier(temperature_air, temperature_amb, conductivity_glass, thickniss_glass, area_glass);%Calculating heat loss though the glass plate From sildes of introduction and https://canvas.tue.nl/courses/3505/discussion_topics/28288
    %air_dQ=air_dQ+delta_time*Fourier(temperature_air, temperature_amb, conductivity_styrofoam, thickniss_styrofoam, area_styrofoam);%Calculating heat loss though side of collector.
    
    %%%Heat flow water to air
    %copper_tube_air_dQ=delta_time*FourierCyl(temperature_water, temperature_air, conductivity_copper, length_copper, radius_1_copper, radius_2_copper);%Calculating heat tranfer via copper tube to water
    %air_dQ=air_dQ-copper_tube_air_dQ;
    %water_dQ=water_dQ+copper_tube_air_dQ;
    
    %%%Heat flow water to ambiant
    water_dQ=water_dQ+delta_time*Fourier(temperature_water, temperature_amb, conductivity_rock_wool, thickniss_rock_wool, area_rock_wool);%Calculating heat loss from vessel
    water_dQ=water_dQ+delta_time*Radiation(temperature_water, temperature_amb, 0.95, 0.95, area_copper, area_copper);%Radiation of copper tube to outside ambiant air.
    
    %%%Heat flow plate to water
    %copper_tube_plate_dQ=delta_time*Fourier(temperature_water, temperature_plate, conductivity_copper, thickniss_copper, area_copper);%Calculating heat tranfer via copper tube to plate
    %plate_dQ=plate_dQ-copper_tube_plate_dQ;%LET OP HIER KLOPT 'area_copper' NIET EN FOURIER IS NIET TOEPASBAAR.
    %water_dQ=water_dQ+copper_tube_plate_dQ;
    
    %%%Heat flow plate to air
    %aluminium_plate_air_dQ=delta_time*Fourier(temperature_air, temperature_plate, conductivity_plate, thickniss_plate, area_plate);%Calculating heat tranfer via copper tube to plate
    %plate_dQ=plate_dQ-aluminium_plate_air_dQ;%LET OP HIER FOURIER IS NIET TOEPASBAAR.
    %air_dQ=air_dQ+aluminium_plate_air_dQ;
    
    %%%Heat flow plate to ambiant
    plate_dQ=plate_dQ+delta_time*Fourier(temperature_plate, temperature_amb, conductivity_styrofoam, 0.5*thickniss_styrofoam, area_plate);%Calculating heat loss from vessel
    plate_dQ=plate_dQ+delta_time*Radiation(temperature_plate, temperature_amb, 0.95, 0.95, area_plate, area_plate);%Radiation of copper tube to outside ambiant air.
    
    
    %%%%%%Procecing the physics of this tick.
    temperature_air=temperature_air+Heat_Capacity(air_dQ, amount_air, heat_capacity_air);
    temperature_water=temperature_water+Heat_Capacity(water_dQ, amount_water, heat_capacity_water);
    temperature_plate=temperature_plate+Heat_Capacity(plate_dQ, amount_plate, heat_capacity_plate);
    
    data(loop, 1) = time;%Here the data is saved in the data matrix.
    data(loop, 2) = temperature_water;
    data(loop, 3) = temperature_plate;
    data(loop, 4) = temperature_air;
    loop = loop+1;%This is needed for saving in the empty data matrix. Doesn't do anything for the simulation.
end

csvwrite('data.csv',data)%Writes the data to a csv file.

plot(data(:,1), data(:,2))%Plots the data in matlab (DO NOT USE THIS IN THE REPORT!!! use orgin for plots in the report).
hold on
plot(data(:,1), data(:,3))
plot(data(:,1), data(:,4))
title('Plot of temperature over time.')
xlabel('Time (s)')
ylabel('Temperature(K)')
legend('Water', 'Plate', 'Air')
hold off
close%COMMENT THIS OUT WHEN RUNNING so that the plot opens. This is here because the plot opening during testing is annoying.