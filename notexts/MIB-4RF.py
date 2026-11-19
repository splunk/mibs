#
# PySNMP MIB module MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:00 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Counter64, Unsigned32, enterprises, iso, NotificationType, IpAddress, MibIdentifier, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter64", "Unsigned32", "enterprises", "iso", "NotificationType", "IpAddress", "MibIdentifier", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fourRFRootModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 1))
fourRFRootModule.setRevisions(('2007-04-30 00:00', '2004-02-13 00:00',))
if mibBuilder.loadTexts: fourRFRootModule.setLastUpdated('200704300000Z')
if mibBuilder.loadTexts: fourRFRootModule.setOrganization('www.4rf.com')
fourRFRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817))
if mibBuilder.loadTexts: fourRFRoot.setStatus('current')
fourRFRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 1))
if mibBuilder.loadTexts: fourRFRegistrations.setStatus('current')
fourRFModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 2))
if mibBuilder.loadTexts: fourRFModules.setStatus('current')
fourRFGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 3))
if mibBuilder.loadTexts: fourRFGeneric.setStatus('current')
fourRFProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 4))
if mibBuilder.loadTexts: fourRFProducts.setStatus('current')
fourRFCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 5))
if mibBuilder.loadTexts: fourRFCapabilities.setStatus('current')
fourRFRequirements = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 6))
if mibBuilder.loadTexts: fourRFRequirements.setStatus('current')
fourRFExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7))
if mibBuilder.loadTexts: fourRFExperimental.setStatus('current')
mibBuilder.exportSymbols("MIB-4RF", fourRFGeneric=fourRFGeneric, fourRFExperimental=fourRFExperimental, fourRFRoot=fourRFRoot, fourRFModules=fourRFModules, PYSNMP_MODULE_ID=fourRFRootModule, fourRFRequirements=fourRFRequirements, fourRFProducts=fourRFProducts, fourRFCapabilities=fourRFCapabilities, fourRFRegistrations=fourRFRegistrations, fourRFRootModule=fourRFRootModule)
