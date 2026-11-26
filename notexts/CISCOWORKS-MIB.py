#
# PySNMP MIB module CISCOWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOWORKS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoworks, = mibBuilder.importSymbols("CISCO-SMI", "ciscoworks")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 14, 1))
cwLogMIB.setRevisions(('2003-02-18 00:00', '1995-04-02 00:00',))
if mibBuilder.loadTexts: cwLogMIB.setLastUpdated('200302180000Z')
if mibBuilder.loadTexts: cwLogMIB.setOrganization('Cisco Systems, Inc.')
cwLog = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 1))
cwTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2))
cwMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3))
cwLogDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(15, 15)).setFixedLength(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogDate.setStatus('current')
cwLogSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ciscoworks", 2), ("device", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogSource.setStatus('current')
cwLogApp = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogApp.setStatus('current')
cwLogMsg = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogMsg.setStatus('current')
cwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0))
cwAppLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwAppLogTrap.setStatus('current')
cwDevLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwDevLogTrap.setStatus('current')
ciscoCwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1))
ciscoCwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2))
ciscoCwMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1, 1)).setObjects(("CISCOWORKS-MIB", "ciscoCwObjectsGroup"), ("CISCOWORKS-MIB", "ciscoCwNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwMIBCompliance = ciscoCwMIBCompliance.setStatus('current')
ciscoCwObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 7)).setObjects(("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwObjectsGroup = ciscoCwObjectsGroup.setStatus('current')
ciscoCwNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 12)).setObjects(("CISCOWORKS-MIB", "cwAppLogTrap"), ("CISCOWORKS-MIB", "cwDevLogTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwNotificationsGroup = ciscoCwNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCOWORKS-MIB", cwLogMIB=cwLogMIB, cwLogApp=cwLogApp, cwTraps=cwTraps, ciscoCwMIBCompliance=ciscoCwMIBCompliance, PYSNMP_MODULE_ID=cwLogMIB, ciscoCwMIBCompliances=ciscoCwMIBCompliances, cwLogMsg=cwLogMsg, cwTrapsPrefix=cwTrapsPrefix, cwAppLogTrap=cwAppLogTrap, ciscoCwMIBGroups=ciscoCwMIBGroups, cwLogSource=cwLogSource, cwMIBConform=cwMIBConform, cwDevLogTrap=cwDevLogTrap, ciscoCwObjectsGroup=ciscoCwObjectsGroup, cwLog=cwLog, cwLogDate=cwLogDate, ciscoCwNotificationsGroup=ciscoCwNotificationsGroup)
