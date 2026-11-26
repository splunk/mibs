#
# PySNMP MIB module CISCO-TRUSTSEC-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-SERVER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoTrustSecServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 596))
ciscoTrustSecServerCapability.setRevisions(('2012-09-07 00:00', '2010-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setRevisionsDescriptions(('Added capability statement ciscoTrustSecServerCapV15R0101SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setContactInfo('Cisco Systems, Inc\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-SERVER-MIB.')
ciscoTrustSecServerCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecServerCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-SERVER-MIB capabilities.')
ciscoTrustSecServerCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecServerCapV15R0101SYPCat6k.setDescription('CISCO-TRUSTSEC-SERVER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SERVER-CAPABILITY", ciscoTrustSecServerCapability=ciscoTrustSecServerCapability, ciscoTrustSecServerCapV12R0250SYPCat6k=ciscoTrustSecServerCapV12R0250SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecServerCapability, ciscoTrustSecServerCapV15R0101SYPCat6k=ciscoTrustSecServerCapV15R0101SYPCat6k)
