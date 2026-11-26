#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-OPTICAL-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
OpticalAlarmSeverityOrZero, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalAlarmSeverityOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOpticalMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 528))
ciscoOpticalMonitorCapability.setRevisions(('2007-01-08 00:00',))
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setOrganization('Cisco Systems, Inc.')
ciscoOpticalMonCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 528, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-CAPABILITY", ciscoOpticalMonCapCatOSV08R0601=ciscoOpticalMonCapCatOSV08R0601, ciscoOpticalMonitorCapability=ciscoOpticalMonitorCapability, PYSNMP_MODULE_ID=ciscoOpticalMonitorCapability)
