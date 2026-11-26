#
# PySNMP MIB module CISCO-VOICE-URI-CLASS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-URI-CLASS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVoiceUriClassMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 99999999))
ciscoVoiceUriClassMIB.setRevisions(('2002-10-10 00:00',))
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setLastUpdated('200210100000Z')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setOrganization('Cisco Systems, Inc.')
class CvUriClassTagIndex(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CvUriClassTag(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPreference(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

cvUriClassMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0))
cvUriClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1))
cvUriClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1))
cvUriClassSIPGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2))
cvUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1), )
if mibBuilder.loadTexts: cvUriClassCfgTable.setStatus('current')
cvUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvUriClassCfgEntry.setStatus('current')
cvUriClassCfgTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1), CvUriClassTagIndex())
if mibBuilder.loadTexts: cvUriClassCfgTag.setStatus('current')
cvUriClassCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sip", 1), ("tel", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgType.setStatus('current')
cvUriClassCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgStatus.setStatus('current')
cvSIPUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2), )
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setStatus('current')
cvSIPUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setStatus('current')
cvSIPUriClassCfgUserIDPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setStatus('current')
cvSIPUriClassCfgHostPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setStatus('current')
cvSIPUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setStatus('current')
cvTELUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3), )
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setStatus('current')
cvTELUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setStatus('current')
cvTELUriClassCfgPhoneNumPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setStatus('current')
cvTELUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setStatus('current')
cvCommonUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4), )
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setStatus('current')
cvCommonUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setStatus('current')
cvCommonUriClassCfgURIPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setStatus('current')
cvUriClassSIPHostPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1), CvUriClassPreference().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setStatus('current')
cvUriClassSIPUserIDPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2), CvUriClassPreference().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setStatus('current')
cvUriClassMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2))
cvUriClassMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1))
cvUriClassMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2))
cvUriClassMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassMIBCompliance = cvUriClassMIBCompliance.setStatus('current')
cvUriClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassGroup = cvUriClassGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-URI-CLASS-MIB", cvUriClassSIPUserIDPreference=cvUriClassSIPUserIDPreference, ciscoVoiceUriClassMIB=ciscoVoiceUriClassMIB, cvUriClassMIBGroups=cvUriClassMIBGroups, cvSIPUriClassCfgTable=cvSIPUriClassCfgTable, CvUriClassTag=CvUriClassTag, cvCommonUriClassCfgURIPattern=cvCommonUriClassCfgURIPattern, cvTELUriClassCfgTable=cvTELUriClassCfgTable, cvSIPUriClassCfgEntry=cvSIPUriClassCfgEntry, cvUriClass=cvUriClass, cvTELUriClassCfgPhoneCtxtPattern=cvTELUriClassCfgPhoneCtxtPattern, cvUriClassSIPHostPreference=cvUriClassSIPHostPreference, cvSIPUriClassCfgPhoneCtxtPattern=cvSIPUriClassCfgPhoneCtxtPattern, cvUriClassMIBConformance=cvUriClassMIBConformance, cvUriClassGroup=cvUriClassGroup, cvUriClassCfgTable=cvUriClassCfgTable, cvCommonUriClassCfgEntry=cvCommonUriClassCfgEntry, cvTELUriClassCfgPhoneNumPattern=cvTELUriClassCfgPhoneNumPattern, cvTELUriClassCfgEntry=cvTELUriClassCfgEntry, cvUriClassCfgTag=cvUriClassCfgTag, CvUriClassPreference=CvUriClassPreference, cvUriClassCfgEntry=cvUriClassCfgEntry, cvSIPUriClassCfgHostPattern=cvSIPUriClassCfgHostPattern, cvUriClassMIBCompliance=cvUriClassMIBCompliance, cvUriClassCfgStatus=cvUriClassCfgStatus, cvUriClassMIBObjects=cvUriClassMIBObjects, cvUriClassCfgType=cvUriClassCfgType, CvUriClassTagIndex=CvUriClassTagIndex, cvCommonUriClassCfgTable=cvCommonUriClassCfgTable, CvUriClassPattern=CvUriClassPattern, PYSNMP_MODULE_ID=ciscoVoiceUriClassMIB, cvSIPUriClassCfgUserIDPattern=cvSIPUriClassCfgUserIDPattern, cvUriClassMIBNotifications=cvUriClassMIBNotifications, cvUriClassMIBCompliances=cvUriClassMIBCompliances, cvUriClassSIPGeneralConfig=cvUriClassSIPGeneralConfig)
