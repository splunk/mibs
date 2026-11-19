#
# PySNMP MIB module CISCO-IEEE8021-CFM-V2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8021-CFM-V2-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 579))
ciscoIeee8021CfmV2Capability.setRevisions(('2010-02-15 00:00', '2009-02-06 00:00',))
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setLastUpdated('201002150000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setOrganization('Cisco Systems, Inc.')
ciscoIeee8021CfmV2CapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setStatus('current')
ciscoIeee8021CfmV2CapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-V2-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021CfmV2Capability, ciscoIeee8021CfmV2Capability=ciscoIeee8021CfmV2Capability, ciscoIeee8021CfmV2CapV12R0254SE=ciscoIeee8021CfmV2CapV12R0254SE, ciscoIeee8021CfmV2CapCatOSV08R0702=ciscoIeee8021CfmV2CapCatOSV08R0702)
