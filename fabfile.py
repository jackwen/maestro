#!/usr/bin/env python
# Copyright 2013 Maestro Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from maestro.core import *
from maestro import system as sys
from maestro.deploy import python as py
from maestro.utils import load_maestro_rc
from maestro.service import mysql
from maestro.service import redis
from maestro.service import memcached
from maestro.crate import management as crate
# load the maestro resource file for provider keys
load_maestro_rc()

import os
import logging
# change log levels
logging.getLogger('paramiko').setLevel(logging.ERROR)
# try to load env password
from fabric.api import env
env.password = os.environ.get('FABRIC_PASSWORD')
if not env.parallel:
    env.output_prefix = False
