#
# PySNMP MIB module CISCO-PACKET-CAPTURE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PACKET-CAPTURE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-PACKET-CAPTURE-CAPABILITY", PYSNMP_MODULE_ID=ciscoPacketCaptureCapability, cpcCapV12R0233SXIPCat6K=cpcCapV12R0233SXIPCat6K, ciscoPacketCaptureCapability=ciscoPacketCaptureCapability, ciscoPacketCaptureCatOSV08R0601=ciscoPacketCaptureCatOSV08R0601)
