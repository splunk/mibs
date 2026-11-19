#
# PySNMP MIB module LENOVO-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lenovo/LENOVO-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:12 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, NotificationType, ObjectIdentity, Gauge32, iso, TimeTicks, MibIdentifier, Bits, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "ObjectIdentity", "Gauge32", "iso", "TimeTicks", "MibIdentifier", "Bits", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lenovo = ModuleIdentity((1, 3, 6, 1, 4, 1, 19046))
lenovo.setRevisions(('2016-10-27 18:30',))
if mibBuilder.loadTexts: lenovo.setLastUpdated('201608150000Z')
if mibBuilder.loadTexts: lenovo.setOrganization('Lenovo Group Ltd.')
lenovoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 1))
if mibBuilder.loadTexts: lenovoProducts.setStatus('current')
lenovoNetworkMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2))
if mibBuilder.loadTexts: lenovoNetworkMibs.setStatus('current')
tor_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 7)).setLabel("tor-mibs")
if mibBuilder.loadTexts: tor_mibs.setStatus('current')
flex_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 18)).setLabel("flex-mibs")
if mibBuilder.loadTexts: flex_mibs.setStatus('current')
network_mibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 2, 3)).setLabel("network-mibs")
if mibBuilder.loadTexts: network_mibs.setStatus('current')
lenovoServerMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 11))
if mibBuilder.loadTexts: lenovoServerMibs.setStatus('current')
lenovoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 19046, 4))
if mibBuilder.loadTexts: lenovoModules.setStatus('current')
mibBuilder.exportSymbols("LENOVO-SMI-MIB", network_mibs=network_mibs, lenovoServerMibs=lenovoServerMibs, lenovoModules=lenovoModules, flex_mibs=flex_mibs, PYSNMP_MODULE_ID=lenovo, lenovoProducts=lenovoProducts, lenovo=lenovo, lenovoNetworkMibs=lenovoNetworkMibs, tor_mibs=tor_mibs)
