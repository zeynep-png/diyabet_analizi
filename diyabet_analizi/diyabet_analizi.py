import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, classification_report

def main():
    print("--- DİYABET TAHMİN SİSTEMİ ---")
    
    # 1. VERİ YÜKLEME 
   
    df = pd.read_csv("diabetes.csv")
   

    # 2. VERİ ÖN İŞLEME
    # Hedef Değişken (Target): 'Outcome' (1: Diyabet Var, 0: Sağlıklı)
    X = df.drop('Outcome', axis=1) # Girdi özellikleri
    y = df['Outcome']              # Tahmin edilecek sütun

    # Veriyi %70 Eğitim, %30 Test olarak ayırıyoruz
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 3. MODEL EĞİTİMİ (Random Forest)
    print("\n[BİLGİ] Model eğitiliyor...")
    # class_weight='balanced': Veri setindeki dengesizliği (hasta sayısı azsa) tolare eder.
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    # 4. TAHMİN
    y_pred = model.predict(X_test)

    # 5. PERFORMANS METRİKLERİ
    acc = accuracy_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n" + "="*40)
    print("SONUÇLAR VE METRİKLER")
    print("="*40)
    print(f"Accuracy (Doğruluk) : {acc:.4f}  -> (Genel Başarı)")
    print(f"Recall (Duyarlılık) : {rec:.4f}  -> (Gerçek hastaları yakalama oranı)")
    print(f"F1 Score            : {f1:.4f}  -> (Denge Puanı)")
    print("-" * 40)
    
    # 6. KARMAŞIKLIK MATRİSİ (CONFUSION MATRIX)
    print("\nKarmaşıklık Matrisi (Confusion Matrix):")
    cm = confusion_matrix(y_test, y_pred)
    
    # Matrisi daha okunabilir formatta yazdıralım
    print(f"               Tahmin: SAĞLIKLI | Tahmin: DİYABET")
    print(f"Gerçek: SAĞLIKLI      {cm[0][0]:<5}     |      {cm[0][1]:<5}")
    print(f"Gerçek: DİYABET       {cm[1][0]:<5}     |      {cm[1][1]:<5}")
    
    print("\n" + "-"*40)
    print("Detaylı Sınıflandırma Raporu:")
    print(classification_report(y_test, y_pred, target_names=['Sağlıklı', 'Diyabet']))

if __name__ == "__main__":
    main()
