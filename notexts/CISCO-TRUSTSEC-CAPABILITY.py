#
# PySNMP MIB module CISCO-TRUSTSEC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CtsPasswordEncryptionType, = mibBuilder.importSymbols("CISCO-TRUSTSEC-TC-MIB", "CtsPasswordEncryptionType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoTrustSecCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 598))
ciscoTrustSecCapability.setRevisions(('2012-09-07 00:00', '2011-09-28 00:00', '2010-11-02 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setStatus('current')
ciscoTrustSecCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setStatus('current')
ciscoTrustSecCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-CAPABILITY", ciscoTrustSecCapV15R0001SYPCat6k=ciscoTrustSecCapV15R0001SYPCat6k, ciscoTrustSecCapability=ciscoTrustSecCapability, ciscoTrustSecCapV12R0250SYPCat6k=ciscoTrustSecCapV12R0250SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecCapability, ciscoTrustSecCapV15R0101SYPCat6kSup2T=ciscoTrustSecCapV15R0101SYPCat6kSup2T, ciscoTrustSecCapV15R0101SYPCat6kSup720=ciscoTrustSecCapV15R0101SYPCat6kSup720)
