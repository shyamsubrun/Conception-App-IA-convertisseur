# Projet de Conversion de Texte en Image

## Description
Ce projet a pour but de développer une application capable de transformer des descriptions textuelles en images correspondantes. L'application, exploitant l'intelligence artificielle et l'apprentissage automatique via l'API d'OpenAI, permet aux utilisateurs de soumettre une phrase descriptive et de recevoir en retour une image générée qui interprète cette description.

## Technologies Utilisées
- **Python** : Langage de programmation pour le backend.
- **OpenAI API** : Pour générer des images à partir de descriptions textuelles.
- **Requests** : Bibliothèque Python pour effectuer des requêtes HTTP.
- **Flask** : Framework Python pour développer l'application web .

## Fonctionnalités
1. **Utilisateurs** :
   - Soumission de descriptions textuelles via une interface web ou API.
   - Réception d'images générées basées sur les descriptions soumises.

2. **Administrateur** :
   - Gestion des requêtes : suivi et historique des descriptions soumises et des images générées.
   - Configuration et gestion de l'API OpenAI : clés API, limites d'utilisation, etc.

## Base de Données (Si utilisé dans un projet long)
Pour stocker les informations liées aux utilisateurs, aux requêtes et aux images générées, une base de données pourrait être utilisée avec les tables suivantes :
- **users** : Utilisateurs (id, nom, login, mdp, type).
- **requests** : Requêtes (id, user_id, description, created_at).
- **images** : Images générées (id, request_id, image_url, created_at).

## Installation
1. Clonez le dépôt : `git clone https://github.com/votre-utilisateur/ProjetConversionTexteImage.git`
2. Installez les dépendances Python : `pip install -r requirements.txt`
3. (Optionnel) Configurez votre application Flask et votre environnement de développement.
4. Lancez l'application.

## Remarques
- L'application nécessite une clé API valide d'OpenAI pour fonctionner correctement. Assurez-vous de la configurer de manière sécurisée.
- Prenez en compte les limites d'utilisation et les coûts associés à l'utilisation de l'API d'OpenAI pour la génération d'images.
