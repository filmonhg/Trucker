var simplemaps_usmap_mapdata = {

	main_settings:{
		//General settings
		width: '700', //or 'responsive'
		background_color: '#FFFFFF',	
		background_transparent: 'no',
		border_color: '#ffffff',
		popups: 'detect', //on_click, on_hover, or detect
	
		//State defaults
		state_description:   'State description',
		state_color: '#88A4BC',
		state_hover_color: '#3B729F',
		state_url: 'http://simplemaps.com',
		border_size: 1.5,		
		all_states_inactive: 'no',
		all_states_zoomable: 'yes',		
		
		//Location defaults
		location_description:  'Location description',
		location_color: '#FF0067',
		location_opacity: .8,
		location_hover_opacity: 1,
		location_url: '',
		location_size: 25,
		location_type: 'square', // circle, square, image
		location_image_source: 'frog.png', //name of image in the map_images folder		
		location_border_color: '#FFFFFF',
		location_border: 2,
		location_hover_border: 2.5,				
		all_locations_inactive: 'no',
		all_locations_hidden: 'no',
		
		//Labels
		label_color: '#d5ddec',	
		label_hover_color: '#d5ddec',		
		label_size: 22,
		label_font: 'Arial',
		hide_labels: 'no',
		hide_eastern_labels: 'no',
		
		//Zoom settings
		zoom: 'yes', //use default regions
		back_image: 'no',   //Use image instead of arrow for back zoom				
		arrow_color: '#3B729F',
		arrow_color_border: '#88A4BC',
		initial_back: 'no', //Show back button when zoomed out and do this JavaScript upon click		
		initial_zoom: -1,  //-1 is zoomed out, 0 is for the first continent etc	
		initial_zoom_solo: 'no', //hide adjacent states when starting map zoomed in
		region_opacity: 1,
		region_hover_opacity: .6,
		zoom_out_incrementally: 'yes',  // if no, map will zoom all the way out on click
		zoom_percentage: .99,
		zoom_time: .5, //time to zoom between regions in seconds
		
		//Popup settings
		popup_color: 'white',
		popup_opacity: .9,
		popup_shadow: 1,
		popup_corners: 5,
		popup_font: '12px/1.5 Verdana, Arial, Helvetica, sans-serif',
		popup_nocss: 'no', //use your own css	
		
		//Advanced settings
		div: 'map',
		auto_load: 'yes',		
		url_new_tab: 'no', 
		images_directory: 'default', //e.g. 'map_images/'
		fade_time:  .1, //time to fade out		
		link_text: '(Link)'  //Text mobile browsers will see for links	
		
	},

	state_specific:{	
		"HI": {
			name: 'Hawaii',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
		},
		"AK": {
			name: 'Alaska',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"FL": {
			name: 'Florida',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default',
			inactive: 'no'
			},
		"NH": {
			name: 'New Hampshire',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"VT": {
			name: 'Vermont',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"ME": {
			name: 'Maine',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'	
			},
		"RI": {
			name: 'Rhode Island',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"NY": {
			name: 'New York',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'	
		},
		"PA": {
			name: 'Pennsylvania',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"NJ": {
			name: 'New Jersey',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"DE": {
			name: 'Delaware',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"MD": {
			name: 'Maryland',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'						
			},
		"VA": {
			name: 'Virginia',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"WV": {
			name: 'West Virginia',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"OH": {
			name: 'Ohio',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"IN": {
			name: 'Indiana',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"IL": {
			name: 'Illinois',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"CT": {
			name: 'Connecticut',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"WI": {
			name: 'Wisconsin',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"NC": {
			name: 'North Carolina',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"DC": {
			name: 'District of Columbia',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
		},
		"MA": {
			name: 'Massachusetts',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"TN": {
			name: 'Tennessee',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"AR": {
			name: 'Arkansas',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"MO": {
			name: 'Missouri',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"GA": {
			name: 'Georgia',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"SC": {
			name: 'South Carolina',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"KY": {
			name: 'Kentucky',
			description: 'default',
			color: 'default',
			zoomable: 'no',
			hover_color: 'default',
			url: 'default'			
			},
		"AL": {
			name: 'Alabama',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'					
			},
		"LA": {
			name: 'Louisiana',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"MS": {
			name: 'Mississippi',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"IA": {
			name: 'Iowa',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"MN": {
			name: 'Minnesota',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"OK": {
			name: 'Oklahoma',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"TX": {
			name: 'Texas',
			description: 100,
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"NM": {
			name: 'New Mexico',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"KS": {
			name: 'Kansas',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'			
			},
		"NE": {
			name: 'Nebraska',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"SD": {
			name: 'South Dakota',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"ND": {
			name: 'North Dakota',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"WY": {
			name: 'Wyoming',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"MT": {
			name: 'Montana',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"CO": {
			name: 'Colorado',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"UT": {
			name: 'Utah',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"AZ": {
			name: 'Arizona',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		"NV": {
			name: 'Nevada',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"OR": {
			name: 'Oregon',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'		
			},
		"WA": {
			name: 'Washington',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"CA": {
			name: 'California',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'					
			},
		"MI": {
			name: 'Michigan',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'				
			},
		"ID": {
			name: 'Idaho',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default'
			},
		// Territories - Hidden unless hide is set to "no"
		"GU": {
			name: 'Guam',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default',
			hide: 'yes'
			},
		"VI": {
			name: 'Virgin Islands',
			image_source: 'x.png',			
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default',
			hide: 'yes'
			},
		"PR": {
			name: 'Puerto Rico',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default',
			hide: 'yes'
			},
		"MP": {
			name: 'Northern Mariana Islands',
			description: 'default',
			color: 'default',
			hover_color: 'default',
			url: 'default',
			hide: 'yes'
			}		
		},
	
	locations:{


0: { 
		name: 'Albuquerque,NM',
		lat: 35.0844444,
		lng: -106.6505556,
		type: 'circle',
		hide: 'no'
},
1: { 
		name: 'Arlington,TX',
		lat: 32.7355556,
		lng: -97.1077778,
		type: 'circle',
		hide: 'no'
},
2: { 
		name: 'Atlanta,GA',
		lat: 33.7488889,
		lng: -84.3880556,
		type: 'circle',
		hide: 'no'
},
3: { 
		name: 'Austin,TX',
		lat: 30.2669444,
		lng: -97.7427778,
		type: 'circle',
		hide: 'no'
},
4: { 
		name: 'Baltimore,MD',
		lat: 39.2902778,
		lng: -76.6125000,
		type: 'circle',
		hide: 'no'
},
5: { 
		name: 'Boston,MA',
		lat: 42.3583333,
		lng: -71.0602778,
		type: 'circle',
		hide: 'no'
},
6: { 
		name: 'Charlotte,NC',
		lat: 35.2269444,
		lng: -80.8433333,
		type: 'circle',
		hide: 'no'
},
7: { 
		name: 'Chicago,IL',
		lat: 41.8500000,
		lng: -87.6500000,
		type: 'circle',
		hide: 'no'
},
8: { 
		name: 'Cleveland,OH',
		lat: 41.4994444,
		lng: -81.6955556,
		type: 'circle',
		hide: 'no'
},
9: { 
		name: 'Columbus,OH',
		lat: 39.9611111,
		lng: -82.9988889,
		type: 'circle',
		hide: 'no'
},
10: { 
		name: 'Dallas,TX',
		lat: 32.7833333,
		lng: -96.8000000,
		type: 'circle',
		hide: 'no'
},
11: { 
		name: 'Denver,CO',
		lat: 39.7391667,
		lng: -104.9841667,
		type: 'circle',
		hide: 'no'
},
12: { 
		name: 'Detroit,MI',
		lat: 42.3313889,
		lng: -83.0458333,
		type: 'circle',
		hide: 'no'
},
13: { 
		name: 'El Paso,TX',
		lat: 31.7586111,
		lng: -106.4863889,
		type: 'circle',
		hide: 'no'
},
14: { 
		name: 'Fort Worth,TX',
		lat: 32.7252778,
		lng: -97.3205556,
		type: 'circle',
		hide: 'no'
},
15: { 
		name: 'Fresno,CA',
		lat: 36.7477778,
		lng: -119.7713889,
		type: 'circle',
		hide: 'no'
},
16: { 
		name: 'Houston,TX',
		lat: 29.7630556,
		lng: -95.3630556,
		type: 'circle',
		hide: 'no'
},
17: { 
		name: 'Indianapolis,IN',
		lat: 39.7683333,
		lng: -86.1580556,
		type: 'circle',
		hide: 'no'
},
18: { 
		name: 'Jacksonville,FL',
		lat: 30.3319444,
		lng: -81.6558333,
		type: 'circle',
		hide: 'no'
},
19: { 
		name: 'Kansas City,MO',
		lat: 39.0997222,
		lng: -94.5783333,
		type: 'circle',
		hide: 'no'
},
20: { 
		name: 'Las Vegas,NV',
		lat: 36.1750000,
		lng: -115.1363889,
		type: 'circle',
		hide: 'no'
},
21: { 
		name: 'Long Beach,CA',
		lat: 33.7669444,
		lng: -118.1883333,
		type: 'circle',
		hide: 'no'
},
22: { 
		name: 'Los Angeles,CA',
		lat: 34.0522222,
		lng: -118.2427778,
		type: 'circle',
		hide: 'no'
},
23: { 
		name: 'Louisville,KY',
		lat: 38.2541667,
		lng: -85.7594444,
		type: 'circle',
		hide: 'no'
},
24: { 
		name: 'Memphis,TN',
		lat: 35.1494444,
		lng: -90.0488889,
		type: 'circle',
		hide: 'no'
},
25: { 
		name: 'Mesa,AZ',
		lat: 33.4222222,
		lng: -111.8219444,
		type: 'circle',
		hide: 'no'
},
26: { 
		name: 'Miami,FL',
		lat: 25.7738889,
		lng: -80.1938889,
		type: 'circle',
		hide: 'no'
},
27: { 
		name: 'Milwaukee,WI',
		lat: 43.0388889,
		lng: -87.9063889,
		type: 'circle',
		hide: 'no'
},
28: { 
		name: 'Minneapolis,MN',
		lat: 44.9800000,
		lng: -93.2636111,
		type: 'circle',
		hide: 'no'
},
29: { 
		name: 'Nashville,TN',
		lat: 36.1658333,
		lng: -86.7844444,
		type: 'circle',
		hide: 'no'
},
30: { 
		name: 'New Orleans,LA',
		lat: 29.9544444,
		lng: -90.0750000,
		type: 'circle',
		hide: 'no'
},
31: { 
		name: 'New York,NY',
		lat: 40.7141667,
		lng: -74.0063889,
		type: 'circle',
		hide: 'no'
},
32: { 
		name: 'Oakland,CA',
		lat: 37.8044444,
		lng: -122.2697222,
		type: 'circle',
		hide: 'no'
},
33: { 
		name: 'Oklahoma City,OK',
		lat: 35.4675000,
		lng: -97.5161111,
		type: 'circle',
		hide: 'no'
},
34: { 
		name: 'Omaha,NE',
		lat: 41.2586111,
		lng: -95.9375000,
		type: 'circle',
		hide: 'no'
},
35: { 
		name: 'Philadelphia,PA',
		lat: 39.9522222,
		lng: -75.1641667,
		type: 'circle',
		hide: 'no'
},
36: { 
		name: 'Phoenix,AZ',
		lat: 33.4483333,
		lng: -112.0733333,
		type: 'circle',
		hide: 'no'
},
37: { 
		name: 'Portland,OR',
		lat: 45.5236111,
		lng: -122.6750000,
		type: 'circle',
		hide: 'no'
},
38: { 
		name: 'Raleigh,NC',
		lat: 35.7719444,
		lng: -78.6388889,
		type: 'circle',
		hide: 'no'
},
39: { 
		name: 'Sacramento,CA',
		lat: 38.5816667,
		lng: -121.4933333,
		type: 'circle',
		hide: 'no'
},
40: { 
		name: 'San Antonio,TX',
		lat: 29.4238889,
		lng: -98.4933333,
		type: 'circle',
		hide: 'no'
},
41: { 
		name: 'San Diego,CA',
		lat: 32.7152778,
		lng: -117.1563889,
		type: 'circle',
		hide: 'no'
},
42: { 
		name: 'San Francisco,CA',
		lat: 37.7750000,
		lng: -122.4183333,
		type: 'circle',
		hide: 'no'
},
43: { 
		name: 'San Jose,CA',
		lat: 37.3394444,
		lng: -121.8938889,
		type: 'circle',
		hide: 'no'
},
44: { 
		name: 'Seattle,WA',
		lat: 47.6063889,
		lng: -122.3308333,
		type: 'circle',
		hide: 'no'
},
45: { 
		name: 'Tucson,AZ',
		lat: 32.2216667,
		lng: -110.9258333,
		type: 'circle',
		hide: 'no'
},
46: { 
		name: 'Tulsa,OK',
		lat: 36.1538889,
		lng: -95.9925000,
		type: 'circle',
		hide: 'no'
},
47: { 
		name: 'Washington,DC',
		lat: 38.8950000,
		lng: -77.0366667,
		type: 'circle',
		hide: 'no'
},
48: { 
		name: 'Wichita,KS',
		lat: 37.6922222,
		lng: -97.3372222,
		type: 'circle',
		hide: 'no'
},



},




data:{ 
	'data': { 
		HI: '14',
		AK: '25',
		FL: '',
		NH: '',
		VT: '',
		ME: '',
		RI: '',
		NY: '',
		PA: '2',
		NJ: '',
		DE: '',
		MD: '',
		VA: '',
		WV: '',
		OH: '',
		IN: '',
		IL: '',
		CT: '',
		WI: '',
		NC: '',
		DC: '',
		MA: '',
		TN: '100',
		AR: '',
		MO: '',
		GA: '',
		SC: '',
		KY: '',
		AL: '',
		LA: '',
		MS: '',
		IA: '',
		MN: '',
		OK: '',
		TX: '',
		NM: '',
		KS: '',
		NE: '',
		SD: '',
		ND: '',
		WY: '',
		MT: '',
		CO: '',
		UT: '',
		AZ: '',
		NV: '',
		OR: '',
		WA: '',
		CA: '',
		MI: '',
		ID: '',
		GU: '',
		VI: '',
		PR: '',
		MP: ''
	},
		color: '#ff0000',
		rounding: '1',
		quintile: 'yes',
	'key': { 
		c1: '#ff8080',
		c2: '#ff4040',
		c3: '#ff0000',
		c4: '#bf0000',
		c5: '#800000',
		l1: '9.2',
		l2: '16.2',
		l3: '22.8',
		l4: '55.0'
	}
},













	
	labels:{
		"HI": {
			color: 'default',
			hover_color: 'default',
			font_family: 'default',
			pill: 'yes',	
			width: 'default',			
		}
	}
	
}
