CREATE TABLE IF NOT EXISTS LONDON_DEPARTURES (FLIGHT_CODE TEXT PRIMARY KEY, DESTINATION TEXT, AIRLINE TEXT, PRICE_POUNDS TEXT, AIRCRAFT_TYPE);

INSERT INTO LONDON_DEPARTURES (FLIGHT_CODE, DESTINATION, AIRLINE, PRICE_POUNDS, AIRCRAFT_TYPE) VALUES 
('BA384', 'Marseille', 'British Airways', '£', 'Airbus A319'),
('TP1363', 'Lisbon', 'TAP Air Portugal', '£', 'Airbus A320 NEO'),
('OS340', 'Vienna', 'Austrian Airlines', '££', 'Airbus A320-200'),
('LX345', 'Zurich', 'airBaltic', '£', 'Airbus A220-300'),
('BA674', 'Preveza', 'British Airways', '££', 'Airbus A320-200'),
('CA856', 'Beijing', 'Air China', '££££', 'Boeing 777-300ER'),
('TK1984', 'Istanbul', 'Turkish Airlines', '£££', 'Airbus A330-300'),
('VS411', 'Lagos', 'Virgin Atlantic', '££££', 'Airbus A330-900'),
('AM8', 'Mexico City', 'AeroMexico', '£££', 'Boeing 787-9 Dreamliner'),
('SQ321', 'Singapore', 'Singapore Airlines', '££££', 'Boeing 777-300ER'),
('EK6', 'Dubai', 'Emirates', '£££', 'Airbus A380-800'),
('AI2016', 'Delhi', 'Air India', '£££', 'Boeing 787-9 Dreamliner'),
('MH1', 'Kuala Lumpur', 'Malaysia Airlines', '££££', 'Airbus A350-900'),
('TG917', 'Bangkok', 'Thai Airways', '££££', 'Boeing 777-300ER'),
('KL1000', 'Amsterdam', 'KLM', '£', 'Embraer E190');


SELECT DISTINCT AIRLINE FROM LONDON_DEPARTURES;

SELECT DISTINCT AIRCRAFT_TYPE FROM LONDON_DEPARTURES;

SELECT * FROM LONDON_DEPARTURES WHERE AIRCRAFT_TYPE='Airbus A320-200';

SELECT * FROM LONDON_DEPARTURES WHERE AIRLINE = 'Air India' AND PRICE_POUNDS IN ('££', '£££');

SELECT * FROM LONDON_DEPARTURES WHERE PRICE_POUNDS='£££';

SELECT * FROM LONDON_DEPARTURES WHERE AIRLINE LIKE '%Airlines%';