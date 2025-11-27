# Reception Asset Tracking System (RATS) v2.0
# Developed by Emirhan Kandemir

verilen_kartlar = {} 

print("--- RESEPSİYON KART SİSTEMİ (RATS) ---")

while True:
    print("\n-------------------------")
    print("1: Kart Ver")
    print("2: Kart Teslim Al")
    print("3: Çıkış")
    print("4: Tüm Listeyi Göster")
    print("5: Hakkında")
    
    
    islem = input("İşlem Seçiniz: ")

    # SENARYO 1: Kart Ver
    if islem == "1":
        try:
            kart_no = int(input("Kart No: "))
            if kart_no in verilen_kartlar:
                print(f"HATA: {kart_no} zaten {verilen_kartlar[kart_no]} kişisinde!")
            else:
                firma = input("Alan Kişi/Firma: ")
                verilen_kartlar[kart_no] = firma
                print(f"OK: {kart_no} -> {firma} teslim edildi.")
        except ValueError:
            print("HATA: Sadece rakam giriniz.")

    # SENARYO 2: Kart Al
    elif islem == "2":
        try:
            kart_no = int(input("Kart No: "))
            if kart_no in verilen_kartlar:
                silinen = verilen_kartlar.pop(kart_no) # .pop hem siler hem ismi getirir
                print(f"OK: {kart_no} geri alındı. ({silinen})")
            else:
                print("HATA: Bu kart zaten bizde.")
        except ValueError:
            print("HATA: Sadece rakam giriniz.")

    # SENARYO 3: Çıkış
    elif islem == "3":
        print("İyi nöbetler!")
        break 
    
    # SENARYO 4: Listeleme
    elif islem == "4":
        print("\n--- DIŞARIDAKİ KARTLAR LİSTESİ ---")
        
        # Eğer liste boşsa kullanıcıyı uyaralım
        if len(verilen_kartlar) == 0:
            print("Şu an tüm kartlar resepsiyonda. Dışarıda kart yok.")
        else:
            
            for numara, isim in verilen_kartlar.items():
                print(f"Kart: {numara} | Alan: {isim}")
        
        input("\nListeyi incelediysen Enter'a bas...")

    # SENARYO 5: Hakkında
    elif islem == "5":
        print("\n--- Developed by Emirhan Kandemir ---")
        input("Devam etmek için Enter'a bas...")
        continue


    else:
        print("Geçersiz seçim.")
