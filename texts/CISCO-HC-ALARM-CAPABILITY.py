#
# PySNMP MIB module CISCO-HC-ALARM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HC-ALARM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType")
ciscoHcAlarmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 398))
ciscoHcAlarmCapability.setRevisions(('2008-08-05 00:00', '2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHcAlarmCapability.setRevisionsDescriptions(('Added capability statement ciscoHcAlarmCapNXOSV04R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setLastUpdated('200808050000Z')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setDescription('The capabilities description of HC-ALARM-MIB.')
ciscoHcAlarmCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapCatOSV08R0401.setDescription('HC-ALARM-MIB capabilities.')
ciscoHcAlarmCapNXOSV04R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapNXOSV04R0101.setDescription('HC-RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-HC-ALARM-CAPABILITY", ciscoHcAlarmCapCatOSV08R0401=ciscoHcAlarmCapCatOSV08R0401, ciscoHcAlarmCapability=ciscoHcAlarmCapability, PYSNMP_MODULE_ID=ciscoHcAlarmCapability, ciscoHcAlarmCapNXOSV04R0101=ciscoHcAlarmCapNXOSV04R0101)
