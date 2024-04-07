# Created by mistu at 05-04-2024
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here
  @library
  Scenario: Verify Addbook API functionality
    Given the book details which needs to be added to Library
    When we execute the Addbook PostAPI method
    Then Book is successfully added
#    And status code of response should be 201

  @library
  Scenario Outline: Verify Addbook API functionality
    Given the book details with <isbn>, <aisle>,<name> and <author>
    When we execute the Addbook PostAPI method
    Then Book is successfully added
    Examples:
      |isbn  |aisle |name |author
      |hahahah |980 |Sahas Diary|Subh
      |kfjfjfh |9887 |Sahas Note|Saha