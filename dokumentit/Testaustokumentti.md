#Testausdokumentti
    Yksikkötestauksen kattavuusraportti.
    Mitä on testattu, miten tämä tehtiin?

- Testi1: Testi testaa print board metodia tarkistamalla antaako peli oikean pelitilanteen yhden siirron jälkeen.
    Minkälaisilla syötteillä testaus tehtiin?
- Jokainen testi alustetaan luomalla Board olio.
- Testi1: Syötteenä toimii PLAY:3 komento, joka simuloi tekoälyalustan antavaa syötettä.
    Miten testit voidaan toistaa?
- Testit ovat suoritettavissa unittesteillä. Aluksi pitää avata poetry virtuaaliympäristö, jonka jälkeen suorittaa src maintests komento. 
    Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)
    Ei siis riitä todeta, että testaus on tehty käyttäen automaattisia yksikkötestejä, vaan tarvitaan konkreettista tietoa testeistä, kuten:
        Testattu, että tekoäly osaa tehdä oikeat siirrot tilanteessa, jossa on varma 4 siirron voitto. Todettu, että siirroille palautuu voittoarvo 100000.
        Testattu 10 kertaan satunnaisesti valituilla lähtö- ja maalipisteillä, että JPS löytää saman pituisen reitin kuin Dijkstran algoritmi.
        Kummallakin algoritmilla on pakattu 8 MB tekstitiedosto, purettu se ja tarkastettu, että tuloksena on täsmälleen alkuperäinen tiedosto.
