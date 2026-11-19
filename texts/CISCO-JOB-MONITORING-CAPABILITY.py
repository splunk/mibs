#
# PySNMP MIB module CISCO-JOB-MONITORING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-JOB-MONITORING-CAPABILITY
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoJobMonitoringCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 557))
ciscoJobMonitoringCapability.setRevisions(('2007-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setLastUpdated('200706070000Z')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoJobMonitoringCapability.setDescription('Agent capabilities for Job-Monitoring-MIB')
ciscoJobMonitoringCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 557, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoJobMonitoringCapabilityV12R04 = ciscoJobMonitoringCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoJobMonitoringCapabilityV12R04.setDescription('JOB MONITORING MIB capabilities')
mibBuilder.exportSymbols("CISCO-JOB-MONITORING-CAPABILITY", ciscoJobMonitoringCapability=ciscoJobMonitoringCapability, ciscoJobMonitoringCapabilityV12R04=ciscoJobMonitoringCapabilityV12R04, PYSNMP_MODULE_ID=ciscoJobMonitoringCapability)
