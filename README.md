
````markdown
# 🏥 Diyabet Tahmin Sistemi (Diabetes Prediction System)

Bu proje, **Pima Indians Diabetes Veri Seti** kullanılarak, hastaların sağlık verilerine (Glikoz, BMI, Yaş vb.) göre diyabet olup olmadıklarını tahmin eden bir makine öğrenmesi uygulamasıdır.

**Ders:** Veri Madenciliği Laboratuvarı  
**Model:** Random Forest Classifier  
**Dil:** Python 3.x

---

## 📂 Proje İçeriği

* **`diyabet_analizi.py`**: Veri işleme, model eğitimi ve raporlama yapan ana Python kodu.
* **`diabetes.csv`**: Pima Indians Diyabet veri seti (768 kayıt).
* **`requirements.txt`**: Projenin çalışması için gerekli kütüphaneler listesi.

---

## ⚙️ Kurulum (Installation)

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Projeyi Klonlayın:**
Terminal veya CMD ekranını açıp projeyi indirin:
```bash
git clone [https://github.com/zeynep-png/diyabet_analizi.git](https://github.com/zeynep-png/diyabet_analizi.git)
cd diyabet_analizi
````

**2. Gerekli Kütüphaneleri Yükleyin:**
Python ortamınıza gerekli paketleri (pandas, sklearn, numpy) kurun:

```bash
pip install -r requirements.txt
```

-----

## 🚀 Çalıştırma (Usage)

Kurulum tamamlandıktan sonra analizi başlatmak için şu komutu çalıştırın:

```bash
python diyabet_analizi.py
```

-----

## 📊 Sonuçların Yorumlanması (Önemli\!)

Kod çalıştığında **Accuracy (Doğruluk)**, **Recall (Duyarlılık)** ve **F1-Score** değerlerini göreceksiniz. Sağlık verilerinde bu metriklerin anlamı şudur:

1.  **Accuracy (Doğruluk):** Modelin genel başarısıdır. Ancak veri seti dengesizse (hasta sayısı azsa) tek başına yeterli değildir.
2.  **Recall (Duyarlılık):** Gerçekten hasta olanların ne kadarını tespit edebildiğimizdir.
      * *Düşük Recall Tehlikesi:* Hasta birine "Sağlıklısın" deyip eve göndermek hayati risk taşır. Bu yüzden sağlıkta en kritik metrik budur.
3.  **Confusion Matrix (Karmaşıklık Matrisi):**
      * **FN (False Negative):** Hasta olduğu halde modelin sağlıklı dediği kişiler (Kaçırılan vakalar).
      * **FP (False Positive):** Sağlıklı olduğu halde modelin hasta dediği kişiler (Yanlış alarm).

-----

## 📝 Veri Seti Özellikleri

Veri seti (`diabetes.csv`) şu sütunları içerir:

  * **Pregnancies:** Hamilelik sayısı
  * **Glucose:** Kandaki glikoz oranı
  * **BloodPressure:** Kan basıncı (Tansiyon)
  * **SkinThickness:** Deri kalınlığı
  * **Insulin:** İnsülin değeri
  * **BMI:** Vücut Kitle İndeksi
  * **DiabetesPedigreeFunction:** Soy ağacı diyabet fonksiyonu
  * **Age:** Yaş
  * **Outcome:** Sonuç (1: Diyabet, 0: Sağlıklı)

<!-- end list -->

```
