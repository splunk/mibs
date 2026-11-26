#
# PySNMP MIB module CISCO-HC-ALARM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HC-ALARM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "StorageType")
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
mibBuilder.exportSymbols("CISCO-HC-ALARM-CAPABILITY", PYSNMP_MODULE_ID=ciscoHcAlarmCapability, ciscoHcAlarmCapCatOSV08R0401=ciscoHcAlarmCapCatOSV08R0401, ciscoHcAlarmCapability=ciscoHcAlarmCapability, ciscoHcAlarmCapNXOSV04R0101=ciscoHcAlarmCapNXOSV04R0101)
