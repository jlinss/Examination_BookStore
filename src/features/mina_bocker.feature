Feature: Mina böcker

  Scenario: Användaren kan markera två böcker som favoriter
    Given att användaren öppnar Läslistan
    When användaren markerar två böcker som favoriter
    And användaren öppnar Mina böcker
    Then ska båda favoritböckerna visas

  Scenario: Användaren kan ta bort en favoritbok
    Given att användaren öppnar Läslistan
    When användaren markerar två böcker som favoriter
    And användaren tar bort en av favoritböckerna
    And användaren öppnar Mina böcker
    Then ska den borttagna boken inte visas
    And ska den andra favoritboken fortfarande visas