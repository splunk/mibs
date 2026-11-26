#
# PySNMP MIB module CISCO-PACKET-CAPTURE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PACKET-CAPTURE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPacketCaptureCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 527))
ciscoPacketCaptureCapability.setRevisions(('2008-10-23 00:00', '2007-01-05 00:00',))
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setLastUpdated('200810230000Z')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setOrganization('Cisco Systems, Inc.')
ciscoPacketCaptureCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on devices with\n                    Supervisor 720 or Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setStatus('current')
cpcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-PACKET-CAPTURE-CAPABILITY", cpcCapV12R0233SXIPCat6K=cpcCapV12R0233SXIPCat6K, PYSNMP_MODULE_ID=ciscoPacketCaptureCapability, ciscoPacketCaptureCatOSV08R0601=ciscoPacketCaptureCatOSV08R0601, ciscoPacketCaptureCapability=ciscoPacketCaptureCapability)
