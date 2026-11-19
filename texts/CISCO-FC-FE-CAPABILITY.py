#
# PySNMP MIB module CISCO-FC-FE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-FE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoMilliSeconds, = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFcFeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 627))
ciscoFcFeCapability.setRevisions(('2015-06-23 00:00', '2005-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFcFeCapability.setRevisionsDescriptions(('Added capability statement ciscoFcFeCapabilityV06R0213PMds.', 'Agent capabilities for Cisco MDS 3.0.',))
if mibBuilder.loadTexts: ciscoFcFeCapability.setLastUpdated('201506230000Z')
if mibBuilder.loadTexts: ciscoFcFeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFcFeCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFcFeCapability.setDescription('Agent capabilities for the CISCO-FC-FE-MIB.')
ciscoFcFeCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoFcFeCapabilityMDS3R0.setDescription('Cisco FC FE MIB capabilities.')
ciscoFcFeCapabilityV06R0213PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setProductRelease('Cisco NX-OS 6.2(13) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoFcFeCapabilityV06R0213PMds.setDescription('CISCO-FC-FE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FC-FE-CAPABILITY", PYSNMP_MODULE_ID=ciscoFcFeCapability, ciscoFcFeCapabilityV06R0213PMds=ciscoFcFeCapabilityV06R0213PMds, ciscoFcFeCapabilityMDS3R0=ciscoFcFeCapabilityMDS3R0, ciscoFcFeCapability=ciscoFcFeCapability)
