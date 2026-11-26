#
# PySNMP MIB module ACOS-CONFIG-SYNC-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-CONFIG-SYNC-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:31 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, NotificationType, Counter64, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "IpAddress")
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
mibBuilder.exportSymbols("ACOS-CONFIG-SYNC-STATUS-MIB", configSyncStatusOperConfigSyncListEntry=configSyncStatusOperConfigSyncListEntry, configSyncStatusOperConfigSyncListRunSyncStatus=configSyncStatusOperConfigSyncListRunSyncStatus, configSyncStatusOperConfigSyncListConfigSyncListListId=configSyncStatusOperConfigSyncListConfigSyncListListId, PYSNMP_MODULE_ID=configSyncStatusModule, configSyncStatus=configSyncStatus, configSyncStatusModule=configSyncStatusModule, configSyncStatusOperConfigSyncListTable=configSyncStatusOperConfigSyncListTable, configSyncStatusOperConfigSyncListSlotId=configSyncStatusOperConfigSyncListSlotId, configSyncStatusOperConfigSyncListStartupSyncStatus=configSyncStatusOperConfigSyncListStartupSyncStatus, configSyncStatusOperConfigSyncListPartitionName=configSyncStatusOperConfigSyncListPartitionName)
