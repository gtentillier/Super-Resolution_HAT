# Guide d'inférence - HAT Super-Résolution

Ce guide documente l'utilisation du modèle HAT (Hybrid Attention Transformer) pour la super-résolution d'images.

Pour le sharpening d'images, voir les restes de code du notebook `netteté.ipynb`.

---

## Installation

### Prérequis
- Python 3.8.20
D'autres versions de Python peuvent fonctionner, j'ai eu des problèmes d'installations de dépendances avec Python 3.7.17 et 3.13.6.

### Étapes d'installation

1. **Créer un environnement virtuel Python 3.8.20**
   ```bash
   python3.8 -m venv .venv
   source .venv/bin/activate
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

D'après la documentation officielle : "PyTorch >= 1.7, (⚠️ **Éviter PyTorch 1.8** qui cause des performances anormales)".
La version de PyTorch dans `requirements.txt` fonctionne correctement d'après mes inférences sur MacOS.

---

## Utilisation

### 1. Préparer les images

Placer les images à traiter dans le dossier `input/`.

### 2. Lancer l'inférence

```bash
source .venv/bin/activate
python hat/test.py -opt options/test/HAT_GAN_Real_SRx4.yml
```

### 3. Récupérer les résultats

Les images super-résolues sont sauvegardées dans :
```
results/HAT_GAN_Real_SRx4/visualization/custom/
```

> **Note** : Si un dossier de résultats du même nom existe déjà, l'ancien est renommé avec un suffixe `_archive_XXXXXX` et un nouveau dossier est créé, où `XXXXXX` est un horodatage de l'archivage (pas de l'inférence correspondante !).

---

## Modèles disponibles

### Modèles pour images réelles, et le plus performant visuellement des tous les tests que j'ai fait

| Configuration | Modèle | Échelle | Description |
|--------------|--------|:-------:|-------------|
| `HAT_GAN_Real_SRx4.yml` | Real_HAT_GAN_SRx4.pth | x4 | **Meilleure fidélité** - Recommandé pour un rendu naturel |

### Modèles standards

| Configuration | Modèle | Échelle | Pré-entraînement |
|--------------|--------|:-------:|------------------|
| `HAT_SRx2.yml` | HAT_SRx2.pth | x2 | Non |
| `HAT_SRx3.yml` | HAT_SRx3.pth | x3 | Non |
| `HAT_SRx4.yml` | HAT_SRx4.pth | x4 | Non |
| `HAT_SRx2_ImageNet-pretrain.yml` | HAT_SRx2_ImageNet-pretrain.pth | x2 | ImageNet |
| `HAT_SRx3_ImageNet-pretrain.yml` | HAT_SRx3_ImageNet-pretrain.pth | x3 | ImageNet |
| `HAT_SRx4_ImageNet-pretrain.yml` | HAT_SRx4_ImageNet-pretrain.pth | x4 | ImageNet |

### Modèles HAT-S (légers)

| Configuration | Modèle | Échelle | Params |
|--------------|--------|:-------:|--------|
| `HAT-S_SRx2.yml` | HAT-S_SRx2.pth | x2 | 9.6M |
| `HAT-S_SRx3.yml` | HAT-S_SRx3.pth | x3 | 9.6M |
| `HAT-S_SRx4.yml` | HAT-S_SRx4.pth | x4 | 9.6M |

### Modèles HAT-L (large, pré-entraînés ImageNet)

| Configuration | Modèle | Échelle |
|--------------|--------|:-------:|
| `HAT-L_SRx2_ImageNet-pretrain.yml` | HAT-L_SRx2_ImageNet-pretrain.pth | x2 |
| `HAT-L_SRx3_ImageNet-pretrain.yml` | HAT-L_SRx3_ImageNet-pretrain.pth | x3 |
| `HAT-L_SRx4_ImageNet-pretrain.yml` | HAT-L_SRx4_ImageNet-pretrain.pth | x4 |

---

## Mode Tile (mémoire GPU limitée)

Si vous manquez de mémoire GPU, activez le mode **tile** dans le fichier de configuration YAML :

```yaml
tile:
  tile_size: 256   # Plus élevé = plus de mémoire utilisée, moins de perte de qualité
  tile_pad: 32     # Chevauchement entre les tuiles
```

> Les valeurs doivent être des multiples de la taille de fenêtre (`window_size: 16`).

Voir `options/test/HAT_tile_example.yml` pour un exemple complet.

---

## Mode GPU/CPU

Pour exécuter sur GPU uniquement, modifier le fichier de configuration :

```yaml
num_gpu: 0->1  # Nombre de GPU à utiliser, 0 pour CPU uniquement
```

---

## Téléchargement des modèles pré-entraînés

Si les modèles ne sont pas présents dans `experiments/pretrained_models/`, les télécharger depuis :
- [Google Drive](https://drive.google.com/drive/folders/1HpmReFfoUqUbnAOQ7rvOeNU3uf_m69w0?usp=sharing)
- [Baidu Netdisk](https://pan.baidu.com/s/1u2r4Lc2_EEeQqra2-w85Xg) (code : qyrl)

---

## Structure des dossiers

```
Super-Resolution_HAT/
├── input/                          # Images à traiter
├── results/                        # Résultats de l'inférence
│   └── <nom_config>/
│       └── visualization/
│           └── custom/             # Images super-résolues
├── experiments/
│   └── pretrained_models/          # Modèles pré-entraînés (.pth)
└── options/
    └── test/                       # Fichiers de configuration
```