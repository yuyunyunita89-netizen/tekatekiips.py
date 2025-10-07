# teka_teki_ips.py

import streamlit as st

# Judul dan deskripsi
st.title("🧠 Teka-Teki Pelajaran IPS")
st.subheader("Jawablah 25 soal pilihan ganda di bawah ini.")
st.markdown("Pilih jawaban yang menurutmu benar dari setiap soal.")

# Soal-soal IPS
soal = [
    {
        "pertanyaan": "1. Ibukota negara Indonesia adalah...",
        "opsi": {"a": "Bandung", "b": "Jakarta", "c": "Surabaya", "d": "Medan"},
        "jawaban": "b"
    },
    {
        "pertanyaan": "2. Indonesia terletak di antara dua benua, yaitu...",
        "opsi": {"a": "Asia dan Afrika", "b": "Asia dan Amerika", "c": "Asia dan Australia", "d": "Asia dan Eropa"},
        "jawaban": "c"
    },
    {
        "pertanyaan": "3. Semboyan bangsa Indonesia adalah...",
        "opsi": {"a": "Bhinneka Tunggal Ika", "b": "Pancasila", "c": "Garuda Pancasila", "d": "Tanah Airku"},
        "jawaban": "a"
    },
    # ... lanjutkan soal ke-4 sampai 25 seperti sebelumnya
]

# Tambahkan semua soal sampai nomor 25
soal.extend([
    {
        "pertanyaan": "4. Pulau terbesar di Indonesia adalah...",
        "opsi": {"a": "Jawa", "b": "Sumatra", "c": "Kalimantan", "d": "Sulawesi"},
        "jawaban": "c"
    },
    {
        "pertanyaan": "5. Sungai terpanjang di Indonesia adalah...",
        "opsi": {"a": "Kapuas", "b": "Mahakam", "c": "Musik", "d": "Bengawan Solo"},
        "jawaban": "a"
    },
    # Lanjutkan hingga soal ke-25
    {
        "pertanyaan": "25. Organisasi internasional yang didirikan untuk menjaga perdamaian dunia adalah...",
        "opsi": {"a": "ASEAN", "b": "PBB", "c": "NATO", "d": "Uni Eropa"},
        "jawaban": "b"
    }
])

# Form untuk kuis
with st.form("quiz_form"):
    jawaban_user = {}
    for i, s in enumerate(soal, 1):
        st.markdown(f"**{s['pertanyaan']}**")
        pilihan = st.radio(
            f"Soal {i}",
            options=list(s["opsi"].keys()),
            format_func=lambda x: f"{x}. {s['opsi'][x]}",
            key=f"soal_{i}"
        )
        jawaban_user[i] = pilihan

    submitted = st.form_submit_button("✅ Selesai Menjawab")

# Evaluasi
if submitted:
    skor = 0
    st.subheader("📊 Hasil Kuis")

    for i, s in enumerate(soal, 1):
        benar = s["jawaban"]
        user_jwb = jawaban_user[i]
        if user_jwb == benar:
            skor += 1
            st.success(f"Soal {i}: Benar ✅")
        else:
            st.error(f"Soal {i}: Salah ❌ (Jawaban benar: {s['opsi'][benar]})")

    st.markdown("---")
    st.write(f"### Skor kamu: {skor} dari {len(soal)}")

    if skor == len(soal):
        st.balloons()
        st.success("🎉 Sempurna! Kamu menguasai IPS dengan sangat baik!")
    elif skor >= 20:
        st.success("👍 Sangat bagus! Pertahankan!")
    elif skor >= 10:
        st.info("🙂 Lumayan, tapi masih bisa ditingkatkan.")
    else:
        st.warning("😅 Yuk, lebih giat belajar IPS lagi!")

