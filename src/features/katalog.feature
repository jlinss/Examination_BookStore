Feature: Katalog

  Scenario: Användaren kan se katalogen
    Given att användaren öppnar Läslistan
    When katalogsidan har laddats
    Then ska katalogsidan visas

  Scenario: Användaren kan öppna sidan Mina böcker
    Given att användaren öppnar Läslistan
    When användaren klickar på "Mina böcker"
    Then ska sidan Mina böcker visas

  Scenario: Användaren kan öppna statistik
    Given att användaren öppnar Läslistan
    When användaren klickar på "Statistik"
    Then ska statistiksidan visas