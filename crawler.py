import socket, time, re, string

def connect_server(ip,port,retry=10):
    s=socket.socket(); #objekt pomocu kojeg klijent komunicira sa serverom, otvaranje kanala prema serveru
    #dohvacanje greski
    try:
        s.connect((ip,port)) #povezivanje sa serverom na otvorenom kanalu preko funkcije socet
    except Exception as e:
        print(e);
        if retry>0:
            time.sleep(1); #ako povezivanje ne uspije, ponovno povezivanje se odgada za 1 sekundu (zasto?)
            retry-=1; #smanjivanje broja pokusaja
            connect_server(ip,port,retry);
    return s; #vrati objekt koji kaze da na tom tocno kanalu komuniciramo sa serverom


def get_source_data(s,ip,page):
    CRLF='\r\n'
    get= 'GET /' + page + ' HTTP/1.1' + CRLF
    get+='Host: '
    get+=ip
    get+=CRLF
    get+=CRLF  #dva razmaka
    #moramo get poslati serveru u bajtovima, prebaciti ga u utf-8
    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1') #vracamo odgovor na latinici, odgovor je html cijele stranice u obliku stringa
    #print (response)
    return response;

def get_links(response):
    links=[];
    start=0;
    #beskonacna petlja za prolazenje po stringu tj html stranici
    while True:
        #pronalazak pocetka oznake linka href='
        start_link=response.find('href="',start)
        if start_link== -1:
            return links; #ako dobijemo -1, znaci nigdje vise se ne pojavljuje oznaka href
        end_link=response.find('"',start_link+6)
        link=response[start_link+6:end_link] #spajanje nadenih linkova
        if link not in links:
            links.append(link);
        start=end_link+1;
    return links;

ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'

#ogranicavanje  broja posjecenih linkova i provjera statusa 200 OK
#
MAX_LINKS=50;
links=set();
red=[page]
while red and len(links)<MAX_LINKS:
    trenutna_str=red.pop(0) #uzimamo prvi iz reda   fifo
    if trenutna_str in links:
        continue
    #ako je vec u visited linkovima, nastavi, a ako nije, nadodaj je na listu
    links.add(trenutna_str);
    s = connect_server(ip, port)
    #print (s)
    response = get_source_data(s, ip, page)
    s.close() #zatvaranje konekcije nakon dobivanja odgovora, kako bi izbjegli previse otvorenih konekcija za svaki link

    #provjera statusa 200OK
    if '200 OK' not in response.split('\r\n')[0]:
        print(f"Stranica {trenutna_str} nije dostupna (nije 200 OK)")
        continue
    found_links = get_links(response)  
    for link in found_links:
        if len(links) >= MAX_LINKS:
            break  
        if link.startswith("/") and link not in links:
            red.append(link)  # Dodajemo samo relativne linkove iste domene
        else:
            print("popis linkova: ",link)
    

print("\nPronađeni linkovi:")
for link in links:
    print(link)








