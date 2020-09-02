# TDD Rediscovered - UnitTests

## What is this?

This is an implementation of [Conway's Game of Life](https://github.com/iancooper/GameOfLife), used to support my course: TDD Rediscovered.

It is public to support students of that course reviewing the code used.

## The Rules

The code was created as a kata, using the following rules:

* We are writing Unit Tests. The Unit is a class and should be isolated from other classes.

* The prompt to write a test is a new method. If we need a method, we write a test before we write the method.

* When we discover that we need collaborators our preference is to mock them, establishing their behaviour from the client, and then implement them with their own tests. 
