#
# PySNMP MIB module ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, Bits, iso, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "IpAddress", "NotificationType")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
cgnv6SharedServiceGroupModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412))
if mibBuilder.loadTexts: cgnv6SharedServiceGroupModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: cgnv6SharedServiceGroupModule.setOrganization('A10 Networks, Inc.')
sharedServiceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1))
sharedServiceGroupOperSharedServiceGroupListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2), )
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListTable.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1), ).setIndexNames((0, "ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", "sharedServiceGroupOperSharedServiceGroupListSlotId"), (0, "ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", "sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId"))
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListEntry.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListSlotId.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListServiceGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListServiceGroupName.setStatus('current')
mibBuilder.exportSymbols("ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", PYSNMP_MODULE_ID=cgnv6SharedServiceGroupModule, sharedServiceGroupOperSharedServiceGroupListServiceGroupName=sharedServiceGroupOperSharedServiceGroupListServiceGroupName, sharedServiceGroupOperSharedServiceGroupListSlotId=sharedServiceGroupOperSharedServiceGroupListSlotId, sharedServiceGroup=sharedServiceGroup, sharedServiceGroupOperSharedServiceGroupListTable=sharedServiceGroupOperSharedServiceGroupListTable, cgnv6SharedServiceGroupModule=cgnv6SharedServiceGroupModule, sharedServiceGroupOperSharedServiceGroupListEntry=sharedServiceGroupOperSharedServiceGroupListEntry, sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId=sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId)
