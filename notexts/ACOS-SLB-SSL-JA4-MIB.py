#
# PySNMP MIB module ACOS-SLB-SSL-JA4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-SLB-SSL-JA4-MIB
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
slbSslJa4Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315))
if mibBuilder.loadTexts: slbSslJa4Module.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: slbSslJa4Module.setOrganization('A10 Networks, Inc.')
sslJa4 = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1))
sslJa4OperRecordTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2), )
if mibBuilder.loadTexts: sslJa4OperRecordTable.setStatus('current')
sslJa4OperRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1), ).setIndexNames((0, "ACOS-SLB-SSL-JA4-MIB", "sslJa4OperRecordSlotId"), (0, "ACOS-SLB-SSL-JA4-MIB", "sslJa4OperRecordRecordListId"))
if mibBuilder.loadTexts: sslJa4OperRecordEntry.setStatus('current')
sslJa4OperRecordSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslJa4OperRecordSlotId.setStatus('current')
sslJa4OperRecordRecordListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslJa4OperRecordRecordListId.setStatus('current')
sslJa4OperRecordAddrV4 = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslJa4OperRecordAddrV4.setStatus('current')
sslJa4OperRecordAddrV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslJa4OperRecordAddrV6.setStatus('current')
sslJa4OperRecordAmount = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 315, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslJa4OperRecordAmount.setStatus('current')
mibBuilder.exportSymbols("ACOS-SLB-SSL-JA4-MIB", sslJa4OperRecordAddrV6=sslJa4OperRecordAddrV6, slbSslJa4Module=slbSslJa4Module, sslJa4OperRecordAddrV4=sslJa4OperRecordAddrV4, sslJa4OperRecordSlotId=sslJa4OperRecordSlotId, sslJa4=sslJa4, PYSNMP_MODULE_ID=slbSslJa4Module, sslJa4OperRecordAmount=sslJa4OperRecordAmount, sslJa4OperRecordTable=sslJa4OperRecordTable, sslJa4OperRecordEntry=sslJa4OperRecordEntry, sslJa4OperRecordRecordListId=sslJa4OperRecordRecordListId)
