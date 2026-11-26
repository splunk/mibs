#
# PySNMP MIB module LENOVO-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lenovo/LENOVO-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:11:54 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Integer32, iso, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, IpAddress, ObjectIdentity, Gauge32, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Integer32", "iso", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "MibIdentifier", "enterprises")
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
mibBuilder.exportSymbols("LENOVO-SMI-MIB", lenovoModules=lenovoModules, tor_mibs=tor_mibs, lenovoNetworkMibs=lenovoNetworkMibs, lenovoServerMibs=lenovoServerMibs, flex_mibs=flex_mibs, lenovo=lenovo, PYSNMP_MODULE_ID=lenovo, network_mibs=network_mibs, lenovoProducts=lenovoProducts)
