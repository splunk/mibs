#
# PySNMP MIB module ACOS-GSLB-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-GSLB-STATISTICS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:33 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, Bits, IpAddress, MibIdentifier, Counter64, NotificationType, Integer32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Integer32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
gslbStatisticsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422))
if mibBuilder.loadTexts: gslbStatisticsModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: gslbStatisticsModule.setOrganization('A10 Networks, Inc.')
if mibBuilder.loadTexts: gslbStatisticsModule.setContactInfo('Address: A10 Networks, Inc.\n\t\t\t\t\t\t\t  2300 Orchard Parkway\n\t\t\t\t\t\t\t  San Jose, CA 95131\n\t\t\t\t\t\t Phone:   +1-888-822-7210 (USA/Canada)\n\t\t\t\t\t\t          +1-408-325-8676 (International)\n\t\t\t\t\t\t E-mail:  support@A10Networks.com')
if mibBuilder.loadTexts: gslbStatisticsModule.setDescription('gslbStatisticsModule OID for ACOS')
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1))
statisticsOperTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2), )
if mibBuilder.loadTexts: statisticsOperTable.setStatus('current')
if mibBuilder.loadTexts: statisticsOperTable.setDescription("GSLB Global stats from object 'gslb.statistics'")
statisticsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1), ).setIndexNames((0, "ACOS-GSLB-STATISTICS-MIB", "statisticsOperSlotId"))
if mibBuilder.loadTexts: statisticsOperEntry.setStatus('current')
if mibBuilder.loadTexts: statisticsOperEntry.setDescription('The statisticsOper entry')
statisticsOperSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperSlotId.setStatus('current')
if mibBuilder.loadTexts: statisticsOperSlotId.setDescription('')
statisticsOperCurrSslCtx = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperCurrSslCtx.setStatus('current')
if mibBuilder.loadTexts: statisticsOperCurrSslCtx.setDescription('curr-ssl-ctx')
mibBuilder.exportSymbols("ACOS-GSLB-STATISTICS-MIB", statisticsOperEntry=statisticsOperEntry, statistics=statistics, statisticsOperTable=statisticsOperTable, statisticsOperCurrSslCtx=statisticsOperCurrSslCtx, PYSNMP_MODULE_ID=gslbStatisticsModule, statisticsOperSlotId=statisticsOperSlotId, gslbStatisticsModule=gslbStatisticsModule)
