import pytest
import requests
import yaml


@pytest.fixture(scope='session')
def confglob():
    with open('confglobfile.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


@pytest.fixture(scope='session')
def baseurl(confglob):
    return confglob['ORDERS-SERVOCE']['baseurl']


@pytest.fixture(scope='session')
def healthcheck(baseurl):
    return requests.get(f'{baseurl}/HealthCheck')