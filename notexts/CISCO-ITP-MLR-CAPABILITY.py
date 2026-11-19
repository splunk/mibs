#
# PySNMP MIB module CISCO-ITP-MLR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MLR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMlrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 423))
ciscoMlrCapability.setRevisions(('2007-05-18 00:00', '2006-10-05 00:00', '2005-02-18 00:00', '2004-04-30 00:00',))
if mibBuilder.loadTexts: ciscoMlrCapability.setLastUpdated('200705180000Z')
if mibBuilder.loadTexts: ciscoMlrCapability.setOrganization('Cisco Systems, Inc.')
ciscoMlrCapabilityV12R0221SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setProductRelease('Cisco IOS 12.2(21)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setStatus('current')
ciscoMlrCapabilityV12R0225SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setStatus('current')
ciscoMlrCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setStatus('current')
ciscoMlrCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-MLR-CAPABILITY", ciscoMlrCapabilityV12R0411SW=ciscoMlrCapabilityV12R0411SW, ciscoMlrCapabilityV12R0225SW01=ciscoMlrCapabilityV12R0225SW01, ciscoMlrCapabilityV12R0221SW01=ciscoMlrCapabilityV12R0221SW01, ciscoMlrCapability=ciscoMlrCapability, ciscoMlrCapabilityV12R0218IXA=ciscoMlrCapabilityV12R0218IXA, PYSNMP_MODULE_ID=ciscoMlrCapability)
