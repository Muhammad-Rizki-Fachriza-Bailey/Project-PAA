import pygame
import random
import time

# Inisialisasi pygame
pygame.init()

# Membuat layar window
lebar = 600
tinggi = 550
lebar_tambahan = lebar + 350
screen = pygame.display.set_mode((lebar_tambahan, tinggi))

# Membuat warna
white = (255, 255, 255)
black = (0, 0, 0)
grey = (210, 210, 210)
red = (255, 0, 0)
green = (0, 255, 0)

# Membuat ukuran blok dan banyak blok
size_blok = 25
banyak_blok_x = lebar // size_blok  # 600 // 25 = 24
banyak_blok_y = tinggi // size_blok  # 550 // 25 = 22

# Menambahkan icon game dan judul
pygame.display.set_caption("Hide and Seek")
icon = pygame.image.load('hide-and-seek.png')
pygame.display.set_icon(icon)

# Membuat font
font = pygame.font.SysFont('Georgia', 25, bold=True)
teks_color = black

# membuat waktu jeda untuk pergerakan
waktu_jeda = 0.5

# variabel untuk mengatur pergerakan terakhir droid
waktu_terakhir_pergerakan = time.time()



# Membuat grid kotak pada layar screen
grid = []
for i in range(banyak_blok_y):
    row = []
    for j in range(banyak_blok_x):
        row.append((j, i))
    grid.append(row)

# Membuat peta
data_peta = [[0] * banyak_blok_x for _ in range(banyak_blok_y)]
for i in range(banyak_blok_y):
    for j in range(banyak_blok_x):
        if i == 0 or j == 0 or i == banyak_blok_y - 1 or j == banyak_blok_x - 1:
            data_peta[i][j] = 1


# Fungsi untuk menggambar peta dan droid
def gambar_peta_dan_droid(data_peta):
    for row in range(banyak_blok_y):
        for col in range(banyak_blok_x):
            x = col * size_blok
            y = row * size_blok
            if data_peta[row][col] == 1:
                pygame.draw.rect(screen, black, (x, y, size_blok, size_blok))
            else:
                pygame.draw.rect(screen, white, (x, y, size_blok, size_blok), 1)

    pygame.draw.rect(screen, red, (droid_merah_x * size_blok, droid_merah_y * size_blok, size_blok, size_blok))
    pygame.draw.rect(screen, green, (droid_hijau_x * size_blok, droid_hijau_y * size_blok, size_blok, size_blok))


# Fungsi untuk mengacak peta dengan metode Recursive Backtracking
def acak_peta():
    global data_peta, droid_merah_x, droid_merah_y, droid_hijau_x, droid_hijau_y

    # Mengisi seluruh peta dengan tembok
    for i in range(banyak_blok_y):
        for j in range(banyak_blok_x):
            data_peta[i][j] = 1

    # Fungsi rekursif untuk membuka jalan pada peta
    def gali(x, y):
        data_peta[y][x] = 0

        arah = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(arah)

        for dx, dy in arah:
            nx, ny = x + dx, y + dy
            nx2, ny2 = x + 2 * dx, y + 2 * dy

            if 0 <= nx2 < banyak_blok_x and 0 <= ny2 < banyak_blok_y and data_peta[ny2][nx2] == 1:
                data_peta[ny][nx] = 0
                gali(nx2, ny2)

    # Memilih titik awal untuk membuka jalan pada peta
    start_x = random.randint(1, banyak_blok_x // 2) * 2
    start_y = random.randint(1, banyak_blok_y // 2) * 2

    gali(start_x, start_y)

    # Memilih posisi droid merah dan hijau secara acak di jalan berwarna putih
    available_positions = [(x, y) for x in range(banyak_blok_x) for y in range(banyak_blok_y) if data_peta[y][x] == 0]
    random.shuffle(available_positions)
    droid_merah_x, droid_merah_y = available_positions[0]
    droid_hijau_x, droid_hijau_y = available_positions[1]


def perbarui_arah_droid_merah():
    global arah_droid_merah
    arah_droid_merah = random.choice(["kiri", "kanan", "atas", "bawah"])


acak_peta()

# Membuat tombol Start dan Quit
start_text = font.render('Start', True, teks_color)
start_button_pos = (lebar + 10, 10)
start_button_size = (100, 50)
start_button = pygame.Rect(start_button_pos, start_button_size)

pause_text = font.render('Pause', True, teks_color)
pause_button_pos = (lebar + 10, 70)
pause_button_size = (100, 50)
pause_button = pygame.Rect(pause_button_pos, pause_button_size)

acak_peta_text = font.render('Acak Peta', True, teks_color)
acak_peta_button_pos = (lebar + 10, 130)
acak_peta_button_size = (150,50)
acak_peta_button = pygame.Rect(acak_peta_button_pos, acak_peta_button_size)

posisi_awal_droid_merah_text = font.render('Acak Posisi Merah', True, teks_color)
posisi_awal_droid_merah_button_pos = (lebar + 10, 190)
posisi_awal_droid_merah_button_size = (250,50)
posisi_awal_droid_merah_button = pygame.Rect(posisi_awal_droid_merah_button_pos,posisi_awal_droid_merah_button_size)

posisi_awal_droid_hijau_text = font.render('Acak Posisi Hijau', True, teks_color)
posisi_awal_droid_hijau_button_pos = (lebar + 10, 250)
posisi_awal_droid_hijau_button_size = (250,50)
posisi_awal_droid_hijau_button = pygame.Rect(posisi_awal_droid_hijau_button_pos,posisi_awal_droid_hijau_button_size)

tambah_merah_text = font.render('Tambah Droid Merah', True, teks_color)
tambah_merah_button_pos = (lebar + 10, 310)
tambah_merah_button_size = (300,50)
tambah_merah_button = pygame.Rect(tambah_merah_button_pos, tambah_merah_button_size)

quit_text = font.render('Quit', True, teks_color)
quit_button_pos = (lebar + 10, 480)
quit_button_size = (100, 50)
quit_button = pygame.Rect(quit_button_pos, quit_button_size)



game_started = False
running = True
arah_droid_merah = "kanan"  # Arah pergerakan droid merah
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True
            elif pause_button.collidepoint(event.pos):
                game_started = False
            elif acak_peta_button.collidepoint(event.pos):
                acak_peta()
            elif posisi_awal_droid_merah_button.collidepoint(event.pos):
                gambar_peta_dan_droid(data_peta)
            elif posisi_awal_droid_hijau_button.collidepoint(event.pos):
                gambar_peta_dan_droid(data_peta)
            elif quit_button.collidepoint(event.pos):
                running = False

    screen.fill(grey)

    if game_started == True:
        waktu_sekarang = time.time()
       # Logika pergerakan droid merah
        if waktu_sekarang - waktu_terakhir_pergerakan >= waktu_jeda:
            waktu_terakhir_pergerakan = waktu_sekarang

            if arah_droid_merah == "kanan":
                if droid_merah_x + 1 < banyak_blok_x and data_peta[droid_merah_y][droid_merah_x + 1] == 0:
                    droid_merah_x += 1
                else:
                    perbarui_arah_droid_merah()
            elif arah_droid_merah == "kiri":
                if droid_merah_x - 1 >= 0 and data_peta[droid_merah_y][droid_merah_x - 1] == 0:
                    droid_merah_x -= 1
                else:
                    perbarui_arah_droid_merah()
            elif arah_droid_merah == "bawah":
                if droid_merah_y + 1 < banyak_blok_y and data_peta[droid_merah_y + 1][droid_merah_x] == 0:
                    droid_merah_y += 1
                else:
                    perbarui_arah_droid_merah()
            elif arah_droid_merah == "atas":
                if droid_merah_y - 1 >= 0 and data_peta[droid_merah_y - 1][droid_merah_x] == 0:
                    droid_merah_y -= 1
                else:
                    perbarui_arah_droid_merah()

    # Jika posisi droid merah sama dengan posisi droid hijau
            if droid_merah_x == droid_hijau_x and droid_merah_y == droid_hijau_y:
            # Mengubah arah droid merah menjadi arah droid hijau
                if droid_merah_x < droid_hijau_x:
                    arah_droid_merah = "kanan"
                elif droid_merah_x > droid_hijau_x:
                    arah_droid_merah = "kiri"
                elif droid_merah_y < droid_hijau_y:
                    arah_droid_merah = "bawah"
                elif droid_merah_y > droid_hijau_y:
                    arah_droid_merah = "atas"


    gambar_peta_dan_droid(data_peta)

    # baris program untuk membuat garis vertikal dan horizontal pada peta
    for i in range(0, lebar, size_blok):
        pygame.draw.line(screen, black, (i, 0), (i, tinggi))
    for j in range(0, tinggi, size_blok):
        pygame.draw.line(screen, black, (0, j), (lebar, j))

    # menggambar button ke layar 
    pygame.draw.rect(screen, (180, 180, 180) if start_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), start_button)
    screen.blit(start_text, (start_button_pos[0] + 10, start_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if pause_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), pause_button)
    screen.blit(pause_text, (pause_button_pos[0] + 10, pause_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if acak_peta_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), acak_peta_button)
    screen.blit(acak_peta_text, (acak_peta_button_pos[0] + 10, acak_peta_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if posisi_awal_droid_merah_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), posisi_awal_droid_merah_button)
    screen.blit(posisi_awal_droid_merah_text, (posisi_awal_droid_merah_button_pos[0] + 10, posisi_awal_droid_merah_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if posisi_awal_droid_hijau_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), posisi_awal_droid_hijau_button)
    screen.blit(posisi_awal_droid_hijau_text, (posisi_awal_droid_hijau_button_pos[0] + 10, posisi_awal_droid_hijau_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if tambah_merah_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), tambah_merah_button)
    screen.blit(tambah_merah_text, (tambah_merah_button_pos[0] + 10, tambah_merah_button_pos[1] + 15))

    pygame.draw.rect(screen, (180, 180, 180) if quit_button.collidepoint(pygame.mouse.get_pos()) else (200, 200, 200), quit_button)
    screen.blit(quit_text, (quit_button_pos[0] + 10, quit_button_pos[1] + 15))

    pygame.display.update()

# Menghentikan pygame
pygame.quit()
