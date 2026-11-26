#
# PySNMP MIB module LINKSYS-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-DHCPv6
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddress, InetAddressType, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetAddressIPv6")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, Integer32, Gauge32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Integer32", "Gauge32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity")
RowStatus, TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('')
if mibBuilder.loadTexts: rlDhcpv6.setContactInfo('')
if mibBuilder.loadTexts: rlDhcpv6.setDescription('The private MIB module definition for DHCP v6 features.')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setDescription('')
mibBuilder.exportSymbols("LINKSYS-DHCPv6", rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6Relay=rlDhcpv6Relay, rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6=rlDhcpv6, PYSNMP_MODULE_ID=rlDhcpv6)
