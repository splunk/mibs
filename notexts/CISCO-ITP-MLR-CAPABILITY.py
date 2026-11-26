#
# PySNMP MIB module CISCO-ITP-MLR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MLR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-ITP-MLR-CAPABILITY", ciscoMlrCapability=ciscoMlrCapability, ciscoMlrCapabilityV12R0218IXA=ciscoMlrCapabilityV12R0218IXA, ciscoMlrCapabilityV12R0225SW01=ciscoMlrCapabilityV12R0225SW01, ciscoMlrCapabilityV12R0411SW=ciscoMlrCapabilityV12R0411SW, PYSNMP_MODULE_ID=ciscoMlrCapability, ciscoMlrCapabilityV12R0221SW01=ciscoMlrCapabilityV12R0221SW01)
