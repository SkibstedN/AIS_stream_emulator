# AIS_stream_emulator
Real-time AIS data stream simulation


pip install Flask
pip install requests


kør localServer.py og herefter csvToJSON.py i hver sin terminal med csv filen i samme folder.

csvToJSON.py læser fra csv filen, omformaterer hver row til JSON og sender det til serveren.

Implementeret random delay for at simulerer data pakker sendt med forskellige intervaller 
fra IOT-devices.

Delayet kan justeres i linie 32 i csvToJSON.py (milisekunder).

Timestamp fra det tidspunkt hvert POST request oprettes, bliver skrevet ind i JSON
objektet og sendt med så man kan måle tiden det tager før dataen når frem til ende 
destinationen.


se aktiviteten i consollerne

