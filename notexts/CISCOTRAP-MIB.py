#
# PySNMP MIB module CISCOTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cisco, = mibBuilder.importSymbols("CISCO-SMI", "cisco")
ifType, ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifType", "ifIndex", "ifDescr")
locIfReason, = mibBuilder.importSymbols("OLD-CISCO-INTERFACES-MIB", "locIfReason")
whyReload, authAddr = mibBuilder.importSymbols("OLD-CISCO-SYSTEM-MIB", "whyReload", "authAddr")
loctcpConnOutBytes, loctcpConnInBytes, loctcpConnElapsed = mibBuilder.importSymbols("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes", "loctcpConnInBytes", "loctcpConnElapsed")
tslineSesType, tsLineUser = mibBuilder.importSymbols("OLD-CISCO-TS-MIB", "tslineSesType", "tsLineUser")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, snmp = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "snmp")
Counter64, TimeTicks, NotificationType, Integer32, iso, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnState, = mibBuilder.importSymbols("TCP-MIB", "tcpConnState")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4)).setObjects(("OLD-CISCO-SYSTEM-MIB", "authAddr"))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
reload = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
tcpConnectionClose = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,1)).setObjects(("OLD-CISCO-TS-MIB", "tslineSesType"), ("TCP-MIB", "tcpConnState"), ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"), ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"), ("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"), ("OLD-CISCO-TS-MIB", "tsLineUser"))
mibBuilder.exportSymbols("CISCOTRAP-MIB", reload=reload, egpNeighborLoss=egpNeighborLoss, authenticationFailure=authenticationFailure, linkDown=linkDown, linkUp=linkUp, tcpConnectionClose=tcpConnectionClose, coldStart=coldStart)
