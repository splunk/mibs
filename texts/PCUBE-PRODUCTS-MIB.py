#
# PySNMP MIB module PCUBE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/PCUBE-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pcubeProducts, pcubeModules = mibBuilder.importSymbols("PCUBE-SMI", "pcubeProducts", "pcubeModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcubeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 2))
pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcubeProductsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcubeProductsMIB.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcubeProductsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcubeProductsMIB.setContactInfo('Cisco Systems\n                Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                 Tel: +1 800 553-NETS\n\n                E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcubeProductsMIB.setDescription('This module defines the object identifiers that are\n        assigned to various hardware platforms, and hence are\n        returned as values for sysObjectID.')
sce100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 1))
sce1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 2))
sce2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 3))
mibBuilder.exportSymbols("PCUBE-PRODUCTS-MIB", sce2000=sce2000, pcubeProductsMIB=pcubeProductsMIB, sce100=sce100, PYSNMP_MODULE_ID=pcubeProductsMIB, sce1000=sce1000)
