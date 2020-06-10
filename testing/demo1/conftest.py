#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='function')
def login():
    print("登录")
    return ['jerry', '123456']
