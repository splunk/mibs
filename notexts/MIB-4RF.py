#
# PySNMP MIB module MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:28 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Counter32, NotificationType, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, TimeTicks, Counter64, enterprises, Bits, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "NotificationType", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "TimeTicks", "Counter64", "enterprises", "Bits", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MIB-4RF", fourRFRequirements=fourRFRequirements, fourRFRootModule=fourRFRootModule, fourRFRoot=fourRFRoot, fourRFCapabilities=fourRFCapabilities, PYSNMP_MODULE_ID=fourRFRootModule, fourRFProducts=fourRFProducts, fourRFModules=fourRFModules, fourRFRegistrations=fourRFRegistrations, fourRFGeneric=fourRFGeneric, fourRFExperimental=fourRFExperimental)
