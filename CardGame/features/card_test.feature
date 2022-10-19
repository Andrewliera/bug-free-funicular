
Feature: testing all card classes
  Scenario: test that rank stores value
    When i make a new class
    Then the value of ranks is stored

    When i make a new Class
    Then the value of suit is stored

    Scenario: drawing a card removes it from the list
      Given i have a set of cards
      When i draw a card
      Then It will be removed from the list
