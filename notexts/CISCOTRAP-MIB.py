#
# PySNMP MIB module CISCOTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cisco, = mibBuilder.importSymbols("CISCO-SMI", "cisco")
ifDescr, ifType, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifType", "ifIndex")
locIfReason, = mibBuilder.importSymbols("OLD-CISCO-INTERFACES-MIB", "locIfReason")
whyReload, authAddr = mibBuilder.importSymbols("OLD-CISCO-SYSTEM-MIB", "whyReload", "authAddr")
loctcpConnElapsed, loctcpConnInBytes, loctcpConnOutBytes = mibBuilder.importSymbols("OLD-CISCO-TCP-MIB", "loctcpConnElapsed", "loctcpConnInBytes", "loctcpConnOutBytes")
tsLineUser, tslineSesType = mibBuilder.importSymbols("OLD-CISCO-TS-MIB", "tsLineUser", "tslineSesType")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmp, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "snmp", "sysUpTime")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, NotificationType, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "NotificationType", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnState, = mibBuilder.importSymbols("TCP-MIB", "tcpConnState")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4)).setObjects(("OLD-CISCO-SYSTEM-MIB", "authAddr"))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
reload = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
tcpConnectionClose = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,1)).setObjects(("OLD-CISCO-TS-MIB", "tslineSesType"), ("TCP-MIB", "tcpConnState"), ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"), ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"), ("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"), ("OLD-CISCO-TS-MIB", "tsLineUser"))
mibBuilder.exportSymbols("CISCOTRAP-MIB", coldStart=coldStart, linkUp=linkUp, authenticationFailure=authenticationFailure, reload=reload, tcpConnectionClose=tcpConnectionClose, egpNeighborLoss=egpNeighborLoss, linkDown=linkDown)
