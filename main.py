import tkinter as tk
from tkinter import ttk, filedialog

# Funkcja do rysowania prostokątów i aktualizacji GUI
def draw_rectangles(canvas, array, color):
    canvas.delete("rect")
    c_height = 300
    c_width = 600
    x_width = c_width / (len(array) + 1)
    offset = 10
    spacing = 10
    normalized_array = [i / max(array) for i in array]
    for i, height in enumerate(normalized_array):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 290
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, tag="rect", fill=color)
    canvas.update()

# Funkcja sortowania bąbelkowego z wizualizacją
def bubble_sort(canvas, array, color, speed):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                draw_rectangles(canvas, array, color)
                root.update_idletasks()
                root.after(speed)

# Funkcja do wczytywania danych z pliku
def load_from_file(canvas, color):
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, "r") as file:
            data = file.read()
            new_array = list(map(int, data.split(',')))
            global array
            array = new_array
            draw_rectangles(canvas, array, color)

# Funkcja resetująca dane do stanu początkowego
def reset_data(canvas, color):
    global array
    array = [10, 3, 8, 5, 2, 7, 4, 6, 9, 1]  # Możesz zmienić na inny zestaw danych
    draw_rectangles(canvas, array, color)

# Główna funkcja tworząca GUI
def main():
    global root, array
    root = tk.Tk()
    root.title("Wizualny Algorytm Sortowania Bąbelkowego")

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.pack()

    author_label = tk.Label(root, text="Autor: Bartłomiej Cieplechowicz 2TP")
    author_label.pack(side=tk.BOTTOM)

    speed_slider = tk.Scale(root, from_=0, to=100, label="Szybkość sortowania", orient=tk.HORIZONTAL)
    speed_slider.pack(side=tk.BOTTOM)

    start_button = tk.Button(root, text="Rozpocznij sortowanie", command=lambda: bubble_sort(canvas, array, color_var.get(), speed_slider.get()))
    start_button.pack(side=tk.BOTTOM)

    reset_button = tk.Button(root, text="Resetuj dane", command=lambda: reset_data(canvas, color_var.get()))
    reset_button.pack(side=tk.BOTTOM)

    load_button = tk.Button(root, text="Wczytaj z pliku", command=lambda: load_from_file(canvas, color_var.get()))
    load_button.pack(side=tk.BOTTOM)

    color_var = tk.StringVar()
    color_chooser = ttk.Combobox(root, textvariable=color_var, values=["red", "green", "blue", "yellow"])
    color_chooser.pack(side=tk.BOTTOM)
    color_chooser.current(0)

    array = [10, 3, 8, 5, 2, 7, 4, 6, 9, 1]
    draw_rectangles(canvas, array, color_var.get())

    root.mainloop()

if __name__ == "__main__":
    main()
