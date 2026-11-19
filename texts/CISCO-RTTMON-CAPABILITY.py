#
# PySNMP MIB module CISCO-RTTMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RTTMON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRttMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 62))
ciscoRttMonCapability.setRevisions(('2006-03-02 00:00', '2005-12-14 00:00', '2005-06-09 00:00', '2005-05-01 00:00', '2004-05-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRttMonCapability.setRevisionsDescriptions(('Added capability definition ciscoRttMonCapV12R0201SRB for\n         12.2(01)SRB', 'Agent capabilities for CISCO-RTTMON-MIB on CRS-1\n         IOS-XR Release 3.3', 'Added capability definition ciscoRttMonCapV12R0403rdT for\n         12.4(3rd)T', 'Added capability definition ciscoRttMonCapV12R0402ndT\n        for 12.4(2nd)T and ciscoRttMonCapV12R0206thSX for\n        12.2(6th)SX', 'Initial Creation',))
if mibBuilder.loadTexts: ciscoRttMonCapability.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: ciscoRttMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRttMonCapability.setContactInfo('       Cisco Systems\n                    Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoRttMonCapability.setDescription('Agent capabilities for CISCO-RTTMON-MIB')
ciscoRttMonCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setProductRelease('Cisco IOS 12.3(6th)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapabilityRev1.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0402ndT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setProductRelease('Cisco IOS 12.4(2nd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0402ndT.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0206thSX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setProductRelease('Cisco IOS 12.2(6th)SX')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0206thSX.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapV12R0403rdT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setProductRelease('Cisco IOS 12.4(3rd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0403rdT.setDescription('Cisco RTTMON MIB capabilities')
ciscoRttMonCapCRS1V3R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setProductRelease('Cisco IOS XR release 3.3 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapCRS1V3R3.setDescription('Cisco RTTMON MIB capabilities.')
ciscoRttMonCapV12R0201SRB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setStatus('current')
if mibBuilder.loadTexts: ciscoRttMonCapV12R0201SRB.setDescription('Cisco RTTMON MIB capabilities')
mibBuilder.exportSymbols("CISCO-RTTMON-CAPABILITY", ciscoRttMonCapCRS1V3R3=ciscoRttMonCapCRS1V3R3, PYSNMP_MODULE_ID=ciscoRttMonCapability, ciscoRttMonCapV12R0402ndT=ciscoRttMonCapV12R0402ndT, ciscoRttMonCapability=ciscoRttMonCapability, ciscoRttMonCapabilityRev1=ciscoRttMonCapabilityRev1, ciscoRttMonCapV12R0403rdT=ciscoRttMonCapV12R0403rdT, ciscoRttMonCapV12R0201SRB=ciscoRttMonCapV12R0201SRB, ciscoRttMonCapV12R0206thSX=ciscoRttMonCapV12R0206thSX)
