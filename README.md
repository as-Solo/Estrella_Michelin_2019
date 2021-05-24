# ¿Dónde se encuentran y cómo de caros son los Restaurantes con tres estrellas Michelín?

El objetivo de este proyecto es poder tratar los datos dados desde un csv para ampliar la información del mismo csv de varias maneras, ya sea operando con la información dada o scrapeando desde las distintas webs que ofrece la base de datos. Para así poder tener una información con la que trabajar y llevar a cabo nuestras hipótesis.


![portada_Michelin.jpg](https://github.com/as-Solo/Estrella_Michelin_2019/blob/main/img/portada_Michelin.jpg)

### Table of Contents

1. Información General
2. Tratamiento de la información
3. [Librerías](#Librerías:)
4. [Tecnología](#Tecnología:)

## Información general

En este proyecto se pretendía practicar todos los conceptos dados hasta ahora, haciendo especial hincapié en alimentar nuestro set de datos, en mi caso el elegido fue https://www.kaggle.com/jackywang529/michelin-restaurants?select=three-stars-michelin-restaurants.csv, para luego poder trabajar con toda la información en conjunto.

Dada la información del csv y la información que su pudo ir añadiendo gracias a las diferentes web que ofrecía el propio csv, nos interesaba poder observar: 
```
- La distribución geográfica de los distintos Restaurantes.
- El precio medio de cada Restaurante
- Cómo afectaba al precio medio el tipo de cocina que se ofrecía
- Cómo podía afectar la situación del Restaurante en el precio.
```

## Tratamiento de la información

Para llevar a cabo este proyecto se han llevado a cabo 4 notebooks correspondientes a cada una de las etapas siguientes: 
1. Una observación del dataset seleccionado y una evaluación de los posibles datos a añadir junto con la realización de las hipótesis. 
2. Se ha limpiado el dataset y se le ha ido añadiendo, en este caso gracias a [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), distinta información que se ha considerado relevante. Para ello se han generado unas funciones que quedan guardadas en el archivo scrapping.py.
3. Con los datos limpios en un nuevo dataset alimentado por el scrapping se han hecho los cálculos y se han guardado las variantes que se querían estudiar, para posteriormente poder hacer gráficos de las mismas y así tener una base de visualización para nuestras hipótesis iniciales.
4. Con los gráficos ya generados y exportados y todos los datos analizados, sólo queda sacar conclusiones de nuestras hipótesis basándonos en las gráficas mostradas.


## Librerías:

***
Para este proyecto se han usado estas librerías y módulos. 
```
import pandas as pd
import numpy as np
import src.scrapping as sc
import requests
from bs4 import BeautifulSoup
import re
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry
import plotly.graph_objects as go
import plotly.express as px

```

## Tecnología: 

A list of technologies used within the project:
* [Jupyter Notebook](https://jupyter.org/)
* [Python](https://www.python.org/): Version 3.8
* [Visual Studio Code](https://code.visualstudio.com/)
* [plotly](https://plotly.com/graphing-libraries/)
* [BeautifulSoap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Autores

* **Alejandro S. del Solo** - (https://github.com/as-Solo)
