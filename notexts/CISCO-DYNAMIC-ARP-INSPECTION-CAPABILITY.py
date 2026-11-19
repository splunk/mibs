#
# PySNMP MIB module CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoDynamicArpInspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 382))
ciscoDynamicArpInspCapability.setRevisions(('2011-03-24 00:00', '2010-05-07 00:00', '2007-07-02 00:00', '2004-01-13 00:00',))
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setLastUpdated('201103240000Z')
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setOrganization('Cisco Systems, Inc.')
cdaiCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setStatus('current')
cdaiCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setStatus('current')
cdaiCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setStatus('current')
cdaiCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY", ciscoDynamicArpInspCapability=ciscoDynamicArpInspCapability, cdaiCapV12R0254SGPCat4K=cdaiCapV12R0254SGPCat4K, cdaiCapV15R0002SGPCat4K=cdaiCapV15R0002SGPCat4K, cdaiCapabilityCatOSV08R0301Cat6k=cdaiCapabilityCatOSV08R0301Cat6k, cdaiCapV12R0233SXHPCat6k=cdaiCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoDynamicArpInspCapability)
