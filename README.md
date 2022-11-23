# 🤖 Artificial-Intelligence
## Feladatleírás
Flow-shop ütemezés határidőkkel Szimulált hűtés algoritmust alkalmazva

## Megoldás lépései
1. A program bekéri a következő adatokat a felhasználótól:
    - Munkák száma
    - Gépek száma
    - Iterációk száma
    - Hűtési stratégia száma
    - Kezdőhőmérséklet
    
    Példa:
    
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/input.png?raw=true)
    
2. A megadott adatok alapján a program random legenerálja megfelelő számú munkát, és azoknak a hosszát, határidejüket, valamint megad egy szintén random kiinduló sorrendet.
3. Következő lépésben indul el a szimulált hűtési algoritmus, amikor is a megadott hűtési stratégiával fogja csökkenteni a rosszabb lehetőségek elfogadásának valószínűségét.
4. Miután meghatározta a program a legjobb eredményt, a következőket írja ki a konzolra:
    - Flow-shop diagram
    - Határidő-táblázat
    - Kezdeti sorrend
    - Legjobb sorrend
    - A program futási ideje az adott hűtési stratégiával
    
    Példa:
    
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/chart_and_table.png?raw=true)
    
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/orders.png?raw=true)
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/runtime.png?raw=true)
