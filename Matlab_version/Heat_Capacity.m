function delta_temperature = Heat_Capacity(energy, mass, heat_capacity)
    %https://en.wikipedia.org/wiki/Heat_capacity#Intensive_properties
    delta_temperature=energy/(mass*heat_capacity);