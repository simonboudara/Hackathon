# Comment vous organiser ?

Ce hackathon est une (première) expérience de réalisation d'un logiciel en groupe.

## 1. Le groupe choisit un sujet

Supposons que vous avez choisi un sujet plutôt *ouvert*: il n'y a pas une solution évidente, unique et directe pour le traiter.  
Vous allez donc proposer des analyses de données pour aider à défricher le sujet et étayer des idées que vous pouvez avoir.

*Notez que: les sujets vous proposent des données mais vous pouvez rechercher d'autres données pour compléter ou remplacer les données fournies.*

[Les sujets sont décrits ici](./sujets.md)

## 2. Le groupe réfléchit aux analyses qu'il souhaite réaliser et dessine leur enchaînement

Les différentes parties de codes, pour réaliser les analyses, peuvent être inter-dépendantes c'est le plus souvent le cas dans des projets réels.

Par exemple, vous arrivez à l'enchaînement des codes `A`, `B`, `C`, `D` et `E`

```python
   A
   |
   B    # B dépend des résultats de A
  /\    #           (des sorties de A)
 /  \
C    D  # C et D dépendent des résultats de B
 \  /   #                     donc aussi de A
  \/
   E    # E dépend des sorties de C et de D
        #           donc aussi de B
        #           donc aussi de A
```

*Notez que: chaque sous module `A`, `B`, `C`, `D` et `E` peut aussi utiliser des données *extérieures* que les autres modules n'utilisent pas.*

## 3. Le groupe se répartit la réalisation de ces analyses

### 3.a Gérer les dépendances entre modules

Il est important, surtout en temps limité, que chacun puisse commencer à
travailler sur son module **sans attendre que les autres** aient terminé les
leurs.

Une manière de résoudre ce problème est:

* de définir précisément les structures de données qui sont en entrée de chaque module `A`, `B`, `C`, `D` et `E`
* et générer aléatoirement des tables de données d'entrée (*ou de travailler sur des données dont la structure ressemble*)
* de cette façon tous les développeurs commencent à travailler en même temps.

Pour les débutants, une manière de faire est d'essayer de simplifier le schéma (si cela est possible):

```python
     A
     |
 ----------
 |  |  |  |
 B  C  D  E
```

### 3.b Gérer les évolutions du projet

Vous n'êtes pas sûrs:

* d'avoir pensé dès le début à tout ce que vous voulez faire
* que les modules resteront figés, des idées nouvelles ou des incohérences peuvent apparaître et remettre en question l'organisation
* que tout le monde a compris la même chose.

Il est donc nécessaire de faire des points d'avancement réguliers et rapides pour contrôler que tout se passe bien:

* si chacun a bien compris ce qu'il doit faire et arrive à avancer
* si de nouvelles idées ou des incohérences sont apparues.

## 4. Mettre en commun le travail

Sûrement la partie la plus difficile dans un projet est l'intégration des codes de chacun pour la réalisation du projet final. Pour les élèves les plus à l'aise, vous allez utiliser `git`, pour les plus débutants vous pouvez travailler à plusieurs à base d'échanges de fichiers (et/ou nous appeler pour essayer `git`).

### 4.a Travailler à plusieurs en utilisant `git`

Pour rappel, le workflow est le suivant:

* l'un de vous crée un dépôt sur `github``, et donne les droits en écriture aux
  autres
* les autres clonent ce dépôt
* chacun travaille sur sa partie, committe régulièrement, et publie ses commits
  sur github (avec `git push`), en ayant éventuellement fait un `git pull` avant
  pour être à jour

Dans ce modèle l'intégration du tout se fait au fil de l'eau, puisque à chaque
`pull` on fait en réalité un `merge` qui intègre les modifications des autres.

Ou bien, on peut aussi décider que chacun travaille sur une branche différente,
de cette façon l'intégration se fait de manière plus explicite, au moment où on
`merge` les branches.

### 4.b travailler à plusieurs à base d'échanges de fichiers

Pour les débutants:

* chacun travaille sur un (ou plusieurs) fichiers (ayant des noms différents des fichiers des autres)
* et vous avez un fichier commun qui va inclure tous les autres fichiers pour appeller les différents codes
* pour que le projet reste simple: mettez tous les fichiers dans un même dossier.

Dès le début vous devez constituer une trame simple et l'exécuter *à-vide*:

* un dossier avec les fichiers des développeurs (vides ou très simples) et le fichier général
* quand vous exécutez le fichier général tous les fichiers des développeurs doivent être inclus et leur code appelé.

Pour cela, vous devez savoir faire des `import` en `Python`:

* en plus des librairies comme `pandas` `, vous pouvez importer des modules que vous avez écrits vous-même et qui se trouvent dans le même répertoire que le fichier qui les importe
* (*Un module `python` est simplement un fichier contenant du `python` et dont le nom de fichier est suffixé par `.py`.*)

Ainsi, par exemple si vous avez  un fichier `A.py` qui contient

```python
# dans A.py
def une_fonction():
      print("hello")
```

eh bien, vous pouvez utiliser ce code dans un autre fichier qui serait **dans le même dossier** en faisant:

```python
# projet.py est dans le même dossier que A.py
import A
A.une_fonction()
```

Ce mécanisme vous permet de découper le code en plusieurs fichiers.

#### 4.b.1 le style: définissez des fonctions

Mettez les parties (cohérentes) de votre code dans des fonctions.

Plutôt que d'écrire:

```python
# la version naïve
# c'est simple mais pas réutilisable

df = pd.read_csv("data.csv")
df = df.dropna()
df = df.rename(columns={"foo": "bar"})
```

Adoptez un style qui consiste à écrire:

```python
# il est préférable d'écrire la même chose
# dans une version "fonctionnelle"
# qui devient réutilisable

def load_data(filename):
    df = pd.read_csv(filename)
    df = df.dropna()
    df = df.rename(columns={"foo": "bar"})
    return df

df = load_data("data.csv")
```

De cette manière, vous *exposez* la fonction `load_data`, qui pourra ainsi être ré-utilisée
ailleurs (dans le fichier général).

#### 4.b.2 Les notebooks comme des modules

Il est possible d'avoir des notebook Jupyter sous le format `.py`. C'est ce que vous allez utiliser et pour
vous faciliter la vie on vous fournit un (tel) notebook vide `empty_notebook.py`.

Dans ce cas-là, le notebook est un module Python comme un autre, et ainsi on
peut **importer des fonctions entre les notebooks**.

Pour essayer, mettez dans un notebook `import empty_notebook`, et vous pourrez
alors appeler `empty_notebook.foo()`.

Cela peut être une façon pour vous de découper le travail en plusieurs
notebooks.

#### 4.b.3 Attention à l'autoreload

Il y a **un piège à éviter**:

* lorsque vous importez un module, `Python`` va le charger **mais seulement la
première fois**
* c'est voulu, car le chargement d'un module peut être coûteux, et on ne veut pas
le refaire à chaque fois

Ainsi:

* si vous êtes dans le notebook principal
* vous importez le module `nettoyage`
* puis ensuite vous modifiez le module `nettoyage.py` (par exemple parce que
  vous avez reçu par mail une autre version)
* et là vous réexécutez l'import de `nettoyage`

... eh bien dans ce cas-là `Python` **ne rechargera pas** le module, et vous aurez l'impression que vos modifications ne sont **pas prises en compte**&nbsp;!

Pour éviter ce problème, vous avez deux possibilités

1. demander à `Python` de recharger le module à chaque fois, en faisant:

   ```python
   import importlib
   importlib.reload(nettoyage)
   ```

2. ou bien (recommandé) utiliser l'extension `autoreload` de `IPython`, qui permet
  de recharger les modules à chaque fois  (*cette méthode est un peu absconse, mais elle est recommandée car on fait la
  configuration une fois pour toutes*):

   ```bash
   # à exécuter DANS VOTRE TERMINAL bash
   # une fois pour toutes

   mkdir -p ~/.ipython/profile_default
   cat >> ~/.ipython/profile_default/ipython_config.py << EOF
   c.InteractiveShellApp.exec_lines = []
   c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
   c.InteractiveShellApp.exec_lines.append('%autoreload 2')
   EOF
   ```

  Une fois cette configuration effectuée, tant que vous êtes dans `IPython` ou dans un notebook,
  vous ne vous préoccupez plus de ce problème, tout se met à fonctionner comme attendu.
