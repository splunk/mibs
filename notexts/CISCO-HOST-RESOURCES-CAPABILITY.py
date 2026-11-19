#
# PySNMP MIB module CISCO-HOST-RESOURCES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HOST-RESOURCES-CAPABILITY
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHostResourcesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 547))
ciscoHostResourcesCapability.setRevisions(('2007-10-04 00:00', '2007-09-17 00:00',))
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setLastUpdated('200710040000Z')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setOrganization('Cisco Systems, Inc.')
ciscoHostResourcesCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setStatus('current')
ciscoHostResourcesCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-HOST-RESOURCES-CAPABILITY", ciscoHostResourcesCapability=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityV12R04=ciscoHostResourcesCapabilityV12R04, PYSNMP_MODULE_ID=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityCTSV120=ciscoHostResourcesCapabilityCTSV120)
