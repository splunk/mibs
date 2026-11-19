#
# PySNMP MIB module CISCO-FABRICPATH-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FABRICPATH-TOPOLOGY-CAPABILITY
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
ciscoFabricPathTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 620))
ciscoFabricPathTopologyCapability.setRevisions(('2013-07-16 12:00',))
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setLastUpdated('201307161200Z')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setOrganization('Cisco Systems, Inc.')
ciscoFabricPathTopologyCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 620, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRICPATH-TOPOLOGY-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricPathTopologyCapability, ciscoFabricPathTopologyCapNxOSV06R0202PN7k=ciscoFabricPathTopologyCapNxOSV06R0202PN7k, ciscoFabricPathTopologyCapability=ciscoFabricPathTopologyCapability)
