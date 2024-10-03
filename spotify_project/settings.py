#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:16:15 2024

@author: raail
"""

# settings.py
import os
from dotenv import load_dotenv, dotenv_values


# Get the environment variables from at the os level
load_dotenv()
config = dotenv_values(".env.development")


# Get environment variables
CLIENTID = os.getenv("CLIENTID")
CLIENTSECRET = os.getenv("CLIENTSECRET")


