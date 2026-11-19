#
# PySNMP MIB module CISCO-FC-FE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-FE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoMilliSeconds, = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-FC-FE-CAPABILITY", PYSNMP_MODULE_ID=ciscoFcFeCapability, ciscoFcFeCapabilityV06R0213PMds=ciscoFcFeCapabilityV06R0213PMds, ciscoFcFeCapabilityMDS3R0=ciscoFcFeCapabilityMDS3R0, ciscoFcFeCapability=ciscoFcFeCapability)
