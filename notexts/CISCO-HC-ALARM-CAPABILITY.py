#
# PySNMP MIB module CISCO-HC-ALARM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HC-ALARM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention")
ciscoHcAlarmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 398))
ciscoHcAlarmCapability.setRevisions(('2008-08-05 00:00', '2004-03-22 00:00',))
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setLastUpdated('200808050000Z')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setOrganization('Cisco Systems, Inc.')
ciscoHcAlarmCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setStatus('current')
ciscoHcAlarmCapNXOSV04R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-HC-ALARM-CAPABILITY", PYSNMP_MODULE_ID=ciscoHcAlarmCapability, ciscoHcAlarmCapability=ciscoHcAlarmCapability, ciscoHcAlarmCapNXOSV04R0101=ciscoHcAlarmCapNXOSV04R0101, ciscoHcAlarmCapCatOSV08R0401=ciscoHcAlarmCapCatOSV08R0401)
