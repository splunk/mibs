#
# PySNMP MIB module BASIS-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/BASIS-SERIAL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
basisLines, = mibBuilder.importSymbols("BASIS-MIB", "basisLines")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 69))
basisSerialMIB.setRevisions(('2003-05-03 00:00',))
if mibBuilder.loadTexts: basisSerialMIB.setLastUpdated('200305030000Z')
if mibBuilder.loadTexts: basisSerialMIB.setOrganization('Cisco Systems, Inc.')
serialInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 1))
serialPortNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNumOfValidEntries.setStatus('current')
serialInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1), )
if mibBuilder.loadTexts: serialInterfaceTable.setStatus('current')
serialInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1), ).setIndexNames((0, "BASIS-SERIAL-MIB", "serialPortNum"))
if mibBuilder.loadTexts: serialInterfaceEntry.setStatus('current')
serialPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNum.setStatus('current')
serialPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("main", 1), ("debug", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortType.setStatus('current')
serialPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortEnable.setStatus('current')
serialPortbps = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bps9600", 1), ("bps2400", 2), ("bps19200", 3))).clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortbps.setStatus('current')
basisSerialMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2))
basisSerialMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1))
basisSerialMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2))
basisSerialCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2, 1)).setObjects(("BASIS-SERIAL-MIB", "basisSerialConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialCompliance = basisSerialCompliance.setStatus('current')
basisSerialConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1, 1)).setObjects(("BASIS-SERIAL-MIB", "serialPortNumOfValidEntries"), ("BASIS-SERIAL-MIB", "serialPortNum"), ("BASIS-SERIAL-MIB", "serialPortType"), ("BASIS-SERIAL-MIB", "serialPortEnable"), ("BASIS-SERIAL-MIB", "serialPortbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialConfGroup = basisSerialConfGroup.setStatus('current')
mibBuilder.exportSymbols("BASIS-SERIAL-MIB", serialInterfaceTable=serialInterfaceTable, basisSerialConfGroup=basisSerialConfGroup, serialPortNum=serialPortNum, basisSerialCompliance=basisSerialCompliance, serialInterface=serialInterface, serialPortEnable=serialPortEnable, serialPortbps=serialPortbps, serialPortType=serialPortType, PYSNMP_MODULE_ID=basisSerialMIB, basisSerialMIB=basisSerialMIB, serialPortNumOfValidEntries=serialPortNumOfValidEntries, serialInterfaceEntry=serialInterfaceEntry, basisSerialMIBGroups=basisSerialMIBGroups, basisSerialMIBCompliances=basisSerialMIBCompliances, basisSerialMIBConformance=basisSerialMIBConformance)
