#
# PySNMP MIB module CISCO-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-XGCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
CCallControlProfileIndexOrZero, = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "CCallControlProfileIndexOrZero")
CMgcGroupIndexOrZero, = mibBuilder.importSymbols("CISCO-MGC-MIB", "CMgcGroupIndexOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
CXgcpRetryMethod, = mibBuilder.importSymbols("CISCO-XGCP-MIB", "CXgcpRetryMethod")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 408))
ciscoXgcpCapability.setRevisions(('2006-03-01 00:00', '2006-02-14 00:00', '2005-06-24 00:00', '2005-01-06 00:00', '2004-10-04 00:00', '2004-06-16 00:00', '2002-12-31 00:00',))
if mibBuilder.loadTexts: ciscoXgcpCapability.setLastUpdated('200603010000Z')
if mibBuilder.loadTexts: ciscoXgcpCapability.setOrganization('Cisco Systems, Inc.')
ciscoXgcpCapabilityV4R010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setProductRelease('MGX8850 Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setStatus('current')
ciscoXgcpCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setStatus('deprecated')
ciscoXgcpCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setProductRelease('MGX8850 release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setStatus('current')
ciscoXgcpCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setProductRelease('MGX8880 release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setStatus('current')
ciscoXgcpCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setProductRelease('MGX8880 release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setStatus('current')
ciscoXgcpCapabilityV12R03AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setStatus('deprecated')
ciscoXgcpCapabilityV12R04AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setStatus('current')
mibBuilder.exportSymbols("CISCO-XGCP-CAPABILITY", ciscoXgcpCapabilityV4R010=ciscoXgcpCapabilityV4R010, ciscoXgcpCapabilityV5R015=ciscoXgcpCapabilityV5R015, ciscoXgcpCapabilityV12R04AS5000=ciscoXgcpCapabilityV12R04AS5000, ciscoXgcpCapability=ciscoXgcpCapability, ciscoXgcpCapabilityV12R03=ciscoXgcpCapabilityV12R03, ciscoXgcpCapabilityV5R100=ciscoXgcpCapabilityV5R100, PYSNMP_MODULE_ID=ciscoXgcpCapability, ciscoXgcpCapabilityV5R300=ciscoXgcpCapabilityV5R300, ciscoXgcpCapabilityV12R03AS5000=ciscoXgcpCapabilityV12R03AS5000)
