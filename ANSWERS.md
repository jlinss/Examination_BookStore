Svar på teorifrågor

1. Skillnaden mellan olika typer av tester

Enhetstest: Man testar en liten del av programmet, till exempel en metod i en klass. Man vill se om den delen fungerar själv.

Integrationstest: Man testar om olika delar av programmet fungerar tillsammans. Till exempel om BookStore och FavoriteBooks kan arbeta tillsammans utan problem.

Regressionstest: Man testar om funktioner som fungerade innan fortfarande fungerar efter att man har ändrat koden.

Prestandatest: Man testar hur snabbt systemet fungerar och om det klarar många användare samtidigt.

2. Hur fungerar TDD?

TDD betyder Test-Driven Development. Först skriver man ett test för en funktion som man inte har gjort ännu. Sedan kör man testet och ser att det inte fungerar. Efter det skriver man kod så att testet blir godkänt. Till sist kan man förbättra koden och köra testerna igen för att se att allt fungerar.
Det här kallas Red, Green, Refactor.

3. Skillnaden mellan BDD och TDD

TDD handlar om att skriva tester medan man utvecklar koden. Man testar små delar steg för steg.

BDD handlar mer om hur programmet ska fungera och vad användaren ska kunna göra. Man kan skriva scenarier med Given, When och Then. Det gör att man kan förstå vad som ska hända, även om man inte kan programmera så mycket.

4. Vilka tester skulle jag använda för en webbsida som Läslistan?

Jag skulle använda olika typer av tester eftersom de testar olika saker i programmet.

Med enhetstester skulle jag testa metoderna i BookStore och FavoriteBooks. Med integrationstester skulle jag kontrollera att dessa två klasser fungerar tillsammans.

För frontend skulle jag använda Playwright för att testa att man kan navigera mellan sidorna, använda formuläret, lägga till böcker och markera favoriter. Jag skulle använda pytest-bdd för att skriva scenarier i feature-filer och sedan koppla dem till Python-kod.

Jag skulle också köra regressionstester när jag ändrar eller lägger till nya funktioner. Jag skulle använda GitHub Actions för att testerna körs automatiskt när jag pushar kod till main. Om webbsidan får många användare skulle jag också testa prestandan för att se om sidan fortfarande fungerar bra.