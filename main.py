# Reception Asset Tracking System (RATS)
# Developed by Emirhan Kandemir

# Başlangıçta kimseye kart vermedik, veritabanı boş.
verilen_kartlar = {} 

print("--- RESEPSİYON KART SİSTEMİ BAŞLATILDI (RATS) ---")

while True:
    print("\n-------------------------")
    print("1: Kart Ver (Check-out)")
    print("2: Kart Teslim Al (Check-in)")
    print("3: Çıkış")
    
    islem = input("İşlem Seçiniz: ")

    # SENARYO 1: Kurye geldi, kart vereceğiz.
    if islem == "1":
        try:
            kart_no = int(input("Vereceğiniz Kart Numarası: "))
            
            # Eğer kart zaten başkasındaysa uyarı ver
            if kart_no in verilen_kartlar:
                print(f"HATA: {kart_no} numaralı kart zaten {verilen_kartlar[kart_no]} isimli kişide!")
            else:
                firma = input("Kimin/Firmanın Adı: ")
                verilen_kartlar[kart_no] = firma
                print(f"BAŞARILI: {kart_no} numaralı kart {firma}'ya teslim edildi.")
        except ValueError:
            print("HATA: Lütfen kart numarası için sadece RAKAM giriniz.")

    # SENARYO 2: Kurye geri geldi, kartı alacağız.
    elif islem == "2":
        try:
            kart_no = int(input("Teslim Alınan Kart Numarası: "))
            
            # Kartın bizde kayıtlı olup olmadığını kontrol et
            if kart_no in verilen_kartlar:
                silinen_kisi = verilen_kartlar[kart_no] 
                del verilen_kartlar[kart_no] # Kaydı siliyoruz
                print(f"BAŞARILI: {kart_no} numaralı kart {silinen_kisi}'den geri alındı.")
            else:
                print("HATA: Bu kart numarası sistemde 'verilmiş' olarak görünmüyor.")
        except ValueError:
            print("HATA: Lütfen kart numarası için sadece RAKAM giriniz.")

    # SENARYO 3: Programı kapat.
    elif islem == "3":
        print("Sistem kapatılıyor. İyi nöbetler!")
        break 

    # Geçersiz bir tuşa basılırsa
    else:
        print("Geçersiz seçim, lütfen 1, 2 veya 3'e basınız.")

    # Her işlemden sonra mevcut durumu göster
    print(f"\n[GÜNCEL DURUM] Dışarıdaki Kartlar: {verilen_kartlar}")
