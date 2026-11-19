#
# PySNMP MIB module ACOS-FW-TCP-WINDOW-CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-FW-TCP-WINDOW-CHECK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:09 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Counter64, NotificationType, TimeTicks, Bits, Unsigned32, MibIdentifier, Integer32, Counter32, ObjectIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "NotificationType", "TimeTicks", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
fwTcpWindowCheckModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484))
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setOrganization('A10 Networks, Inc.')
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setContactInfo('Address: A10 Networks, Inc.\n\t\t\t\t\t\t\t  2300 Orchard Parkway\n\t\t\t\t\t\t\t  San Jose, CA 95131\n\t\t\t\t\t\t Phone:   +1-888-822-7210 (USA/Canada)\n\t\t\t\t\t\t          +1-408-325-8676 (International)\n\t\t\t\t\t\t E-mail:  support@A10Networks.com')
if mibBuilder.loadTexts: fwTcpWindowCheckModule.setDescription('fwTcpWindowCheckModule OID for ACOS')
tcpWindowCheck = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1))
tcpWindowCheckStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1), )
if mibBuilder.loadTexts: tcpWindowCheckStatsTable.setStatus('current')
if mibBuilder.loadTexts: tcpWindowCheckStatsTable.setDescription("Configure TCP window check from object 'fw.tcp-window-check'")
tcpWindowCheckStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1), ).setIndexNames((0, "ACOS-FW-TCP-WINDOW-CHECK-MIB", "tcpWindowCheckStatsSlotId"))
if mibBuilder.loadTexts: tcpWindowCheckStatsEntry.setStatus('current')
if mibBuilder.loadTexts: tcpWindowCheckStatsEntry.setDescription('The tcpWindowCheckStats stats entry')
tcpWindowCheckStatsSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpWindowCheckStatsSlotId.setStatus('current')
if mibBuilder.loadTexts: tcpWindowCheckStatsSlotId.setDescription('')
tcpWindowCheckStatsOutsideWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 484, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpWindowCheckStatsOutsideWindow.setStatus('current')
if mibBuilder.loadTexts: tcpWindowCheckStatsOutsideWindow.setDescription('outside-window')
mibBuilder.exportSymbols("ACOS-FW-TCP-WINDOW-CHECK-MIB", fwTcpWindowCheckModule=fwTcpWindowCheckModule, tcpWindowCheck=tcpWindowCheck, tcpWindowCheckStatsTable=tcpWindowCheckStatsTable, tcpWindowCheckStatsOutsideWindow=tcpWindowCheckStatsOutsideWindow, tcpWindowCheckStatsSlotId=tcpWindowCheckStatsSlotId, PYSNMP_MODULE_ID=fwTcpWindowCheckModule, tcpWindowCheckStatsEntry=tcpWindowCheckStatsEntry)
