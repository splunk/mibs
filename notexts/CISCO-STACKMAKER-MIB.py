#
# PySNMP MIB module CISCO-STACKMAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-STACKMAKER-MIB
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
mibBuilder.exportSymbols("CISCO-STACKMAKER-MIB", csmStackIpAddress=csmStackIpAddress, ciscoStackMakerMIB=ciscoStackMakerMIB, ciscoStackMakerBasicGroup=ciscoStackMakerBasicGroup, ciscoStackMakerMIBGroups=ciscoStackMakerMIBGroups, ciscoStackMakerMIBCompliance=ciscoStackMakerMIBCompliance, csmStackTable=csmStackTable, ciscoStackMakerMIBCompliances=ciscoStackMakerMIBCompliances, ciscoStackMakerMIBObjects=ciscoStackMakerMIBObjects, csmStackEntry=csmStackEntry, csmStackIndex=csmStackIndex, csmClearStackTable=csmClearStackTable, csmStackName=csmStackName, ciscoStackMakerConf=ciscoStackMakerConf, ciscoStackMakerMIBConformance=ciscoStackMakerMIBConformance, PYSNMP_MODULE_ID=ciscoStackMakerMIB)
