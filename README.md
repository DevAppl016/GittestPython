# GittestPython

Application Python de calculs mathématiques de base, avec tests unitaires complets et intégration continue (CI) via GitHub Actions.

## Fonctionnalités

- Addition et division sécurisée (protection contre la division par zéro)
- Validation des types d'entrée
- Tests automatisés avec `pytest` et `unittest`
- Couverture de code mesurée avec `coverage`
- Pipeline CI/CD avec lint (`flake8`) et vérification de types (`mypy`)

## Structure du projet
GittestPython/

├── .github/

│   └── workflows/

│       └── tests.yaml       # Pipeline CI : lint, tests, couverture

├── src/

│   └── mon_app/

│       ├── init.py

│       └── calcul.py        # Fonctions addition() et division()

├── tests/

│   ├── init.py

│   ├── test_calcul.py       # Tests pytest

│   └── test_calcul_unittest.py  # Tests unittest

├── requirements-dev.txt     # Dépendances de développement

├── setup.cfg                # Configuration pytest/coverage/flake8/mypy

└── README.md

## Installation

```bash
git clone https://github.com/DevAppl016/GittestPython.git
cd GittestPython
pip install -r requirements-dev.txt
```

## Utilisation

```python
from mon_app.calcul import addition, division

resultat = addition(2, 3)        # 5
resultat = division(10, 2)       # 5.0
```

## Lancer les tests

**Avec pytest (couverture incluse) :**
```bash
pytest --cov=src/mon_app --cov-report=term-missing
```

**Avec unittest :**
```bash
python -m unittest discover tests
```

**Vérification du code (lint + types) :**
```bash
flake8 src/ tests/
mypy src/
```

## Intégration continue

Chaque push ou pull request sur `main` déclenche automatiquement :
1. Lint (`flake8`) et vérification de types (`mypy`)
2. Tests sur Python 3.11 et 3.12
3. Génération d'un rapport de couverture HTML (`htmlcov/`)

Le rapport de couverture est disponible en téléchargement dans les artefacts de chaque exécution GitHub Actions.

## Contexte

Projet réalisé dans le cadre de ma formation en développement, démontrant la maîtrise de :
- Python (fonctions typées, gestion d'exceptions)
- Tests unitaires (`pytest`, `unittest`, paramétrage, mocks)
- Intégration continue (GitHub Actions, matrice multi-versions Python)
- Bonnes pratiques de structuration de projet (`src/`, `setup.cfg`, couverture de code)
