#
# PySNMP MIB module CISCO-VIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-VIM-MIB", cvimFaultSource=cvimFaultSource, cvimMIBFaultGroup=cvimMIBFaultGroup, cvimFaultClearNotif=cvimFaultClearNotif, cvimMIBCompliance=cvimMIBCompliance, PYSNMP_MODULE_ID=ciscoVimMIB, ciscoVimMIBNotifs=ciscoVimMIBNotifs, cvimMIBNotificationGroup=cvimMIBNotificationGroup, cvimFaultCreationTime=cvimFaultCreationTime, ciscoVimMIBGroups=ciscoVimMIBGroups, ciscoVimMIBFaults=ciscoVimMIBFaults, CFaultSeverity=CFaultSeverity, ciscoVimMIB=ciscoVimMIB, cvimFaultSeverity=cvimFaultSeverity, CFaultCode=CFaultCode, cvimPodId=cvimPodId, ciscoVimMIBConform=ciscoVimMIBConform, cvimNodeId=cvimNodeId, cvimFaultDescription=cvimFaultDescription, cvimFaultCode=cvimFaultCode, ciscoVimMIBCompliances=ciscoVimMIBCompliances, cvimFaultActiveNotif=cvimFaultActiveNotif)
