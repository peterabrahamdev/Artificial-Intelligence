## [EN](#-artificial-intelligence-project) [ES](#-proyecto-de-inteligencia-artificial) [HU](#-mesterséges-intelligencia-projekt)
# 🤖 Artificial Intelligence Project
## Task description

Flow-shop scheduling with deadlines using the Simulated Annealing algorithm.

## Steps of the solution

1. The program requests the input of the following data from the user:
     - Number of jobs
     - Number of machines
     - Number of iterations
     - Cooling strategy's number
     - Initial temperature
    
     Example:
     
     ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/input.png?raw=true)


1. Based on the given data, the program randomly generates an appropriate number of jobs, their length and deadline, and also provides a random starting order.
2. In the next step, the simulated annealing algorithm starts and it will reduce the probability of accepting worse options with the specified cooling strategy.
3. After the program has determined the best result, it writes the following to the console:
     - Flow-shop chart
     - Deadline table
     - Initial order
     - Best order
     - The running time of the program with the given cooling strategy
    
    Example:
    
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/chart_and_table.png?raw=true)
    
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/orders.png?raw=true)
    ![alt text](https://github.com/APeterIstvan/Artificial-Intelligence/blob/main/runtime.png?raw=true)


# 🤖 Mesterséges Intelligencia Projekt
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
