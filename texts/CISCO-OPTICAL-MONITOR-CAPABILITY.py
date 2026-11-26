#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-OPTICAL-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
OpticalAlarmSeverityOrZero, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalAlarmSeverityOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOpticalMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 528))
ciscoOpticalMonitorCapability.setRevisions(('2007-01-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dwdm@cisco.com,\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setDescription('The capabilities description of\n        CISCO-OPTICAL-MONITOR-MIB.')
ciscoOpticalMonCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 528, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoOpticalMonCapCatOSV08R0601.setDescription('CISCO-OPTICAL-MONITOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-CAPABILITY", ciscoOpticalMonCapCatOSV08R0601=ciscoOpticalMonCapCatOSV08R0601, PYSNMP_MODULE_ID=ciscoOpticalMonitorCapability, ciscoOpticalMonitorCapability=ciscoOpticalMonitorCapability)
