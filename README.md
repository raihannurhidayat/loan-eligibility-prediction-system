# 🏦 Loan Eligibility Prediction System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey.svg)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black.svg)

Sistem prediksi kelayakan pinjaman (*loan eligibility*) menggunakan *machine learning* berbasis *Random Forest Classifier*. Proyek ini mencakup seluruh pipeline ML: dari eksplorasi data, preprocessing, pelatihan model, evaluasi, hingga deployment API menggunakan Flask di platform Vercel.

---

## 📋 Informasi Proyek

| Info | Detail |
|------|--------|
| **Nama** | Muhamad Raihan Nurhidayat |
| **NPM** | 237006108 |
| **Kelas** | D |
| **Mata Kuliah** | Machine Learning |
| **Semester** | 6 (UAS) |
| **Dataset** | German Credit Dataset (UCI ML Repository) |

---

## 🎯 Deskripsi

Sistem ini memprediksi kelayakan pinjaman seorang pemohon berdasarkan data historis menggunakan algoritma **Random Forest**. Model dilatih menggunakan German Credit Dataset yang berisi 1000 pemohon pinjaman dengan 20 fitur dan target biner (Good/Bad credit).

**Jenis Tugas**: Supervised Learning · Binary Classification  
**Tech Stack**: `Python 3.10+` · `Scikit-learn` · `Flask` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn`

---

## 📊 Dataset

### German Credit Dataset
- **Sumber**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))
- **Jumlah Data**: 1000 instances (700 Good, 300 Bad)
- **Fitur**: 20 fitur (7 numerik, 13 kategorikal)
- **Target**: `Creditability` (1 = Good, 0 = Bad)
- **Missing Values**: Tidak ada

### Fitur Utama (Top 4 dari Feature Importance)
1. **Account Balance** - Saldo rekening saat ini
2. **Duration of Credit (month)** - Durasi kredit dalam bulan
3. **Credit Amount** - Jumlah kredit
4. **Age (years)** - Usia pemohon

Untuk dokumentasi lengkap dataset, lihat [ml/docs/purpose.md](ml/docs/purpose.md).

---

## 🏗️ Struktur Repository

```
loan-eligibility-prediction-system/
├── ml/                          # Komponen Machine Learning
│   ├── notebooks/
│   │   └── main.ipynb         # Jupyter notebook (full ML pipeline)
│   ├── models/
│   │   └── rf_model.pkl       # Model Random Forest terlatih
│   ├── data/
│   │   ├── raw/
│   │   │   └── dataset_credit.csv
│   │   └── processed/         # Data hasil preprocessing
│   │       ├── X.csv
│   │       ├── y.csv
│   │       ├── feature.csv
│   │       └── label.csv
│   └── docs/
│       └── purpose.md         # Dokumentasi dataset
│
├── backend/                     # Flask API Backend
│   ├── app.py                 # API endpoints
│   ├── rf_model.pkl           # Copy model untuk deployment
│   ├── vercel.json            # Konfigurasi deployment Vercel
│   ├── requirements.txt       # Dependencies Python
│   └── venv/                 # Virtual environment
│
├── vercel.json                 # Konfigurasi deployment utama
├── .gitignore
└── README.md
```

---

## 🤖 Model Machine Learning

### Arsitektur
- **Algorithm**: Random Forest Classifier
- **Tuning**: GridSearchCV untuk optimasi hyperparameter

### Parameter Model (Terbaik)
```python
RandomForestClassifier(
    n_estimators=200,          # Jumlah pohon
    max_depth=10,              # Kedalaman maksimum pohon
    min_samples_split=10,      # Minimum sampel untuk split
    min_samples_leaf=4,        # Minimum sampel per leaf
    max_samples=0.8,          # 80% data per pohon (bagging)
    max_features='sqrt',       # Standard klasifikasi
    class_weight='balanced',   # Handle class imbalance
    random_state=42,
    n_jobs=-1                  # Gunakan semua CPU cores
)
```

### Performa Model
| Metrik | Nilai |
|--------|-------|
| **Accuracy** | 79.00% |
| **ROC-AUC Score** | 0.8346 |
| **Precision (Good)** | 0.86 |
| **Recall (Good)** | 0.84 |
| **F1-Score (Good)** | 0.85 |
| **Cross-Validation (5-fold)** | 72.90% (±8.94%) |

### Confusion Matrix
```
[[ 41  19]   # TN: 41, FP: 19
 [ 23 117]]  # FN: 23, TP: 117
```

### Top 5 Feature Importance
1. Account Balance (19.92%)
2. Duration of Credit (11.58%)
3. Credit Amount (11.35%)
4. Age (years) (8.02%)
5. Value Savings/Stocks (7.72%)

---

## 🚀 API Endpoints

Base URL: `https://loan-eligibility-prediction-system.vercel.app`

### 1. GET `/`
Informasi API dan daftar endpoint.

**Response**:
```json
{
  "message": "German Credit Random Forest API",
  "version": "1.0",
  "endpoints": {
    "/predict": "POST - Prediksi satu record",
    "/predict_batch": "POST - Prediksi banyak record",
    "/health": "GET - Cek status API"
  },
  "model": "Random Forest (tuned)",
  "features_count": 4
}
```

### 2. GET `/health`
Cek status kesehatan API.

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 3. POST `/predict`
Prediksi kelayakan kredit untuk satu pemohon.

**Request Body**:
```json
{
  "Account Balance": 2,
  "Duration of Credit (month)": 12,
  "Value Savings/Stocks": 1,
  "Credit Amount": 2000
}
```

**Response**:
```json
{
  "prediction": 1,
  "prediction_label": "Good",
  "probability_good": 0.85,
  "probability_bad": 0.15,
  "features_received": 4
}
```

### 4. POST `/predict_batch`
Prediksi batch untuk multiple records.

**Request Body**:
```json
[
  {"Account Balance": 2, "Duration of Credit (month)": 12, ...},
  {"Account Balance": 1, "Duration of Credit (month)": 24, ...}
]
```

### 5. GET `/model_info`
Informasi detail tentang model.

---

## 🛠️ Instalasi & Penggunaan

### Prerequisites
- Python 3.10+
- pip

### 1. Clone Repository
```bash
git clone https://github.com/[username]/loan-eligibility-prediction-system.git
cd loan-eligibility-prediction-system
```

### 2. Setup Backend
```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Jalankan API Lokal
```bash
python app.py
```
API akan berjalan di `http://localhost:8080`

### 4. Gunakan Notebook
Buka `ml/notebooks/main.ipynb` menggunakan Jupyter Notebook atau Jupyter Lab:
```bash
jupyter notebook ml/notebooks/main.ipynb
```

---

## 📦 Dependencies

### Backend (requirements.txt)
```
flask
flask-cors
pandas
numpy
scikit-learn
joblib
gunicorn
```

### ML Development
```
jupyter
matplotlib
seaborn
jcopml
```

---

## 🌐 Deployment

### Vercel Deployment
1. Push kode ke GitHub
2. Connect repository ke [Vercel](https://vercel.com)
3. Vercel akan otomatis mendeteksi `vercel.json` dan melakukan deployment

**CORS Configuration**:
- ✅ `https://loan-eligibility-prediction-website.vercel.app`
- ✅ `http://localhost:3000`

---

## 📈 ML Pipeline (Notebook)

Notebook `ml/notebooks/main.ipynb` mencakup:

1. **Data Understanding**
   - Load dataset
   - Eksplorasi data (head, info, missing values, unique values)
   - Analisis distribusi target

2. **Data Preparation**
   - Split features (X) dan target (y)
   - Train-test split (80:20) dengan stratifikasi
   - Save processed data

3. **Modeling**
   - Inisialisasi Random Forest
   - Hyperparameter tuning dengan GridSearchCV
   - Training model

4. **Evaluation**
   - Accuracy score
   - Classification report
   - Confusion matrix
   - ROC-AUC score
   - Cross-validation (5-fold)
   - Feature importance analysis

5. **Export Model**
   - Save model dengan Joblib (`rf_model.pkl`)

---

## 🔍 Feature Encoding

Dataset menggunakan numerical encoding untuk fitur kategorikal:

| Fitur | Encoding |
|-------|----------|
| Account Balance | 1: < 0 DM, 2: 0-200 DM, 3: ≥ 200 DM, 4: No account |
| Payment Status | 0-4 (berdasarkan kategori kredit sebelumnya) |
| Purpose | 0-10 (new car, used car, furniture, etc.) |
| ... | Lihat [purpose.md](ml/docs/purpose.md) untuk detail lengkap |

---

## 📝 Catatan

- Model menggunakan `class_weight='balanced'` untuk menangani ketidakseimbangan kelas (700 Good vs 300 Bad)
- API hanya membutuhkan 4 fitur utama untuk prediksi (sesuai FEATURES di app.py)
- Untuk prediksi lengkap dengan 20 fitur, perlu modifikasi di `app.py`
- Dataset asli dari UCI menggunakan encoding berbeda (1=Good, 2=Bad), dataset ini sudah diubah ke (1=Good, 0=Bad)

---

## 📚 Referensi

1. UCI Machine Learning Repository. *Statlog (German Credit Data)*. [Link](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))
2. Grömping, U. (2019). *South German Credit – Correcting a Widely Used Data Set*.
3. GitHub: [deepanshu88/Datasets](https://github.com/deepanshu88/Datasets)
4. Pennsylvania State University. *Analysis of German Credit Data*. [Link](https://online.stat.psu.edu/stat857/)

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik (UAS Machine Learning Semester 6).

---

**Dibuat dengan ❤️ menggunakan Python & Scikit-learn**
