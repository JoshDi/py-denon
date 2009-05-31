#from denon.data.commands import parameters

commands = [
{'code': 'PW', 'params': [], 'desc': 'POWERON/STANDBY change'},
{'code': 'MV', 'params': [], 'desc': 'MASTER VOLUME UP/DOWN, direct change to **dB  **:00 to 99 by ASCII, 80=0dB, 99=--- (MIN)'},
{'code': 'CV', 'params': [], 'desc': 'CHANNEL VOLUE UP/DOWN, direct change to **dB  ---front Lch  **:38 to 62 by ASCII, 50=0dB'},   
{'code': 'MU', 'params': [], 'desc': 'OUTPUT MUTE ON/OFF change'},
{'code': 'SI', 'params': [], 'desc': 'Select INPUT source'},
{'code': 'ZM', 'params': [], 'desc': 'MAIN-ZONE ON/OFF change'},
{'code': 'Z2', 'params': [], 'desc': 'MULTI ZONE-2 mode set, and select source.  The name of PARAMETER is the same as that of the time of SI COMMAND'},
{'code': 'Z2MU', 'params': [], 'desc': 'ZONE2 OUTPUT MUTE ON/OFF change'},
{'code': 'Z3', 'params': [], 'desc': 'MULTI ZONE-3 mode set, and select source.  The name of PARAMETER is the same as that of the time of SI COMMAND'},
{'code': 'Z3MU', 'params': [], 'desc': 'ZONE3 OUTPUT MUTE ON/OFF change'},
{'code': 'SR', 'params': [], 'desc': 'REC SELECT mode set, and select SOURCE.  The name of PARAMETER is the same as that of the time of SI COMMAND'},
{'code': 'SD', 'params': [], 'desc': 'SET DIGITAL INPUT MODE'},
{'code': 'SV', 'params': [], 'desc': 'VIDEO SELECT MODE set , and select SOURCE'},
]
