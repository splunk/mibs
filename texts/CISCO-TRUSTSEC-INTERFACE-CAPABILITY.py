#
# PySNMP MIB module CISCO-TRUSTSEC-INTERFACE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-INTERFACE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoTrustSecInterfaceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 597))
ciscoTrustSecInterfaceCapability.setRevisions(('2012-09-04 00:00', '2010-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoTrustSecInterfaceCapV15R0101SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setContactInfo('Cisco Systems, Inc\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-INTERFACE-MIB.')
ciscoTrustSecInterfaceCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-INTERFACE-MIB capabilities.')
ciscoTrustSecInterfaceCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setDescription('CISCO-TRUSTSEC-INTERFACE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-INTERFACE-CAPABILITY", ciscoTrustSecInterfaceCapV15R0101SYPCat6k=ciscoTrustSecInterfaceCapV15R0101SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecInterfaceCapability, ciscoTrustSecInterfaceCapability=ciscoTrustSecInterfaceCapability, ciscoTrustSecInterfaceCapV12R0250SYPCat6k=ciscoTrustSecInterfaceCapV12R0250SYPCat6k)
