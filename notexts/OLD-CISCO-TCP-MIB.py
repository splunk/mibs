#
# PySNMP MIB module OLD-CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/OLD-CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnLocalPort, tcpConnLocalAddress, tcpConnRemPort, tcpConnRemAddress = mibBuilder.importSymbols("TCP-MIB", "tcpConnLocalPort", "tcpConnLocalAddress", "tcpConnRemPort", "tcpConnRemAddress")
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
mibBuilder.exportSymbols("OLD-CISCO-TCP-MIB", ltcpConnTable=ltcpConnTable, loctcpConnInBytes=loctcpConnInBytes, ltcp=ltcp, loctcpConnInPkts=loctcpConnInPkts, loctcpConnOutPkts=loctcpConnOutPkts, loctcpConnElapsed=loctcpConnElapsed, ltcpConnEntry=ltcpConnEntry, loctcpConnOutBytes=loctcpConnOutBytes)
