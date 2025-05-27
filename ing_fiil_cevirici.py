def vowel(girdi):
    liste=["a","e","i","o","u"]

    iii=girdi[-2]

    for elemanlar in liste:
        if elemanlar==iii:
            return True
        

def irregular_verbs(verb):
    for elemanlar in düzensiz_fiiler:
        if elemanlar[0]==verb:
            return True



def double_consotans(verb):
    for elemanlar in doubled_consonants_verbs:
        if elemanlar==verb:
            return True



doubled_consonants_verbs=[]
with open("doubled_consonants verbs.txt","r",encoding="utf-8") as file0:
    for elemanlar in file0:
        elemanlar=elemanlar.strip()
        doubled_consonants_verbs.append(elemanlar)





düzensiz_fiiler=[]
with open("irregular_verbs.txt","r",encoding="utf-8") as file:
    for elemanlar in file:
        elemanlar=elemanlar.strip()
        düzensiz_fiiler.append(elemanlar.split())






all_verbs=[]
with open("ing_filler.txt","r",encoding="utf-8")as file2:
    for verbs in file2:
        verbs=verbs[1:-3]

        all_verbs.append(verbs)





def verbs_controll(c):
    for elemanlar in all_verbs:
        if elemanlar==c:
            return True
        
        

baboli=["can","could","must","will","would","may","might","shall","should","dare","need","ought to"]           

# UYGULAMA BAŞLIYOR BURADAN SONRA

print("""
**************************************

İNGİLİZCE FİİL ÇEVİRİCİYE HOŞGELDİNİZ.
      
**************************************
""")

while True:
    islem=input("\nUygulamaya devam etmek için 1\nÇıkış yapmak içinse 2 ye tıklayınız : ")


    try:
        islem=int(islem)

        if islem==1:

            verb=str(input("\nİşlem yapılacak fiili giriniz : "))


            if verb in baboli:
                print(f"\n{verb} fiili bir modal verb olduğu için 2. ve 3. hali yoktur")



            elif verbs_controll(verb):

                if irregular_verbs(verb):
                    for elemanlar in düzensiz_fiiler:
                        if elemanlar[0]==verb:
                            print(f"\n{verb} fiilinin 2. hali = {elemanlar[1]}  3. hali = {elemanlar[2]}")

            
                elif double_consotans(verb):
                    for elemanlar in doubled_consonants_verbs:
                        if elemanlar==verb:
                            sh=verb[-1]
                            new=verb+sh+"ed"
                            print(f"\n{verb} fiilinin 2. hali = {new} 3. hali = {new}")
                
                
                else:
                    son_harf=verb[-1]

                    if son_harf=="w" or son_harf=="x":
                        print(f"\n{verb} fiilinin 2. hali = {verb+"ed"}  3. hali = {verb+"ed"}")


                    elif son_harf=="e":
                        print(f"\n{verb} fiilinin 2. hali = {verb+"d"}   3. hali = {verb+"d"}")

                    
                    elif son_harf=="y":
                        if vowel(verb):
                            print(f"\n{verb} fiilinin 2. hali = {verb+"ed"}  3. hali = {verb+"ed"}")

                        
                        else:
                            new_w=verb[0:-1]
                            
                            print(f"\n{verb} fiilinin 2. hali = {new_w+"ied"}  3. hali = {verb+"ied"}")


                    
                    else:
                        print(f"\n{verb} fiilinin 2. hali = {verb+"ed"}  3. hali  = {verb+"ed"}")



            else:
                print("\nBu Kelime Bir Fiil Değil.")



        elif islem==2:
            break



        else:
            print("\nLütfen sadece 1 veya 2 rakamını tuşlayınız.")



    except ValueError:
        print("\nLütfen sadece rakam giriniz.")
