import pytest

from softlab.sdg_function_generator import SDGFunctionGenerator

class MockFunctionGenerator:
    def query(q):
        responses = {"*IDN?": "Siglent Technologies,SDG2122X,SDG2XCAQ2R1992,2.01.01.23R8\n"}
        return responses[q]


@pytest.fixture(scope="module")
def fg(monkeysession, run_on_hardware):

    def mock_init(*args, **kwargs):
        pass

    ip = "10.0.10.67"

    if run_on_hardware:
        function_generator = SDGFunctionGenerator(ip)
    else:
        monkeysession.setattr(SDGFunctionGenerator, "__init__", mock_init)
        function_generator = SDGFunctionGenerator(ip)
        function_generator.device = MockFunctionGenerator

    return function_generator


def test_get_idn(fg):
    assert 'SDG' in fg.idn()
