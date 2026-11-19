#
# PySNMP MIB module CISCO-FLEX-LINKS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FLEX-LINKS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoFlexLinksCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 444))
ciscoFlexLinksCapability.setRevisions(('2010-05-18 00:00', '2005-07-28 00:00', '2005-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlexLinksCapability.setRevisionsDescriptions(('Added cFlexLinksCapV12R0254SGPCat4K.\n\n                 Updated cFlexLinksCapV12R0218SXFPCat6k with\n                 VARIATION clause of cflIfConfigStatus.', 'Added cFlexLinksCapV12R0218SXFPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setDescription('The capabilities description of CISCO-FLEX-LINKS-MIB.')
ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoFlexLinksCapCatOSV08R0501.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0218SXFPCat6k.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0254SGPCat4K.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-CAPABILITY", ciscoFlexLinksCapability=ciscoFlexLinksCapability, PYSNMP_MODULE_ID=ciscoFlexLinksCapability, cFlexLinksCapV12R0218SXFPCat6k=cFlexLinksCapV12R0218SXFPCat6k, ciscoFlexLinksCapCatOSV08R0501=ciscoFlexLinksCapCatOSV08R0501, cFlexLinksCapV12R0254SGPCat4K=cFlexLinksCapV12R0254SGPCat4K)
