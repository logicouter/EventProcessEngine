#!/usr/bin/env python
#encoding=utf-8

class Action():
    def __init__(self, _actionName, _actionTuple):
        self._actionName = _actionName
        self._actionTuple = _actionTuple
        self._nextActionDesc = None
    def alert(self, _content, _receivers):
        alertDesc = Action("alert", (_content, _receivers))
        self._nextActionDesc = alertDesc
        return alertDesc
    def doPlan(self, _planId):
        doPlanDesc = Action("doPlan", (_planId))
        self._nextActionDesc = doPlanDesc
        return doPlanDesc

