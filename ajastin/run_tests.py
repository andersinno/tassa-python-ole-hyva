# -*- coding: utf-8 -*-

import pytest

pytest.main([
    "-vvv",
    "--cov",
    ".",
    "--cov-report",
    "html",
    "interval_timer_tests"
])
