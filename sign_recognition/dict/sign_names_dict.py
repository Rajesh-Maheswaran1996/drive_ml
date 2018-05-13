# -*- coding: utf-8 -*-
# mapping: GTSRB id (as int) to sign description (string)
import pickle

# outdated: various GTSRB signs
sign_name_GTSRB_full_dict = {15: 'Durchfahrt verboten', 
	32: 'Alle Regeln frei', 
	16: 'Durchfahrt verboten LKWs', 
	24: 'Straße wird enger links', 
	22: 'Bodenwellen', 
	34: 'Links Abbiegen', 
	3: 'Geschwindigkeitsbegrenzung 60', 
	19: 'Scharfe Kurve links', 
	11: 'Nächste Kreuzung Vorfahrt', 
	2: 'Geschwindigkeitsbegrenzung 50', 
	14: 'STOP', 	
	27: 'Vorsicht Fußgänger', 
	41: 'Überholverbot aufgehoben', 
	26: 'Vorsicht Ampel', 
	21: 'Kurvige Straße', 
	1: 'Geschwindigkeitsbegrenzung 30',
	39: 'Blauer Pfeil untenlinks', 
	5: 'Geschwindigkeitsbegrenzung 80', 
	17: 'Einbahnstraße falsche Seite', 
	8: 'Geschwindigkeitsbegrenzung 120',
	33: 'Rechts Abbiegen', 
	23: 'Rutschgefahr',
	7: 'Geschwindigkeitsbegrenzung 100',
	36: 'Geradeaus oder rechts abbiegen',
	10: 'Überholverbot LKW',
	9: 'Überholverbot PKW',
	30: 'Vorsicht Schnee',
	13: 'Vorfahrt gewähren',
	38: 'Blauer Pfeil untenrechts',
	18: '!-Zeichen', 
	31: 'Vorsicht Wild',
	4: 'Geschwindigkeitsbegrenzung 70',
	42: 'LKW-Überholverbot aufgehoben', 
	37: 'Geradeaus oder links abbiegen', 
	43: 'Kein Schild', 
	25: 'Vorsicht Bauarbeiten', 
	35: 'Geradeaus', 
	28: 'Vorsicht Kinder', 
	0: 'Geschwindigkeitsbegrenzung 20', 
	29: 'Vorsicht Fahrrad', 
	20: 'Scharfe Kurve rechts', 
	12: 'Vorfahtsstraße', 
	40: 'Kreisverkehr', 
	6: 'Geschwindigkeitsbegrenzung Ende 80'}

# all carolo cup signs currently in use
sign_name_carolo_dict = {
	1: '30 Zone Anfang (speed limit start)',
	9: 'Absolutes Überholverbot Anfang (no passing zone start)',
	12: 'Vorfahrtstraße (priority on next intersections)',
	13: 'Vorfahrt Gewähren (give way to incoming)',
	14: 'Stop Zeichen (stop for at least 3 sec)',
	33: 'Vorgeschriebene Fahrtrichtung Rechts (turn right on intersection)',
	34: 'Vorgeschriebene Fahrtrichtung Links (turn left on intersection)',
	41: 'Absolutes Überholverbot Ende (no passing zone end)',
	43: 'Nullklasse (zero class)',
	100: 'Gegenverkehr Vorrang gewähren (Barred area, let oncoming pass)',
	101: '30 Zone Ende (end of speed limit)',
	102: 'Fußgängerüberweg (crosswalk)',
	103: 'Richtungstafel Kurve links (sharp turn left)',
	104: 'Richtungstafel Kurve links (even sharper turn left)',
	105: 'Richtungstafel Kurve rechts (sharp turn right)',
	106: 'Richtungstafel Kurve rechts (even sharper turn right)',
	107: 'Gefälle 10% (downhill 10%)',
	108: 'Steigung 10% (uphill 10%)',
	109: 'Parken Bereich (parking zone)',
	110: 'Kraftfahrtstraße Anfang (expressway begin)',
	111: 'Kraftfahrtstraße Ende (expressway end)'
}

with open('sign_names_dict.pkl', 'wb') as f:
	pickle.dump(sign_name_carolo_dict, f)
	

