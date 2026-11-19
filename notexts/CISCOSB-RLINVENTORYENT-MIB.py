#
# PySNMP MIB module CISCOSB-RLINVENTORYENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-RLINVENTORYENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class UnitIfindexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1), ).setIndexNames((0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitOrIfindex"), (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-RLINVENTORYENT-MIB", rlInventoryEntName=rlInventoryEntName, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber, rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, UnitIfindexType=UnitIfindexType, rlInventoryEntEntry=rlInventoryEntEntry, rlInventoryEntPID=rlInventoryEntPID)
