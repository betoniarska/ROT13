
def salakirjoita(sana):

    kirjaimet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    a = 0
    uusi = ""
    while i < len(sana):

        while a < len(kirjaimet):
            if sana[i] == " ":
                uusi = uusi + " "
                break
            if sana[i] == kirjaimet[a]:  
                loop = 26 - len(kirjaimet[0:a])
            
                if len(kirjaimet[0:a]) + 13 < 26:
                    uusi = uusi + kirjaimet[len(kirjaimet[0:a]) + 13]
                    a = 0
                    break
                elif len(kirjaimet[0:a]) + 13 >= 26:
                    uusi = uusi + kirjaimet[a-13]
                    a = 0
                    break

            a = a + 1
        i = i + 1
    print(uusi)

salakirjoita("izc inenzvrfcnyiryh")






