#
# PySNMP MIB module MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, IpAddress, Unsigned32, iso, NotificationType, Counter32, Counter64, enterprises, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "iso", "NotificationType", "Counter32", "Counter64", "enterprises", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("MIB-4RF", fourRFRequirements=fourRFRequirements, PYSNMP_MODULE_ID=fourRFRootModule, fourRFModules=fourRFModules, fourRFRegistrations=fourRFRegistrations, fourRFProducts=fourRFProducts, fourRFCapabilities=fourRFCapabilities, fourRFRootModule=fourRFRootModule, fourRFExperimental=fourRFExperimental, fourRFGeneric=fourRFGeneric, fourRFRoot=fourRFRoot)
