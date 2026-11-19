#
# PySNMP MIB module PCUBE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/PCUBE-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, enterprises, IpAddress, iso, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "enterprises", "IpAddress", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcube = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655))
pcube.setRevisions(('2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcube.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcube.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcube.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcube.setContactInfo('Cisco Systems\n                 Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcube.setDescription('The Structure of Management Information for the\n        Pcube enterprise.')
pcubeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 1))
if mibBuilder.loadTexts: pcubeProducts.setStatus('current')
if mibBuilder.loadTexts: pcubeProducts.setDescription('pcubeProducts is the root OBJECT IDENTIFIER from\n        which sysObjectID values are assigned.  Actual\n        values are defined in PCUBE-PRODUCTS-MIB.')
pcubeModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 2))
if mibBuilder.loadTexts: pcubeModules.setStatus('current')
if mibBuilder.loadTexts: pcubeModules.setDescription('pcubeModules provides a root object identifier\n        from which MODULE-IDENTITY values may be assigned.')
pcubeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 3))
if mibBuilder.loadTexts: pcubeMgmt.setStatus('current')
if mibBuilder.loadTexts: pcubeMgmt.setDescription('pcubeMgmt is the main subtree for new MIB development.')
pcubeWorkgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 4))
if mibBuilder.loadTexts: pcubeWorkgroup.setStatus('current')
if mibBuilder.loadTexts: pcubeWorkgroup.setDescription("pcubeWorkgroup is the main subtree for objects and events of\n        P-Cube's products.")
mibBuilder.exportSymbols("PCUBE-SMI", pcubeProducts=pcubeProducts, pcubeWorkgroup=pcubeWorkgroup, PYSNMP_MODULE_ID=pcube, pcube=pcube, pcubeMgmt=pcubeMgmt, pcubeModules=pcubeModules)
