#
# PySNMP MIB module LENOVO-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lenovo/LENOVO-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, Gauge32, IpAddress, Integer32, NotificationType, iso, Unsigned32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "Gauge32", "IpAddress", "Integer32", "NotificationType", "iso", "Unsigned32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lenovo = ModuleIdentity((1, 3, 6, 1, 4, 1, 19046))
lenovo.setRevisions(('2016-10-27 18:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lenovo.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: lenovo.setLastUpdated('201608150000Z')
if mibBuilder.loadTexts: lenovo.setOrganization('Lenovo Group Ltd.')
if mibBuilder.loadTexts: lenovo.setContactInfo('Lenovo\n         Postal: 1009 Think Place\n         Morrisville, NC 27560\n         USA\n         Tel: +1 (919) 968-4465\n         E-mail: snmp@lenovo.com')
if mibBuilder.loadTexts: lenovo.setDescription('The Structure of Management Information for the\n         Lenovo Enterprise Business Group.')
lenovoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 1))
if mibBuilder.loadTexts: lenovoProducts.setStatus('current')
if mibBuilder.loadTexts: lenovoProducts.setDescription('Root object identifier from which sysObjectID values are assigned.  \n\t\t Values are defined in LENOVO-PRODUCTS-MIB.')
lenovoNetworkMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2))
if mibBuilder.loadTexts: lenovoNetworkMibs.setStatus('current')
if mibBuilder.loadTexts: lenovoNetworkMibs.setDescription('Root object identifier for management-related Lenovo network MIBs.')
tor_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 7)).setLabel("tor-mibs")
if mibBuilder.loadTexts: tor_mibs.setStatus('current')
if mibBuilder.loadTexts: tor_mibs.setDescription('Root for pre-10.x Lenovo RackSwitch switch MIBs.')
flex_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 18)).setLabel("flex-mibs")
if mibBuilder.loadTexts: flex_mibs.setStatus('current')
if mibBuilder.loadTexts: flex_mibs.setDescription('Root for pre-10.x Lenovo Flex chassis switch MIBs.')
network_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 3)).setLabel("network-mibs")
if mibBuilder.loadTexts: network_mibs.setStatus('current')
if mibBuilder.loadTexts: network_mibs.setDescription('Root for Lenovo device-independent switch MIBs.')
lenovoServerMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 11))
if mibBuilder.loadTexts: lenovoServerMibs.setStatus('current')
if mibBuilder.loadTexts: lenovoServerMibs.setDescription('Root object identifier for management-related Lenovo server MIBs.')
lenovoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 4))
if mibBuilder.loadTexts: lenovoModules.setStatus('current')
if mibBuilder.loadTexts: lenovoModules.setDescription('Root bject identifier from which MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("LENOVO-SMI-MIB", lenovoModules=lenovoModules, lenovoProducts=lenovoProducts, PYSNMP_MODULE_ID=lenovo, lenovo=lenovo, lenovoNetworkMibs=lenovoNetworkMibs, flex_mibs=flex_mibs, network_mibs=network_mibs, lenovoServerMibs=lenovoServerMibs, tor_mibs=tor_mibs)
