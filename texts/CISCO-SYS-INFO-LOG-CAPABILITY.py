#
# PySNMP MIB module CISCO-SYS-INFO-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYS-INFO-LOG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysInfoLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 321))
ciscoSysInfoLogCapability.setRevisions(('2005-08-24 00:00', '2003-08-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setRevisionsDescriptions(('Added capability statement \n                 ciscoSysInfoLogCapCatOSV08R0501.\n\n                 Added VARIATION for csilServerProtocol in \n                 capability statement \n                 ciscoSysInfoLogCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setLastUpdated('200508240000Z')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setDescription('The capabilities description of\n                 CISCO-SYS-INFO-LOG-MIB.')
ciscoSysInfoLogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSysInfoLogCapCatOSV08R0101.setDescription('CISCO-SYS-INFO-LOG-MIB capabilities.')
ciscoSysInfoLogCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSysInfoLogCapCatOSV08R0501.setDescription('CISCO-SYS-INFO-LOG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-CAPABILITY", ciscoSysInfoLogCapability=ciscoSysInfoLogCapability, ciscoSysInfoLogCapCatOSV08R0501=ciscoSysInfoLogCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoSysInfoLogCapability, ciscoSysInfoLogCapCatOSV08R0101=ciscoSysInfoLogCapCatOSV08R0101)
