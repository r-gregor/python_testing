#! /usr/bin/env python3

import platform

print('Uname:', platform.uname())

print()
print('Distribution :', platform.linux_distribution())
print('Architecture :', platform.architecture())
print('Machine :', platform.machine())
print('Node :', platform.node())
print('Processor :', platform.processor())
print('Release :', platform.release())
print('System :', platform.system())
print('Version :', platform.version())
print('Platform :', platform.platform())
