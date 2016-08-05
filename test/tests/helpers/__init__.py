import json
import logging
import requests
from fabric.api import task, roles, run, sudo

from envassert import port

logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def fetch_json(url):

    logger.debug('Fetching json data using fabric/curl at {0}'.format(url))

    # I tried so many ways to use requests or urllib with
    # fabric.api.execute and it always attempted the request on
    # the local host, not the remote. Reverting to curl. -John

    response = run('curl {}'.format(url))
    data = json.loads(response)
    logger.debug(data)

    return data


def fetch_json_request(url):

    # http://servername:8080/api/1.1/config/
    logger.debug('Fetching json data using requests at {0}'.format(url))

    data = False
    try:
        r = requests.get(url)
        data = r.json()
    except ValueError:
        logger.critical('Did not receive a json object from {0}'.format(url))
    except requests.HTTPError as e:
        logger.critical('Unable to reach rackhd at {0}, {1}:{2}'.format(url, e.errno, e.message))

    return data


def rackhd_config(base='http://localhost:8080'):
    url = '{0}/api/1.1/config'.format(base)
    return fetch_json_request(url)


def rackhd_nodes(base='http://localhost:8080'):
    url = '{0}/api/1.1/nodes'.format(base)
    return fetch_json_request(url)


def rackhd_node_workflows(id, base='http://localhost:8080'):
    url = '{0}/api/1.1/nodes/{1}/workflows'.format(base, id)
    return fetch_json_request(url)


def rackhd_workflow(id, base='http://localhost:8080'):
    url = '{0}/api/1.1/workflows/{1}'.format(base, id)
    return fetch_json_request(url)


def rackhd_workflow_task(id, taskname, base='http://localhost:8080'):

    workflow = rackhd_workflow(id)
    task = False
    for t in workflow['tasks'].keys():
        if workflow['tasks'][t]['injectableName'] == taskname:
            task = workflow['tasks'][t]
            logger.debug('task: {0}'.format(task))

    return task


@task
def check_rackhd_ports():
    assert port.is_listening(8080)  # rackhd northbound
    assert port.is_listening(9080)  # rackhd southbound


@task
def list_packages():
    response = run("dpkg-query -W -f='${binary:Package;-13}\t\t${Version}\t${binary:Summary}\n' on\*")
    return response

@task
def reset_rackhd():
    logger.debug('resetting rackhd')
    run('/vagrant/examples/reset-rackhd.bash')

@task
def do_sudo(cmd='hostname -f'):
    logger.debug('running as sudo: {0}'.format(cmd))
    sudo(cmd)
