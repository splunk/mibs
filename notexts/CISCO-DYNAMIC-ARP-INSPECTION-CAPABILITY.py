#
# PySNMP MIB module CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY", ciscoDynamicArpInspCapability=ciscoDynamicArpInspCapability, cdaiCapV12R0233SXHPCat6k=cdaiCapV12R0233SXHPCat6k, cdaiCapV15R0002SGPCat4K=cdaiCapV15R0002SGPCat4K, cdaiCapV12R0254SGPCat4K=cdaiCapV12R0254SGPCat4K, cdaiCapabilityCatOSV08R0301Cat6k=cdaiCapabilityCatOSV08R0301Cat6k, PYSNMP_MODULE_ID=ciscoDynamicArpInspCapability)
