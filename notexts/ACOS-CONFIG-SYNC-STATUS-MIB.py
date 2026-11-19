#
# PySNMP MIB module ACOS-CONFIG-SYNC-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-CONFIG-SYNC-STATUS-MIB
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
mibBuilder.exportSymbols("ACOS-CONFIG-SYNC-STATUS-MIB", configSyncStatusOperConfigSyncListStartupSyncStatus=configSyncStatusOperConfigSyncListStartupSyncStatus, configSyncStatusModule=configSyncStatusModule, PYSNMP_MODULE_ID=configSyncStatusModule, configSyncStatusOperConfigSyncListEntry=configSyncStatusOperConfigSyncListEntry, configSyncStatusOperConfigSyncListTable=configSyncStatusOperConfigSyncListTable, configSyncStatusOperConfigSyncListPartitionName=configSyncStatusOperConfigSyncListPartitionName, configSyncStatus=configSyncStatus, configSyncStatusOperConfigSyncListSlotId=configSyncStatusOperConfigSyncListSlotId, configSyncStatusOperConfigSyncListRunSyncStatus=configSyncStatusOperConfigSyncListRunSyncStatus, configSyncStatusOperConfigSyncListConfigSyncListListId=configSyncStatusOperConfigSyncListConfigSyncListListId)
