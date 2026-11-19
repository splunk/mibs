#
# PySNMP MIB module CISCO-FABRICPATH-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FABRICPATH-TOPOLOGY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricPathTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 620))
ciscoFabricPathTopologyCapability.setRevisions(('2013-07-16 12:00',))
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setLastUpdated('201307161200Z')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setOrganization('Cisco Systems, Inc.')
ciscoFabricPathTopologyCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 620, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRICPATH-TOPOLOGY-CAPABILITY", ciscoFabricPathTopologyCapNxOSV06R0202PN7k=ciscoFabricPathTopologyCapNxOSV06R0202PN7k, ciscoFabricPathTopologyCapability=ciscoFabricPathTopologyCapability, PYSNMP_MODULE_ID=ciscoFabricPathTopologyCapability)
