# Created by mistu at 06-04-2024
Feature: Github API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200