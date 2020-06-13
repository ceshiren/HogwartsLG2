#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.dependency(name='cart')
def test_addcart():
    print("add cart")
    raise NameError


@pytest.mark.dependency(depends=["cart"])
def test_settle():
    print("settle")
