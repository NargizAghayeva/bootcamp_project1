ad = ""
soyad = ""
yaş = 0
email_adresi = ""
ad_günü = ""
şəxsi_məlumatlar_doldurulub = False
kontaktlar = {}


print("Mənim sadə proqramıma xoş gəlmisiniz!")
cavab = input("Proqramı çalışdırmaq üçün \"başla\", bitirmək üçün \"sonlandır\" yazın: ")


while cavab not in {"başla", "sonlandır"}:
    cavab = input("Yazdığınız mətn düzgün deyildi. Bir daha sınayın: ")


if cavab == "başla":
    print("Proqram başlayır!")

    while True:
        print("---------------------")
        print("|       Menyu       |")
        print("---------------------")
        if şəxsi_məlumatlar_doldurulub:
            print("| 1. Şəxsi məlumatları redaktə et")
            print("| 2. Şəxsi məlumatları gör")
            print("| 3. Kontakt əlavə et")
            print("| 4. Mövcud kontaktı redaktə et")
            print("| 5. Mövcud kontaktları gör")
            print("| 6. Kontakt axtarışı et")
            print("| 7. Mesaj yaz")
            print("| 8. Proqramı dayandır")
            seçim = input("Seçiminiz: ")

            while seçim not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
                seçim = input("Seçiminiz keçərli deyil. Bir daha seçim edin: ")

            print()
            if seçim == "1":
                print("---------------------")
                print("|  Məlumat Redaktə  |")
                print("---------------------")
                ad = input("Adınızı daxil edin: ")
                soyad = input("Soyadınızı daxil edin: ")
                yaş = int(input("Yaşınızı daxil edin: "))
                email_adresi = input("Email adresi daxil edin: ")
                ad_günü = input("Ad gününüzü daxil edin: ")
            elif seçim == "2":      
                print("---------------------")
                print("|    Məlumatlar     |")
                print("---------------------")
                print(f"Ad, Soyad: {ad} {soyad}")
                print(f"Yaş: {yaş}")
                print(f"Əlaqə email ünvanı: {email_adresi}")
                print(f"Ad günü: {ad_günü}")
            elif seçim == "3":    
                print("---------------------")
                print("|   Yeni Kontakt    |")
                print("---------------------")
                yeni_kontakt_ad = input("Əlavə ediləcək kontaktın adı: ")
                if yeni_kontakt_ad in kontaktlar.keys():
                    print("Bu adda kontakt artıq mövcuddur!")
                else:
                    yeni_kontakt_nömrə = input("Əlavə ediləcək kontaktın nömrəsi: ")
                    kontaktlar[yeni_kontakt_ad] = yeni_kontakt_nömrə
            elif seçim == "4":
                print("---------------------")
                print("|  Kontakt Redaktə  |")
                print("---------------------")
                redaktə_kontakt_ad = input("Redaktə ediləcək kontaktın adı: ")
                if redaktə_kontakt_ad not in kontaktlar.keys():
                    print("Bu adda kontakt mövcud deyil!")
                else:
                    redaktə_kontakt_nömrə = input("Redaktə ediləcək kontaktın nömrəsi: ")
                    kontaktlar[redaktə_kontakt_ad] = redaktə_kontakt_nömrə
            elif seçim == "5":
                print("---------------------")
                print("|    Kontaktlar     |")
                print("---------------------")
                for kontakt in kontaktlar.keys():
                    print(f"{kontakt} -> {kontaktlar[kontakt]}")
            elif seçim == "6":
                print("---------------------")
                print("|  Kontakt Axtarış  |")
                print("---------------------")
                axtarış_kontakt_ad = input("Axtarmaq istədiyiniz kontaktın adını daxil edin: ")
                if axtarış_kontakt_ad not in kontaktlar.keys():
                    print("Bu adda kontakt mövcud deyil!")
                else:
                    axtarış_kontakt_nömrə = kontaktlar[axtarış_kontakt_ad]
                    print(f"Axtarılan kontaktın nömrəsi: {axtarış_kontakt_nömrə}")
            elif seçim == "7":
                print("---------------------")
                print("|       Mesaj       |")
                print("---------------------")
                mesaj_kontakt_ad = input("Mesaj yazmaq istədiyiniz kontaktın adını daxil edin: ")
                if mesaj_kontakt_ad not in kontaktlar.keys():
                    print("Bu adda kontakt mövcud deyil!")
                else:
                    mesaj_kontakt_nömrə = kontaktlar[mesaj_kontakt_ad]
                    mesaj = input("Göndərmək istədiyiniz mesajı yazın:\n")
                    print()
                    print(f"{mesaj_kontakt_ad} adlı kontakta ({mesaj_kontakt_nömrə}) mesaj göndərildi:\n{mesaj}")
            else:
                break
            
        else:
            print("| 1. Şəxsi məlumatları doldur")
            print("| 2. Proqramı dayandır")
            seçim = input("Seçiminiz: ")

            while seçim not in {"1", "2"}:
                seçim = input("Seçiminiz keçərli deyil. Bir daha seçim edin: ")
            
            print()
            if seçim == "1":
                print("---------------------")
                print("| Şəxsi Məlumatlar  |")
                print("---------------------")
                ad = input("Adınızı daxil edin: ")
                soyad = input("Soyadınızı daxil edin: ")
                yaş = int(input("Yaşınızı daxil edin: "))
                email_adresi = input("Email adresi daxil edin: ")
                ad_günü = input("Ad gününüzü daxil edin: ")
                print("Şəxsi məlumatlar tamamlandı!")
                şəxsi_məlumatlar_doldurulub = True
            else:
                break
                
        input()


print("Proqramın sonu!")
input()
