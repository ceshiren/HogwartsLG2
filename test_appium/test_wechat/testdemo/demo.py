#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys

with open('../datas/contacts.yml') as f:
    datas = yaml.safe_load(f)
    print(datas)
    addlist = datas['add']
    dellist = datas['del']
    print(addlist)
    print(dellist)
    # contactaddlist = datas[]
