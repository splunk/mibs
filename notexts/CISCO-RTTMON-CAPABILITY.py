#
# PySNMP MIB module CISCO-RTTMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RTTMON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
ciscoRttMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 62))
ciscoRttMonCapability.setRevisions(('2006-03-02 00:00', '2005-12-14 00:00', '2005-06-09 00:00', '2005-05-01 00:00', '2004-05-31 00:00',))
if mibBuilder.loadTexts: ciscoRttMonCapability.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: ciscoRttMonCapability.setOrganization('Cisco Systems, Inc.')
ciscoRttMonCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setProductRelease('Cisco IOS 12.3(6th)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setStatus('current')
ciscoRttMonCapV12R0402ndT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setProductRelease('Cisco IOS 12.4(2nd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setStatus('current')
ciscoRttMonCapV12R0206thSX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setProductRelease('Cisco IOS 12.2(6th)SX')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setStatus('current')
ciscoRttMonCapV12R0403rdT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setProductRelease('Cisco IOS 12.4(3rd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setStatus('current')
ciscoRttMonCapCRS1V3R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setProductRelease('Cisco IOS XR release 3.3 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setStatus('current')
ciscoRttMonCapV12R0201SRB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setStatus('current')
mibBuilder.exportSymbols("CISCO-RTTMON-CAPABILITY", ciscoRttMonCapV12R0403rdT=ciscoRttMonCapV12R0403rdT, ciscoRttMonCapV12R0206thSX=ciscoRttMonCapV12R0206thSX, PYSNMP_MODULE_ID=ciscoRttMonCapability, ciscoRttMonCapV12R0402ndT=ciscoRttMonCapV12R0402ndT, ciscoRttMonCapCRS1V3R3=ciscoRttMonCapCRS1V3R3, ciscoRttMonCapability=ciscoRttMonCapability, ciscoRttMonCapV12R0201SRB=ciscoRttMonCapV12R0201SRB, ciscoRttMonCapabilityRev1=ciscoRttMonCapabilityRev1)
