#
# PySNMP MIB module OLD-CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/OLD-CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnRemPort, tcpConnLocalPort, tcpConnRemAddress, tcpConnLocalAddress = mibBuilder.importSymbols("TCP-MIB", "tcpConnRemPort", "tcpConnLocalPort", "tcpConnRemAddress", "tcpConnLocalAddress")
ltcp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 6))
ltcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 6, 1), )
if mibBuilder.loadTexts: ltcpConnTable.setStatus('deprecated')
ltcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: ltcpConnEntry.setStatus('deprecated')
loctcpConnInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnInBytes.setStatus('deprecated')
loctcpConnOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnOutBytes.setStatus('deprecated')
loctcpConnInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnInPkts.setStatus('deprecated')
loctcpConnOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnOutPkts.setStatus('deprecated')
loctcpConnElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnElapsed.setStatus('deprecated')
mibBuilder.exportSymbols("OLD-CISCO-TCP-MIB", loctcpConnInBytes=loctcpConnInBytes, loctcpConnOutPkts=loctcpConnOutPkts, ltcpConnTable=ltcpConnTable, loctcpConnInPkts=loctcpConnInPkts, loctcpConnOutBytes=loctcpConnOutBytes, loctcpConnElapsed=loctcpConnElapsed, ltcp=ltcp, ltcpConnEntry=ltcpConnEntry)
