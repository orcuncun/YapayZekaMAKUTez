import matplotlib.pyplot as plt
import numpy as np

# 1. Kaydedilen verileri oku
try:
    q_data = np.load("q_rewards.npy")
    dqn_data = np.load("dqn_rewards.npy")
except FileNotFoundError:
    print("Hata: Önce eğitim dosyalarını çalıştırıp verileri kaydetmelisiniz!")
    exit()

# 2. Grafik alanını oluştur
plt.figure(figsize=(10, 5))

# 3. Verileri çiz (Öğrenme eğrisi)
plt.plot(q_data, label='Q-Learning', color='blue', alpha=0.6)
plt.plot(dqn_data, label='Deep Q-Learning (DQN)', color='green', alpha=0.6)

# 4. Akademik detaylar ekle
plt.title("Pekiştirmeli Öğrenme Performans Karşılaştırması")
plt.xlabel("Episode (Deneme Sayısı)")
plt.ylabel("Toplam Ödül")
plt.legend() # Hangi çizginin ne olduğunu gösteren kutucuk
plt.grid(True) # Kareli arka plan (okumayı kolaylaştırır)

# 5. GÖRSELİ GÖSTER
plt.show() 

# 6. GÖRSELİ KAYDET
plt.savefig("karsilastirma_grafigi.png")