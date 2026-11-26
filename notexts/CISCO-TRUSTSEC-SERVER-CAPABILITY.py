#
# PySNMP MIB module CISCO-TRUSTSEC-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-SERVER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 596))
ciscoTrustSecServerCapability.setRevisions(('2012-09-07 00:00', '2010-10-30 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecServerCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecServerCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SERVER-CAPABILITY", ciscoTrustSecServerCapability=ciscoTrustSecServerCapability, ciscoTrustSecServerCapV15R0101SYPCat6k=ciscoTrustSecServerCapV15R0101SYPCat6k, ciscoTrustSecServerCapV12R0250SYPCat6k=ciscoTrustSecServerCapV12R0250SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecServerCapability)
