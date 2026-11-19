#
# PySNMP MIB module CISCO-TRUSTSEC-POLICY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-POLICY-CAPABILITY
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTrustSecPolicyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 601))
ciscoTrustSecPolicyCapability.setRevisions(('2013-05-01 00:00', '2013-01-09 00:00', '2010-11-16 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setLastUpdated('201305010000Z')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecPolicyCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setStatus('current')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-POLICY-CAPABILITY", ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T, ciscoTrustSecPolicyCapability=ciscoTrustSecPolicyCapability, PYSNMP_MODULE_ID=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapV12R0250SYPCat6k=ciscoTrustSecPolicyCapV12R0250SYPCat6k, ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720)
