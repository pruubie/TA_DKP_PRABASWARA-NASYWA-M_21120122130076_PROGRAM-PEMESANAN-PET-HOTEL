import tkinter as tk
from tkinter import messagebox, ttk
import time
import threading
import datetime

class SplashScreen(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Pruubie Pet Hotel")
        self.geometry("300x300")
        self.configure(bg="white")

        self.label_splash = tk.Label(self, text="Pruubie Pet Hotel", font=("Lucida Bright", 16, "bold"), bg="white", fg="peachpuff4")
        self.label_splash.pack(pady=20)

        self.image = tk.PhotoImage(file=r"C:\\Users\\LENOVO\Documents\\pawkiciw2.png")
        self.label_image = tk.Label(self, image=self.image)
        self.label_image.pack()

        self.progress_bar = ttk.Progressbar(self, mode="indeterminate")
        self.progress_bar.pack(pady=20)

        self.label_loading = tk.Label(self, text="Loading...", font=("Lucida Bright", 12), bg="white")
        self.label_loading.pack()

        self.start_loading()

    def start_loading(self):
        self.progress_bar.start(10)
        threading.Thread(target=self.load_data).start()

    def load_data(self):
        time.sleep(2)

        self.progress_bar.stop()
        self.destroy()
        app.window.deiconify()

class PetBoardingApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pruubie Pet Hotel")
        self.window.geometry("1500x900")
        self.window.config(bg="white")
        self.main_frame = None
        self.closing_frame = None
        self.customer_name = ""
        self.customer_phone = ""
        self.customer_address = ""
        self.pet_name = ""
        self.pet_type = ""
        self.pet_age = ""
        self.pet_characteristics = ""

        self.service_var = tk.StringVar()

        self.create_widgets()

        self.splash_screen = SplashScreen()
        self.window.withdraw()

    def create_widgets(self):
        self.welcome_frame = tk.Frame(self.window, bg="white")
        self.welcome_frame.pack()

        self.label_welcome_title = tk.Label(self.welcome_frame, text="Hai Pawrents! Selamat Datang di Pruubie Pet Hotel!", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_welcome_title.pack(pady=10)

        self.image = tk.PhotoImage(file=r"C:\\Users\\LENOVO\Documents\\pawkiciw2.png")
        self.label_image = tk.Label(self.welcome_frame, image=self.image)
        self.label_image.pack()

        self.label_Mohon_baca = tk.Label(self.welcome_frame, text="Sebelum membuat pesanan, pahami ketentuan penitipan di bawah ini dulu ya Pawrents!", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_Mohon_baca.pack()

        #syarat anabul
        self.label_syarat_anabul = tk.Label(self.welcome_frame, text="---------------- Syarat Anabul yang bisa dititipkan pada Pruubie Pet Hotel ----------------", font=("Lucida Bright", 12), bg="white")
        self.label_syarat_anabul.pack(pady=5)

        self.label_syarat_anabul_detail = tk.Label(self.welcome_frame, text="1. Anabul harus sehat, nafsu makan baik, tidak demam, umur sesuai dengan syarat minimal 3 bulan, berat badan minimal 1,5 kg.\n2. Anabul juga harus sudah melalui masa adaptasi di rumah selama 7-14 hari.\n3. Anabul tidak batuk, pilek, bersin, muntah, diare, tidak ada masalah kulit, tak ada infeksi, dan tidak cacingan.", font=("Lucida Bright", 12), bg="white")
        self.label_syarat_anabul_detail.pack(pady=5)

        # grade
        self.label_grade_penitipan = tk.Label(self.welcome_frame, text="---------------- Grade Penitipan ----------------", font=("Lucida Bright", 12), bg="white")
        self.label_grade_penitipan.pack(pady=5)

        self.label_grade_vip = tk.Label(self.welcome_frame, text="- VIP (100.000 per hari)\n   Kandang full AC, kandang mewah ukuran 120cm x 100 cm x 100 cm. Lantai keramik, air minum mineral bukan air mentah, \nsudah termasuk makanan mewah minimal Royal Canin dan setara, pasir gumpal wangi dan litter rutin dibersihkan.\n", font=("Lucida Bright", 12), bg="white")
        self.label_grade_vip.pack(pady=5)

        self.label_grade_deluxe = tk.Label(self.welcome_frame, text="- Deluxe (85.000 per hari)\n   Kandang full AC, kandang aluminium premium ukuran 80 cm x 70 cm x 50 cm. Lantai keramik, minum air mineral, \nmakanan mewah dan setara, pasir gumpal dan litter rutin dibersihkan.\n", font=("Lucida Bright", 12), bg="white")
        self.label_grade_deluxe.pack(pady=5)

        self.label_grade_standard = tk.Label(self.welcome_frame, text="- Standar (60.000 per hari)\n   Kandang full AC, kandang lipat ukuran 60, termasuk air minum mineral, makanan mewah dan setara, pasir gumpal wangi \ndan litter rutin dibersihkan.", font=("Lucida Bright", 12), bg="white")
        self.label_grade_standard.pack(pady=5)

        #fasilitas lainnya
        self.label_fasilitas_lainnya = tk.Label(self.welcome_frame, text="---------------- Fasilitas Lainnya ----------------", font=("Lucida Bright", 12), bg="white")
        self.label_fasilitas_lainnya.pack(pady=5)

        self.label_fasilitas_detail = tk.Label(self.welcome_frame, text="Pawrents mendapatkan update foto anabul setiap hari, kebersihan kandang dan alat makan terjamin, free grooming dan antar jemput, dan staff ahli yang berpengalaman.", font=("Lucida Bright", 12), bg="white")
        self.label_fasilitas_detail.pack(pady=5)

        self.label_klik = tk.Label(self.welcome_frame, text="Jika sudah mengerti, silakan klik tombol di bawah ini untuk memulai!", font=("Lucida Bright", 14), bg="white")
        self.label_klik.pack()

        self.button_start = tk.Button(self.welcome_frame, text="MULAI", command=self.next_step1, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_start.pack(pady=10)

        self.main_frame = tk.Frame(self.window, bg="white", highlightbackground="white", highlightcolor="white")

    def clear_widgets(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()

    def next_step1(self):
        self.clear_widgets()

        self.step1_frame = tk.Frame(self.window, bg="white")
        self.step1_frame.pack()


        self.label_step1_title = tk.Label(self.step1_frame, text="Silakan Isi Data Diri Pawrents!", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_step1_title.pack(pady=10)

        self.label_step1_name = tk.Label(self.step1_frame, text="Nama :", font=("Lucida Bright", 12), bg="white")
        self.label_step1_name.pack()

        self.entry_step1_name = tk.Entry(self.step1_frame, font=("Lucida Bright", 12))
        self.entry_step1_name.pack(pady=5)

        self.label_step1_phone = tk.Label(self.step1_frame, text="Nomor Telepon:", font=("Lucida Bright", 12), bg="white")
        self.label_step1_phone.pack()

        self.entry_step1_phone = tk.Entry(self.step1_frame, font=("Lucida Bright", 12))
        self.entry_step1_phone.pack(pady=5)

        self.label_step1_address = tk.Label(self.step1_frame, text="Alamat:", font=("Lucida Bright", 12), bg="white")
        self.label_step1_address.pack()

        self.entry_step1_address = tk.Entry(self.step1_frame, font=("Lucida Bright", 12))
        self.entry_step1_address.pack(pady=5)

        self.button_next_step1 = tk.Button(self.step1_frame, text="NEXT", command=self.validate_step1, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_next_step1.pack(pady=10)

    def validate_step1(self):
        self.customer_name = self.entry_step1_name.get()
        self.customer_phone = self.entry_step1_phone.get()
        self.customer_address = self.entry_step1_address.get()

        if not self.customer_name or not self.customer_phone or not self.customer_address:
            messagebox.showerror("Error", "Mohon isi semua field yang tersedia.")
        else:
            self.next_step2()

    def next_step2(self):
        self.clear_widgets()

        self.step2_frame = tk.Frame(self.window, bg="white")
        self.step2_frame.pack()

        self.label_step2_title = tk.Label(self.step2_frame, text="Silakan Isi Data Anabul!", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_step2_title.pack(pady=10)

        self.label_step2_pet_typecombo = tk.Label(self.step2_frame, text="Pilih Anabul:", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_typecombo.pack()

        self.pet_choose_combobox = ttk.Combobox(self.step2_frame, font=("Lucida Bright", 12), state="readonly")
        self.pet_choose_combobox['values'] = ['Kucing', 'Anjing', 'Kelinci']
        self.pet_choose_combobox.pack(pady=5)

        self.label_step2_pet_name = tk.Label(self.step2_frame, text="Nama Anabul:", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_name.pack()

        self.entry_step2_pet_name = tk.Entry(self.step2_frame, font=("Lucida Bright", 12))
        self.entry_step2_pet_name.pack(pady=5)

        self.label_step2_pet_type = tk.Label(self.step2_frame, text="Ras :", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_type.pack()

        self.entry_step2_pet_type = tk.Entry(self.step2_frame, font=("Lucida Bright", 12))
        self.entry_step2_pet_type.pack(pady=5)

        self.label_step2_pet_age = tk.Label(self.step2_frame, text="Usia :", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_age.pack()

        self.entry_step2_pet_age = tk.Entry(self.step2_frame, font=("Lucida Bright", 12))
        self.entry_step2_pet_age.pack(pady=5)

        self.label_step2_pet_characteristics = tk.Label(self.step2_frame, text="Karakteristik :", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_characteristics.pack()

        self.entry_step2_pet_characteristics = tk.Entry(self.step2_frame, font=("Lucida Bright", 12))
        self.entry_step2_pet_characteristics.pack(pady=5)

        self.label_step2_pet_allergies = tk.Label(self.step2_frame, text="Alergi :", font=("Lucida Bright", 12), bg="white")
        self.label_step2_pet_allergies.pack()

        self.entry_step2_pet_allergies = tk.Entry(self.step2_frame, font=("Lucida Bright", 12))
        self.entry_step2_pet_allergies.pack(pady=5)

        self.button_next_step2 = tk.Button(self.step2_frame, text="NEXT", command=self.validate_step2, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_next_step2.pack(pady=10)

    def validate_step2(self):
        self.pet_name = self.entry_step2_pet_name.get()
        self.pet_choose = self.pet_choose_combobox.get()
        self.pet_type = self.entry_step2_pet_type.get()
        self.pet_age = self.entry_step2_pet_age.get()
        self.pet_characteristics = self.entry_step2_pet_characteristics.get()
        self.pet_allergies = self.entry_step2_pet_allergies.get()

        if not self.pet_name or not self.pet_type or not self.pet_choose or not self.pet_age or not self.pet_characteristics or not self.pet_allergies:
            messagebox.showerror("Error", "Mohon isi semua field yang tersedia.")
        else:
            self.next_step3()

    def next_step3(self):
        self.clear_widgets()

        self.step3_frame = tk.Frame(self.window, bg="white")
        self.step3_frame.pack()

        self.label_step3_title = tk.Label(self.step3_frame, text="Silakan Isi Informasi Tambahan", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_step3_title.pack(pady=10)

        self.label_pilih_service = tk.Label(self.step3_frame, text="Pilih grade penitipan yang sesuai dengan kebutuhan Anabul!", font=("Lucida Bright", 13), bg="white")
        self.label_pilih_service.pack(pady=15)

        self.service_var = tk.StringVar()
        self.service_var.set(0)

        regular_radio = tk.Radiobutton(self.step3_frame, text="VIP", variable=self.service_var, value="VIP", font=("Lucida Bright", 12), bg="white")
        regular_radio.pack()

        premium_radio = tk.Radiobutton(self.step3_frame, text="Deluxe", variable=self.service_var, value="Deluxe", font=("Lucida Bright", 12), bg="white")
        premium_radio.pack()

        special_radio = tk.Radiobutton(self.step3_frame, text="Standar", variable=self.service_var, value="Standar", font=("Lucida Bright", 12), bg="white")
        special_radio.pack()

        self.label_Garis = tk.Label(self.step3_frame, text="--------------------------------------------------------------------------------", font=("Lucida Bright", 12), bg="white")
        self.label_Garis.pack()

        self.label_pilih_jumlah_hari = tk.Label(self.step3_frame, text="Masukan jumlah hari penitipan Anabul!", font=("Lucida Bright", 13), bg="white")
        self.label_pilih_jumlah_hari.pack(pady=15)

        self.label_step3_num_days = tk.Label(self.step3_frame, text="Jumlah Hari:", font=("Lucida Bright", 12), bg="white")
        self.label_step3_num_days.pack()

        self.entry_step3_num_days = tk.Entry(self.step3_frame, font=("Lucida Bright", 12))
        self.entry_step3_num_days.pack(pady=5)

        self.label_peringatan_day = tk.Label(self.step3_frame, text="Perhatian : Maksimal pemesanan adalah H-1 penitipan, mohon isi tanggal dengan benar!", font=("Lucida Bright", 13), bg="white")
        self.label_peringatan_day.pack(pady=10)

        self.label_step3_start_date = tk.Label(self.step3_frame, text="Tanggal Mulai (dd mm yyyy):", font=("Lucida Bright", 12), bg="white")
        self.label_step3_start_date.pack()

        self.entry_step3_start_date = tk.Entry(self.step3_frame, font=("Lucida Bright", 12))
        self.entry_step3_start_date.pack(pady=5)

        self.label_anterin = tk.Label(self.step3_frame, text="Anabul mau dijemput oleh kami atau diantar oleh Pawrents?", font=("Lucida Bright", 12), bg="white")
        self.label_anterin.pack(pady=5)

        self.pickup_var = tk.StringVar()
        self.pickup_var.set(0)

        pickup_radio = tk.Radiobutton(self.step3_frame, text="Pick up dari Pet Hotel", variable=self.pickup_var, value="pick up", font=("Lucida Bright", 12), bg="white")
        pickup_radio.pack()

        selfdeliv_radio = tk.Radiobutton(self.step3_frame, text="Diantar oleh Pawrents", variable=self.pickup_var, value="self delivery", font=("Lucida Bright", 12), bg="white")
        selfdeliv_radio.pack()

        self.label_regular = tk.Label(self.step3_frame, text="Jika belum mengerti mengenai fasilitas tiap grade, klik tombol dibawah untuk memunculkan informasi mengenai fasilitas tiap grade!", font=("Lucida Bright", 12, "bold"), bg="white")
        self.label_regular.pack(pady=5)

        self.button_next_step3 = tk.Button(self.step3_frame, text="Informasi Fasilitas", command=self.show_message_VIP, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_next_step3.pack(pady=10)

        button_VIP = tk.Button(text="NEXT", command=self.validate_step3, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        button_VIP.pack(pady=50)

    def show_message_VIP(self):
        messagebox.showinfo("Fasilitas", "1. VIP (100.000 perhari)\n Kandang full AC, kandang mewah ukuran 120cm x 100 cm x 100 cm. Lantai keramik, air minum mineral bukan air mentah, sudah termasuk makanan mewah minimal Royal Canin dan setara, pasir gumpal wangi dan litter rutin dibersihkan.\n \n 2. Deluxe (85.000 perhari)\n Kandang full AC. Kandang aluminium premium ukuran 80 cm x 70 cm x 50 cm. Lantai keramik, minum air mineral, makanan mewah dan setara, pasir gumpal dan litter rutin dibersihkan.\n \n 3.Standar (60.000 perhari)\n Kandang full AC. Kandang lipat ukuran 60, termasuk air minum mineral, makanan mewah dan setara, pasir gumpal wangi dan litter rutin dibersihkan.")

    def validate_step3(self):
        self.num_days = self.entry_step3_num_days.get()
        self.start_date_str = self.entry_step3_start_date.get()
        self.selected_pickup = self.pickup_var.get()

        while not self.selected_pickup:
            messagebox.showerror("Error", "Mohon pilih salah satu jenis layanan antar.")
            return

        if self.selected_pickup == "pick up":
            self.selected_pickup = "Anabul akan dipick up oleh kami pada"
        elif self.selected_pickup == "self delivery":
            self.selected_pickup = "Anabul akan diantar oleh Pet Parents pada"
        else:
            messagebox.showerror("Error", "Mohon pilih salah satu jenis layanan antar.")
            return

        while not self.num_days or not self.start_date_str:
            messagebox.showerror("Error", "Mohon isi semua field yang tersedia.")
            return

        try:
            num_days = int(self.num_days) 
            if num_days <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan jumlah hari penitipan dengan angka valid.")
            return

        try:
            self.start_date = datetime.datetime.strptime(self.start_date_str, "%d %m %Y").date()
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan tanggal mulai dengan format Hari Bulan Tahun (misal: 31 05 2023).")
            return
        
        today = datetime.datetime.now().date()
        if self.start_date <= today:
            messagebox.showerror("Error", "Tanggal mulai harus lebih dari hari ini.")
            return
        
        self.selected_service = self.service_var.get()
        if self.selected_service == "VIP":
            price_per_day = 100000
        elif self.selected_service == "Deluxe":
            price_per_day = 85000
        elif self.selected_service == "Standar":
            price_per_day = 60000
        else:
            messagebox.showerror("Error", "Mohon pilih salah satu jenis grade.")
            return

        self.calculate_price(price_per_day)
        self.show_summary()

    def calculate_price(self, price_per_day):
        try:
            num_days = int(self.num_days)
            self.total_price = num_days * price_per_day
            self.show_summary()
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan angka pada field Jumlah Hari.")

        for widget in self.window.winfo_children():
            widget.destroy()

    def run(self):
        self.window.mainloop()

    def show_summary(self):
        self.clear_widgets()

        self.label_title = tk.Label(self.window, text="Pruubie Pet Hotel", font=("Lucida Bright", 16, "bold"), bg="white", fg="peachpuff4", highlightbackground="white", highlightcolor="white")
        self.label_title.pack(pady=10)

        self.image = tk.PhotoImage(file=r"C:\\Users\\LENOVO\Documents\\pawkiciw2.png")
        self.label_image = tk.Label(self.window, image=self.image)
        self.label_image.pack()

        self.summary_frame = tk.Frame(self.window, bg="white")
        self.summary_frame.pack()

        self.label_summary_title = tk.Label(self.summary_frame, text="Ringkasan Pemesanan", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_summary_title.pack(pady=10)

        self.label_sum_title_name = tk.Label(self.summary_frame, text="--- Data Pawrent---", font=("Lucida Bright", 12, "bold"), bg="white")
        self.label_sum_title_name.pack(pady=10)

        self.label_summary_name = tk.Label(self.summary_frame, text= f"{self.customer_name} - {self.customer_phone}" , font=("Lucida Bright", 12), bg="white")
        self.label_summary_name.pack()

        self.label_summary_address = tk.Label(self.summary_frame, text=f"{self.customer_address}", font=("Lucida Bright", 12), bg="white")
        self.label_summary_address.pack()

        self.label_sum_title_pet = tk.Label(self.summary_frame, text="--- Data Anabul ---", font=("Lucida Bright", 12, "bold"), bg="white")
        self.label_sum_title_pet.pack(pady=10)

        pet_name_text = f"{self.pet_name} ({self.pet_choose} - {self.pet_type})"
        self.label_summary_pet_name = tk.Label(self.summary_frame, text=pet_name_text, font=("Lucida Bright", 12), bg="white")
        self.label_summary_pet_name.pack()

        self.label_summary_pet_age = tk.Label(self.summary_frame, text="Usia : " + str(self.pet_age) + " Tahun", font=("Lucida Bright", 12), bg="white")
        self.label_summary_pet_age.pack()

        self.label_summary_pet_characteristics = tk.Label(self.summary_frame, text="Karakteristik : " + self.pet_characteristics, font=("Lucida Bright", 12), bg="white")
        self.label_summary_pet_characteristics.pack()

        self.label_summary_pet_allergies = tk.Label(self.summary_frame, text="Alergi : " + self.pet_allergies, font=("Lucida Bright", 12), bg="white")
        self.label_summary_pet_allergies.pack()

        self.label_sum_title_datapen = tk.Label(self.summary_frame, text="--- Data Penitipan ---", font=("Lucida Bright", 12, "bold"), bg="white")
        self.label_sum_title_datapen.pack(pady=10)

        self.label_summary_num_days = tk.Label(self.summary_frame, text=f"{self.num_days} hari {self.selected_service} Grade", font=("Lucida Bright", 12), bg="white")
        self.label_summary_num_days.pack()

        self.label_summary_total_price = tk.Label(self.summary_frame, text="Total Harga: Rp " + str(self.total_price), font=("Lucida Bright", 12), bg="white")
        self.label_summary_total_price.pack()

        start_date_formatted = self.start_date.strftime("%d %B %Y")  
        summary_text = f"{self.selected_pickup} {start_date_formatted}"
        self.label_summary_pickup = tk.Label(self.summary_frame, text=summary_text, font=("Lucida Bright", 12), bg="white")
        self.label_summary_pickup.pack()

        self.label_payment_info = tk.Label(self.summary_frame, text="Apabila data sudah benar, silakan melakukan pembayaran ke Kartu Kredit 0138249813 (BNI) atas nama Pruubieswiry", font=("Lucida Bright", 12, "bold"), bg="white")
        self.label_payment_info.pack(pady=10)

        self.button_confirm = tk.Button(self.summary_frame, text="Konfirmasi Pembayaran", command=self.show_success_message, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_confirm.pack(pady=10)

        self.button_cancel = tk.Button(self.summary_frame, text="Data salah - Isi data ulang", command=self.next_step1, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_cancel.pack(pady=20)

    def show_success_message(self):
        messagebox.showinfo("Konfirmasi", "Pesanan Pawrents telah dibuat!.")
        self.clear_widgets()
        self.closing_frame = tk.Frame(self.window, bg="white")
        self.closing_frame.pack()

        self.label_closing_title = tk.Label(self.closing_frame, text="Pruubie Pet Hotel", font=("Lucida Bright", 16, "bold"), fg="peachpuff4", bg="white")
        self.label_closing_title.pack(pady=10)

        self.image = tk.PhotoImage(file=r"C:\\Users\\LENOVO\Documents\\pawkiciw2.png")
        self.label_image = tk.Label(self.closing_frame, image=self.image)
        self.label_image.pack()

        self.label_closing = tk.Label(self.closing_frame, text="Terima kasih telah mempercayai Pruubie Pet Hotel! Pembayaran anda dalam proses checking.", font=("Lucida Bright", 14), bg="white")
        self.label_closing.pack(pady=10)

        self.label_contact_cs = tk.Label(self.closing_frame, text="Kami akan segera mengonfirmasi pesanan Anda melalui nomor telepon yang telah Anda berikan. Mohon tunggu.", font=("Lucida Bright", 14), bg="white")
        self.label_contact_cs.pack(pady=10)

        self.label_contact_miaw = tk.Label(self.closing_frame, text="Salam miaw miaw!", font=("Lucida Bright", 14), bg="white")
        self.label_contact_miaw.pack(pady=10)

        self.button_close = tk.Button(self.closing_frame, text="Tutup", command=self.window.destroy, font=("Cooper Black", 16), bg="peachpuff4", fg="white", relief="flat")
        self.button_close.pack(pady=10)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PetBoardingApp()
    app.run()