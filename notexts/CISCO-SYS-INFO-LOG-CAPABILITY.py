#
# PySNMP MIB module CISCO-SYS-INFO-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYS-INFO-LOG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysInfoLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 321))
ciscoSysInfoLogCapability.setRevisions(('2005-08-24 00:00', '2003-08-01 00:00',))
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setLastUpdated('200508240000Z')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysInfoLogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setStatus('current')
ciscoSysInfoLogCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-CAPABILITY", ciscoSysInfoLogCapCatOSV08R0501=ciscoSysInfoLogCapCatOSV08R0501, ciscoSysInfoLogCapCatOSV08R0101=ciscoSysInfoLogCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoSysInfoLogCapability, ciscoSysInfoLogCapability=ciscoSysInfoLogCapability)
