#
# PySNMP MIB module CISCO-STACK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-STACK-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoStackCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 378))
ciscoStackCapability.setRevisions(('2008-03-19 00:00', '2006-03-15 00:00', '2005-01-19 00:00', '2003-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoStackCapability.setRevisionsDescriptions(('Added ciscoStackCapCatOSV08R0701PCat6k for Cisco   \n                 CatOS 8.7(1).', 'Add VARIATIONs for notifications chassisAlarmOff, \n                 chassisAlarmOn, moduleDown and moduleUp, in \n                 ciscoStackCapCatOSV08R0101Cat6k.', 'Added ciscoStackCapV12R0112cE01PCat6k for Cisco IOS\n                12.1(12c)E1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoStackCapability.setLastUpdated('200803190000Z')
if mibBuilder.loadTexts: ciscoStackCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoStackCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com,\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoStackCapability.setDescription('The capabilities description of\n                 CISCO-STACK-MIB.')
ciscoStackCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapCatOSV08R0101Cat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapV12R0111bEXCat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapV12R0112cE01PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setProductRelease('Cisco IOS 12.1(12c)E1 on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapV12R0112cE01PCat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapCatOSV08R0701PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapCatOSV08R0701PCat6k.setDescription('CISCO-STACK-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-STACK-CAPABILITY", ciscoStackCapV12R0112cE01PCat6k=ciscoStackCapV12R0112cE01PCat6k, ciscoStackCapCatOSV08R0701PCat6k=ciscoStackCapCatOSV08R0701PCat6k, ciscoStackCapability=ciscoStackCapability, PYSNMP_MODULE_ID=ciscoStackCapability, ciscoStackCapV12R0111bEXCat6k=ciscoStackCapV12R0111bEXCat6k, ciscoStackCapCatOSV08R0101Cat6k=ciscoStackCapCatOSV08R0101Cat6k)
