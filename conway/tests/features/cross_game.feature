Feature: Conway's Game of Life
  As a fan of Conway's Game of Life,
  I want to seed a board and then evolve it,
  So that I can see life grow and die.

  Scenario: Seed with five live cells in a cross shape
    Given I have a board with:
      .*.
      ***
      .*.
    Then I expect the board to evolve to:
      ***
      *.*
      ***



