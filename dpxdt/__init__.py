#!/usr/bin/env python
# Copyright 2013 Brett Slatkin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Common module for dpxdt client and server pieces."""

import logging
import sys
logging.basicConfig(
    format='%(levelname)s %(filename)s:%(lineno)s] %(message)s')


# Local Libraries
sys.path.append(".")
import gflags
FLAGS = gflags.FLAGS


gflags.DEFINE_bool(
    'verbose', False,
    'When set, do verbose logging output.')


gflags.DEFINE_bool(
    'verbose_queries', False,
    'When set, do verbose logging of SQL queries.')

gflags.DEFINE_bool(
    'verbose_workers', False,
    'When set, do verbose logging of background Worker progress.')
