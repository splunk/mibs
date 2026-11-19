#
# PySNMP MIB module IB-DHCPSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:36:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ibDHCPServ, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDHCPServ", "IbString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, ModuleIdentity, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, MibIdentifier, Bits, ObjectIdentity, enterprises, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "MibIdentifier", "Bits", "ObjectIdentity", "enterprises", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDhcpv4ServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9999, 1))
ibDhcpv4ServerModule.setRevisions(('2011-07-15 00:00',))
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setLastUpdated('201107150000Z')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setOrganization('Infoblox')
ibDhcpv4ServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1))
ibDhcpv4ServerSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1))
ibDhcpv4ServerSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpv4ServerSystemDescr.setStatus('current')
mibBuilder.exportSymbols("IB-DHCPSERV-MIB", PYSNMP_MODULE_ID=ibDhcpv4ServerModule, ibDhcpv4ServerModule=ibDhcpv4ServerModule, ibDhcpv4ServerObjects=ibDhcpv4ServerObjects, ibDhcpv4ServerSystemDescr=ibDhcpv4ServerSystemDescr, ibDhcpv4ServerSystem=ibDhcpv4ServerSystem)
