#
# PySNMP MIB module CISCOSB-RLINVENTORYENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-RLINVENTORYENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class UnitIfindexType(TextualConvention, Integer32):
    description = 'Unit or ifindex type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntTable.setDescription('A table that contains INVENTORY entities in the system.')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1), ).setIndexNames((0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitOrIfindex"), (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntEntry.setDescription('An entry (conceptual row) in the  rlInventoryEnvTable.')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setDescription('this field will be equal to zero if this is a unit else 1 if this is a port.')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setDescription('if rlInventoryEntUnitOrIfindex = 0 this field contain the unit number else if  rlInventoryEntUnitOrIfindex = 1\nThis field contain the if_index number.')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntVendorID.setDescription('Vendor identification')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntPID.setDescription('Physical identification')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntName.setDescription('Unit number of interface name')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntDescription.setDescription('Description of the entity')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setDescription('The serial number of the interface or unit.')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setDescription('if rlInventoryEntUnitOrIfindex = 1 this field contain the unit number that associated to this port')
mibBuilder.exportSymbols("CISCOSB-RLINVENTORYENT-MIB", UnitIfindexType=UnitIfindexType, rlInventoryEntPID=rlInventoryEntPID, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntName=rlInventoryEntName, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex, rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntEntry=rlInventoryEntEntry)
