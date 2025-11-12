from microbit import *
from random import randint
import time
import math
import audio
import music
import neopixel

# ----------------------
# Constantes & matériel
# ----------------------
# LEDs NeoPixel (4 LEDs sur pin14)
N_LEDS = 4
PIN_NEOPIX = pin14
leds = neopixel.NeoPixel(PIN_NEOPIX, N_LEDS)

# Seuils capteurs
RAIN_THRESHOLD = 500
GAS_THRESHOLD = 500
LIGHT_NIGHT = 20

# Actionneurs (servos, relais, etc.)
# pin8 : porte, pin9 : fenêtre
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.freq = freq
        self.angle = angle
        self.pin = pin
        analog_period = round((1 / self.freq) * 1000)  # période en ms
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = 0
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

servo_porte = Servo(pin8)
servo_fenetre = Servo(pin9)

# Sorties diverses
pin12.write_digital(0)
pin13.write_analog(0)
pin16.write_digital(0)

# ----------------------
# Ressources visuelles & audio
# ----------------------
leds.clear(); leds.show()

bateau = Image("00099:" "09090:" "09090:" "99999:" "09990")
cross = Image("90009:" "09090:" "00900:" "09090:" "90009")

alarm_signal = ['c5:4', 'e5:4', 'c5:4', 'e5:4', 'c5:4', 'e5:4']
bip_signal = ['c5:4']

# ----------------------
# Menus hiérarchiques
# ----------------------
menus = {
    0:  {"contenu": ["main_menu", "digicode", "led 5x5", "capteurs", "music", "RGB", "Aération"]},
    1:  {"contenu": ["digicode", "alarme", "codeRGB"]},
    11: {"contenu": ["alarme", "on", "off"]},
    2:  {"contenu": ["led_5x5", "croix", "bateau", "coeur"]},
    3:  {"contenu": ["capteurs", "gaz", "time", "rain", "temp"]},
    4:  {"contenu": ["music", "song1", "song2", "song3"]},
    5:  {"contenu": ["RGB", "disco", "breath", "on", "off"]},
    6:  {"contenu": ["Aeration", "ouvrir", "fermer"]},
    31: {"contenu": ["gaz", "value"]},
    32: {"contenu": ["time", "cycle"]},
    33: {"contenu": ["rain", "value"]},
    34: {"contenu": ["temp", "value"]},
}

numero_tableau_actuel = 0
ligne_actuelle = 1  # on ignore l'index 0 (nom du tableau)


def calculer_numero_suivant(numero_actuel, ligne):
    # concaténation décimale correcte
    return numero_actuel * 10 + ligne


def afficher_tableau_actuel():
    tableau = menus[numero_tableau_actuel]["contenu"]
    nom = tableau[0]
    selection = tableau[ligne_actuelle]
    print("Tableau:", nom, "| Selection:", selection)
    display.show(Image.ALL_CLOCKS[ligne_actuelle % len(Image.ALL_CLOCKS)])


def passer_a_ligne_suivante():
    global ligne_actuelle
    tableau = menus[numero_tableau_actuel]["contenu"]
    ligne_actuelle = (ligne_actuelle + 1) % len(tableau)
    if ligne_actuelle == 0:
        ligne_actuelle = 1
    afficher_tableau_actuel()


def passer_a_ligne_precedente():
    global ligne_actuelle
    tableau = menus[numero_tableau_actuel]["contenu"]
    ligne_actuelle -= 1
    if ligne_actuelle < 1:
        ligne_actuelle = len(tableau) - 1
    afficher_tableau_actuel()


def validation():
    global numero_tableau_actuel, ligne_actuelle
    numero_suivant = calculer_numero_suivant(numero_tableau_actuel, ligne_actuelle)
    if numero_suivant not in menus:
        print("Erreur : tableau suivant non trouvé.")
        display.show(Image.NO)
        return
    numero_tableau_actuel = numero_suivant
    ligne_actuelle = 1
    afficher_tableau_actuel()


def retour_tableau_precedent():
    global numero_tableau_actuel, ligne_actuelle
    if numero_tableau_actuel < 10:
        numero_tableau_actuel = 0
    else:
        numero_tableau_actuel //= 10
    ligne_actuelle = 1
    afficher_tableau_actuel()


# ----------------------
# Helpers actionneurs
# ----------------------

def leds_all_off():
    leds.clear(); leds.show()


def leds_set(idx, r, g, b):
    if 0 <= idx < N_LEDS:
        leds[idx] = (r, g, b)
        leds.show()


def alarme_flash_beep(sequence, repeats=1):
    for _ in range(repeats):
        pin16.write_digital(1)
        music.play(sequence)
        pin16.write_digital(0)
        sleep(100)


def ouvrir_aeration():
    servo_porte.write_angle(180)
    servo_fenetre.write_angle(180)
    pin12.write_digital(1)
    pin13.write_analog(700)


def fermer_aeration():
    servo_porte.write_angle(0)
    servo_fenetre.write_angle(0)
    pin12.write_digital(0)
    pin13.write_analog(0)


# ----------------------
# Boucle principale
# ----------------------

def verifier_appui():
    start_time_a = 0
    start_time_b = 0

    afficher_tableau_actuel()

    while True:
        # --- Gestion navigation A/B (avec appui court/long)
        if button_a.is_pressed() and start_time_a == 0:
            start_time_a = time.ticks_ms()
        if not button_a.is_pressed() and start_time_a != 0:
            duration_a = time.ticks_ms() - start_time_a
            start_time_a = 0
            if duration_a < 1000:
                passer_a_ligne_suivante()
            else:
                validation()

        if button_b.is_pressed() and start_time_b == 0:
            start_time_b = time.ticks_ms()
        if not button_b.is_pressed() and start_time_b != 0:
            duration_b = time.ticks_ms() - start_time_b
            start_time_b = 0
            if duration_b < 1000:
                passer_a_ligne_precedente()
            else:
                retour_tableau_precedent()

        # --- Lecture capteurs (robuste)
        try:
            pluie = pin0.read_analog()
        except Exception as e:
            pluie = 0
            print("Erreur lecture pluie:", e)

        try:
            gaz = pin1.read_analog()
        except Exception as e:
            gaz = 1023
            print("Erreur lecture gaz:", e)

        # --- Réactions automatiques (sécurité)
        if pluie > RAIN_THRESHOLD:
            leds_all_off()
            leds_set(1, 0, 0, 255)
            fermer_aeration()
            alarme_flash_beep(['c5:4'], repeats=2)
            leds_all_off()

        if gaz < GAS_THRESHOLD:
            leds_all_off()
            leds_set(2, 255, 0, 0)
            ouvrir_aeration()
            leds_all_off()

        # --- Actions contextuelles via logo
        if pin_logo.is_touched():
            if numero_tableau_actuel == 2:
                if ligne_actuelle == 1:
                    display.show(cross)
                elif ligne_actuelle == 2:
                    display.show(bateau)
                elif ligne_actuelle == 3:
                    display.show(Image.HEART)

            elif numero_tableau_actuel == 4:
                if ligne_actuelle == 1:
                    audio.play(Sound.HAPPY)
                elif ligne_actuelle == 2:
                    audio.play(Sound.HELLO)
                elif ligne_actuelle == 3:
                    audio.play(Sound.YAWN)

            elif numero_tableau_actuel == 6:
                if ligne_actuelle == 1:
                    ouvrir_aeration()
                elif ligne_actuelle == 2:
                    fermer_aeration()

            elif numero_tableau_actuel == 11:
                if ligne_actuelle == 1:
                    alarme_flash_beep(alarm_signal, repeats=5)
                elif ligne_actuelle == 2:
                    alarme_flash_beep(bip_signal, repeats=5)

            elif numero_tableau_actuel == 5:
                if ligne_actuelle == 1:
                    for i in range(N_LEDS):
                        r = randint(0, 255)
                        g = randint(0, 255)
                        b = randint(0, 255)
                        leds[i] = (r, g, b)
                        leds.show()
                        sleep(100)
                elif ligne_actuelle == 2:
                    for val in range(0, 256, 8):
                        for i in range(N_LEDS):
                            leds[i] = (val, val, val)
                        leds.show()
                        sleep(20)
                    for val in range(255, -1, -8):
                        for i in range(N_LEDS):
                            leds[i] = (val, val, val)
                        leds.show()
                        sleep(20)
                elif ligne_actuelle == 3:
                    for i in range(N_LEDS):
                        leds[i] = (255, 255, 255)
                    leds.show()
                elif ligne_actuelle == 4:
                    leds_all_off()

            elif numero_tableau_actuel == 31 and ligne_actuelle == 1:
                print("le taux de gaz actuel est de", gaz)
            elif numero_tableau_actuel == 32 and ligne_actuelle == 1:
                light = display.read_light_level()
                print("il fait nuit" if light < LIGHT_NIGHT else "il fait jour")
            elif numero_tableau_actuel == 33 and ligne_actuelle == 1:
                print("il pleut" if pluie > RAIN_THRESHOLD else "la meteo est claire")
            elif numero_tableau_actuel == 34 and ligne_actuelle == 1:
                temp = temperature()
                print("nous avons une temperature de", temp, "°C")

            sleep(200)

        sleep(50)


verifier_appui()
