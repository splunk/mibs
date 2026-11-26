#
# PySNMP MIB module CISCO-NAC-NAD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NAC-NAD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoNacNadCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 440))
ciscoNacNadCapability.setRevisions(('2008-11-10 00:00', '2008-07-17 00:00', '2006-12-12 00:00', '2005-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNacNadCapability.setRevisionsDescriptions(('Updated capabilities statement CISCO-NAC-NAD-MIB for 3750.', 'Added capability statement ciscoNacNadCapCatOSV08R0701.', 'Added capability statement ciscoNacNadCapCatOSV08R0601.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNacNadCapability.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: ciscoNacNadCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNacNadCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-nac@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNacNadCapability.setDescription('The capabilities description of CISCO-NAC-NAD-MIB.')
ciscoNacNadCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0501.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0601.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0701.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapV12R0246SECat3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setProductRelease('Cisco IOS 12.2(46)SE on Catalyst 3750.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapV12R0246SECat3k.setDescription('CISCO-NAC-NAD-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-NAC-NAD-CAPABILITY", ciscoNacNadCapCatOSV08R0501=ciscoNacNadCapCatOSV08R0501, ciscoNacNadCapCatOSV08R0601=ciscoNacNadCapCatOSV08R0601, ciscoNacNadCapV12R0246SECat3k=ciscoNacNadCapV12R0246SECat3k, ciscoNacNadCapability=ciscoNacNadCapability, PYSNMP_MODULE_ID=ciscoNacNadCapability, ciscoNacNadCapCatOSV08R0701=ciscoNacNadCapCatOSV08R0701)
