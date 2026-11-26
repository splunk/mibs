#
# PySNMP MIB module ACOS-FW-TCP-WINDOW-CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-FW-TCP-WINDOW-CHECK-MIB
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
fwTcpWindowCheckModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484))
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setOrganization('A10 Networks, Inc.')
tcpWindowCheck = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1))
tcpWindowCheckStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1), )
if mibBuilder.loadTexts: tcpWindowCheckStatsTable.setStatus('current')
tcpWindowCheckStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1), ).setIndexNames((0, "ACOS-FW-TCP-WINDOW-CHECK-MIB", "tcpWindowCheckStatsSlotId"))
if mibBuilder.loadTexts: tcpWindowCheckStatsEntry.setStatus('current')
tcpWindowCheckStatsSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpWindowCheckStatsSlotId.setStatus('current')
tcpWindowCheckStatsOutsideWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpWindowCheckStatsOutsideWindow.setStatus('current')
mibBuilder.exportSymbols("ACOS-FW-TCP-WINDOW-CHECK-MIB", tcpWindowCheckStatsSlotId=tcpWindowCheckStatsSlotId, tcpWindowCheckStatsOutsideWindow=tcpWindowCheckStatsOutsideWindow, tcpWindowCheckStatsEntry=tcpWindowCheckStatsEntry, PYSNMP_MODULE_ID=fwTcpWindowCheckModule, tcpWindowCheckStatsTable=tcpWindowCheckStatsTable, fwTcpWindowCheckModule=fwTcpWindowCheckModule, tcpWindowCheck=tcpWindowCheck)
