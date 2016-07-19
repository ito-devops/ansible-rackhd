import json
import logging
import requests

logger = logging.getLogger(__name__)

def get_config(base_url='http://localhost:8080/'):

    # http://servername:8080/api/1.1/config/
    url = '{0}api/1.1/config'.format(base_url)
    logger.debug('Fetching config at {0}'.format(url))

    data = False
    try:
        r = requests.get(url)
        data = r.json()
    except ValueError:
        logger.critical('Did not receive a json object from {0}'.format(url))
    except requests.HTTPError as e:
        logger.critical('Unable to reach rackhd at {0}, {1}:{2}'.format(url, e.errno, e.message))

    return data
