#
# PySNMP MIB module CISCO-FLEX-LINKS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FLEX-LINKS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFlexLinksCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 444))
ciscoFlexLinksCapability.setRevisions(('2010-05-18 00:00', '2005-07-28 00:00', '2005-06-22 00:00',))
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setOrganization('Cisco Systems, Inc.')
ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setStatus('current')
cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setStatus('current')
cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-CAPABILITY", ciscoFlexLinksCapability=ciscoFlexLinksCapability, cFlexLinksCapV12R0254SGPCat4K=cFlexLinksCapV12R0254SGPCat4K, ciscoFlexLinksCapCatOSV08R0501=ciscoFlexLinksCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoFlexLinksCapability, cFlexLinksCapV12R0218SXFPCat6k=cFlexLinksCapV12R0218SXFPCat6k)
