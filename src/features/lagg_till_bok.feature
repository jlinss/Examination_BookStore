Feature: Lägg till bok

  Scenario: Användaren kan öppna formuläret
    Given att användaren öppnar Läslistan
    When användaren klickar på "Lägg till bok"
    Then ska formuläret för att lägga till en bok visas

  Scenario: Användaren kan lägga till en ny bok
    Given att användaren öppnar Läslistan
    When användaren öppnar formuläret för att lägga till en bok
    And användaren fyller i titeln "Testbok 123" och författaren "Testförfattare"
    And användaren klickar på knappen för att lägga till boken
    Then ska boken "Testbok 123" visas på sidan