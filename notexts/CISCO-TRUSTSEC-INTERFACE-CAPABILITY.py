#
# PySNMP MIB module CISCO-TRUSTSEC-INTERFACE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-INTERFACE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoTrustSecInterfaceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 597))
ciscoTrustSecInterfaceCapability.setRevisions(('2012-09-04 00:00', '2010-10-30 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecInterfaceCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecInterfaceCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-INTERFACE-CAPABILITY", ciscoTrustSecInterfaceCapV12R0250SYPCat6k=ciscoTrustSecInterfaceCapV12R0250SYPCat6k, ciscoTrustSecInterfaceCapability=ciscoTrustSecInterfaceCapability, ciscoTrustSecInterfaceCapV15R0101SYPCat6k=ciscoTrustSecInterfaceCapV15R0101SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecInterfaceCapability)
