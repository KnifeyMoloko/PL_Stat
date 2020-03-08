"""
Helper functions for dealing with environment variables and the like.
Author: Maciej Cisowski
"""
from os import environ
from logging import getLogger

logger = getLogger("helpers.environment")


def get_env_vars():
    return dict(environ)


def get_api_key():
    env_vars = get_env_vars()
    logger.debug("Getting API_KEY from environment variables...")
    if "API_KEY" in env_vars.keys():
        return env_vars["API_KEY"]
    else:
        print(env_vars)
        logger.error("Did not find API_KEY in environment variables!")
        raise ValueError
