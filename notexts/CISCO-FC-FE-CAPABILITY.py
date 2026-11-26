#
# PySNMP MIB module CISCO-FC-FE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-FE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoMilliSeconds, = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFcFeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 627))
ciscoFcFeCapability.setRevisions(('2015-06-23 00:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoFcFeCapability.setLastUpdated('201506230000Z')
if mibBuilder.loadTexts: ciscoFcFeCapability.setOrganization('Cisco Systems, Inc.')
ciscoFcFeCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setStatus('current')
ciscoFcFeCapabilityV06R0213PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setProductRelease('Cisco NX-OS 6.2(13) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-FE-CAPABILITY", ciscoFcFeCapabilityMDS3R0=ciscoFcFeCapabilityMDS3R0, ciscoFcFeCapability=ciscoFcFeCapability, ciscoFcFeCapabilityV06R0213PMds=ciscoFcFeCapabilityV06R0213PMds, PYSNMP_MODULE_ID=ciscoFcFeCapability)
