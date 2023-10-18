@tasks @acceptance

Feature: Comments

  @task_id @comment_id
  Scenario:  Verify GET all comments is returning all data correctly
      As a user I want to GET the comments from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "GET" method using the "None" as parameter
    Then I receive a 200 status code in response

  @task_id
  Scenario:  Verify POST comments creates the comment correctly
      As a user I want to create a comment from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "comment data" as parameter
    """
    {
     "task_id": "task_id",
     "content": "comment created in scenario"
    }
    """
    Then I receive a 200 status code in response

  @task_id @comment_id
  Scenario:  Verify GET comment by id return comment data correctly
      As a user I want to retrieve a comment providing comment id from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "comment id" as parameter
    Then I receive a 200 status code in response


  @task_id @comment_id
  Scenario:  Verify DELETE coments delete the comment correctly
      As a user I want to delete a comment from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "DELETE" method using the "comment_id" as parameter
    Then I receive a 204 status code in response
    And I validate the response data from file

  @task_id @comment_id
  Scenario:  Verify POST comments endpoint update the comment correctly
      As a user I want to update a comment from TODOIST API
    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "update comments data" as parameter
    """
    {
     "content": "comment updated from scenario"
    }
    """
    Then I receive a 200 status code in response
