#
# PySNMP MIB module CISCO-JOB-MONITORING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-JOB-MONITORING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-JOB-MONITORING-CAPABILITY", ciscoJobMonitoringCapabilityV12R04=ciscoJobMonitoringCapabilityV12R04, PYSNMP_MODULE_ID=ciscoJobMonitoringCapability, ciscoJobMonitoringCapability=ciscoJobMonitoringCapability)
