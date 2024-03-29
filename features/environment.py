"""
(c) Copyright Jalasoft. 2023

environment.py
    file with all fixture methods for feature and step files
"""
import logging
from random import randint

import requests

from config.config import BASE_URL, HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
    method to define variables that will be used in steps definitions
    :param context:   object     Context object to store and get variables
    """
    context.session = requests.Session()
    context.headers = HEADERS
    context.project_list = []
    context.section_list = []
    context.task_list = []

    context.url = BASE_URL
    LOGGER.debug("Headers before feature: %s", context.headers)
    projects = get_all_projects(context)
    # LOGGER.debug(projects)
    context.project_id_from_all = projects["body"][1]["id"]


def before_feature(context, feature):
    """
    Method to be executed before each feature
    :param context:     object      Contains context information
    :param feature:     object      Contains feature information
    """
    LOGGER.debug("Before feature")
    context.resource_list = {
        "labels": [],
        "comments": [],
        "tasks": [],
        "sections": [],
        "projects": []
    }
    context.feature_name = feature.name.lower()


def before_scenario(context, scenario):
    """
    before
    """
    LOGGER.debug("Scenario tags: %s", scenario.tags)
    LOGGER.debug("***** Scenario Name: %s", scenario.name)

    if "project_id" in scenario.tags:

        response = create_project(context=context, name_project="project x")
        context.project_id = response["body"]["id"]
        LOGGER.debug("Project id created: %s", context.project_id)
        context.resource_list["projects"].append(context.project_id)

    if "section_id" in scenario.tags:

        response = create_section(context=context,
                                  project_id=context.project_id_from_all,
                                  section_name="section x")
        context.section_id = response["body"]["id"]
        LOGGER.debug("Section id created: %s", context.section_id)
        context.resource_list["sections"].append(context.section_id)

    if "task_id" in scenario.tags:

        response = create_task(context=context)
        context.task_id = response["body"]["id"]
        LOGGER.debug("Task id created: %s", context.task_id)
        context.resource_list["tasks"].append(context.task_id)

    if "comment_id" in scenario.tags:

        response = create_comment(context=context,
                                  content="first comment",
                                  task_id=context.task_id)
        context.comment_id = response["body"]["id"]
        LOGGER.debug("Comment id created: %s", context.comment_id)
        context.resource_list["comments"].append(context.comment_id)

    if "label_id" in scenario.tags:

        response = create_label(context=context,
                                content="before scenario label",
                                )
        context.label_id = response["body"]["id"]
        context.label_name = response["body"]["name"]
        LOGGER.debug("Label id of created label: %s", context.label_id)
        context.resource_list["labels"].append(context.label_id)


def after_scenario(context, scenario):
    """
    Method to execute instructions after scenario
    """
    LOGGER.info(f"*** Status for Scenario {scenario.name}: {scenario.status}!***")


def after_feature(context, feature):
    """
    Method to execute instructions after feature
    :param context: current context
    :param feature: current feature

    """
    LOGGER.debug("After feature for  %s feature", feature.name)
    delete_resources(context)


def after_all(context):
    """
    After all hook
    """
    LOGGER.debug("After all")


def create_project(context, name_project):
    """
    Create Project
    """
    body_project = {
        "name": name_project
    }
    response = RestClient().send_request(method_name="post",
                                         session=context.session,
                                         url=context.url+"projects",
                                         headers=context.headers,
                                         data=body_project)
    return response


def create_section(context, project_id, section_name):
    """
    Create Section
    """
    body_section = {
        "project_id": project_id,
        "name": section_name
    }
    response = RestClient().send_request(method_name="post",
                                         session=context.session,
                                         url=context.url+"sections",
                                         headers=context.headers,
                                         data=body_section)
    return response


def get_all_projects(context):
    """
    Method to get all projects
    :param context:   object    Store contextual information about test
    :return:
    """
    response = RestClient().send_request(method_name="get",
                                         session=context.session,
                                         url=context.url + "projects",
                                         headers=context.headers)

    return response


def create_task(context, project_id=None, section_id=None):
    """
    Create task
    """
    data = {
        "content": "Precondition task in before scenario",
        "due_string": "tomorrow at 11:00",
        "due_lang": "en",
        "priority": 4
    }
    if project_id:
        data["project_id"] = project_id
    if section_id:
        data["section_id"] = section_id

    response = RestClient().send_request(method_name="post",
                                         session=context.session,
                                         headers=context.headers,
                                         url=context.url + "tasks", data=data)

    return response


def create_comment(context, content, task_id):
    """
    Create Task request method
    """
    data = {
        "task_id": task_id,
        "content": content,

    }
    response = RestClient().send_request("post", session=context.session,
                                         headers=HEADERS,
                                         url=context.url + "comments",
                                         data=data)

    return response


def create_label(context, content):
    """
    Create label request method

    :param: content: label name

    :return: create request response
    """
    data = {
        "name": f'{content}{randint(0,1000)}',
        "color": "yellow"
    }
    response = RestClient().send_request("post", session=context.session,
                                         headers=HEADERS,
                                         url=context.url + "labels",
                                         data=data)

    return response


def delete_resources(context):
    """
    Delete al resources created for feature execution
    """
    LOGGER.debug("Resources: %s", context.resource_list)
    for resource in context.resource_list:
        LOGGER.debug("Resource: %s", resource)
        for res in context.resource_list[resource]:
            # i.e https://api.todoist.com/rest/v2/ projects / project_id
            url = f"{context.url}{resource}/{res}"
            RestClient().send_request(method_name="delete", session=context.session,
                                      url=url, headers=context.headers)
            LOGGER.info("Deleting %s: %s", resource, res)
