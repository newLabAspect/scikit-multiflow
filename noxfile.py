import nox


@nox.session(python=["3.12"])
def test(session: nox.Session) -> None:
    session.install(".")
    session.install("pytest","numpy","scikit-learn","pandas","sortedcontainers","scipy","matplotlib")
    session.run("pytest")