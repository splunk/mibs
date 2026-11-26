#
# PySNMP MIB module CISCO-VMPS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VMPS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVmpsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 365))
ciscoVmpsCapability.setRevisions(('2004-04-07 00:00', '2004-03-12 00:00', '2003-10-31 00:00',))
if mibBuilder.loadTexts: ciscoVmpsCapability.setLastUpdated('200404070000Z')
if mibBuilder.loadTexts: ciscoVmpsCapability.setOrganization('Cisco Systems, Inc.')
ciscoVmpsCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setStatus('current')
ciscoVmpsCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setStatus('current')
ciscoVmpsCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setStatus('current')
mibBuilder.exportSymbols("CISCO-VMPS-CAPABILITY", ciscoVmpsCapCatOSV08R0101=ciscoVmpsCapCatOSV08R0101, ciscoVmpsCapability=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0401=ciscoVmpsCapCatOSV08R0401, ciscoVmpsCapCatOSV08R0301=ciscoVmpsCapCatOSV08R0301, PYSNMP_MODULE_ID=ciscoVmpsCapability)
