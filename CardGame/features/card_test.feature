
Feature: testing all card classes
  Scenario: test that rank stores value
    Given I have created a Rank object
    When i make a new rank class
    Then the value of ranks is stored

    Given i make a new Suit Object
    When i make a new suit class
    Then the value of suit is stored

    Scenario: drawing a card removes it from the list
      Given i have a set of cards
      When i draw a card
      Then It will be removed from the list
