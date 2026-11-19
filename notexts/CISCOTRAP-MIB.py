#
# PySNMP MIB module CISCOTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cisco, = mibBuilder.importSymbols("CISCO-SMI", "cisco")
ifType, ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifType", "ifIndex", "ifDescr")
locIfReason, = mibBuilder.importSymbols("OLD-CISCO-INTERFACES-MIB", "locIfReason")
whyReload, authAddr = mibBuilder.importSymbols("OLD-CISCO-SYSTEM-MIB", "whyReload", "authAddr")
loctcpConnInBytes, loctcpConnOutBytes, loctcpConnElapsed = mibBuilder.importSymbols("OLD-CISCO-TCP-MIB", "loctcpConnInBytes", "loctcpConnOutBytes", "loctcpConnElapsed")
tslineSesType, tsLineUser = mibBuilder.importSymbols("OLD-CISCO-TS-MIB", "tslineSesType", "tsLineUser")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, snmp = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "snmp")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnState, = mibBuilder.importSymbols("TCP-MIB", "tcpConnState")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4)).setObjects(("OLD-CISCO-SYSTEM-MIB", "authAddr"))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
reload = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
tcpConnectionClose = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,1)).setObjects(("OLD-CISCO-TS-MIB", "tslineSesType"), ("TCP-MIB", "tcpConnState"), ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"), ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"), ("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"), ("OLD-CISCO-TS-MIB", "tsLineUser"))
mibBuilder.exportSymbols("CISCOTRAP-MIB", tcpConnectionClose=tcpConnectionClose, coldStart=coldStart, authenticationFailure=authenticationFailure, linkDown=linkDown, reload=reload, linkUp=linkUp, egpNeighborLoss=egpNeighborLoss)
