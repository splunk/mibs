#
# PySNMP MIB module CISCO-VIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoVimMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 855))
ciscoVimMIB.setRevisions(('2018-07-16 00:00',))
if mibBuilder.loadTexts: ciscoVimMIB.setLastUpdated('201807160000Z')
if mibBuilder.loadTexts: ciscoVimMIB.setOrganization('Cisco Systems, Inc.')
class CFaultSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("emergency", 1), ("critical", 2), ("major", 3), ("alert", 4), ("informational", 5))

class CFaultCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("resourceUsage", 2), ("resourceThreshold", 3), ("serviceFailure", 4), ("hardwareFailure", 5), ("networkConnectivity", 6))

ciscoVimMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 0))
ciscoVimMIBFaults = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 1))
ciscoVimMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2))
cvimPodId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100)))
if mibBuilder.loadTexts: cvimPodId.setStatus('current')
cvimFaultCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 2), DateAndTime())
if mibBuilder.loadTexts: cvimFaultCreationTime.setStatus('current')
cvimNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512)))
if mibBuilder.loadTexts: cvimNodeId.setStatus('current')
cvimFaultSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 100)))
if mibBuilder.loadTexts: cvimFaultSource.setStatus('current')
cvimFaultSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 5), CFaultSeverity())
if mibBuilder.loadTexts: cvimFaultSeverity.setStatus('current')
cvimFaultCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 6), CFaultCode())
if mibBuilder.loadTexts: cvimFaultCode.setStatus('current')
cvimFaultDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048)))
if mibBuilder.loadTexts: cvimFaultDescription.setStatus('current')
cvimFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultActiveNotif.setStatus('current')
cvimFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 2)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultClearNotif.setStatus('current')
ciscoVimMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1))
ciscoVimMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2))
cvimMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1, 1)).setObjects(("CISCO-VIM-MIB", "cvimMIBFaultGroup"), ("CISCO-VIM-MIB", "cvimMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBCompliance = cvimMIBCompliance.setStatus('current')
cvimMIBFaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBFaultGroup = cvimMIBFaultGroup.setStatus('current')
cvimMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 2)).setObjects(("CISCO-VIM-MIB", "cvimFaultActiveNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBNotificationGroup = cvimMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIM-MIB", cvimMIBCompliance=cvimMIBCompliance, CFaultCode=CFaultCode, CFaultSeverity=CFaultSeverity, cvimFaultActiveNotif=cvimFaultActiveNotif, cvimFaultCode=cvimFaultCode, ciscoVimMIBConform=ciscoVimMIBConform, cvimNodeId=cvimNodeId, ciscoVimMIBNotifs=ciscoVimMIBNotifs, cvimFaultSource=cvimFaultSource, cvimFaultClearNotif=cvimFaultClearNotif, cvimPodId=cvimPodId, PYSNMP_MODULE_ID=ciscoVimMIB, cvimMIBNotificationGroup=cvimMIBNotificationGroup, cvimFaultCreationTime=cvimFaultCreationTime, ciscoVimMIBFaults=ciscoVimMIBFaults, cvimFaultSeverity=cvimFaultSeverity, ciscoVimMIB=ciscoVimMIB, cvimFaultDescription=cvimFaultDescription, ciscoVimMIBCompliances=ciscoVimMIBCompliances, ciscoVimMIBGroups=ciscoVimMIBGroups, cvimMIBFaultGroup=cvimMIBFaultGroup)
