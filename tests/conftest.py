import pytest

from space_battle.ioc_container import ioc_scopes


@pytest.fixture(autouse=True)
def _setup_scoped_ioc() -> None:
    ioc_scopes.setup()
