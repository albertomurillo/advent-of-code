import pytest


@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(
    terminalreporter: pytest.TerminalReporter,
    exitstatus: pytest.ExitCode,  # noqa: ARG001
    config: pytest.Config,  # noqa: ARG001
) -> None:
    tr = terminalreporter

    # Display the custom report only if a certain verbosity is set.
    if tr.verbosity < 1:
        return

    tr.ensure_newline()
    tr.section("Test Durations (ms)", sep="=", yellow=True)
    reports: list[pytest.TestReport] = tr.stats.get("passed", [])
    reports.sort(key=lambda x: x.duration, reverse=True)
    for report in reports:
        tr.write_line(f"{report.duration * 1000:8.2f}ms  {report.nodeid}")
    tr.section("End of Test Durations (ms)", sep="=", yellow=True)
