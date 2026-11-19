#
# PySNMP MIB module ACOS-GSLB-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-GSLB-STATISTICS-MIB
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
gslbStatisticsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422))
if mibBuilder.loadTexts: gslbStatisticsModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: gslbStatisticsModule.setOrganization('A10 Networks, Inc.')
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1))
statisticsOperTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2), )
if mibBuilder.loadTexts: statisticsOperTable.setStatus('current')
statisticsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1), ).setIndexNames((0, "ACOS-GSLB-STATISTICS-MIB", "statisticsOperSlotId"))
if mibBuilder.loadTexts: statisticsOperEntry.setStatus('current')
statisticsOperSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperSlotId.setStatus('current')
statisticsOperCurrSslCtx = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperCurrSslCtx.setStatus('current')
mibBuilder.exportSymbols("ACOS-GSLB-STATISTICS-MIB", statisticsOperCurrSslCtx=statisticsOperCurrSslCtx, PYSNMP_MODULE_ID=gslbStatisticsModule, statistics=statistics, statisticsOperSlotId=statisticsOperSlotId, statisticsOperTable=statisticsOperTable, statisticsOperEntry=statisticsOperEntry, gslbStatisticsModule=gslbStatisticsModule)
