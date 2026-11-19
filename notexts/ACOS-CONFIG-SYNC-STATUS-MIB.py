#
# PySNMP MIB module ACOS-CONFIG-SYNC-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-CONFIG-SYNC-STATUS-MIB
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
configSyncStatusModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170))
if mibBuilder.loadTexts: configSyncStatusModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: configSyncStatusModule.setOrganization('A10 Networks, Inc.')
configSyncStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1))
configSyncStatusOperConfigSyncListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2), )
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListTable.setStatus('current')
configSyncStatusOperConfigSyncListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1), ).setIndexNames((0, "ACOS-CONFIG-SYNC-STATUS-MIB", "configSyncStatusOperConfigSyncListSlotId"), (0, "ACOS-CONFIG-SYNC-STATUS-MIB", "configSyncStatusOperConfigSyncListConfigSyncListListId"))
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListEntry.setStatus('current')
configSyncStatusOperConfigSyncListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListSlotId.setStatus('current')
configSyncStatusOperConfigSyncListConfigSyncListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListConfigSyncListListId.setStatus('current')
configSyncStatusOperConfigSyncListPartitionName = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListPartitionName.setStatus('current')
configSyncStatusOperConfigSyncListRunSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListRunSyncStatus.setStatus('current')
configSyncStatusOperConfigSyncListStartupSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 170, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configSyncStatusOperConfigSyncListStartupSyncStatus.setStatus('current')
mibBuilder.exportSymbols("ACOS-CONFIG-SYNC-STATUS-MIB", configSyncStatusOperConfigSyncListConfigSyncListListId=configSyncStatusOperConfigSyncListConfigSyncListListId, configSyncStatus=configSyncStatus, configSyncStatusModule=configSyncStatusModule, configSyncStatusOperConfigSyncListPartitionName=configSyncStatusOperConfigSyncListPartitionName, configSyncStatusOperConfigSyncListStartupSyncStatus=configSyncStatusOperConfigSyncListStartupSyncStatus, configSyncStatusOperConfigSyncListRunSyncStatus=configSyncStatusOperConfigSyncListRunSyncStatus, configSyncStatusOperConfigSyncListTable=configSyncStatusOperConfigSyncListTable, PYSNMP_MODULE_ID=configSyncStatusModule, configSyncStatusOperConfigSyncListEntry=configSyncStatusOperConfigSyncListEntry, configSyncStatusOperConfigSyncListSlotId=configSyncStatusOperConfigSyncListSlotId)
