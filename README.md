# Smart Home Micro:bit – Maison Connectée Intelligente

## Description
Ce projet a été réalisé dans le cadre du **Projet S3 – Parcours GI/GEE/Info**. Il s'agit d'une **maison connectée intelligente** basée sur une carte **BBC Micro:bit**, capable de surveiller différents paramètres environnementaux et d’agir automatiquement via des servomoteurs, des LEDs et un système d’alarme.

Le programme est développé en **MicroPython** et gère une interface de navigation hiérarchique permettant d’interagir avec les capteurs et actionneurs.

---

## Fonctionnalités principales
-   Lecture et affichage de plusieurs capteurs :
    - Détection de pluie
    - Capteur de gaz
    - Température ambiante
    - Luminosité ambiante
-   Contrôle automatique :
    - Aération (servo-moteurs pour porte et fenêtre)
    - Alarme sonore et visuelle
    - Éclairage RGB via NeoPixel
-   Interface interactive :
    - Bouton **A** → navigation vers le bas
    - Bouton **B** → navigation vers le haut
    - Appui long **A** → valider un choix
    - Appui long **B** → revenir en arrière
    - **Logo tactile** → exécuter l’action sélectionnée

---

## Matériel utilisé
- 1 × BBC Micro:bit (V2 recommandé)
- 1 × Module NeoPixel (4 LEDs RGB)
- 2 × Servomoteurs (porte et fenêtre)
- 1 × Capteur de pluie (entrée analogique)
- 1 × Capteur de gaz (entrée analogique)
- 1 × Buzzer / haut-parleur
- Fils de connexion et alimentation 5V

---

## Installation
1. **Télécharge le code :**
   ```bash
   git clone https://github.com/<esrabs>/microbit_smar_home.git
   ```
2. Ouvre le fichier **`smart_home_microbit.py`** dans [Mu Editor](https://codewith.mu/) ou sur [python.microbit.org](https://python.microbit.org/).
3. **Renomme** le fichier en `main.py` avant de le transférer sur la carte Micro:bit.
4. Branche la carte et observe le fonctionnement !
---

## Utilisation
Une fois le programme lancé :
- Le menu principal s’affiche sur la matrice LED.
- Navigue avec **A** et **B**.
- Valide avec un **appui long A**.
- Exécute les actions en touchant le **logo tactile**.

Exemples :
- Menu **LED 5x5** → affiche des symboles (cœur, bateau, croix)
- Menu **Capteurs** → lit pluie, gaz, température, luminosité
- Menu **RGB** → effets “disco”, “breathing”, on/off
- Menu **Aération** → ouvre/ferme les servos

---
## Montage / Assemblage
Le montage de la **maison connectée** peut suivre le guide officiel **Keyestudio KS4027–KS4028** (bois + acrylique, modules, visserie, câblage). Tu y trouveras :
- la **liste des pièces** (carte Micro:bit, carte d’extension IO, servos, module RGB 6812, capteurs, visserie…)
- les **étapes d’assemblage** de la structure (panneaux bois/acrylique)
- les **connexions** des capteurs/actionneurs vers la carte d’extension
- un **tutoriel MicroPython** (Mu Editor) pour tester les modules


 **Guide officiel :** [KS4027–KS4028 Smart Home Kit for Micro:bit Python Tutorial](https://docs.keyestudio.com/projects/KS4027-KS4028/en/latest/KS4027-KS4028.html)



### Schéma de câblage
- **NeoPixel (6812 RGB)** → `P14`
- **Servo porte** → `P8`
- **Servo fenêtre** → `P9`
- **Pluie** → `P0` (analog)
- **Gaz (MQ-2)** → `P1` (analog)
- **Buzzer / alarme** → `P16`
- **LEDs intégrées / matrice** → écran 5×5 du Micro:bit


>  Vérifie la **masse commune (GND)** entre tous les modules et respecte l’**alimentation** des servos (souvent 5V) séparée de la carte quand c’est nécessaire.


---


## 🧑‍💻 Auteurs
Projet réalisé par **Esrae Ben Selma**  
Encadré par les enseignants du département **Électronique, Automatique et Informatique Industrielle – EILCO**.





