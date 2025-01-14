import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Egzersiz hareketleri ve tekrar sayıları
exercises = {
    "Bicycle Crunches": "15 tekrar",
    "Bridge": "20 tekrar",
    "Burpees": "10 tekrar",
    "Donkey Kicks": "12 tekrar (her bacak)",
    "Flutter Kicks": "30 saniye",
    "Heel Taps": "20 tekrar",
    "High Knees": "30 saniye",
    "Jumping Jacks": "30 saniye",
    "Leg Raises": "15 tekrar",
    "Lunges": "10 tekrar (her bacak)",
    "Mountain Climbers": "30 saniye",
    "Plank": "30 saniye",
    "Push-Up": "12 tekrar",
    "Side Lunges": "10 tekrar (her bacak)",
    "Side Plank": "20 saniye (her taraf)",
    "Squat": "20 tekrar",
    "Superman": "15 tekrar",
    "Toe Touches": "20 tekrar",
    "Tricep Dips": "12 tekrar",
    "Wall Sit": "30 saniye"
}

# Kullanıcı Bilgilerini Almak için Fonksiyonlar
def calculate_bmr(gender, weight, height, age):
    if gender.lower() == 'erkek':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_daily_calories(bmr, activity_level):
    activity_multipliers = {
        'Az Hareketli': 1.2,
        'Orta Hareketli': 1.55,
        'Çok Hareketli': 1.725
    }
    return bmr * activity_multipliers[activity_level]

def adjust_calories_for_goal(calories, goal):
    if goal == 'Kilo Vermek':
        return calories - 500
    elif goal == 'Kilo Almak':
        return calories + 500
    else:
        return calories

def calculate_macros(calories):
    protein = calories * 0.3 / 4
    fat = calories * 0.25 / 9
    carbs = calories * 0.45 / 4
    return protein, fat, carbs

def create_diet_plan(diet_preference, allergies):
    food_database = {
        'Vegan': {
            'Sabah': {'Yulaf Ezmesi': (150, 5, 27, 6), 'Badem Sütü': (30, 2.5, 1, 1)},
            'Öğle': {'Kinoa ve Nohut Salatası': (350, 10, 45, 12), 'Avokado': (160, 15, 9, 2)},
            'Akşam': {'Tofu Stir-Fry': (350, 20, 15, 25)}
        },
        'Normal': {
            'Sabah': {'Yumurta': (78, 5, 1, 6), 'Tam Buğday Ekmeği': (69, 1, 12, 4)},
            'Öğle': {'Tavuk Göğsü': (165, 3.6, 0, 31), 'Bulgur Pilavı': (151, 0.2, 34, 4)},
            'Akşam': {'Balık': (206, 12, 0, 22), 'Salata': (33, 0.2, 7, 2)}
        },
        'Vejetaryen': {
            'Sabah': {'Yumurta': (78, 5, 1, 6), 'Tam Buğday Ekmeği': (69, 1, 12, 4)},
            'Öğle': {'Mercimek Çorbası': (186, 3, 30, 12), 'Zeytinyağlı Sebze': (200, 10, 20, 5)},
            'Akşam': {'Sebzeli Makarna': (220, 2, 43, 8)}
        }
    }
    diet_plan = food_database[diet_preference]
    for meal in diet_plan:
        diet_plan[meal] = {food: macros for food, macros in diet_plan[meal].items() if food.lower() not in [allergy.lower().strip() for allergy in allergies]}
    return diet_plan

def suggest_exercises():
    # Rastgele 4 egzersiz seç ve tekrar sayılarını belirle
    random_exercises = random.sample(list(exercises.items()), 4)
    return random_exercises

def show_results_page(results):
    # Yeni sayfa oluşturma
    results_frame = tk.Frame(root)
    results_frame.grid(row=0, column=1, sticky='nsew')

    # Sonuçları ve önerileri göster
    tk.Label(results_frame, text=results, justify=tk.LEFT, padx=10, pady=10).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(results_frame, text="Geri", command=show_main_page, bg="#ff9999", fg="black").grid(row=1, column=0, pady=10)

    main_frame.grid_forget()  # Ana sayfayı gizle
    results_frame.tkraise()  # Yeni sayfayı göster

def show_main_page():
    main_frame.grid(row=0, column=1, sticky='nsew')  # Ana sayfayı göster
    main_frame.tkraise()

def show_exercise_list():
    exercise_frame = tk.Frame(root)
    exercise_frame.grid(row=0, column=1, sticky='nsew')

    # Canvas ve Scrollbar oluşturma
    canvas = tk.Canvas(exercise_frame)
    scrollbar = tk.Scrollbar(exercise_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Egzersiz hareketlerini göster
    tk.Label(scrollable_frame, text="Egzersiz Hareketleri", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    all_exercises = [
        'Bicycle Crunches',
        'Bridge',
        'Burpees',
        'Donkey Kicks',
        'Flutter Kicks',
        'Heel Taps',
        'High Knees',
        'Jumping Jacks',
        'Leg Raises',
        'Lunges',
        'Mountain Climbers',
        'Plank',
        'Push-Up',
        'Side Lunges',
        'Side Plank',
        'Squat',
        'Superman',
        'Toe Touches',
        'Tricep Dips',
        'Wall Sit'
    ]

    for i, exercise in enumerate(all_exercises):
        tk.Label(scrollable_frame, text=exercise, justify=tk.LEFT, padx=10, pady=5).grid(row=i+1, sticky='w', padx=10, pady=2)
    
    tk.Button(scrollable_frame, text="Geri", command=show_main_page, bg="#99ccff", fg="black").grid(row=len(all_exercises)+1, column=0, columnspan=2, pady=10)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    main_frame.grid_forget()  # Ana sayfayı gizle
    exercise_frame.tkraise()  # Yeni sayfayı göster

def show_diet_list():
    diet_frame = tk.Frame(root)
    diet_frame.grid(row=0, column=1, sticky='nsew')

    tk.Label(diet_frame, text="Diyet Listesi", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # 5 tane diyet butonu oluştur
    diets = [
        "Akdeniz Diyeti",
        "Ketojenik Diyet (Keto Diyeti)",
        "Paleo Diyeti",
        "Intermittent Fasting (Aralıklı Oruç)",
        "DASH Diyeti (Hipertansiyonu Durdurmak İçin Diyet Yaklaşımları)"
    ]

    for i, diet in enumerate(diets):
        tk.Button(diet_frame, text=diet, bg="#ffcc99", fg="black").grid(row=i+1, column=0, padx=10, pady=5)

    tk.Button(diet_frame, text="Geri", command=show_main_page, bg="#99ccff", fg="black").grid(row=len(diets) + 1, column=0, pady=10)

    main_frame.grid_forget()  # Ana sayfayı gizle
    diet_frame.tkraise()  # Yeni sayfayı göster

# Hesaplamaları Yapan ve Sonuçları Gösteren Fonksiyon
def calculate_and_display_results():
    try:
        name = name_var.get()
        age = int(age_var.get())
        gender = gender_var.get()
        height = float(height_var.get())
        weight = float(weight_var.get())
        activity_level = activity_level_var.get()
        goal = goal_var.get()
        diet_preference = diet_preference_var.get()
        allergies = allergies_var.get().split(',') if allergies_var.get() else []

        if not gender or not activity_level or not goal or not diet_preference:
            raise ValueError("Lütfen tüm alanları doldurun.")

        bmr = calculate_bmr(gender, weight, height, age)
        daily_calories = calculate_daily_calories(bmr, activity_level)
        adjusted_calories = adjust_calories_for_goal(daily_calories, goal)
        protein, fat, carbs = calculate_macros(adjusted_calories)

        diet_plan = create_diet_plan(diet_preference, allergies)
        exercise_suggestions = suggest_exercises()

        # Diyet planını dikey sütunlara yerleştir
        diet_str = "Diyet Planı:\n"
        meals = ['Sabah', 'Öğle', 'Akşam']
        for meal in meals:
            diet_str += f"\n{meal}:\n"
            if meal in diet_plan:
                for food, macros in diet_plan[meal].items():
                    diet_str += f"{food}: {macros[0]} kalori, {macros[1]}g yağ, {macros[2]}g karbonhidrat, {macros[3]}g protein\n"

        exercise_str = "Egzersiz Önerileri:\n"
        for i, (exercise, reps) in enumerate(exercise_suggestions, 1):
            exercise_str += f"Egzersiz {i}: {exercise} - {reps}\n"

        results = (f"Günlük Kalori İhtiyacı: {adjusted_calories:.2f} kcal\n"
                   f"Protein: {protein:.2f} gr\nYağ: {fat:.2f} gr\nKarbonhidrat: {carbs:.2f} gr\n\n"
                   f"{diet_str}\n\n{exercise_str}")

        # Yeni sayfayı aç ve sonuçları göster
        show_results_page(results)

    except ValueError as ve:
        messagebox.showerror("Hata", str(ve))
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen bir hata oluştu: {str(e)}")

# tkinter Penceresi Oluşturma
root = tk.Tk()
root.title("Kişisel Sağlık Asistanı")
root.geometry("800x600")  # Pencere boyutunu ayarla

# Pencereyi ortala
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Menü çubuğu oluşturma
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menü oluşturma
menu = tk.Menu(menubar, tearoff=0)
menu.add_command(label="Bilgilerim", command=show_main_page)
menu.add_command(label="Egzersiz Hareketleri", command=show_exercise_list)
menu.add_command(label="Diyet Listesi", command=show_diet_list)  # Yeni diyet listesi butonu
menubar.add_cascade(label="Menü", menu=menu)

# Sol tarafta menü çerçevesi oluşturma
menu_frame = tk.Frame(root, width=200, bg="lightgrey")
menu_frame.grid(row=0, column=0, sticky='ns')

# Menü başlığı
tk.Label(menu_frame, text="Menü", bg="lightgrey", font=("Helvetica", 16)).pack(pady=10)

# Formu Göster Butonu
tk.Button(menu_frame, text="Kullanıcı Bilgiler Formu", command=show_main_page, bg="#ccffcc", fg="black").pack(pady=10)
# Egzersiz Hareketleri Butonu
tk.Button(menu_frame, text="Egzersiz Hareketleri", command=show_exercise_list, bg="#ffcc99", fg="black").pack(pady=10)
# Diyet Listesi Butonu
tk.Button(menu_frame, text="Diyet Listesi", command=show_diet_list, bg="#ffcc99", fg="black").pack(pady=10)

# Kullanıcı Girişi için Değişkenler
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
height_var = tk.StringVar()
weight_var = tk.StringVar()
activity_level_var = tk.StringVar()
goal_var = tk.StringVar()
diet_preference_var = tk.StringVar()
allergies_var = tk.StringVar()

# Ana Sayfa (Bilgilerim Formu)
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1, sticky='nsew')

# Kullanıcı Girişi için Arayüz Elemanları
tk.Label(main_frame, text="İsim:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(main_frame, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Yaş:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(main_frame, textvariable=age_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Cinsiyet:").grid(row=2, column=0, padx=10, pady=5)
ttk.Combobox(main_frame, textvariable=gender_var, values=["Kadın", "Erkek"]).grid(row=2, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Boy (cm):").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(main_frame, textvariable=height_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Kilo (kg):").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(main_frame, textvariable=weight_var).grid(row=4, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Hareketlilik Seviyesi:").grid(row=5, column=0, padx=10, pady=5)
ttk.Combobox(main_frame, textvariable=activity_level_var, values=["Az Hareketli", "Orta Hareketli", "Çok Hareketli"]).grid(row=5, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Hedef:").grid(row=6, column=0, padx=10, pady=5)
ttk.Combobox(main_frame, textvariable=goal_var, values=["Kilo Vermek", "Kilo Almak", "Formu Korumak"]).grid(row=6, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Beslenme Tercihi:").grid(row=7, column=0, padx=10, pady=5)
ttk.Combobox(main_frame, textvariable=diet_preference_var, values=["Normal", "Vegan", "Vejetaryen"]).grid(row=7, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Alerji veya Tüketilmeyen Besinler:").grid(row=8, column=0, padx=10, pady=5)
tk.Entry(main_frame, textvariable=allergies_var).grid(row=8, column=1, padx=10, pady=5)

tk.Button(main_frame, text="Hesapla", command=calculate_and_display_results, bg="#ff9966", fg="black").grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()        