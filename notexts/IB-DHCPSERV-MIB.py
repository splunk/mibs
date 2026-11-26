#
# PySNMP MIB module IB-DHCPSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:11:06 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ibDHCPServ, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDHCPServ", "IbString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Bits, Counter32, ObjectIdentity, MibIdentifier, enterprises, Unsigned32, iso, TimeTicks, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Bits", "Counter32", "ObjectIdentity", "MibIdentifier", "enterprises", "Unsigned32", "iso", "TimeTicks", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDhcpv4ServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9999, 1))
ibDhcpv4ServerModule.setRevisions(('2011-07-15 00:00',))
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setLastUpdated('201107150000Z')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setOrganization('Infoblox')
ibDhcpv4ServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1))
ibDhcpv4ServerSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1))
ibDhcpv4ServerSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpv4ServerSystemDescr.setStatus('current')
mibBuilder.exportSymbols("IB-DHCPSERV-MIB", ibDhcpv4ServerObjects=ibDhcpv4ServerObjects, ibDhcpv4ServerSystem=ibDhcpv4ServerSystem, ibDhcpv4ServerModule=ibDhcpv4ServerModule, ibDhcpv4ServerSystemDescr=ibDhcpv4ServerSystemDescr, PYSNMP_MODULE_ID=ibDhcpv4ServerModule)
