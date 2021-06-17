1. Introducció

En aquest document s’explica l’especificació d’un simulador a mida, part del segon projecte de l’assignatura Simulació.

Pel que fa referència a les peces necessàries per a construir un simulador a mida podem trobar les següents:
* Mòdul d’entrada
* Motor de simulació
* Objectes de simulació
* Events de simulació
* Mòdul de sortida i mostra d’estadístics
* Aleatorietat

Per tant, aquestes peces les podrem trobar dins del codi del nostre projecte i s’aniran aclarint a mida que s’avança en la lectura del document. D’altra banda també es trobarà una descripció del cas a simular, el diagrama d’especificació en U.M.L. de les entitats que hi trobarem en el sistema de simulació i diagrames de seqüència dels processos que es duen a terme en el sistema.

Conjuntament amb aquest fitxer es podrà obtenir el codi font del simulador.

2. Descripció del sistema

El cas a tractar està basat en un simulador de tres ascensors d’un edifici de negocis que s’espatllen cada 100, 200 i 300 serveis entre pisos, i el primer ascensor sols es mou en plantes senars, el segon en plantes parells i el tercer funciona sols quan algun està espatllat. Calen 60 minuts per a reparar la incidència de qualsevol ascensor.

Donada la complexitat d’un sistema d’ascensor, treballarem amb una versió simplificada que queda clara amb les hipòtesis especificades a continuació

2.1 Hipòtesis

Igual que a qualsevol projecte de simulació, s’han considerat una serie hipòtesis sistèmiques i simplificadores.

2.1.1 Hipòtesis sistèmiques

Pel que fa referència a les dades:
En un ascensor no hi ha límit de persones, de manera que cada cop que un ascensor arribi a un pis, totes les persones que estiguin esperant entraran.
El temps per defecte d’arribada d’usuaris segueix una distribució estadística, on la mitjana d’aquesta distribució es defineix en l’entrada del simulador..
El temps de transport dels ascensors entre pisos es fixe.
Els ascensors fallen segons una probabilitat indicada per l’entrada del simulador.
El nombre de pisos es fixe.

D’altra banda, pel que fa referència a les estructurals
Un usuari pot cridar un ascensor des de qualsevol pis.
Un ascensor només s’espatllarà després d’haver acabat l’etapa d’entity transfer.
En el moment que les persones baixen de l’ascensor, surten del sistema.

2.1.2 Hipòtesis simplificadores

L’ascensor només es mou entre els pisos dels que els crida, per exemple, si una persona en el pis 0 crida l’ascensor, l’ascensor només es mourà cap a aquest pis i no la portarà al destí que vol.
Les persones de l’ascensor baixen en el següent pis en què ha de parar l’ascensor.
El temps per anar de un pis a l’altre es el mateix per cada pis. Aquest temps es defineix a partir de la consola.

# Fet amb

* [Python](https://docs.python.org/3/) - language used
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE used

