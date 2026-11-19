#
# PySNMP MIB module ACOS-FW-TCP-WINDOW-CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-FW-TCP-WINDOW-CHECK-MIB
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
mibBuilder.exportSymbols("ACOS-FW-TCP-WINDOW-CHECK-MIB", fwTcpWindowCheckModule=fwTcpWindowCheckModule, tcpWindowCheck=tcpWindowCheck, tcpWindowCheckStatsSlotId=tcpWindowCheckStatsSlotId, tcpWindowCheckStatsTable=tcpWindowCheckStatsTable, tcpWindowCheckStatsOutsideWindow=tcpWindowCheckStatsOutsideWindow, PYSNMP_MODULE_ID=fwTcpWindowCheckModule, tcpWindowCheckStatsEntry=tcpWindowCheckStatsEntry)
