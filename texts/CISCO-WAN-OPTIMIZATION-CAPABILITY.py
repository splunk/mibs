#
# PySNMP MIB module CISCO-WAN-OPTIMIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-OPTIMIZATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanOptimizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 611))
ciscoWanOptimizationCapability.setRevisions(('2015-11-09 00:00', '2015-10-05 00:00', '2012-06-23 00:00', '2012-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setRevisionsDescriptions(('Added CIFS and Video AO objects to the list of Not-supported\n        objects in ciscoWanOptimizationCapabilityWAASV6R0 agent.', 'Added ciscoWanOptimizationCapabilityWAASV6R0 agent for\n        CISCO-WAN-OPTIMIZATION-MIB', 'Added ciscoWanOptimizationCapabilityWAASV5R0 agent for\n        CISCO-WAN-OPTIMIZATION-CAPABILITY MIB.', 'Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setLastUpdated('201511090000Z')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-waas@cisco.com')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setDescription('Agent capabilities for CISCO-WAN-OPTIMIZATION MIB')
ciscoWanOptimizationCapabilityWAASV4R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setProductRelease('OS=WAAS\n                     OSVERSION=V4R4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV4R4.setDescription('Agent capabilities for CISCO-WAN-OPTIMIZATION-MIB of WAAS V4R4')
ciscoWanOptimizationCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V5R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV5R0.setDescription('Agent capability for CISCO-WAN-OPTIMIZATION-MIB of WAAS V5R0')
ciscoWanOptimizationCapabilityWAASV6R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setProductRelease('OS=WAAS\n                     OSVERSION=V6R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV6R0.setDescription('Agent capability for CISCO-WAN-OPTIMIZATION-MIB of WAAS V6R0')
mibBuilder.exportSymbols("CISCO-WAN-OPTIMIZATION-CAPABILITY", ciscoWanOptimizationCapabilityWAASV4R4=ciscoWanOptimizationCapabilityWAASV4R4, ciscoWanOptimizationCapabilityWAASV6R0=ciscoWanOptimizationCapabilityWAASV6R0, ciscoWanOptimizationCapabilityWAASV5R0=ciscoWanOptimizationCapabilityWAASV5R0, PYSNMP_MODULE_ID=ciscoWanOptimizationCapability, ciscoWanOptimizationCapability=ciscoWanOptimizationCapability)
