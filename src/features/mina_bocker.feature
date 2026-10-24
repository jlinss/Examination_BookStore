
Feature: Mina böcker

  Scenario: Användaren kan öppna Mina böcker
    Given att användaren öppnar Läslistan
    When användaren klickar på "Mina böcker"
    Then ska sidan Mina böcker visas

  Scenario: Användaren kan se sina favoriter
    Given att användaren öppnar Läslistan
    When användaren öppnar Mina böcker
    Then ska favoritboken visas
