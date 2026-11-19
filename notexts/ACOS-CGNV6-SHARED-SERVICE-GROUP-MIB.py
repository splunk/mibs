#
# PySNMP MIB module ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:03 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Integer32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", cgnv6SharedServiceGroupModule=cgnv6SharedServiceGroupModule, sharedServiceGroup=sharedServiceGroup, sharedServiceGroupOperSharedServiceGroupListTable=sharedServiceGroupOperSharedServiceGroupListTable, sharedServiceGroupOperSharedServiceGroupListEntry=sharedServiceGroupOperSharedServiceGroupListEntry, PYSNMP_MODULE_ID=cgnv6SharedServiceGroupModule, sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId=sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId, sharedServiceGroupOperSharedServiceGroupListSlotId=sharedServiceGroupOperSharedServiceGroupListSlotId, sharedServiceGroupOperSharedServiceGroupListServiceGroupName=sharedServiceGroupOperSharedServiceGroupListServiceGroupName)
