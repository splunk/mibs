#
# PySNMP MIB module CISCO-TRUSTSEC-SXP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-SXP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoVrfName, = mibBuilder.importSymbols("CISCO-TC", "CiscoVrfName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecSxpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 591))
ciscoTrustSecSxpCapability.setRevisions(('2012-09-07 00:00', '2012-04-10 00:00', '2011-09-28 00:00', '2011-03-23 00:00', '2010-11-03 00:00', '2010-03-25 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecSxpCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SXP-CAPABILITY", ciscoTrustSecSxpCapV15R0101SYPCat6k=ciscoTrustSecSxpCapV15R0101SYPCat6k, ciscoTrustSecSxpCapV15R0001SYPCat6k=ciscoTrustSecSxpCapV15R0001SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV12R0250SYPCat6k=ciscoTrustSecSxpCapV12R0250SYPCat6k, ciscoTrustSecSxpCapV15R0101SGPCat4k=ciscoTrustSecSxpCapV15R0101SGPCat4k, ciscoTrustSecSxpCapV12R0233SXJPCat6k=ciscoTrustSecSxpCapV12R0233SXJPCat6k, ciscoTrustSecSxpCapability=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV12R0233SXI4PCat6k=ciscoTrustSecSxpCapV12R0233SXI4PCat6k)
