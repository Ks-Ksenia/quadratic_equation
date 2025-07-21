import threading
from unittest.mock import Mock

import pytest

from space_battle.ioc_container.ioc import IoC
from space_battle.setup.state import ioc_setup_game_state
from space_battle.event_loop import HardStopEventLoopCommand, SoftStopEventLoopCommand, RunEventLoopInThreadCommand


@pytest.fixture(autouse=True)
def _ioc_setup():
    ioc_setup_game_state()


@pytest.fixture()
def exception_handler_store():
    return IoC.resolve("ExceptionHandlerStore")


@pytest.fixture()
def event_loop():
    return IoC.resolve("EventLoop")


def test_run_event_loop(event_loop):
    cmd = Mock()
    event = threading.Event()
    cmd.execute = event.set

    event_loop.put_command(cmd)

    RunEventLoopInThreadCommand(event_loop).execute()
    event.wait()

    event_loop.put_command(HardStopEventLoopCommand(event_loop))


def test_hard_stop(event_loop):
    cmd1 = Mock()
    cmd2 = Mock()

    event_loop.put_command(cmd1)
    event_loop.put_command(HardStopEventLoopCommand(event_loop))
    event_loop.put_command(cmd2)

    event = threading.Event()
    event_loop.add_after_hook(event.set)

    RunEventLoopInThreadCommand(event_loop).execute()

    event.wait()
    cmd1.execute.assert_called_once()
    cmd2.execute.assert_not_called()


def test_soft_stop(event_loop):
    cmd1 = Mock()
    cmd2 = Mock()

    event_loop.put_command(cmd1)
    event_loop.put_command(SoftStopEventLoopCommand(event_loop))
    event_loop.put_command(cmd2)

    event = threading.Event()
    event_loop.add_after_hook(event.set)

    RunEventLoopInThreadCommand(event_loop).execute()

    event.wait()
    cmd1.execute.assert_called_once()
    cmd2.execute.assert_called_once()