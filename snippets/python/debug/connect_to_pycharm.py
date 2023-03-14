# pip install pydevd-pycharm~=...  # pycharm build version
import pydevd_pycharm
pydevd_pycharm.settrace('172.17.0.1', port=4445, stdoutToServer=True, stderrToServer=True)
