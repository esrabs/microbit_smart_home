# 🏠 Smart Home Micro:bit – Maison Connectée Intelligente

## 🎯 Description
Ce projet a été réalisé dans le cadre du **Projet S3 – Parcours GI/GEE/Info**. Il s'agit d'une **maison connectée intelligente** basée sur une carte **BBC Micro:bit**, capable de surveiller différents paramètres environnementaux et d’agir automatiquement via des servomoteurs, des LEDs et un système d’alarme.

Le programme est développé en **MicroPython** et gère une interface de navigation hiérarchique permettant d’interagir avec les capteurs et actionneurs.

---

## 🚀 Fonctionnalités principales
- 📡 Lecture et affichage de plusieurs capteurs :
  - Détection de pluie
  - Capteur de gaz
  - Température ambiante
  - Luminosité ambiante
- ⚙️ Contrôle automatique :
  - Aération (servo-moteurs pour porte et fenêtre)
  - Alarme sonore et visuelle
  - Éclairage RGB via NeoPixel
- 🧭 Interface interactive :
  - Bouton **A** → navigation vers le bas
  - Bouton **B** → navigation vers le haut
  - Appui long **A** → valider un choix
  - Appui long **B** → revenir en arrière
  - **Logo tactile** → exécuter l’action sélectionnée

---

## 🧩 Matériel utilisé
- 1 × BBC Micro:bit (V2 recommandé)
- 1 × Module NeoPixel (4 LEDs RGB)
- 2 × Servomoteurs (porte et fenêtre)
- 1 × Capteur de pluie (entrée analogique)
- 1 × Capteur de gaz (entrée analogique)
- 1 × Buzzer / haut-parleur
- Fils de connexion et alimentation 5V

---

## ⚙️ Installation
1. **Télécharge le code :**
   ```bash
   git clone https://github.com/<ton-utilisateur>/smart-home-microbit.git
   ```
2. Ouvre le fichier **`smart_home_microbit.py`** dans [Mu Editor](https://codewith.mu/) ou sur [python.microbit.org](https://python.microbit.org/).
3. **Renomme** le fichier en `main.py` avant de le transférer sur la carte Micro:bit.
4. Branche la carte et observe le fonctionnement !

---

## 💡 Utilisation
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

## 🧠 Organisation du code
```text
smart_home_microbit.py
│
├── Classe Servo           → Gestion des servomoteurs
├── Menus hiérarchiques    → Navigation par boutons A/B
├── Fonctions helpers      → LED, alarme, aération
└── Boucle principale      → Lecture capteurs + interactions
```

---

## 📸 Exemple d’application
📷 *Maison connectée avec capteurs et servos contrôlés par Micro:bit*

*(Tu peux ajouter ici une image ou un schéma dans un dossier `/assets`)*

---

## 🧑‍💻 Auteurs
Projet réalisé par **[Ton prénom et ton groupe]**  
Encadré par les enseignants du département **Électronique, Automatique et Informatique Industrielle – EILCO**.

---

## 📄 Licence
Ce projet est distribué sous la licence **MIT**.  
Tu es libre de le modifier, l’utiliser et le redistribuer.

---

## 🏷️ Badges (optionnel)
![MicroPython](https://img.shields.io/badge/MicroPython-2E5C94?style=for-the-badge&logo=python&logoColor=white)
![Micro:bit](https://img.shields.io/badge/BBC%20Micro:bit-00ED00?style=for-the-badge&logo=bbc&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
