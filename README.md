Läslistan – testautomatisering

Beskrivning

   Det här projektet innehåller automatiserade tester för både backend och frontend i webbapplikationen Läslistan.
   För att skriva och köra testerna används Python, pytest, pytest-bdd och Playwright. 
   Syftet är att kontrollera att de viktigaste funktionerna fungerar som förväntat.

Vad testas?

   Backend

      - Att det går att lägga till en ny bok i BookStore.
      - Att en bok kan läggas till bland favoriterna.
      - Att det går att ta bort en bok från favoriterna.
      - Att upprepade anrop till toggleFavorite fungerar som förväntat.
      - Att BookStore och FavoriteBooks fungerar tillsammans.

   Frontend

      - Att användaren kan navigera mellan katalogen, formuläret och Mina böcker.
      - Att användaren kan markera böcker som favoriter och ta bort dem från favoritlistan.
      - Att det går att lägga till en ny bok via formuläret.
      - Att formuläret hanterar de uppgifter som användaren skriver in.

Installation:

1. Klona projektet från GitHub.
2. Skapa och aktivera en virtuell Python-miljö.
3. Installera de paket som behövs:

   python -m pip install -r requirements.txt

   Installera Chromium för Playwright:
    
   python -m playwright install chromium

Köra testerna

För att köra enhets- och integrationstesterna:

- python -m pytest tests/unit tests/integration -v

För att köra alla tester i projektet:

- python -m pytest -v

Tekniker
- Python
- pytest
- pytest-bdd
- Playwright
- Git och GitHub
- GitHub Actions