#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:15:06 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, iso, ObjectIdentity, Bits, ModuleIdentity, Counter64, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "iso", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Gauge32", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitCommonRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 1))
taitCommonRegModule.setRevisions(('2012-02-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: taitCommonRegModule.setRevisionsDescriptions(('Update with new identity.',))
if mibBuilder.loadTexts: taitCommonRegModule.setLastUpdated('201202201200Z')
if mibBuilder.loadTexts: taitCommonRegModule.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setContactInfo('postal: Tait International Limited\n                   558 Wairakei Road\n                   PO Box 1645\n                   Christchurch\n                   New Zealand\n\n           phone:  +64 3358 3399\n           email:  support@taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setDescription('The Tait Communication registration module.')
tait = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570))
if mibBuilder.loadTexts: tait.setStatus('current')
if mibBuilder.loadTexts: tait.setDescription('The root of the sub-tree for Tait Communications.')
taitRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1))
if mibBuilder.loadTexts: taitRegistrations.setStatus('current')
if mibBuilder.loadTexts: taitRegistrations.setDescription('Sub-tree for registrations, which includes modules.')
taitModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1))
if mibBuilder.loadTexts: taitModules.setStatus('current')
if mibBuilder.loadTexts: taitModules.setDescription('Sub-tree for module registrations. It contains the textual context files.')
taitGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 2))
if mibBuilder.loadTexts: taitGeneric.setStatus('current')
if mibBuilder.loadTexts: taitGeneric.setDescription('Sub-tree for common objects and events for products.')
taitProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 3))
if mibBuilder.loadTexts: taitProducts.setStatus('current')
if mibBuilder.loadTexts: taitProducts.setDescription('Sub-tree for product-specific objects and events.')
mibBuilder.exportSymbols("TAIT-COMMON-MIB", PYSNMP_MODULE_ID=taitCommonRegModule, taitRegistrations=taitRegistrations, taitProducts=taitProducts, taitGeneric=taitGeneric, tait=tait, taitCommonRegModule=taitCommonRegModule, taitModules=taitModules)
