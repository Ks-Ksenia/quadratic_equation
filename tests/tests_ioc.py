from unittest.mock import Mock

import pytest

from space_battle.ioc_container.ioc import IoC
from space_battle.exceptions import IoCResolveError
from space_battle.ioc_container.ioc_scopes import Scope, setup as scoped_ioc_setup
from tests.constants import MOCK_ARGS, MOCK_KWARGS


@pytest.fixture(autouse=True)
def _setup_scoped_ioc():
    scoped_ioc_setup()


@pytest.fixture(autouse=True)
def _clear_scope(_setup_scoped_ioc):
    yield
    IoC.resolve("IoC.Scope.Current.Clear").execute()


def test_ioc_scope_ops():
    root_scope = IoC.resolve("IoC.Scope.Current")
    assert isinstance(root_scope, Scope)

    new_scope = IoC.resolve("IoC.Scope.Create", "scope1")
    assert new_scope is not root_scope

    IoC.resolve("IoC.Scope.Current.Set", new_scope).execute()
    assert IoC.resolve("IoC.Scope.Current") is new_scope

    assert IoC.resolve("IoC.Scope.Parent") is root_scope

    IoC.resolve("IoC.Scope.Current.Clear").execute()
    assert IoC.resolve("IoC.Scope.Current") is root_scope


def test_root_parent_error():
    with pytest.raises(IoCResolveError):
        IoC.resolve("IoC.Scope.Parent")


def test_create_scope_with_parent():
    scope1 = IoC.resolve("IoC.Scope.Create", "scope1")
    scope2 = IoC.resolve("IoC.Scope.Create", "scope2", scope1)
    IoC.resolve("IoC.Scope.Current.Set", scope2).execute()

    assert IoC.resolve("IoC.Scope.Current") is scope2
    assert IoC.resolve("IoC.Scope.Parent") is scope1


def test_resolve_error():
    with pytest.raises(IoCResolveError):
        IoC.resolve("Nonexistent Dependency")


def test_resolve_from_root():
    mock = Mock()
    IoC.resolve("IoC.Scope.Register", "mock", mock).execute()

    IoC.resolve("mock", *MOCK_ARGS, **MOCK_KWARGS)
    mock.assert_called_once_with(*MOCK_ARGS, **MOCK_KWARGS)


def test_resolve_from_current():
    scope1 = IoC.resolve("IoC.Scope.Create", "scope1")
    IoC.resolve("IoC.Scope.Current.Set", scope1).execute()

    mock = Mock()
    IoC.resolve("IoC.Scope.Register", "mock", mock).execute()

    IoC.resolve("mock", *MOCK_ARGS, **MOCK_KWARGS)
    mock.assert_called_once_with(*MOCK_ARGS, **MOCK_KWARGS)


def test_resolve_from_parent():
    scope1 = IoC.resolve("IoC.Scope.Create", "scope1")

    mock = Mock()
    IoC.resolve("IoC.Scope.Register", "mock", mock).execute()

    scope2 = IoC.resolve("IoC.Scope.Create", "scope2", scope1)
    IoC.resolve("IoC.Scope.Current.Set", scope2).execute()

    IoC.resolve("mock", *MOCK_ARGS, **MOCK_KWARGS)
    mock.assert_called_once_with(*MOCK_ARGS, **MOCK_KWARGS)
