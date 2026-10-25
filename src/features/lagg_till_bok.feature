Feature: Lägg till bok

  Scenario: Användaren kan öppna formuläret
    Given att användaren öppnar Läslistan
    When användaren klickar på "Lägg till bok"
    Then ska formuläret för att lägga till en bok visas

  Scenario: Användaren kan lägga till en ny bok
    Given att användaren öppnar Läslistan
    When användaren öppnar formuläret för att lägga till en bok
    And användaren fyller i titeln "Luften är fri" och författaren "Sara Lövestram"
    And användaren klickar på knappen för att lägga till boken
    Then ska boken "Luften är fri" visas på sidan

  Scenario: Knappen för att lägga till en bok är inaktiverad när obligatoriska uppgifter saknas
    Given att användaren öppnar Läslistan
    When användaren öppnar formuläret för att lägga till en bok
    Then ska knappen för att lägga till boken vara inaktiverad