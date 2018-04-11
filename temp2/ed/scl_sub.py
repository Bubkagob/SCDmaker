#!/usr/bin/env python

#
# Generated Fri Apr  6 14:56:56 2018 by generateDS.py version 2.29.11.
# Python 3.6.4 (default, Jan  5 2018, 02:35:40)  [GCC 7.2.1 20171224]
#
# Command line options:
#   ('-o', 'scl_api.py')
#   ('-s', 'scl_sub.py')
#
# Command line arguments:
#   SCL.xsd
#
# Command line:
#   /usr/bin/generateDS.py -o "scl_api.py" -s "scl_sub.py" SCL.xsd
#
# Current working directory (os.getcwd()):
#   ed
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class tBaseElementSub(supermod.tBaseElement):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, extensiontype_=None):
        super(tBaseElementSub, self).__init__(anytypeobjs_, Text, Private, extensiontype_, )
supermod.tBaseElement.subclass = tBaseElementSub
# end class tBaseElementSub


class tUnNamingSub(supermod.tUnNaming):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, extensiontype_=None):
        super(tUnNamingSub, self).__init__(anytypeobjs_, Text, Private, desc, extensiontype_, )
supermod.tUnNaming.subclass = tUnNamingSub
# end class tUnNamingSub


class tNamingSub(supermod.tNaming):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, extensiontype_=None):
        super(tNamingSub, self).__init__(anytypeobjs_, Text, Private, name, desc, extensiontype_, )
supermod.tNaming.subclass = tNamingSub
# end class tNamingSub


class tIDNamingSub(supermod.tIDNaming):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, id=None, desc=None, extensiontype_=None):
        super(tIDNamingSub, self).__init__(anytypeobjs_, Text, Private, id, desc, extensiontype_, )
supermod.tIDNaming.subclass = tIDNamingSub
# end class tIDNamingSub


class tAnyContentFromOtherNamespaceSub(supermod.tAnyContentFromOtherNamespace):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        super(tAnyContentFromOtherNamespaceSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, extensiontype_, )
supermod.tAnyContentFromOtherNamespace.subclass = tAnyContentFromOtherNamespaceSub
# end class tAnyContentFromOtherNamespaceSub


class tTextSub(supermod.tText):
    def __init__(self, anytypeobjs_=None, source=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tTextSub, self).__init__(anytypeobjs_, source, valueOf_, mixedclass_, content_, )
supermod.tText.subclass = tTextSub
# end class tTextSub


class tPrivateSub(supermod.tPrivate):
    def __init__(self, anytypeobjs_=None, type_=None, source=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tPrivateSub, self).__init__(anytypeobjs_, type_, source, valueOf_, mixedclass_, content_, )
supermod.tPrivate.subclass = tPrivateSub
# end class tPrivateSub


class tHeaderSub(supermod.tHeader):
    def __init__(self, id=None, version=None, revision='', toolID=None, nameStructure='IEDName', Text=None, History=None):
        super(tHeaderSub, self).__init__(id, version, revision, toolID, nameStructure, Text, History, )
supermod.tHeader.subclass = tHeaderSub
# end class tHeaderSub


class tHitemSub(supermod.tHitem):
    def __init__(self, anytypeobjs_=None, version=None, revision=None, when=None, who=None, what=None, why=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tHitemSub, self).__init__(anytypeobjs_, version, revision, when, who, what, why, valueOf_, mixedclass_, content_, )
supermod.tHitem.subclass = tHitemSub
# end class tHitemSub


class tValSub(supermod.tVal):
    def __init__(self, sGroup=None, valueOf_=None):
        super(tValSub, self).__init__(sGroup, valueOf_, )
supermod.tVal.subclass = tValSub
# end class tValSub


class tValueWithUnitSub(supermod.tValueWithUnit):
    def __init__(self, unit=None, multiplier='', valueOf_=None, extensiontype_=None):
        super(tValueWithUnitSub, self).__init__(unit, multiplier, valueOf_, extensiontype_, )
supermod.tValueWithUnit.subclass = tValueWithUnitSub
# end class tValueWithUnitSub


class tVoltageSub(supermod.tVoltage):
    def __init__(self, unit=None, multiplier='', valueOf_=None):
        super(tVoltageSub, self).__init__(unit, multiplier, valueOf_, )
supermod.tVoltage.subclass = tVoltageSub
# end class tVoltageSub


class tBitRateInMbPerSecSub(supermod.tBitRateInMbPerSec):
    def __init__(self, unit=None, multiplier='', valueOf_=None):
        super(tBitRateInMbPerSecSub, self).__init__(unit, multiplier, valueOf_, )
supermod.tBitRateInMbPerSec.subclass = tBitRateInMbPerSecSub
# end class tBitRateInMbPerSecSub


class tDurationInSecSub(supermod.tDurationInSec):
    def __init__(self, unit=None, multiplier='', valueOf_=None):
        super(tDurationInSecSub, self).__init__(unit, multiplier, valueOf_, )
supermod.tDurationInSec.subclass = tDurationInSecSub
# end class tDurationInSecSub


class tDurationInMilliSecSub(supermod.tDurationInMilliSec):
    def __init__(self, unit=None, multiplier='', valueOf_=None):
        super(tDurationInMilliSecSub, self).__init__(unit, multiplier, valueOf_, )
supermod.tDurationInMilliSec.subclass = tDurationInMilliSecSub
# end class tDurationInMilliSecSub


class tIEDSub(supermod.tIED):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, type_=None, manufacturer=None, configVersion=None, owner=None, Services=None, AccessPoint=None):
        super(tIEDSub, self).__init__(anytypeobjs_, Text, Private, name, desc, type_, manufacturer, configVersion, owner, Services, AccessPoint, )
supermod.tIED.subclass = tIEDSub
# end class tIEDSub


class tServicesSub(supermod.tServices):
    def __init__(self, DynAssociation=None, SettingGroups=None, GetDirectory=None, GetDataObjectDefinition=None, DataObjectDirectory=None, GetDataSetValue=None, SetDataSetValue=None, DataSetDirectory=None, ConfDataSet=None, DynDataSet=None, ReadWrite=None, TimerActivatedControl=None, ConfReportControl=None, GetCBValues=None, ConfLogControl=None, ReportSettings=None, LogSettings=None, GSESettings=None, SMVSettings=None, GSEDir=None, GOOSE=None, GSSE=None, FileHandling=None, ConfLNs=None):
        super(tServicesSub, self).__init__(DynAssociation, SettingGroups, GetDirectory, GetDataObjectDefinition, DataObjectDirectory, GetDataSetValue, SetDataSetValue, DataSetDirectory, ConfDataSet, DynDataSet, ReadWrite, TimerActivatedControl, ConfReportControl, GetCBValues, ConfLogControl, ReportSettings, LogSettings, GSESettings, SMVSettings, GSEDir, GOOSE, GSSE, FileHandling, ConfLNs, )
supermod.tServices.subclass = tServicesSub
# end class tServicesSub


class tAccessPointSub(supermod.tAccessPoint):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, router=False, clock=False, Server=None, LN=None):
        super(tAccessPointSub, self).__init__(anytypeobjs_, Text, Private, name, desc, router, clock, Server, LN, )
supermod.tAccessPoint.subclass = tAccessPointSub
# end class tAccessPointSub


class tServerSub(supermod.tServer):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, timeout=30, Authentication=None, LDevice=None, Association=None):
        super(tServerSub, self).__init__(anytypeobjs_, Text, Private, desc, timeout, Authentication, LDevice, Association, )
supermod.tServer.subclass = tServerSub
# end class tServerSub


class tLDeviceSub(supermod.tLDevice):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, inst=None, ldName=None, LN0=None, LN=None, AccessControl=None):
        super(tLDeviceSub, self).__init__(anytypeobjs_, Text, Private, desc, inst, ldName, LN0, LN, AccessControl, )
supermod.tLDevice.subclass = tLDeviceSub
# end class tLDeviceSub


class tAccessControlSub(supermod.tAccessControl):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tAccessControlSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.tAccessControl.subclass = tAccessControlSub
# end class tAccessControlSub


class tAssociationSub(supermod.tAssociation):
    def __init__(self, kind=None, associationID=None, iedName=None, ldInst=None, prefix='', lnClass=None, lnInst=None):
        super(tAssociationSub, self).__init__(kind, associationID, iedName, ldInst, prefix, lnClass, lnInst, )
supermod.tAssociation.subclass = tAssociationSub
# end class tAssociationSub


class tAnyLNSub(supermod.tAnyLN):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, lnType=None, DataSet=None, ReportControl=None, LogControl=None, DOI=None, Inputs=None, extensiontype_=None):
        super(tAnyLNSub, self).__init__(anytypeobjs_, Text, Private, desc, lnType, DataSet, ReportControl, LogControl, DOI, Inputs, extensiontype_, )
supermod.tAnyLN.subclass = tAnyLNSub
# end class tAnyLNSub


class tLNSub(supermod.tLN):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, lnType=None, DataSet=None, ReportControl=None, LogControl=None, DOI=None, Inputs=None, lnClass=None, inst=None, prefix=''):
        super(tLNSub, self).__init__(anytypeobjs_, Text, Private, desc, lnType, DataSet, ReportControl, LogControl, DOI, Inputs, lnClass, inst, prefix, )
supermod.tLN.subclass = tLNSub
# end class tLNSub


class tLN0Sub(supermod.tLN0):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, lnType=None, DataSet=None, ReportControl=None, LogControl=None, DOI=None, Inputs=None, lnClass='LLN0', inst='', GSEControl=None, SampledValueControl=None, SettingControl=None, SCLControl=None, Log=None, extensiontype_=None):
        super(tLN0Sub, self).__init__(anytypeobjs_, Text, Private, desc, lnType, DataSet, ReportControl, LogControl, DOI, Inputs, lnClass, inst, GSEControl, SampledValueControl, SettingControl, SCLControl, Log, extensiontype_, )
supermod.tLN0.subclass = tLN0Sub
# end class tLN0Sub


class tDataSetSub(supermod.tDataSet):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, FCDA=None):
        super(tDataSetSub, self).__init__(anytypeobjs_, Text, Private, name, desc, FCDA, )
supermod.tDataSet.subclass = tDataSetSub
# end class tDataSetSub


class tFCDASub(supermod.tFCDA):
    def __init__(self, ldInst=None, prefix='', lnClass=None, lnInst=None, doName=None, daName=None, fc=None):
        super(tFCDASub, self).__init__(ldInst, prefix, lnClass, lnInst, doName, daName, fc, )
supermod.tFCDA.subclass = tFCDASub
# end class tFCDASub


class tControlSub(supermod.tControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, extensiontype_=None):
        super(tControlSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, extensiontype_, )
supermod.tControl.subclass = tControlSub
# end class tControlSub


class tControlWithTriggerOptSub(supermod.tControlWithTriggerOpt):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, intgPd=0, TrgOps=None, extensiontype_=None):
        super(tControlWithTriggerOptSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, intgPd, TrgOps, extensiontype_, )
supermod.tControlWithTriggerOpt.subclass = tControlWithTriggerOptSub
# end class tControlWithTriggerOptSub


class tTrgOpsSub(supermod.tTrgOps):
    def __init__(self, dchg=False, qchg=False, dupd=False, period=False, gi=True):
        super(tTrgOpsSub, self).__init__(dchg, qchg, dupd, period, gi, )
supermod.tTrgOps.subclass = tTrgOpsSub
# end class tTrgOpsSub


class tReportControlSub(supermod.tReportControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, intgPd=0, TrgOps=None, rptID=None, confRev=None, buffered=False, bufTime=0, OptFields=None, RptEnabled=None):
        super(tReportControlSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, intgPd, TrgOps, rptID, confRev, buffered, bufTime, OptFields, RptEnabled, )
supermod.tReportControl.subclass = tReportControlSub
# end class tReportControlSub


class tRptEnabledSub(supermod.tRptEnabled):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, max=1, ClientLN=None):
        super(tRptEnabledSub, self).__init__(anytypeobjs_, Text, Private, desc, max, ClientLN, )
supermod.tRptEnabled.subclass = tRptEnabledSub
# end class tRptEnabledSub


class tClientLNSub(supermod.tClientLN):
    def __init__(self, iedName=None, ldInst=None, prefix='', lnClass=None, lnInst=None):
        super(tClientLNSub, self).__init__(iedName, ldInst, prefix, lnClass, lnInst, )
supermod.tClientLN.subclass = tClientLNSub
# end class tClientLNSub


class tLogControlSub(supermod.tLogControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, intgPd=0, TrgOps=None, logName=None, logEna=True, reasonCode=True):
        super(tLogControlSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, intgPd, TrgOps, logName, logEna, reasonCode, )
supermod.tLogControl.subclass = tLogControlSub
# end class tLogControlSub


class tInputsSub(supermod.tInputs):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, ExtRef=None):
        super(tInputsSub, self).__init__(anytypeobjs_, Text, Private, desc, ExtRef, )
supermod.tInputs.subclass = tInputsSub
# end class tInputsSub


class tExtRefSub(supermod.tExtRef):
    def __init__(self, daName=None, intAddr=None, iedName=None, ldInst=None, prefix='', lnClass=None, lnInst=None, doName=None):
        super(tExtRefSub, self).__init__(daName, intAddr, iedName, ldInst, prefix, lnClass, lnInst, doName, )
supermod.tExtRef.subclass = tExtRefSub
# end class tExtRefSub


class tLogSub(supermod.tLog):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tLogSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.tLog.subclass = tLogSub
# end class tLogSub


class tControlWithIEDNameSub(supermod.tControlWithIEDName):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, confRev=None, IEDName=None, extensiontype_=None):
        super(tControlWithIEDNameSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, confRev, IEDName, extensiontype_, )
supermod.tControlWithIEDName.subclass = tControlWithIEDNameSub
# end class tControlWithIEDNameSub


class tGSEControlSub(supermod.tGSEControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, confRev=None, IEDName=None, type_='GOOSE', appID=None):
        super(tGSEControlSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, confRev, IEDName, type_, appID, )
supermod.tGSEControl.subclass = tGSEControlSub
# end class tGSEControlSub


class tSampledValueControlSub(supermod.tSampledValueControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, datSet=None, confRev=None, IEDName=None, smvID=None, multicast=True, smpRate=None, nofASDU=None, SmvOpts=None):
        super(tSampledValueControlSub, self).__init__(anytypeobjs_, Text, Private, name, desc, datSet, confRev, IEDName, smvID, multicast, smpRate, nofASDU, SmvOpts, )
supermod.tSampledValueControl.subclass = tSampledValueControlSub
# end class tSampledValueControlSub


class tSettingControlSub(supermod.tSettingControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, numOfSGs=None, actSG=1):
        super(tSettingControlSub, self).__init__(anytypeobjs_, Text, Private, desc, numOfSGs, actSG, )
supermod.tSettingControl.subclass = tSettingControlSub
# end class tSettingControlSub


class tSCLControlSub(supermod.tSCLControl):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None):
        super(tSCLControlSub, self).__init__(anytypeobjs_, Text, Private, desc, )
supermod.tSCLControl.subclass = tSCLControlSub
# end class tSCLControlSub


class tDOISub(supermod.tDOI):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, ix=None, accessControl=None, SDI=None, DAI=None):
        super(tDOISub, self).__init__(anytypeobjs_, Text, Private, desc, name, ix, accessControl, SDI, DAI, )
supermod.tDOI.subclass = tDOISub
# end class tDOISub


class tSDISub(supermod.tSDI):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, ix=None, SDI=None, DAI=None):
        super(tSDISub, self).__init__(anytypeobjs_, Text, Private, desc, name, ix, SDI, DAI, )
supermod.tSDI.subclass = tSDISub
# end class tSDISub


class tDAISub(supermod.tDAI):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, sAddr=None, valKind='Set', ix=None, Val=None):
        super(tDAISub, self).__init__(anytypeobjs_, Text, Private, desc, name, sAddr, valKind, ix, Val, )
supermod.tDAI.subclass = tDAISub
# end class tDAISub


class tServiceYesNoSub(supermod.tServiceYesNo):
    def __init__(self):
        super(tServiceYesNoSub, self).__init__()
supermod.tServiceYesNo.subclass = tServiceYesNoSub
# end class tServiceYesNoSub


class tServiceWithMaxSub(supermod.tServiceWithMax):
    def __init__(self, max=None, extensiontype_=None):
        super(tServiceWithMaxSub, self).__init__(max, extensiontype_, )
supermod.tServiceWithMax.subclass = tServiceWithMaxSub
# end class tServiceWithMaxSub


class tServiceWithMaxAndMaxAttributesSub(supermod.tServiceWithMaxAndMaxAttributes):
    def __init__(self, max=None, maxAttributes=None, extensiontype_=None):
        super(tServiceWithMaxAndMaxAttributesSub, self).__init__(max, maxAttributes, extensiontype_, )
supermod.tServiceWithMaxAndMaxAttributes.subclass = tServiceWithMaxAndMaxAttributesSub
# end class tServiceWithMaxAndMaxAttributesSub


class tServiceWithMaxAndModifySub(supermod.tServiceWithMaxAndModify):
    def __init__(self, max=None, modify=True):
        super(tServiceWithMaxAndModifySub, self).__init__(max, modify, )
supermod.tServiceWithMaxAndModify.subclass = tServiceWithMaxAndModifySub
# end class tServiceWithMaxAndModifySub


class tServiceWithMaxAndMaxAttributesAndModifySub(supermod.tServiceWithMaxAndMaxAttributesAndModify):
    def __init__(self, max=None, maxAttributes=None, modify=True):
        super(tServiceWithMaxAndMaxAttributesAndModifySub, self).__init__(max, maxAttributes, modify, )
supermod.tServiceWithMaxAndMaxAttributesAndModify.subclass = tServiceWithMaxAndMaxAttributesAndModifySub
# end class tServiceWithMaxAndMaxAttributesAndModifySub


class tServiceWithMaxAndClientSub(supermod.tServiceWithMaxAndClient):
    def __init__(self, max=None, client=True):
        super(tServiceWithMaxAndClientSub, self).__init__(max, client, )
supermod.tServiceWithMaxAndClient.subclass = tServiceWithMaxAndClientSub
# end class tServiceWithMaxAndClientSub


class tServiceSettingsSub(supermod.tServiceSettings):
    def __init__(self, cbName='Fix', datSet='Fix', extensiontype_=None):
        super(tServiceSettingsSub, self).__init__(cbName, datSet, extensiontype_, )
supermod.tServiceSettings.subclass = tServiceSettingsSub
# end class tServiceSettingsSub


class tReportSettingsSub(supermod.tReportSettings):
    def __init__(self, cbName='Fix', datSet='Fix', rptID='Fix', optFields='Fix', bufTime='Fix', trgOps='Fix', intgPd='Fix'):
        super(tReportSettingsSub, self).__init__(cbName, datSet, rptID, optFields, bufTime, trgOps, intgPd, )
supermod.tReportSettings.subclass = tReportSettingsSub
# end class tReportSettingsSub


class tLogSettingsSub(supermod.tLogSettings):
    def __init__(self, cbName='Fix', datSet='Fix', logEna='Fix', trgOps='Fix', intgPd='Fix'):
        super(tLogSettingsSub, self).__init__(cbName, datSet, logEna, trgOps, intgPd, )
supermod.tLogSettings.subclass = tLogSettingsSub
# end class tLogSettingsSub


class tGSESettingsSub(supermod.tGSESettings):
    def __init__(self, cbName='Fix', datSet='Fix', appID='Fix', dataLabel='Fix'):
        super(tGSESettingsSub, self).__init__(cbName, datSet, appID, dataLabel, )
supermod.tGSESettings.subclass = tGSESettingsSub
# end class tGSESettingsSub


class tSMVSettingsSub(supermod.tSMVSettings):
    def __init__(self, cbName='Fix', datSet='Fix', svID='Fix', optFields='Fix', smpRate='Fix', SmpRate=None):
        super(tSMVSettingsSub, self).__init__(cbName, datSet, svID, optFields, smpRate, SmpRate, )
supermod.tSMVSettings.subclass = tSMVSettingsSub
# end class tSMVSettingsSub


class tConfLNsSub(supermod.tConfLNs):
    def __init__(self, fixPrefix=False, fixLnInst=False):
        super(tConfLNsSub, self).__init__(fixPrefix, fixLnInst, )
supermod.tConfLNs.subclass = tConfLNsSub
# end class tConfLNsSub


class tControlBlockSub(supermod.tControlBlock):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, ldInst=None, cbName=None, Address=None, extensiontype_=None):
        super(tControlBlockSub, self).__init__(anytypeobjs_, Text, Private, desc, ldInst, cbName, Address, extensiontype_, )
supermod.tControlBlock.subclass = tControlBlockSub
# end class tControlBlockSub


class tCommunicationSub(supermod.tCommunication):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, SubNetwork=None):
        super(tCommunicationSub, self).__init__(anytypeobjs_, Text, Private, desc, SubNetwork, )
supermod.tCommunication.subclass = tCommunicationSub
# end class tCommunicationSub


class tSubNetworkSub(supermod.tSubNetwork):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, type_=None, BitRate=None, ConnectedAP=None):
        super(tSubNetworkSub, self).__init__(anytypeobjs_, Text, Private, name, desc, type_, BitRate, ConnectedAP, )
supermod.tSubNetwork.subclass = tSubNetworkSub
# end class tSubNetworkSub


class tConnectedAPSub(supermod.tConnectedAP):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, iedName=None, apName=None, Address=None, GSE=None, SMV=None, PhysConn=None):
        super(tConnectedAPSub, self).__init__(anytypeobjs_, Text, Private, desc, iedName, apName, Address, GSE, SMV, PhysConn, )
supermod.tConnectedAP.subclass = tConnectedAPSub
# end class tConnectedAPSub


class tAddressSub(supermod.tAddress):
    def __init__(self, P=None):
        super(tAddressSub, self).__init__(P, )
supermod.tAddress.subclass = tAddressSub
# end class tAddressSub


class tGSESub(supermod.tGSE):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, ldInst=None, cbName=None, Address=None, MinTime=None, MaxTime=None):
        super(tGSESub, self).__init__(anytypeobjs_, Text, Private, desc, ldInst, cbName, Address, MinTime, MaxTime, )
supermod.tGSE.subclass = tGSESub
# end class tGSESub


class tSMVSub(supermod.tSMV):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, ldInst=None, cbName=None, Address=None):
        super(tSMVSub, self).__init__(anytypeobjs_, Text, Private, desc, ldInst, cbName, Address, )
supermod.tSMV.subclass = tSMVSub
# end class tSMVSub


class tPhysConnSub(supermod.tPhysConn):
    def __init__(self, type_=None, P=None):
        super(tPhysConnSub, self).__init__(type_, P, )
supermod.tPhysConn.subclass = tPhysConnSub
# end class tPhysConnSub


class tPSub(supermod.tP):
    def __init__(self, type_=None, valueOf_=None, extensiontype_=None):
        super(tPSub, self).__init__(type_, valueOf_, extensiontype_, )
supermod.tP.subclass = tPSub
# end class tPSub


class tP_IPSub(supermod.tP_IP):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_IPSub, self).__init__(type_, valueOf_, )
supermod.tP_IP.subclass = tP_IPSub
# end class tP_IPSub


class tP_IP_SUBNETSub(supermod.tP_IP_SUBNET):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_IP_SUBNETSub, self).__init__(type_, valueOf_, )
supermod.tP_IP_SUBNET.subclass = tP_IP_SUBNETSub
# end class tP_IP_SUBNETSub


class tP_IP_GATEWAYSub(supermod.tP_IP_GATEWAY):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_IP_GATEWAYSub, self).__init__(type_, valueOf_, )
supermod.tP_IP_GATEWAY.subclass = tP_IP_GATEWAYSub
# end class tP_IP_GATEWAYSub


class tP_OSI_NSAPSub(supermod.tP_OSI_NSAP):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_NSAPSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_NSAP.subclass = tP_OSI_NSAPSub
# end class tP_OSI_NSAPSub


class tP_OSI_TSELSub(supermod.tP_OSI_TSEL):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_TSELSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_TSEL.subclass = tP_OSI_TSELSub
# end class tP_OSI_TSELSub


class tP_OSI_SSELSub(supermod.tP_OSI_SSEL):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_SSELSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_SSEL.subclass = tP_OSI_SSELSub
# end class tP_OSI_SSELSub


class tP_OSI_PSELSub(supermod.tP_OSI_PSEL):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_PSELSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_PSEL.subclass = tP_OSI_PSELSub
# end class tP_OSI_PSELSub


class tP_OSI_AP_TitleSub(supermod.tP_OSI_AP_Title):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_AP_TitleSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_AP_Title.subclass = tP_OSI_AP_TitleSub
# end class tP_OSI_AP_TitleSub


class tP_OSI_AP_InvokeSub(supermod.tP_OSI_AP_Invoke):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_AP_InvokeSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_AP_Invoke.subclass = tP_OSI_AP_InvokeSub
# end class tP_OSI_AP_InvokeSub


class tP_OSI_AE_QualifierSub(supermod.tP_OSI_AE_Qualifier):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_AE_QualifierSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_AE_Qualifier.subclass = tP_OSI_AE_QualifierSub
# end class tP_OSI_AE_QualifierSub


class tP_OSI_AE_InvokeSub(supermod.tP_OSI_AE_Invoke):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_OSI_AE_InvokeSub, self).__init__(type_, valueOf_, )
supermod.tP_OSI_AE_Invoke.subclass = tP_OSI_AE_InvokeSub
# end class tP_OSI_AE_InvokeSub


class tP_MAC_AddressSub(supermod.tP_MAC_Address):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_MAC_AddressSub, self).__init__(type_, valueOf_, )
supermod.tP_MAC_Address.subclass = tP_MAC_AddressSub
# end class tP_MAC_AddressSub


class tP_APPIDSub(supermod.tP_APPID):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_APPIDSub, self).__init__(type_, valueOf_, )
supermod.tP_APPID.subclass = tP_APPIDSub
# end class tP_APPIDSub


class tP_VLAN_PRIORITYSub(supermod.tP_VLAN_PRIORITY):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_VLAN_PRIORITYSub, self).__init__(type_, valueOf_, )
supermod.tP_VLAN_PRIORITY.subclass = tP_VLAN_PRIORITYSub
# end class tP_VLAN_PRIORITYSub


class tP_VLAN_IDSub(supermod.tP_VLAN_ID):
    def __init__(self, type_=None, valueOf_=None):
        super(tP_VLAN_IDSub, self).__init__(type_, valueOf_, )
supermod.tP_VLAN_ID.subclass = tP_VLAN_IDSub
# end class tP_VLAN_IDSub


class tAbstractDataAttributeSub(supermod.tAbstractDataAttribute):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, sAddr=None, bType=None, valKind='Set', type_=None, count=0, Val=None, extensiontype_=None):
        super(tAbstractDataAttributeSub, self).__init__(anytypeobjs_, Text, Private, desc, name, sAddr, bType, valKind, type_, count, Val, extensiontype_, )
supermod.tAbstractDataAttribute.subclass = tAbstractDataAttributeSub
# end class tAbstractDataAttributeSub


class tLNodeTypeSub(supermod.tLNodeType):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, id=None, desc=None, iedType='', lnClass=None, DO=None):
        super(tLNodeTypeSub, self).__init__(anytypeobjs_, Text, Private, id, desc, iedType, lnClass, DO, )
supermod.tLNodeType.subclass = tLNodeTypeSub
# end class tLNodeTypeSub


class tDOSub(supermod.tDO):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, type_=None, accessControl=None, transient=False):
        super(tDOSub, self).__init__(anytypeobjs_, Text, Private, desc, name, type_, accessControl, transient, )
supermod.tDO.subclass = tDOSub
# end class tDOSub


class tDOTypeSub(supermod.tDOType):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, id=None, desc=None, iedType='', cdc=None, SDO=None, DA=None):
        super(tDOTypeSub, self).__init__(anytypeobjs_, Text, Private, id, desc, iedType, cdc, SDO, DA, )
supermod.tDOType.subclass = tDOTypeSub
# end class tDOTypeSub


class tSDOSub(supermod.tSDO):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, type_=None):
        super(tSDOSub, self).__init__(anytypeobjs_, Text, Private, name, desc, type_, )
supermod.tSDO.subclass = tSDOSub
# end class tSDOSub


class tDASub(supermod.tDA):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, sAddr=None, bType=None, valKind='Set', type_=None, count=0, Val=None, fc=None, dchg=False, qchg=False, dupd=False):
        super(tDASub, self).__init__(anytypeobjs_, Text, Private, desc, name, sAddr, bType, valKind, type_, count, Val, fc, dchg, qchg, dupd, )
supermod.tDA.subclass = tDASub
# end class tDASub


class tDATypeSub(supermod.tDAType):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, id=None, desc=None, iedType='', BDA=None):
        super(tDATypeSub, self).__init__(anytypeobjs_, Text, Private, id, desc, iedType, BDA, )
supermod.tDAType.subclass = tDATypeSub
# end class tDATypeSub


class tBDASub(supermod.tBDA):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name=None, sAddr=None, bType=None, valKind='Set', type_=None, count=0, Val=None):
        super(tBDASub, self).__init__(anytypeobjs_, Text, Private, desc, name, sAddr, bType, valKind, type_, count, Val, )
supermod.tBDA.subclass = tBDASub
# end class tBDASub


class tEnumTypeSub(supermod.tEnumType):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, id=None, desc=None, EnumVal=None):
        super(tEnumTypeSub, self).__init__(anytypeobjs_, Text, Private, id, desc, EnumVal, )
supermod.tEnumType.subclass = tEnumTypeSub
# end class tEnumTypeSub


class tEnumValSub(supermod.tEnumVal):
    def __init__(self, ord=None, valueOf_=None):
        super(tEnumValSub, self).__init__(ord, valueOf_, )
supermod.tEnumVal.subclass = tEnumValSub
# end class tEnumValSub


class tDataTypeTemplatesSub(supermod.tDataTypeTemplates):
    def __init__(self, LNodeType=None, DOType=None, DAType=None, EnumType=None):
        super(tDataTypeTemplatesSub, self).__init__(LNodeType, DOType, DAType, EnumType, )
supermod.tDataTypeTemplates.subclass = tDataTypeTemplatesSub
# end class tDataTypeTemplatesSub


class HistoryTypeSub(supermod.HistoryType):
    def __init__(self, Hitem=None):
        super(HistoryTypeSub, self).__init__(Hitem, )
supermod.HistoryType.subclass = HistoryTypeSub
# end class HistoryTypeSub


class SettingGroupsTypeSub(supermod.SettingGroupsType):
    def __init__(self, SGEdit=None, ConfSG=None):
        super(SettingGroupsTypeSub, self).__init__(SGEdit, ConfSG, )
supermod.SettingGroupsType.subclass = SettingGroupsTypeSub
# end class SettingGroupsTypeSub


class AuthenticationTypeSub(supermod.AuthenticationType):
    def __init__(self, none=True, password=False, weak=False, strong=False, certificate=False):
        super(AuthenticationTypeSub, self).__init__(none, password, weak, strong, certificate, )
supermod.AuthenticationType.subclass = AuthenticationTypeSub
# end class AuthenticationTypeSub


class OptFieldsTypeSub(supermod.OptFieldsType):
    def __init__(self, seqNum=False, timeStamp=False, dataSet=False, reasonCode=False, dataRef=False, entryID=False, configRef=False, bufOvfl=False, segmentation=False):
        super(OptFieldsTypeSub, self).__init__(seqNum, timeStamp, dataSet, reasonCode, dataRef, entryID, configRef, bufOvfl, segmentation, )
supermod.OptFieldsType.subclass = OptFieldsTypeSub
# end class OptFieldsTypeSub


class SmvOptsTypeSub(supermod.SmvOptsType):
    def __init__(self, refreshTime=False, sampleSynchronized=False, sampleRate=False, security=False, dataRef=False):
        super(SmvOptsTypeSub, self).__init__(refreshTime, sampleSynchronized, sampleRate, security, dataRef, )
supermod.SmvOptsType.subclass = SmvOptsTypeSub
# end class SmvOptsTypeSub


class LN0Sub(supermod.LN0):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, lnType=None, DataSet=None, ReportControl=None, LogControl=None, DOI=None, Inputs=None, lnClass='LLN0', inst='', GSEControl=None, SampledValueControl=None, SettingControl=None, SCLControl=None, Log=None):
        super(LN0Sub, self).__init__(anytypeobjs_, Text, Private, desc, lnType, DataSet, ReportControl, LogControl, DOI, Inputs, lnClass, inst, GSEControl, SampledValueControl, SettingControl, SCLControl, Log, )
supermod.LN0.subclass = LN0Sub
# end class LN0Sub


class tTerminalSub(supermod.tTerminal):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, name='', connectivityNode=None, substationName=None, voltageLevelName=None, bayName=None, cNodeName=None):
        super(tTerminalSub, self).__init__(anytypeobjs_, Text, Private, desc, name, connectivityNode, substationName, voltageLevelName, bayName, cNodeName, )
supermod.tTerminal.subclass = tTerminalSub
# end class tTerminalSub


class tLNodeSub(supermod.tLNode):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, desc=None, lnInst='', lnClass=None, iedName='None', ldInst='', prefix='', lnType=None):
        super(tLNodeSub, self).__init__(anytypeobjs_, Text, Private, desc, lnInst, lnClass, iedName, ldInst, prefix, lnType, )
supermod.tLNode.subclass = tLNodeSub
# end class tLNodeSub


class tLNodeContainerSub(supermod.tLNodeContainer):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, extensiontype_=None):
        super(tLNodeContainerSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, extensiontype_, )
supermod.tLNodeContainer.subclass = tLNodeContainerSub
# end class tLNodeContainerSub


class SCLSub(supermod.SCL):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, Header=None, Substation=None, Communication=None, IED=None, DataTypeTemplates=None):
        super(SCLSub, self).__init__(anytypeobjs_, Text, Private, Header, Substation, Communication, IED, DataTypeTemplates, )
supermod.SCL.subclass = SCLSub
# end class SCLSub


class tConnectivityNodeSub(supermod.tConnectivityNode):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, pathName=None):
        super(tConnectivityNodeSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, pathName, )
supermod.tConnectivityNode.subclass = tConnectivityNodeSub
# end class tConnectivityNodeSub


class tPowerSystemResourceSub(supermod.tPowerSystemResource):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, extensiontype_=None):
        super(tPowerSystemResourceSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, extensiontype_, )
supermod.tPowerSystemResource.subclass = tPowerSystemResourceSub
# end class tPowerSystemResourceSub


class tSubFunctionSub(supermod.tSubFunction):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, GeneralEquipment=None):
        super(tSubFunctionSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, GeneralEquipment, )
supermod.tSubFunction.subclass = tSubFunctionSub
# end class tSubFunctionSub


class tFunctionSub(supermod.tFunction):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, SubFunction=None, GeneralEquipment=None):
        super(tFunctionSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, SubFunction, GeneralEquipment, )
supermod.tFunction.subclass = tFunctionSub
# end class tFunctionSub


class tTapChangerSub(supermod.tTapChanger):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, type_='LTC', virtual=False):
        super(tTapChangerSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, type_, virtual, )
supermod.tTapChanger.subclass = tTapChangerSub
# end class tTapChangerSub


class tSubEquipmentSub(supermod.tSubEquipment):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, phase='none', virtual=False):
        super(tSubEquipmentSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, phase, virtual, )
supermod.tSubEquipment.subclass = tSubEquipmentSub
# end class tSubEquipmentSub


class tEquipmentSub(supermod.tEquipment):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, extensiontype_=None):
        super(tEquipmentSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, extensiontype_, )
supermod.tEquipment.subclass = tEquipmentSub
# end class tEquipmentSub


class tEquipmentContainerSub(supermod.tEquipmentContainer):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, PowerTransformer=None, GeneralEquipment=None, extensiontype_=None):
        super(tEquipmentContainerSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, PowerTransformer, GeneralEquipment, extensiontype_, )
supermod.tEquipmentContainer.subclass = tEquipmentContainerSub
# end class tEquipmentContainerSub


class tBaySub(supermod.tBay):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, PowerTransformer=None, GeneralEquipment=None, ConductingEquipment=None, ConnectivityNode=None):
        super(tBaySub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, PowerTransformer, GeneralEquipment, ConductingEquipment, ConnectivityNode, )
supermod.tBay.subclass = tBaySub
# end class tBaySub


class tVoltageLevelSub(supermod.tVoltageLevel):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, PowerTransformer=None, GeneralEquipment=None, Voltage=None, Bay=None):
        super(tVoltageLevelSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, PowerTransformer, GeneralEquipment, Voltage, Bay, )
supermod.tVoltageLevel.subclass = tVoltageLevelSub
# end class tVoltageLevelSub


class tSubstationSub(supermod.tSubstation):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, PowerTransformer=None, GeneralEquipment=None, VoltageLevel=None, Function=None):
        super(tSubstationSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, PowerTransformer, GeneralEquipment, VoltageLevel, Function, )
supermod.tSubstation.subclass = tSubstationSub
# end class tSubstationSub


class tGeneralEquipmentSub(supermod.tGeneralEquipment):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, type_=None):
        super(tGeneralEquipmentSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, type_, )
supermod.tGeneralEquipment.subclass = tGeneralEquipmentSub
# end class tGeneralEquipmentSub


class tPowerTransformerSub(supermod.tPowerTransformer):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, type_='PTR', TransformerWinding=None):
        super(tPowerTransformerSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, type_, TransformerWinding, )
supermod.tPowerTransformer.subclass = tPowerTransformerSub
# end class tPowerTransformerSub


class tAbstractConductingEquipmentSub(supermod.tAbstractConductingEquipment):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, Terminal=None, SubEquipment=None, extensiontype_=None):
        super(tAbstractConductingEquipmentSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, Terminal, SubEquipment, extensiontype_, )
supermod.tAbstractConductingEquipment.subclass = tAbstractConductingEquipmentSub
# end class tAbstractConductingEquipmentSub


class tTransformerWindingSub(supermod.tTransformerWinding):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, Terminal=None, SubEquipment=None, type_='PTW', TapChanger=None):
        super(tTransformerWindingSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, Terminal, SubEquipment, type_, TapChanger, )
supermod.tTransformerWinding.subclass = tTransformerWindingSub
# end class tTransformerWindingSub


class tConductingEquipmentSub(supermod.tConductingEquipment):
    def __init__(self, anytypeobjs_=None, Text=None, Private=None, name=None, desc=None, LNode=None, virtual=False, Terminal=None, SubEquipment=None, type_=None):
        super(tConductingEquipmentSub, self).__init__(anytypeobjs_, Text, Private, name, desc, LNode, virtual, Terminal, SubEquipment, type_, )
supermod.tConductingEquipment.subclass = tConductingEquipmentSub
# end class tConductingEquipmentSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SCL'
        rootClass = supermod.SCL
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:scl="http://www.iec.ch/61850/2003/SCL"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SCL'
        rootClass = supermod.SCL
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SCL'
        rootClass = supermod.SCL
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:scl="http://www.iec.ch/61850/2003/SCL"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SCL'
        rootClass = supermod.SCL
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
