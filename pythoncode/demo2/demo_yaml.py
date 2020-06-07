#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

# document = """
#   a: 1
#   b:
#     c: 3
#     d: 4
# """
# print(yaml.dump(yaml.load(document)))
# print(yaml.load(document))
# print(yaml.safe_load(document))
print(yaml.safe_load(open("datas.yml")))
# print(yaml.safe_dump(['a', 'b', 'c']))
