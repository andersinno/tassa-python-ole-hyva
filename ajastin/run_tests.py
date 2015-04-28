# -*- coding: utf-8 -*-

import pytest

pytest.main([
    "-vvvs",
    "--cov",
    ".",
    "--cov-report",
    "html",
    "interval_timer_tests"
])
