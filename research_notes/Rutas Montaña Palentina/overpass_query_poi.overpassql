[out:json][timeout:120];
(
 nwr["amenity"="shelter"](42.75,-4.85,43.05,-4.05);
 nwr["tourism"~"^(alpine_hut|wilderness_hut|viewpoint|camp_site|hostel|information|museum|picnic_site)$"](42.75,-4.85,43.05,-4.05);
 nwr["natural"="spring"](42.75,-4.85,43.05,-4.05);
 nwr["amenity"~"^(drinking_water|parking|doctors|clinic|hospital|pharmacy|bus_station)$"](42.75,-4.85,43.05,-4.05);
 nwr["leisure"="picnic_table"](42.75,-4.85,43.05,-4.05);
 nwr["aeroway"="helipad"](42.75,-4.85,43.05,-4.05);
 nwr["emergency"="landing_site"](42.75,-4.85,43.05,-4.05);
 nwr["railway"="station"](42.75,-4.85,43.05,-4.05);
);
out center tags;
