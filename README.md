Watson Detection Tool.
=====================

La finalidad de esta herramienta consiste en generar información de inteligencia que pueda ser aprovechada por otros sistemas, tales como IDS y Firewalls inteligentes.En su modo habitual permite detectar conexiones a sistemas maliciosos empleando para ello diversas listas de reputación configurables por el usuario. (Si incluye entre otras, el servicio Online AntiBotnet de INCIBE)

La información obtenida por el programa se exporta como Indicador de Compromiso (IOC) en dos formatos: OpenIOC y Cybox.

El programa tiene dos modos de funcionamiento, el primero de ellos consiste en analizar las conexiones establecidas por los procesos y generar los IOCs pertinentes. El segundo modo consiste en la escucha pasiva del tráfico de red, en donde se reconstruyen los flujos de comunicación, se detectan los end-points y se analizan con las bases de datos de reputación.


Prerequisitos
-------------

De sistema, en los sistemas Debian/Ubuntu se resuelven ejecutando el siguiente comando:
```
apt-get install zlib1g-dev libxslt-dev libxml2 libxml2-dev tshark
```

De Python, se resuelven ejecutando el siguiente comando:

```
pip install -r dependencies.txt
```

Uso
---

```
usage: watsondt.py [-h] [-c] [-p {openioc,cybox}] [-a] [-l LIVE_CAPTURE] [-i]
                   [-v]

Watson Detection Tool

optional arguments:
  -h, --help            show this help message and exit
  -c, --show-conn       Muestra SOLO procesos con conexiones
  -p {openioc,cybox}, --generate-profile {openioc,cybox}
                        Genera un IOC en formato especificado.
  -a, --all-conn        Muestra todas las conexiones
  -l LIVE_CAPTURE, --live-capture LIVE_CAPTURE
                        Captura el trafico de una interfaz de red en tiempo
                        real.
  -i, --incibe          Comprueba que la IP de origen no esté presente en el
                        servicio AntiBotnet de INCIBE.
  -v, --version         Muestra la version del programa
```

Autor
-----
Luis González Fernández
