def game_description():  # oyunun tanımını içeren bir fonksiyon yazıyoruz
    """Oyunun kurallarını açıklayan bir karşılama mesajı oluşturur."""
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")    # Karşılama mesajı
    print("Kurallar:")      # Kurallar başlığı
    print("1. Taş, Kağıt veya Makas seçimi yaparak bilgisayara karşı oynayacaksınız.")   # Oyun kuralı 1
    print("2. İlk iki turu kazanan oyunu kazanır.")     # Oyun kuralı 2
    print("3. Her turdan sonra sonucu göreceksiniz.")   # Oyun kuralı 3
    print("4. Bu oyun için heyecanlı mısın?? Hadi Başlayalım!! İyi şanslar!\n")     # İyi şanslar mesajı yazdırır  \n bir alt satıra geçirir


import random  # random kütüphanesini import ediyoruz (bilgisayarın rastgele seçim yapabilmesi için)

choices = ["rock", "paper", "scissors"]  #  # Oyuncu ve bilgisayarın seçim yapabileceği seçenekleri içeren liste
yes_no = ['Y', 'N']  #  # Evet ve hayır seçeneklerini içeren liste (bilgisayara yeni oyun oynamak isteyip istemediğini sormak için)

player_wins = 0   # Oyuncunun kazandığı oyun sayısını tutan sayaç
computer_wins = 0  # Bilgisayarın kazandığı oyun sayısını tutan sayaç
played_games = 0   # Oynanan toplam oyun sayısını tutan sayaç
game_round = 0   # Oyun içindeki round sayısını tutan sayaç
game = 0   # Oynanan oyun sayısını tutan sayaç


def game_loop():   # Oyun döngüsünü başlatan fonksiyon
    """Oyun döngüsünü çalıştırır, her oyun için sayaçları sıfırlar ve genel galibi belirler."""   # Fonksiyonun ne yaptığını açıklayan docstring
    global player_wins, computer_wins, played_games, game_round, game   # Global değişkenler tanımlıyoruz

    while True:   # Sonsuz döngü, oyuncu oyunu bitirene kadar devam eder
        game += 1  # Oyun sayısını bir arttırıyoruz
        player_tour_win = 0   # Oyuncunun tur galibiyetlerini sıfırlıyoruz
        computer_tour_win = 0   # Bilgisayarın tur galibiyetlerini sıfırlıyoruz

        while player_tour_win < 2 and computer_tour_win < 2:    # Oyuncu veya bilgisayar iki tur kazanana kadar döngü devam ede
            game_round += 1  # Round sayacını bir arttırıyoruz
            print("----------------------------------------------------")
            print(f"##### GAME : {game}, ROUND: {game_round} ######")  # Oyun ve round bilgisini ekrana yazdırıyoruz

            # Oyuncuya seçim yapması için bir girdi alıyoruz (taş, kağıt, makas veya çıkmak için 'exit' yazabilir)
            player_choice = input(" 'rock', 'paper', 'scissors' or if you want to leave 'exit': ").lower()  # oyuncuya dışarıdan değer girdiriyoruz
            if player_choice == "exit":  # Eğer oyuncu 'exit' yazarsa
                print("Oyundan çıkılıyor!! Teşekkürler!!")   # Oyundan çıkıldığına dair mesaj veriyoruz
                return   # Fonksiyondan çıkıyoruz, oyun tamamen sona eriyor

            # Eğer oyuncu geçerli bir seçim yapmazsa tekrar seçim yapması istenir
            while player_choice not in choices:   # Oyuncunun girişi geçerli değilse döngü başa döner
                player_choice = input(" 'rock', 'paper', 'scissors' or if you want to leave 'exit': ").lower()   # Tekrar girdi isteriz
                if player_choice == "exit":   # Oyuncu 'exit' yazarsa
                    print("Oyundan çıkılıyor!! Teşekkürler!!")   # Oyundan çıkıldığına dair mesaj veririz
                    return   # Fonksiyondan çıkarız, oyun sona erer

            # Bilgisayarın rastgele seçim yapmasını sağlıyoruz
            computer_coice = random.choice(choices)    # Bilgisayar rastgele bir seçim yapar
            print(f"Computer Chose: {computer_coice} \n")   # Bilgisayarın seçimini ekrana yazdırırız

            # Oyuncu ve bilgisayarın seçimlerini karşılaştırarak sonucu belirleriz
            if player_choice == computer_coice:   # Seçimler aynıysa beraberlik durumu
                print("Bu tur berabere!!")
            elif (player_choice == "rock" and computer_coice == "scissors") or \
                    (player_choice == "paper" and computer_coice == "rock") or \
                    (player_choice == "scissors" and computer_coice == "paper"):   # Oyuncu kazanırsa
                print("Bu turu sen kazandın!!")   # Oyuncunun kazandığına dair mesaj
                player_tour_win += 1    # Oyuncu tur kazanma sayacını bir arttırırız
            else:     # Bilgisayar kazanırsa
                print("Bilgisayar bu turu kazandı!!")    # Bilgisayarın kazandığına dair mesaj
                computer_tour_win += 1    # Bilgisayar tur kazanma sayacını bir arttırırız

            # Tur sonucunu ekrana yazdırırız
            print(f"Tour Result: Player {player_tour_win} - {computer_tour_win} Computer\n")  # tur sonucu heaplama ve ekrana yazdırma

        # Eğer oyuncu 2 tur kazanmışsa oyunu kazanmış olur
        if player_tour_win == 2:
            print("Tebrikler!! OYUNU KAZANDIN! Beni yendin!! :)) \n")   # Oyuncunun kazandığına dair mesaj
            player_wins += 1     # Oyuncunun oyun kazanma sayacını bir arttırırız
        else:    # Aksi takdirde bilgisayar oyunu kazanmış olur
            print("Bilgisayar OYUNU KAZANDI! \n")    # Bilgisayarın kazandığına dair mesaj
            computer_wins += 1    # Bilgisayarın oyun kazanma sayacını bir arttırırız

        # Round sayacını sıfırlarız ve oynanan oyun sayacını bir arttırırız
        game_round = 0   # Round sayacını sıfırlarız
        played_games += 1    # Oynanan oyun sayacını bir arttırırız

        # Oyun sonuçlarını ekrana yazdırırız
        print(f"-----Toplam Oynanan Oyun Sayısı: {played_games} -----")    # Toplam oynanan oyun sayısını ekrana yazdırırız
        print(f"**** OYUN SONUCU: Oyuncu {player_wins} - {computer_wins} Bilgisayar ****\n ")    # Genel oyun sonucunu ekrana yazdırırız

        # Yeni bir oyun oynamak isteyip istemediğini oyuncuya sorarız
        print("----------------------------------------------------")
        play_request = input("Başka bir oyun daha oynamak ister misin? (Y/N): ").lower()    # Oyuncuya yeni bir oyun oynamak isteyip istemediğini sorarız
        if play_request != "y":   # Eğer cevap 'Y' değilse
            break     # Döngüyü kırarız, oyun sona erer

        # Bilgisayarın yeni bir oyun oynamak isteyip istemediğini kontrol ederiz
        choice_yes_no = random.choice(yes_no)  # Bilgisayar rastgele 'Y' veya 'N' seçer
        if choice_yes_no == "Y":    # Eğer bilgisayar 'Y' seçtiyse
            print(f"Bilgisayar Cevabı: Bende oynamak istiyorum. Hadi oynayalım!! : {choice_yes_no} \n")   # Bilgisayarın oynamak istediğini ekrana yazdırırız
            continue    # Oyun devam eder
        elif choice_yes_no == "N":     # Eğer bilgisayar 'N' seçtiyse
            print(f"Bilgisayar Cevabı: Tekrar oynamak istemiyorum!! Yoruldum :) : {choice_yes_no} \n")    # Bilgisayarın oynamak istemediğini ekrana yazdırırız
            break    # Döngüyü kırarız, oyun sona erer


# Oyunu başlatan fonksiyonu tanımlarız
def rock_paper_scissors_ADINIZ_SOYADINIZ():
    game_description()   # Oyun tanımını ekrana yazdırırız
    game_loop()    # Oyun döngüsünü çalıştırırız
    print("Oyun sona erdi!! Teşekkürler!")    # Oyun bttiğinde teşekkür mesajı ekrana yazdırırız

# Oyunu başlatırız
rock_paper_scissors_ADINIZ_SOYADINIZ()
