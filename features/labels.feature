@comments @acceptance

Feature: Labels

  Scenario:  Verify GET all labels is returning all data correctly
      As a user I want to GET the labels from TODOIST API

    Given I set the base url and headers
     When I call to labels endpoint using "GET" method using the "None" as parameter
     Then I receive a 200 status code in response
      And I validate the response data from file

  Scenario:  Verify POST labels creates the label correctly
      As a user I want to create a label from TODOIST API

    Given I set the base url and headers
     When I call to labels endpoint using "POST" method using the "comment data" as parameter
      """
      {
      "name": "tasklabel fro scenario",
      "color": "green"
      }
      """
     Then I receive a 200 status code in response
      And I validate the response data from file

  @label_id
  Scenario:  Verify GET labels by id return label data correctly
      As a user I want to retrieve a label providing label id from TODOIST API

    Given I set the base url and headers
     When I call to labels endpoint using "GET" method using the "label id" as parameter
     Then I receive a 200 status code in response
      And I validate the response data from file

  @label_id
  Scenario:  Verify POST labels endpoint update the label correctly
      As a user I want to update a label from TODOIST API
    Given I set the base url and headers
     When I call to labels endpoint using "POST" method using the "update labels data" as parameter
    """
    {
     "name": "label updated from scenario",
     "color": "salmon"
    }
    """
     Then I receive a 200 status code in response
      And I validate the response data from file

  @label_id
  Scenario:  Verify DELETE labels delete the label correctly
      As a user I want to delete a label from TODOIST API

    Given I set the base url and headers
     When I call to labels endpoint using "DELETE" method using the "label_id" as parameter
     Then I receive a 204 status code in response
      And I validate the response data from file

  @label_id
  Scenario:  Verify POST labels can not create a label with an existing name
      As a user I want to verify if two labels with the same name can be created from TODOIST API

    Given I set the base url and headers
     When I call to labels endpoint using "POST" method using the "existing label name data" as parameter
    """
    {
     "name": "label_name",
     "color": "green"
    }
    """
     Then I receive a 400 status code in response
      And I validate the response data from file