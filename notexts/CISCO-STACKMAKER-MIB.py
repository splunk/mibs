#
# PySNMP MIB module CISCO-STACKMAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-STACKMAKER-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, IpAddress, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, NotificationType, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoStackMakerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 59))
if mibBuilder.loadTexts: ciscoStackMakerMIB.setLastUpdated('9610311200Z')
if mibBuilder.loadTexts: ciscoStackMakerMIB.setOrganization('Cisco Systems, Inc.')
ciscoStackMakerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 1))
ciscoStackMakerConf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1))
csmStackName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csmStackName.setStatus('current')
csmClearStackTable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearTable", 1), ("noClearTable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csmClearStackTable.setStatus('current')
csmStackTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3), )
if mibBuilder.loadTexts: csmStackTable.setStatus('current')
csmStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-STACKMAKER-MIB", "csmStackIndex"))
if mibBuilder.loadTexts: csmStackEntry.setStatus('current')
csmStackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: csmStackIndex.setStatus('current')
csmStackIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csmStackIpAddress.setStatus('current')
ciscoStackMakerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3))
ciscoStackMakerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1))
ciscoStackMakerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2))
ciscoStackMakerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1, 1)).setObjects(("CISCO-STACKMAKER-MIB", "ciscoStackMakerBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackMakerMIBCompliance = ciscoStackMakerMIBCompliance.setStatus('current')
ciscoStackMakerBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2, 1)).setObjects(("CISCO-STACKMAKER-MIB", "csmStackName"), ("CISCO-STACKMAKER-MIB", "csmClearStackTable"), ("CISCO-STACKMAKER-MIB", "csmStackIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackMakerBasicGroup = ciscoStackMakerBasicGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-STACKMAKER-MIB", ciscoStackMakerMIBGroups=ciscoStackMakerMIBGroups, ciscoStackMakerMIBConformance=ciscoStackMakerMIBConformance, csmStackTable=csmStackTable, csmStackEntry=csmStackEntry, csmClearStackTable=csmClearStackTable, ciscoStackMakerMIB=ciscoStackMakerMIB, csmStackIpAddress=csmStackIpAddress, ciscoStackMakerBasicGroup=ciscoStackMakerBasicGroup, ciscoStackMakerMIBCompliance=ciscoStackMakerMIBCompliance, PYSNMP_MODULE_ID=ciscoStackMakerMIB, ciscoStackMakerConf=ciscoStackMakerConf, ciscoStackMakerMIBCompliances=ciscoStackMakerMIBCompliances, csmStackIndex=csmStackIndex, csmStackName=csmStackName, ciscoStackMakerMIBObjects=ciscoStackMakerMIBObjects)
