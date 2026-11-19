#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 326))
ciscoL2L3IfConfigCapability.setRevisions(('2014-04-04 00:00', '2013-08-28 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setOrganization('Cisco Systems, Inc.')
ciscoL2L3IfConfigCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setStatus('current')
ciscoL2L3IfConfigCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on \n                    Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setStatus('current')
ciscoL2L3IfConfigCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY", ciscoL2L3IfConfigCapNxOSV06R0202PN7K=ciscoL2L3IfConfigCapNxOSV06R0202PN7K, ciscoL2L3IfConfigCapV12R0119E=ciscoL2L3IfConfigCapV12R0119E, PYSNMP_MODULE_ID=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapability=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapNxOSV06R0201PMds=ciscoL2L3IfConfigCapNxOSV06R0201PMds)
