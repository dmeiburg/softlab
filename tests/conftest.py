import pytest

def pytest_addoption(parser):
    parser.addoption("--hw", action="store_true", default=False,
                     help="run test agains real hardware")

@pytest.fixture(scope="module")
def run_on_hardware(request):
    return request.config.getoption("--hw")

@pytest.fixture(scope="session")
def monkeysession(request):
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()
