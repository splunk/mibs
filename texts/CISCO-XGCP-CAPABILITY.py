#
# PySNMP MIB module CISCO-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-XGCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CCallControlProfileIndexOrZero, = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "CCallControlProfileIndexOrZero")
CMgcGroupIndexOrZero, = mibBuilder.importSymbols("CISCO-MGC-MIB", "CMgcGroupIndexOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
CXgcpRetryMethod, = mibBuilder.importSymbols("CISCO-XGCP-MIB", "CXgcpRetryMethod")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 408))
ciscoXgcpCapability.setRevisions(('2006-03-01 00:00', '2006-02-14 00:00', '2005-06-24 00:00', '2005-01-06 00:00', '2004-10-04 00:00', '2004-06-16 00:00', '2002-12-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoXgcpCapability.setRevisionsDescriptions(('Deprecated ciscoXgcpCapabilityV12R03AS5000 and added\n             ciscoXgcpCapabilityV12R04AS5000.', 'Added ciscoXgcpCapabilityV5R300 for \n             MGX8880 release 5.3.00.\n             Deprecated ciscoXgcpCapabilityV12R03 and added\n             ciscoXgcpCapabilityV12R03AS5000.', 'Added ciscoXgcpCapabilityV5R100 for \n             MGX8850 release 5.1.00', 'Fixed syntax error in cXgcpMediaGwSupportedPackages\n             of ciscoXgcpCapabilityV12R03.', 'Added ciscoXgcpCapabilityV5R015 for \n             MGX8850 release 5.0.15', 'Added ciscoXgcpCapabilityV12R03 for Cisco IOS 12.3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoXgcpCapability.setLastUpdated('200603010000Z')
if mibBuilder.loadTexts: ciscoXgcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoXgcpCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoXgcpCapability.setDescription('The agent capabilities for CISCO-XGCP-MIB.')
ciscoXgcpCapabilityV4R010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setProductRelease('MGX8850 Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV4R010.setDescription('XGCP MIB capabilities for VXSM in Release 4.0.10.')
ciscoXgcpCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R03.setDescription('Cisco XGCP MIB capabilities')
ciscoXgcpCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setProductRelease('MGX8850 release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R015.setDescription('XGCP MIB capabilities for VXSM in \n                 MGX8850 release 5.0.15.')
ciscoXgcpCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setProductRelease('MGX8880 release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R100.setDescription('XGCP MIB capabilities for VXSM in \n                 MGX8880 release 5.1.00.')
ciscoXgcpCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setProductRelease('MGX8880 release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV5R300.setDescription('XGCP MIB capabilities for VXSM in \n                 MGX8880 release 5.3.00.')
ciscoXgcpCapabilityV12R03AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R03AS5000.setDescription('Cisco XGCP MIB capabilities')
ciscoXgcpCapabilityV12R04AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpCapabilityV12R04AS5000.setDescription('Cisco XGCP MIB capabilities')
mibBuilder.exportSymbols("CISCO-XGCP-CAPABILITY", ciscoXgcpCapabilityV5R300=ciscoXgcpCapabilityV5R300, ciscoXgcpCapabilityV5R100=ciscoXgcpCapabilityV5R100, ciscoXgcpCapabilityV12R04AS5000=ciscoXgcpCapabilityV12R04AS5000, PYSNMP_MODULE_ID=ciscoXgcpCapability, ciscoXgcpCapabilityV5R015=ciscoXgcpCapabilityV5R015, ciscoXgcpCapabilityV12R03AS5000=ciscoXgcpCapabilityV12R03AS5000, ciscoXgcpCapabilityV4R010=ciscoXgcpCapabilityV4R010, ciscoXgcpCapabilityV12R03=ciscoXgcpCapabilityV12R03, ciscoXgcpCapability=ciscoXgcpCapability)
