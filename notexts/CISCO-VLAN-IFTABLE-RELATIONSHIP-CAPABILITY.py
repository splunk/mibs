#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 369))
ciscoVlanIfTableRelCapability.setRevisions(('2013-08-08 00:00', '2006-01-18 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setLastUpdated('201308080000Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setOrganization('Cisco Systems, Inc.')
ciscoVlanIfTableRelCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setStatus('current')
ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setStatus('current')
ciscoVlanIfTableRelCapNxOSV6R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY", ciscoVlanIfTableRelCapIOSXRV3R2CRS1=ciscoVlanIfTableRelCapIOSXRV3R2CRS1, ciscoVlanIfTableRelCapability=ciscoVlanIfTableRelCapability, PYSNMP_MODULE_ID=ciscoVlanIfTableRelCapability, ciscoVlanIfTableRelCapV12R0119E=ciscoVlanIfTableRelCapV12R0119E, ciscoVlanIfTableRelCapNxOSV6R0202PN7K=ciscoVlanIfTableRelCapNxOSV6R0202PN7K)
