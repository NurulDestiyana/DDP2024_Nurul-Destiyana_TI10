import streamlit as st
import re

def format_rupiah(value):
    """Format angka menjadi format rupiah."""
    return f"Rp {value:,.2f}"

def parse_rupiah(value):
    """Mengonversi input string rupiah menjadi float."""
    if value:
        return float(re.sub(r'[^\d]', '', value))
    return 0.0

def hitung_kebutuhan_hidup(makanan, tempat_tinggal, transportasi, tagihan, hiburan, lain_lain):
    """Menghitung total pengeluaran dan memberikan saran berdasarkan total pengeluaran."""
    total_pengeluaran = makanan + tempat_tinggal + transportasi + tagihan + hiburan + lain_lain
    
    if total_pengeluaran < 2000000:
        saran = "Pengeluaran Anda tergolong rendah. Anda bisa menabung lebih banyak!"
    elif total_pengeluaran <= 5000000:
        saran = "Pengeluaran Anda tergolong wajar. Pastikan untuk tetap mengelola keuangan dengan baik."
    else:
        saran = "Pengeluaran Anda tergolong tinggi. Pertimbangkan untuk mengurangi beberapa pengeluaran."
    
    return total_pengeluaran, saran

def hitung_tabungan(tabungan_awal, simpanan_bulanan, suku_bunga_tahunan, jangka_waktu_tahun):
    """Menghitung total tabungan setelah jangka waktu tertentu."""
    total_tabungan = tabungan_awal
    for bulan in range(jangka_waktu_tahun * 12):
        total_tabungan += simpanan_bulanan
        if (bulan + 1) % 12 == 0:
            total_tabungan += total_tabungan * suku_bunga_tahunan
    return total_tabungan

def main():
    # Membuat sidebar untuk navigasi
    st.sidebar.title("Navigasi")
    option = st.sidebar.selectbox("Pilih Aplikasi:", ["Beranda", "Kebutuhan Hidup", "Kalkulator Tabungan", "Pelacak Dana Darurat"])

    if option == "Beranda":
        st.title("Selamat Datang di WEB Mengelola Keuangan Harian")
        st.image("home.jpg", caption="Gambar Aplikasi Keuangan", use_container_width=True)
        
        st.write("""
        Aplikasi ini dirancang untuk membantu Anda mengelola keuangan pribadi Anda dengan lebih baik. 
        Berikut adalah fitur-fitur yang tersedia:
        """)
        
        st.subheader("1. Kebutuhan Hidup")
        st.write("""Fitur ini memungkinkan Anda untuk menghitung total pengeluaran bulanan Anda berdasarkan kategori 
        seperti makanan, tempat tinggal, transportasi, tagihan, hiburan, dan lain-lain. Anda juga akan mendapatkan saran berdasarkan total pengeluaran Anda.""")
        
        st.subheader("2. Kalkulator Tabungan")
        st.write("""Dengan fitur ini, Anda dapat menghitung total tabungan Anda setelah jangka waktu tertentu 
        dengan mempertimbangkan tabungan awal , simpanan bulanan, dan suku bunga tahunan.""")
        
        st.subheader("3. Pelacak Dana Darurat")
        st.write("""Fitur ini membantu Anda merencanakan dan melacak dana darurat Anda. 
        Anda dapat memasukkan target dana darurat, jumlah tabungan saat ini, dan kontribusi bulanan untuk mengetahui berapa lama waktu yang dibutuhkan untuk mencapai target tersebut.""")

    elif option == "Kebutuhan Hidup":
        st.title("Aplikasi Kebutuhan Hidup")
        st.image("1.jpg", caption="Gambar KEBUTUHAN HIDUP", use_container_width=True)

        makanan = parse_rupiah(st.text_input("Makanan (Rp):", "0"))
        tempat_tinggal = parse_rupiah(st.text_input("Tempat Tinggal (Rp):", "0"))
        transportasi = parse_rupiah(st.text_input("Transportasi (Rp):", "0"))
        tagihan = parse_rupiah(st.text_input("Tagihan (Rp):", "0"))
        hiburan = parse_rupiah(st.text_input("Hiburan (Rp):", "0"))
        lain_lain = parse_rupiah(st.text_input("Lain-lain (Rp):", "0"))

        if st.button("Hitung Total"):
            total_pengeluaran, saran = hitung_kebutuhan_hidup(makanan, tempat_tinggal, transportasi, tagihan, hiburan, lain_lain)
            st.success(f"Total pengeluaran bulanan Anda adalah: {format_rupiah(total_pengeluaran)}")
            st.info(saran)
        
        if st.button("Kembali ke Menu Utama"):
            return

    elif option == "Kalkulator Tabungan":
        st.title("Kalkulator Tabungan dengan Streamlit")
        st.image("2.jpg", caption="Gambar KALKULATOR TABUNGAN", use_container_width=True)

        tabungan_awal = parse_rupiah(st.text_input("Masukkan jumlah tabungan awal (Rp):", "0"))
        simpanan_bulanan = parse_rupiah(st.text_input("Masukkan jumlah simpanan bulanan (Rp):", "0"))
        suku_bunga_tahunan = parse_rupiah(st.text_input("Masukkan suku bunga tahunan (%):", "0")) / 100
        jangka_waktu_tahun = st.number_input("Masukkan jangka waktu tabungan (tahun):", min_value=1)

        if st.button("Hitung Total Tabungan"):
            total = hitung_tabungan(tabungan_awal, simpanan_bulanan, suku_bunga_tahunan, jangka_waktu_tahun)
            st.success(f"Total tabungan setelah {jangka_waktu_tahun} tahun adalah: {format_rupiah(total)}")

        if st.button("Kembali ke Menu Utama"):
            return

    elif option == "Pelacak Dana Darurat":
        st.title("Pelacak Dana Darurat")
        st.image("3.jpg", caption="Gambar PELACAK DANA DARURAT", use_container_width=True)

        goal = st.number_input("Masukkan target dana darurat (Rp):", min_value=0.0)
        current_savings = st.number_input("Masukkan jumlah tabungan saat ini (Rp):", min_value=0.0)
        monthly_contribution = st.number_input("Masukkan kontribusi bulanan (Rp):", min_value=0.0)

        def calculate_time_to_goal(goal, current_savings, monthly_contribution):
            if monthly_contribution <= 0:
                return "Kontribusi bulanan harus lebih dari 0."
            months_needed = (goal - current_savings) / monthly_contribution
            return months_needed

        if st.button("Hitung Waktu untuk Mencapai Target"):
            months = calculate_time_to_goal(goal, current_savings, monthly_contribution)
            if isinstance(months, str):
                st.error(months)
            else:
                years = months // 12
                remaining_months = months % 12
                st.success(f"Anda akan mencapai target dana darurat dalam {int(years)} tahun dan {int(remaining_months)} bulan.")

        if st.button("Kembali ke Menu Utama"):
            return

if __name__ == "__main__":
    main()