# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making GameAISDK available.

This source code file is licensed under the GNU General Public License Version 3.
For full details, please refer to the file "LICENSE.txt" which is provided as part of this source code package.

Copyright (C) 2020 THL A29 Limited, a Tencent company.  All rights reserved.
"""

import logging

from connect.BusConnect import BusConnect

from protocol import common_pb2


class ProgressReport(object):
    """
    Report training progress to MC
    """

    def __init__(self):
        self.__logger = logging.getLogger('agent')
        self.__connect = BusConnect()

    def Init(self):
        """
        Init tbus connection for report progress
        """
        if self.__connect.Connect() is not True:
            self.__logger.error('Agent connect failed.')
            return False

        return True

    def SendTrainProgress(self, progress):
        """
        Report training progress to MC
        """
        self.__logger.info('im train progress: %d', progress)

        stateMsg = common_pb2.tagMessage()
        stateMsg.eMsgID = common_pb2.MSG_IM_TRAIN_STATE
        stateMsg.stIMTrainState.nProgress = progress

        if self.__connect.SendMsg(stateMsg, BusConnect.PEER_NODE_MC) == 0:
            return True
        return False
