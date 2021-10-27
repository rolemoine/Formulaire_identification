# Formulaire_identification

Dans ce répertoire on retrouve un formulaire d'identification sécurisé afin de se connecter à une page.
Les nouveaux utilisateurs pourront se créer un compte et le mot de passe sera hashé grâce à la bibliothèque werkzeug. La clé de sécurité 
permettant de vérifier et de crypter le mot de passe a été laissée dans le fichier Python. 

La framework flask a été utilisée lors de ce projet et le langage utilisé est le langage Python.
Aussi, après avoir téléchargé les bibliothèques contenues dans requirements.txt, il faudra exécuter le fichier app.py puis 
se connecter au local host: 127.0.0.1:5000/login

L'arborescence se déroule comme suit :

├── app.py  
├── data2.db  
├── requirements.txt  
├── static  
│   ├── css  
│   │   └── login.css  
│   └── pictures  
│       ├── fjord.jpeg  
│       └── index.jpg  
└── templates  
    ├── bienvenue.html  
    ├── login.html  
    └── register.html  

4 directories, 9 files


Enfin, une base de donnée en SQL a été utilisée pour stocker les identifiants et mots de passe de l'ensemble des utilisateurs.
