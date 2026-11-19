#
# PySNMP MIB module IB-DHCPSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:37:36 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ibDHCPServ, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDHCPServ", "IbString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, ObjectIdentity, Unsigned32, TimeTicks, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Bits, NotificationType, Gauge32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibDhcpv4ServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9999, 1))
ibDhcpv4ServerModule.setRevisions(('2011-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDhcpv4ServerModule.setRevisionsDescriptions(('Added DHCPv4 Server module.',))
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setLastUpdated('201107150000Z')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setContactInfo('See IB-SMI-MIB for information.')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setDescription('This module defines the Infoblox DHCPv4 Server One MIB.')
ibDhcpv4ServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1))
ibDhcpv4ServerSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1))
ibDhcpv4ServerSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpv4ServerSystemDescr.setStatus('current')
if mibBuilder.loadTexts: ibDhcpv4ServerSystemDescr.setDescription('A textual description of the server.  This value SHOULD\n                  include the full name and version identification of the\n                  server.')
mibBuilder.exportSymbols("IB-DHCPSERV-MIB", ibDhcpv4ServerModule=ibDhcpv4ServerModule, PYSNMP_MODULE_ID=ibDhcpv4ServerModule, ibDhcpv4ServerSystem=ibDhcpv4ServerSystem, ibDhcpv4ServerSystemDescr=ibDhcpv4ServerSystemDescr, ibDhcpv4ServerObjects=ibDhcpv4ServerObjects)
