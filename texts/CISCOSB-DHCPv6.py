#
# PySNMP MIB module CISCOSB-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-DHCPv6
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, IpAddress, Counter32, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "Counter32", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
RowStatus, DisplayString, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention", "MacAddress")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlDhcpv6.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDhcpv6.setDescription('The private MIB module definition for DHCP v6 features.')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setDescription('')
mibBuilder.exportSymbols("CISCOSB-DHCPv6", rlDhcpv6=rlDhcpv6, rlDhcpv6DuidEn=rlDhcpv6DuidEn, PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Relay=rlDhcpv6Relay)
