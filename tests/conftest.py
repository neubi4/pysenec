import pytest
import pysenec

def pytest_addoption(parser):
    parser.addoption(
        "--senec-host",
        type=str,
        action="store",
        help="Local Senec host (or IP)",
    )


def before_vcr_record(request):
    """Filters requests"""
    request.host = "senec"
    return request


@pytest.fixture(scope='module')
def vcr_config():
    return {
        # Replace the Authorization request header with "DUMMY" in cassettes
        "filter_headers": [('authorization', 'DUMMY')],
        "before_record_request": before_vcr_record,
    }


@pytest.fixture()
async def senec(request, aiohttp_client):
    host = request.config.getoption("--senec-host")
    senec_obj = pysenec.Senec(host, aiohttp_client)
    return senec_obj
