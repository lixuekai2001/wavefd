"""
Functions and classes in the wavefd package.
"""
from .lame import lame_lambda, lame_mu
from .wavelets import RickerWavelet

from ._version import get_versions as _get_versions


# Get the version number through versioneer
__version__ = _get_versions()['version']
__commit__ = _get_versions()['full-revisionid']


def test(doctest=True, verbose=True, coverage=False):
    """
    Run the test suite.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests. If you
    haven't already, you can install it with `conda
    <http://conda.pydata.org/>`__ or `pip <https://pip.pypa.io/en/stable/>`__.

    Parameters
    ----------

    doctest : bool
        If ``True``, will run the doctests as well (code examples that start
        with a ``>>>`` in the docs).
    verbose : bool
        If ``True``, will print extra information during the test run.
    coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.

    Raises
    ------

    AssertionError
        If pytest returns a non-zero error code indicating that some tests have
        failed.

    """
    import pytest
    args = []
    if verbose:
        args.append('-vv')
    if coverage:
        args.append('--cov=wavefd')
        args.append('--cov-report=term-missing')
    if doctest:
        args.append('--doctest-modules')
    args.append('--pyargs')
    args.append('wavefd')
    status = pytest.main(args)
    assert status == 0, "Some tests have failed."
