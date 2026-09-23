import pandas as pd
import matplotlib.pyplot as plt

# ---------- A. Pengorganisasian Data ----------
# Ganti path sesuai lokasi file di komputer / Google Colab
path = "nilai.xlsx"
dataraw = pd.read_excel(path)
print("=== TABEL DATA ===")
print(dataraw)

# Tabel frekuensi grade
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
datafrq["Persentase (%)"] = (datafrq["Frekuensi"] / datafrq["Frekuensi"].sum() * 100).round(1)
print("\n=== TABEL FREKUENSI ===")
print(datafrq)

# ---------- B. Penyajian Data ----------
warna = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

# Grafik garis
ax = datafrq["Frekuensi"].plot(marker="o", color="#27275F", figsize=(7, 4.5))
ax.set_title("Grafik Garis Frekuensi Grade Mahasiswa")
ax.set_ylabel("Jumlah Mahasiswa"); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig("grafik_garis.png", dpi=150); plt.show(); plt.close()

# Grafik batang
ax = datafrq["Frekuensi"].plot(kind="bar", color=warna, figsize=(7, 4.5), rot=0)
ax.set_title("Grafik Batang Frekuensi Grade Mahasiswa")
ax.set_ylabel("Jumlah Mahasiswa")
for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()),
                ha="center", va="bottom")
plt.tight_layout(); plt.savefig("grafik_batang.png", dpi=150); plt.show(); plt.close()

# Pie chart
ax = datafrq.plot(kind="pie", y="Frekuensi", autopct="%1.0f%%", legend=False,
                  colors=warna, figsize=(6, 6), startangle=90)
ax.set_ylabel(""); ax.set_title("Pie Chart Persentase Grade Mahasiswa")
plt.tight_layout(); plt.savefig("pie_chart.png", dpi=150); plt.show(); plt.close()

# ---------- C. Statistika Deskriptif ----------
dataraw["Nilai"] = pd.to_numeric(dataraw["Nilai"], errors="coerce")
dt = dataraw["Nilai"]
stats = dt.describe()
stats["Standard Error"] = dt.sem()
stats["Median"] = dt.median()
stats["Mode"] = dt.mode().iloc[0]
stats["variance"] = dt.var()
stats["range"] = dt.max() - dt.min()
stats["skewness"] = dt.skew()
stats["kurtosis"] = dt.kurtosis()
print("\n=== STATISTIKA DESKRIPTIF NILAI AKHIR ===")
print(stats)

# Tambahan: IQR & deteksi outlier
q1, q3 = dt.quantile(0.25), dt.quantile(0.75)
iqr = q3 - q1
batas_bawah, batas_atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("\n=== IQR & OUTLIER ===")
print(f"IQR = {iqr:.2f} | Batas bawah = {batas_bawah:.3f} | Batas atas = {batas_atas:.3f}")
print("Outlier :", dt[(dt < batas_bawah) | (dt > batas_atas)].tolist() or "tidak ada")
print(f"Koefisien variasi (SD/Mean) = {dt.std() / dt.mean() * 100:.1f}%")
