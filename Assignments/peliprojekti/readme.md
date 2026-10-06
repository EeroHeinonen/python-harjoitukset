# Haaparannan hunsvotit

Eero Heinonen

# Ohjeet
__Peli käynnistetään suorittamalla gameNoExt.py tiedosto.__

game.py tiedoston suorittamiseen vaaditaan ulkoinen moduuli "pyfiglet".
(pip install pyfiglet)

# Dokumentaatio
Peli sijoittuu tulevaisuuteen vuoteen 2083 ja sen ideana on käydä läpi eri huoneita (kaupunkeja) Suomen kartalla, keräten rahaa etsimällä sitä kaupungeista tai päihittämällä vastustajia.

Pelin tavoitteena on päästä alkuhuoneesta (Olohuone, living room), loppuhuoneeseen (Haaparannan karkkikauppa, Haaparanta candy store, store), jossa pelaaja voi ostaa lopullisen esineen (Salmiakki), jos on kerännyt tarpeeksi rahaa matkallaan.

Peliä pelataan syöttämällä komentoja joka huoneessa, kuten liiku huoneesta toiseen (move), nosta esineitä (pick up), käytä esineitä (use) ja näytä tavaraluettelo (inventory).

Huoneiden välillä liikkuminen tapahtuu syöttämällä yksi neljästä suunnasta (ylös: u, alas: d, vasen: l sekä oikea: r), peli ei kerro käyttäjälle mikä suunta johtaa mihin, vaan käyttäjän täytyy itse kartoittaa pelin huoneet.

Vastustajia voi päihittää käyttämällä löydettyjä esineitä, mutta ei muilla tavoin. Löydettyjä esineitä voi käyttää, sen tyypistä riippuen, joko pelaajan omien elämäpisteiden nostoon tai vastustajien päihittämiseen. Pelissä ei kuitenkaan ole minkäänlaista kuvailevaa väkivaltaa. Vastustajat saattavat pudottaa joko rahaa tai jonkin esineen jonka pelaaja voi nostaa.

Peli sisältää myös tallena/lataa järjestelmän, jonka avulla on mahdollistaa tallentaa pelin kyseisen pelaajan tilanne, sekä myös ladata se myöhemmässä ajankohdassa, kuten käynnistyskertojen välillä. Peli tallentaa kyseisen pelaajan tilanteen erilliseen tiedostoon sekä luo jokaiselle pelaajalle henkilökohtaisen tiedoston, mahdollistaen monta tallenusta. Lataus tapahtuu automaattisesti pelaajan syöttäessä nimensä pelin alussa tai vaihtoehtoisesti päävalikon kautta tapahtuvan lataus-valikon (Load data) kautta. Päävalikossa pelaaja voi myös poistaa tallenustietoja poista-valikossa. (Delete data)

Pelin vaikeusastetta on myös mahdollista muuttaa asetus-valikon (Settings) kautta.

Peli sisällyttää fossiilivapaiden energiamuotojen käytön periaatteen tiedottamalla käyttäjälle pelin intro tekstissä kävelyn olevan ainoa vaihtoehto liikkumiselle ja moottoriajoneuvojen olevan käyttökiellossa, sillä ilmaston lämpeneminen on saavuttanut kriittisen pisteen, jossa pieninkin määrä viherhuone päästöjä aiheuttaisi maailmanlaajuisen katastrofin.

# Rakenne
```text
peliprojekti/
├── Modules/
│ ├── __pycache__/
│ ├── __init__.py
│ ├── bc.py
│ ├── enemy.py
│ ├── item.py
│ ├── play.py
│ ├── player.py
│ ├── room.py
│ └── settings.py
├── game.py
├── gameNoExt.py
├── ohjeet.txt
├── readme.md
├── tarina.txt
└── saves/
  └── .gitkeep
└── Tasks/
  ├── gameProject1.py
  └── gameProject2.py
```
