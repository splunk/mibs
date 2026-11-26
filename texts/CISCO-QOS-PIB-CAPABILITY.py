#
# PySNMP MIB module CISCO-QOS-PIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-QOS-PIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoQosPibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 390))
ciscoQosPibCapability.setRevisions(('2003-08-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosPibCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosPibCapability.setLastUpdated('200308140000Z')
if mibBuilder.loadTexts: ciscoQosPibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosPibCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosPibCapability.setDescription('The capabilities description of \n                CISCO-QOS-PIB-MIB.')
ciscoQosPibCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 390, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQosPibCapCatOSV08R0101Cat6K.setDescription('CISCO-QOS-PIB-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-QOS-PIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoQosPibCapability, ciscoQosPibCapCatOSV08R0101Cat6K=ciscoQosPibCapCatOSV08R0101Cat6K, ciscoQosPibCapability=ciscoQosPibCapability)
