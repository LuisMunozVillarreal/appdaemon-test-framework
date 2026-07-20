from appdaemontestframework.pytest_conftest import *  # noqa: F403


@fixture  # noqa: F405
def configure_appdaemontestframework_for_pytester(testdir):
    """
    Extra test fixtue use for testing pytest runners.
    """
    testdir.makeini(
        """
        [pytest]
        asyncio_default_fixture_loop_scope = function
    """
    )
    testdir.makeconftest(
        """
        from appdaemontestframework.pytest_conftest import *
    """
    )
